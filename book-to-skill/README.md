# book-to-skill

Skills de Claude creados a partir de libros. Cada carpeta es un skill
autocontenido (`SKILL.md` + `references/`).

| Skill | Libro fuente |
|---|---|
| [`graph-data-science/`](graph-data-science/SKILL.md) | *Graph Data Science For Dummies, 2nd Neo4j Special Edition* — Dr. Alicia Frame y Zach Blumenfeld (Wiley, 2022) |
| [`critica-estadistica/`](critica-estadistica/SKILL.md) | *How to Lie with Statistics* — Darrell Huff (W. W. Norton, 1954) |
| [`enarm/`](enarm/SKILL.md) | *CAM. Curso de Actualización Médica: Fundamentos para presentar el ENARM* — Ramos Herrera et al. (McGraw-Hill, 2015). Copia fuente incompleta: sin Pediatría, Urgencias/cirugía, Oftalmología, Infectología ni Imagenología. |

## Cómo se construye un skill desde un libro

1. Extraer el texto del PDF y leerlo completo. Para libros muy extensos,
   repartir los capítulos entre varios agentes en paralelo con una plantilla
   común de apuntes, y verificar después que no haya texto copiado.
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
