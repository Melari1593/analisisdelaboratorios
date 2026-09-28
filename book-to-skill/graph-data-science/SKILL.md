---
name: graph-data-science
description: Guía para resolver problemas con ciencia de datos de grafos (graph data science) — modelar datos conectados como nodos y relaciones, elegir el algoritmo de grafos correcto (búsqueda de caminos, centralidad, detección de comunidades, similitud, predicción de enlaces), escribir proyecciones y llamadas de Neo4j Graph Data Science (GDS) en Cypher, extraer features de grafo para machine learning, y planear un proyecto de grafos. Úsalo SIEMPRE que el usuario trabaje con datos donde las conexiones importan (redes, interacciones proteína-proteína, pacientes-pruebas-diagnósticos, transacciones, fraude, recomendaciones, grafos de conocimiento), mencione Neo4j, Cypher, GDS, PageRank, Louvain, WCC, betweenness, node embeddings o "grafo de conocimiento", o pregunte "¿qué nodos son más importantes?", "¿cómo se agrupan?", "¿cómo se propaga X?", "¿qué conexión falta?" — aunque no diga "grafo". NO usar para gráficas/charts de datos (eso es visualización), ni para teoría de grafos puramente matemática sin datos.
---

# Graph Data Science

Skill destilado de *Graph Data Science For Dummies, 2nd Neo4j Special Edition*
(A. Frame y Z. Blumenfeld, Wiley 2022). El contenido está reescrito y resumido;
el código de ejemplo está actualizado a la sintaxis de Neo4j GDS 2.x.

## Idea central

Las redes reales no son aleatorias: las conexiones no están distribuidas de forma
uniforme ni son estáticas. La estadística tabular por sí sola no describe ni
predice bien el comportamiento de sistemas conectados. Un **grafo** (nodos =
sustantivos, relaciones = verbos) modela esos sistemas de forma fiel y
"dibujable en un pizarrón"; la **ciencia de datos de grafos** extrae conocimiento
de la estructura para responder preguntas y alimentar predicciones.

## Flujo de trabajo

Sigue estos pasos en orden; salta los que el usuario ya tenga resueltos.

1. **Traduce la pregunta a una de las cuatro familias** (ver
   `references/conceptos.md`):
   - *Movimiento* — ¿cómo viaja algo por la red? → caminos.
   - *Influencia* — ¿qué puntos controlan la red? → centralidad.
   - *Grupos e interacciones* — ¿quién se agrupa con quién, qué enlace falta? →
     comunidades, similitud, predicción de enlaces.
   - *Patrones* — ¿qué estructura es significativa? → consultas de patrón,
     similitud, embeddings.

2. **Modela el grafo.** Define etiquetas de nodo, tipos de relación y dirección.
   Escríbelo como frases ("el Paciente SE_HIZO la Prueba que DETECTÓ el
   Biomarcador"). Si el usuario no tiene grafo aún, empieza aquí: un grafo de
   conocimiento es la base de todo lo demás.

3. **Decide consulta vs. algoritmo.**
   - Sabes exactamente lo que buscas ("¿cuántos pacientes a 2 saltos de X?") →
     **consulta Cypher** local.
   - Sabes qué *indicador* buscas pero no qué vas a encontrar ("¿hay grupos
     inusualmente densos?") → **algoritmo** sobre el grafo completo.

4. **Revisa estadísticas y calidad primero.** Cuenta nodos, relaciones y la
   distribución de grados *por tipo de nodo*. Busca outliers topológicos (nodos
   con grado desproporcionado, p. ej. valores de relleno como `000-00-0000`)
   y exclúyelos antes de agrupar; si no, generan clústeres gigantes falsos.

5. **Proyecta solo lo que necesitas.** En GDS los algoritmos corren sobre una
   proyección en memoria. Selecciona etiquetas, relaciones y orientación
   adecuadas a la pregunta. Compara nodos solo contra nodos de su mismo tipo.

6. **Ejecuta el algoritmo en el modo correcto** (`stream`, `stats`, `mutate`,
   `write`) — ver `references/algoritmos.md`. Encadena algoritmos como
   "recetas": p. ej. grado → excluir outliers → WCC → betweenness dentro del
   clúster sospechoso.

7. **Interpreta con un experto de dominio.** Los algoritmos señalan candidatos,
   no conclusiones. Visualiza el subgrafo y valida hallazgos antes de actuar.

8. **Convierte resultados en features para ML** si hace falta predecir.
   Un solo score casi nunca separa bien las clases (hay traslape → falsos
   positivos/negativos); combina varios features de grafo con los tabulares
   existentes en un clasificador. Ver `references/receta-fraude.md`.

9. **Itera.** Los grafos reales cambian: recalcula features y reentrena de forma
   periódica (offline), y usa el modelo en producción.

## Referencias

Lee solo la que necesites para la tarea:

| Archivo | Cuándo leerlo |
|---|---|
| `references/conceptos.md` | Explicar qué es un grafo, las 3 áreas de GDS, las 4 familias de preguntas, la ruta de adopción (grafo de conocimiento → algoritmos → ML nativo de grafos), embeddings. |
| `references/algoritmos.md` | Elegir algoritmo, saber qué hace cada familia, sintaxis GDS (proyecciones, modos, limpieza). |
| `references/receta-fraude.md` | Ejemplo completo de principio a fin: outliers → clústeres → centralidad → features para ML. Plantilla adaptable a cualquier dominio con identificadores compartidos. |
| `references/adopcion-proyecto.md` | Planear, justificar (ROI) y aprobar un proyecto de grafos en una organización. |

## Reglas prácticas

- Nunca interpretes un score de centralidad sin compararlo con la distribución
  de nodos del mismo tipo.
- Siempre libera proyecciones al terminar (`CALL gds.graph.drop('nombre')`).
- Cuando escribas Cypher para el usuario, explica en una línea qué hace cada
  consulta y qué propiedad deja escrita en el grafo.
- Si la versión de GDS del usuario es anterior a 2.x, avisa que los nombres de
  procedimientos cambian (p. ej. `gds.graph.create` → `gds.graph.project`).
- Aplicaciones típicas que el libro destaca: reposicionamiento de fármacos,
  trayectorias de pacientes, recomendaciones y marketing, detección de fraude,
  vista 360° de clientes y linaje de datos para IA responsable.
