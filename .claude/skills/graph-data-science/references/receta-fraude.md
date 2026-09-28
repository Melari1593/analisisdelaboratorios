# Receta completa: detectar entidades sospechosas por identificadores compartidos

Caso del libro: detección de fraude de primera parte (cuentas falsas creadas sin
intención de pagar). El patrón sirve para cualquier dominio donde entidades
comparten identificadores: pacientes duplicados por número de expediente,
muestras de laboratorio con el mismo código de barras, proveedores con la misma
cuenta bancaria, etc.

## Modelo

- `(:Client)` — personas con datos personales.
- `(:Mule)` — etiqueta adicional para clientes que se sabe transfirieron dinero
  de forma fraudulenta (en datos reales normalmente **no** la tendrías; aquí
  sirve para validar).
- Identificadores: `(:Phone)`, `(:Email)`, `(:SSN)`.
- Relaciones: `(Client)-[:HAS_PHONE]->(Phone)`, `-[:HAS_EMAIL]->(Email)`,
  `-[:HAS_SSN]->(SSN)`.

## Paso 1 — Encontrar outliers con Degree Centrality

Los outliers en un grafo se definen por conectividad, no por valor de
propiedad. Cada tipo de nodo tiene su conectividad esperada (un banco recibe
muchos depósitos; una persona, pocos), así que compara solo nodos del mismo tipo.

```cypher
// Proyección: clientes + identificadores, relaciones invertidas para que el
// grado de cada identificador = número de clientes que lo usan
CALL gds.graph.project('ids',
  ['Client', 'Phone', 'Email', 'SSN'],
  {
    HAS_PHONE: {orientation: 'REVERSE'},
    HAS_EMAIL: {orientation: 'REVERSE'},
    HAS_SSN:   {orientation: 'REVERSE'}
  });

CALL gds.degree.mutate('ids', {mutateProperty: 'clientDegree'});

CALL gds.graph.nodeProperties.write('ids', ['clientDegree'],
  ['Phone', 'Email', 'SSN']);

MATCH (n) WHERE n:Phone OR n:Email OR n:SSN
RETURN labels(n) AS tipo, n.email, n.phoneNumber, n.ssn,
       n.clientDegree AS clientes
ORDER BY clientes DESC LIMIT 10;
```

Resultado típico: unos pocos identificadores con cientos de clientes
(`fake@fake.com`, `000-000-0000`, `000-00-0000`). Son **datos de relleno**, no
fraude: gente que no quiso llenar el formulario. Si no los excluyes, generan
falsos positivos masivos.

## Paso 2 — Marcar y excluir los outliers

Cambia su etiqueta para que queden fuera de proyecciones futuras:

```cypher
MATCH (n:Email) WHERE n.email IN ['fake@fake.com', 'no@gmail.com']
SET n:BadEmail REMOVE n:Email;

MATCH (n:SSN) WHERE n.ssn = '000-00-0000'
SET n:BadSSN REMOVE n:SSN;

MATCH (n:Phone) WHERE n.phoneNumber = '000-000-0000'
SET n:BadPhone REMOVE n:Phone;

CALL gds.graph.drop('ids');
```

Mejor práctica: en vez de listar valores a mano, define un umbral de grado
basado en la distribución (p. ej. percentil 99.9) y revisa los casos con un
experto.

## Paso 3 — Encontrar clústeres sospechosos con WCC

Islas de nodos muy interconectados y poco ligadas al resto no son
comportamiento financiero típico. Weakly Connected Components agrupa todo lo
alcanzable ignorando la dirección.

```cypher
CALL gds.graph.project('clusters',
  ['Client', 'Phone', 'Email', 'SSN'],   // las etiquetas "Bad*" ya no entran
  ['HAS_PHONE', 'HAS_EMAIL', 'HAS_SSN']);

CALL gds.wcc.write('clusters', {writeProperty: 'componentId'});
```

Distribución de tamaños:

```cypher
MATCH (c:Client)
WITH c.componentId AS comp, count(*) AS size
WITH CASE
       WHEN size <= 2 THEN '1-2'
       WHEN size <= 5 THEN '3-5'
       WHEN size <= 9 THEN '6-9'
       ELSE '>=10' END AS rango
RETURN rango, count(*) AS clusters
ORDER BY rango;
```

