# Algoritmos de grafos y Neo4j GDS

## Las cinco familias más usadas

| Familia | Qué hace | Usos | Algoritmos típicos (GDS) |
|---|---|---|---|
| **Búsqueda de caminos** | Explora rutas entre nodos | Logística, ruteo de menor costo, propagación | `gds.shortestPath.dijkstra`, `gds.allShortestPaths.*`, `gds.bfs`, `gds.dfs`, A* |
| **Centralidad** | Mide importancia/rol de cada nodo según su posición | Influenciadores, puentes, vulnerabilidades en cascada, outliers | `gds.degree`, `gds.pageRank`, `gds.betweenness`, `gds.closeness`, `gds.articleRank` |
| **Detección de comunidades** | Encuentra grupos con interacciones más densas dentro que fuera | Segmentación, comportamiento similar, duplicados, resiliencia, preparar datos | `gds.wcc`, `gds.louvain`, `gds.leiden`, `gds.labelPropagation`, `gds.triangleCount`, `gds.localClusteringCoefficient` |
| **Similitud** | Compara conjuntos/propiedades para puntuar parecido entre nodos | Recomendaciones personalizadas, jerarquías de categorías | `gds.nodeSimilarity` (Jaccard/Overlap), `gds.knn` |
| **Predicción topológica de enlaces** | Estima la probabilidad de una relación nueva u oculta según cercanía y estructura (triángulos, vecinos comunes) | Reposicionamiento de fármacos, investigación criminal | `gds.alpha.linkprediction.*` (Adamic-Adar, Common Neighbors, Preferential Attachment…), pipelines de link prediction |

Embeddings de nodo en GDS: `gds.fastRP`, `gds.node2vec`, `gds.graphSage`.

## Cuál elegir (guía rápida)

- "¿Qué nodo tiene más conexiones / hay outliers?" → **Degree**.
- "¿Quién es influyente considerando la calidad de sus vecinos?" → **PageRank**.
- "¿Quién actúa de puente/intermediario?" → **Betweenness**.
- "¿Qué partes están conectadas entre sí, sin importar dirección?" (islas,
  entidades que comparten identificadores) → **WCC**.
- "¿Hay grupos más densos de lo esperado al azar?" → **Louvain** / **Leiden**
  (maximizan modularidad).
- "¿Qué nodos se parecen por sus vecinos?" → **Node Similarity** / **KNN**.
- "¿Qué relación falta o va a aparecer?" → predicción de enlaces o embeddings +
  clasificador.

## Mecánica de GDS

### 1. Proyectar el grafo en memoria

Proyección nativa (rápida; etiquetas y tipos completos):

```cypher
CALL gds.graph.project(
  'mi-proyeccion',
  ['Paciente', 'Prueba'],
  {REALIZO: {orientation: 'UNDIRECTED'}}
);
```

`orientation`: `NATURAL` (como está guardada), `REVERSE` (invertida; útil para
contar cuántos apuntan *hacia* un nodo) o `UNDIRECTED`.

Proyección con Cypher (para filtrar o crear relaciones derivadas) — sintaxis
GDS 2.x con agregación:

```cypher
MATCH (a:Paciente)-[:TIENE]->(:Variante)<-[:TIENE]-(b:Paciente)
WHERE a.cohorte = $cohorte AND b.cohorte = $cohorte
WITH gds.graph.project('pacientes-variante', a, b,
       {relationshipType: 'COMPARTE_VARIANTE'}) AS g
RETURN g.graphName, g.nodeCount, g.relationshipCount;
```

(La forma antigua `gds.graph.project.cypher(...)` está deprecada.)

### 2. Estimar memoria antes de grafos grandes

```cypher
CALL gds.pageRank.write.estimate('mi-proyeccion', {writeProperty: 'pr'});
```

### 3. Elegir el modo de ejecución

| Modo | Efecto | Cuándo |
|---|---|---|
| `stream` | Devuelve resultados por fila, no guarda nada | Explorar, depurar |
| `stats` | Solo métricas resumen | Revisar distribución antes de escribir |
| `mutate` | Guarda el resultado en la proyección en memoria | Encadenar algoritmos |
| `write` | Guarda el resultado como propiedad en la base de datos | Persistir para consultas, visualización o ML |

```cypher
CALL gds.degree.mutate('mi-proyeccion', {mutateProperty: 'grado'});
CALL gds.graph.nodeProperties.write('mi-proyeccion', ['grado'], ['Prueba']);
```

### 4. Limpiar

```cypher
CALL gds.graph.drop('mi-proyeccion');
```

## Plataforma Neo4j (según el libro)

- **Neo4j Graph Data Science**: biblioteca de algoritmos y ML que escala a
  cientos de miles de millones de nodos/relaciones.
- **Neo4j DBMS**: base de datos nativa de grafos, múltiples bases, clúster,
  sharding y acceso federado.
- **Cypher**: lenguaje declarativo tipo SQL con sintaxis ASCII-art:
  `(p:Persona {nombre: "Ana"})-[:LE_GUSTA]->(t:Tecnologia {tipo: "Grafos"})`.
- **Neo4j Desktop / Browser**: consultar, visualizar y administrar.
- **Neo4j Bloom**: exploración visual sin código; "search phrases" en lenguaje
  natural que ejecutan consultas; estilos (tamaño, color) basados en
  resultados de algoritmos.

Alternativas fuera de Neo4j para prototipos en Python: `networkx` (grafos
pequeños), `igraph`, `graph-tool`, `PyTorch Geometric` / `DGL` (ML nativo).
