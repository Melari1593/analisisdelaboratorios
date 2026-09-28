# book-to-skill

Skills de Claude creados a partir de libros. Cada carpeta es un skill
autocontenido (`SKILL.md` + `references/`).

| Skill | Libro fuente |
|---|---|
| [`graph-data-science/`](graph-data-science/SKILL.md) | *Graph Data Science For Dummies, 2nd Neo4j Special Edition* — Dr. Alicia Frame y Zach Blumenfeld (Wiley, 2022) |
| [`critica-estadistica/`](critica-estadistica/SKILL.md) | *How to Lie with Statistics* — Darrell Huff (W. W. Norton, 1954) |

## Cómo se construye un skill desde un libro

1. Extraer el texto del PDF y leerlo completo.
2. Separar el conocimiento accionable (procedimientos, criterios de decisión,
   código) del relleno (publicidad, licencias, enlaces).
3. Escribir `SKILL.md` con un flujo de trabajo paso a paso y una `description`
   que diga cuándo activarlo.
4. Mover el detalle a `references/` para cargarlo solo cuando haga falta.
5. Reescribir con palabras propias: **no se copia el texto del libro** (tiene
   copyright). El código se actualiza a versiones actuales de las herramientas.

## Instalación

Copia la carpeta del skill a `~/.claude/skills/` (personal) o a
`.claude/skills/` de un proyecto, o empaquétala como `.zip` y súbela en
claude.ai → Settings → Capabilities → Skills.