Lo esperable: la gran mayoría en clústeres de 1–2 (la gente no comparte
identificadores) y muy pocos de ≥10. En el ejemplo del libro: ~11 000 de 1–2,
272 de 3–5, 120 de 6–9 y **5** de ≥10. Esos cinco son los que hay que revisar.

Marca identificadores compartidos y resume los clústeres grandes:

```cypher
MATCH (n) WHERE (n:Email OR n:Phone OR n:SSN) AND n.clientDegree > 1
SET n:SharedId;

MATCH (c:Client)
WITH c.componentId AS comp, count(*) AS nClients
WHERE nClients >= 10
WITH collect(comp) AS comps
MATCH (n:SharedId)<-[:HAS_PHONE|HAS_EMAIL|HAS_SSN]-(c:Client)
WHERE n.componentId IN comps
RETURN n.componentId AS comp,
       count(DISTINCT c) AS clientes,
       count(DISTINCT n) AS idsCompartidos
ORDER BY clientes DESC;
```

## Paso 4 — Explorar visualmente y medir intermediación

Visualiza el clúster más interesante (en Bloom o similar). Señales: varias
personas compartiendo pocos correos, nodos que actúan como puentes locales.

Betweenness Centrality puntúa cada nodo por cuántos caminos más cortos pasan
por él. Proyecta solo el clúster, con relaciones cliente–cliente derivadas:

```cypher
MATCH (c1:Client)-[:HAS_PHONE|HAS_EMAIL|HAS_SSN]->(:SharedId)
      <-[:HAS_PHONE|HAS_EMAIL|HAS_SSN]-(c2:Client)
WHERE c1.componentId = $comp AND c1 <> c2
WITH gds.graph.project('cluster-' + toString($comp), c1, c2,
       {relationshipType: 'SHARES_ID'}) AS g
RETURN g.nodeCount, g.relationshipCount;

CALL gds.betweenness.write('cluster-' + toString($comp),
  {writeProperty: 'betweennessCentrality'});
```

En el ejemplo, los nodos más grandes (mayor betweenness) resultaron ser mulas
conocidas. Aquí se envía la lista a analistas de dominio para confirmar.

## Paso 5 — Validar la hipótesis en todo el grafo

Compara la distribución del score entre clases:

```cypher
MATCH (c:Client)
RETURN c:Mule AS esMula,
       avg(c.betweennessCentrality) AS promedio,
       max(c.betweennessCentrality) AS maximo,
       stDev(c.betweennessCentrality) AS desv,
       percentileCont(c.betweennessCentrality, 0.95) AS p95,
       count(*) AS n;
```

En el libro: promedio ≈ 1.08 para mulas vs ≈ 0.007 para no mulas; pero la
mediana de ambos es 0 y hay traslape. **Un solo score no basta**.

## Paso 6 — Features de grafo para un clasificador binario

Extrae por cliente, a una tabla:

- `betweenness` — intermediación.
- `sharedIdentities` — número de identificadores que comparte.
- (opcional) peso de los identificadores compartidos.
- `clusterSize` — tamaño de su componente WCC.
- `mulesNearby` — mulas conocidas a ≤ n saltos.

```cypher
MATCH (c:Client)
OPTIONAL MATCH (c)-[:HAS_PHONE|HAS_EMAIL|HAS_SSN]->(s:SharedId)
WITH c, count(DISTINCT s) AS sharedIdentities
CALL {
  WITH c
  MATCH (c)-[:HAS_PHONE|HAS_EMAIL|HAS_SSN*1..4]-(m:Mule)
  WHERE m <> c
  RETURN count(DISTINCT m) AS mulesNearby
}
MATCH (o:Client {componentId: c.componentId})
WITH c, sharedIdentities, mulesNearby, count(o) AS clusterSize
RETURN c.name AS name,
       coalesce(c.betweennessCentrality, 0) AS betweenness,
       sharedIdentities, clusterSize, mulesNearby,
       c:Mule AS isMule;
```

Exporta a CSV / pandas, combina con features tabulares existentes, divide
train/test y entrena (p. ej. gradient boosting o regresión logística). Si el
modelo es bueno, úsalo en producción y recalcula features y modelo
periódicamente conforme el grafo crece.

Cuidado con la fuga de información: `mulesNearby` usa la etiqueta que quieres
predecir; calcúlala solo con mulas del conjunto de entrenamiento.
