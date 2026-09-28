# Conceptos base

## Qué es un grafo

- Representación matemática de un sistema complejo: **nodos** (vértices,
  entidades) unidos por **relaciones** (aristas, enlaces).
- Origen: Euler y los siete puentes de Königsberg (1736). Su intuición: para
  ese tipo de problema solo importan las conexiones, no la geometría. De ahí
  salieron reglas generales aplicables a cualquier sistema conectado.
- Nodos ≈ sustantivos; relaciones ≈ verbos que les dan contexto. Un buen modelo
  se puede leer como frases: "A VIVE_CON B, B ES_DUEÑO_DE un Auto, A MANEJA
  ese Auto".
- "Grafo" aquí **no** es una gráfica de funciones ni un chart.
- Un **salto (hop)** es recorrer una relación. Las bases de datos nativas de
  grafos guardan las relaciones junto a los datos, así que las consultas de
  varios saltos evitan joins e índices costosos.

## Las tres áreas de la ciencia de datos de grafos

1. **Estadísticas de grafo** — medidas básicas: número de nodos, distribución
   de relaciones/grados, densidad. Orientan qué análisis correr y cómo leerlo.
2. **Analítica de grafos** — responde preguntas concretas sobre datos
   históricos combinando consultas y algoritmos en "recetas"; el resultado se
   usa directamente.
3. **ML e IA potenciados con grafos** — usar datos y resultados de grafo para
   entrenar modelos o apoyar decisiones probabilísticas.

Normalmente 1 y 2 se usan juntas, y lo aprendido mejora el paso 3.

## Las cuatro familias de preguntas

| Familia | Pregunta | Herramientas |
|---|---|---|
| Movimiento | ¿Cómo viaja algo por la red (enfermedad, falla, dinero)? ¿Ruta óptima, restricciones de flujo? | Búsqueda de caminos |
| Influencia | ¿Qué nodos están mejor ubicados estructuralmente — difusores rápidos, puentes entre grupos, cuellos de botella? | Centralidad |
| Grupos e interacciones | ¿Qué nodos forman grupos por número/fuerza de interacciones? ¿Qué conexiones futuras u ocultas hay? | Detección de comunidades, similitud, predicción de enlaces |
| Patrones | ¿Qué estructuras son significativas? ¿Qué entidades ambiguas son la misma? | Consultas de patrón, similitud, embeddings |

Ejemplo de receta: medir primero la densidad de relaciones ayuda a elegir el
algoritmo de comunidades que dará resultados relevantes.

## Ruta de adopción (de menor a mayor madurez)

1. **Grafo de conocimiento** — conjunto interconectado de entidades y hechos
   del mundo real en forma entendible por humanos. A diferencia de una base de
   conocimiento plana, integra información adyacente mediante relaciones para
   derivar conocimiento nuevo. Usos: unificar fuentes diversas, dar contexto a
   sistemas de IA (p. ej. un chatbot que entiende que "un bat para el
   cumpleaños de mi esposo" es equipo deportivo, no un murciélago). Aquí se
   usan **consultas** cuando se sabe exactamente qué buscar.

2. **Algoritmos de grafos** — análisis offline sobre el grafo completo para
   inferir significado de la topología: clústeres, nodos influyentes, rutas.
   Sirven para:
   - *Analítica*: respuesta directa, no supervisada ("¿qué nodo es más
     importante?", "¿cómo se agrupan mis datos?").
   - *Ingeniería de features de grafo*: encontrar, combinar y extraer elementos
     predictivos del grafo (p. ej. PageRank de cada nodo, ID de comunidad) a un
     vector de features para ML. Mejora modelos **con los datos que ya tienes**
     y sin cambiar el pipeline de ML. Los features y métricas se suelen
     escribir de vuelta al grafo.

   Flujo de ML potenciado con grafos: agregar/explorar/limpiar datos →
   consultas o algoritmos para features → preparar y dividir train/test →
   entrenar → producción. Features y reentrenamiento se hacen offline y de
   forma cíclica, aunque el modelo sirva transacciones en tiempo real.

3. **ML nativo de grafos** — el grafo completo es la entrada del modelo; no
   predefines qué features importan. Tareas típicas: predecir enlaces nuevos o
   faltantes, y predecir etiquetas faltantes de nodos (p. ej. clientes que se
   van a ir, relaciones futuras entre defraudadores y víctimas).

   **Embeddings de grafo**: transforman un grafo o subgrafo en vectores de baja
   dimensión que conservan topología, conectividad y atributos.
   - *De nodo*: conectividad de cada nodo (los más usados y flexibles).
   - *De camino*: recorridos a través del grafo.
   - *De grafo completo*: todo el grafo en un solo vector.

   También sirven para exploración, similitud entre entidades y reducción de
   dimensionalidad.

   Idea de "graph networks" (Battaglia et al.): el modelo toma un grafo,
   calcula conservando estados intermedios y devuelve un grafo. Eso permite que
   un experto revise la ruta de aprendizaje (más explicable) y lograr
   predicciones más ricas con menos datos y ciclos de entrenamiento.

## Por qué ahora

Tecnologías más accesibles, capacidad de cómputo sobre grafos enormes, y
evidencia del poder predictivo de la estructura. Según el libro, los artículos
de investigación en IA que usan tecnología de grafos crecieron más de 700 % en
una década.
