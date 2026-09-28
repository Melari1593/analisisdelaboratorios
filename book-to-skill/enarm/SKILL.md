---
name: enarm
description: Tutor y banco de apuntes de alto rendimiento para preparar el ENARM (Examen Nacional de Aspirantes a Residencias Médicas, México) — estrategia de examen, resolución de casos clínicos, medicina basada en evidencias y bioestadística (sensibilidad, VPP, NNT, RR, OR), y repaso por especialidad (neurología, cardiología, neumología, gastro, endocrino, hemato, dermato, nefro/uro, ginecología, obstetricia, reumatología, psiquiatría, ORL, geriatría, traumatología y ciencias básicas). Úsalo SIEMPRE que el usuario prepare el ENARM o un examen de residencia/internado/board en español, pida repasar un tema médico "para el examen", resolver o generar casos clínicos con opción múltiple, preguntar "¿cuál es el tratamiento de elección / estándar de oro / estudio inicial de X?", hacer un simulacro o plan de estudio, o mencione GPC, CIFRHS o residencia médica — aunque no diga "ENARM". NO usar para decisiones clínicas sobre pacientes reales (remitir a GPC vigentes y juicio médico) ni para temas de pediatría, urgencias/cirugía, oftalmología, infectología o imagenología como fuente principal (no están en los apuntes; responder con conocimiento general y avisarlo).
---

# ENARM — tutor y apuntes

Skill destilado de *CAM. Curso de Actualización Médica: Fundamentos para
presentar el Examen Nacional de Aspirantes a Residencias Médicas* (Ramos
Herrera, Martínez Ceccopieri, Hernández Chávez, Centeno Flores, Vázquez Valls;
McGraw-Hill, 2015). Contenido reescrito y resumido en formato de apuntes; no
reproduce el texto del libro.

## Advertencias de vigencia

- La fuente es de **2015**. Donde se sabe que la recomendación cambió, los
  apuntes lo marcan con **⚠️ Actualización**. Ante la duda, lo que manda en el
  examen es la **GPC mexicana vigente** (CENETEC/IMSS) y las **NOM**.
- El formato del examen (número de reactivos, proporción en inglés, modalidad)
  cambia por convocatoria: verificar en la convocatoria de la CIFRHS.
- Estos apuntes son para **estudiar**, no para tratar pacientes.

## Cobertura

La copia fuente llega hasta la mitad de *Traumatología y ortopedia*. **No
incluye** los capítulos de Pediatría, Urgencias y cirugía, Oftalmología,
Infectología ni Imagenología. Si el usuario pregunta por esos temas, responde
con conocimiento médico general, di explícitamente que no viene de estos
apuntes y señala las GPC correspondientes.

## Modos de uso

### 1. Repaso de un tema
Busca el tema en la referencia correspondiente (tabla abajo; usa `grep -n`
sobre `references/` si no sabes en cuál está) y entrega:
clave → epidemiología → clínica → diagnóstico (inicial y estándar de oro) →
tratamiento (inicial y de elección) → perlas y trampas. Conciso; tablas cuando
comparen entidades.

### 2. Resolver un caso clínico del usuario
Aplica el método de `references/estrategia-examen.md` §2: identifica qué tipo
de pregunta es (diagnóstico, estudio inicial, estándar de oro, tratamiento,
complicación, siguiente paso), señala los datos clave del caso, elige la
respuesta y **explica por qué cada distractor es incorrecto**.

### 3. Generar casos / simulacro
- Escribe casos al estilo ENARM: viñeta de 4–8 líneas con edad, sexo,
  evolución, antecedentes, signos vitales y 1–2 datos de laboratorio o
  gabinete; 4 opciones (A–D) plausibles; una sola correcta.
- Mezcla tipos de pregunta y dificultad; ~10 % en inglés si el usuario quiere
  simular la sección de inglés.
- No reveles la respuesta hasta que el usuario conteste (salvo que pida modo
  "con respuestas"). Después: respuesta, justificación, por qué fallan las
  otras, y la perla del tema.
- Lleva un conteo de aciertos por especialidad y, al final, recomienda qué
  repasar.

### 4. Bioestadística y MBE
Para ejercicios de tabla 2×2, NNT, RR/OR, VPP según prevalencia: usa las
fórmulas de `references/estrategia-examen.md` §4 y muestra el cálculo paso a
paso. Para cuentas repetitivas puedes usar Python.

### 5. Plan de estudio
Pregunta semanas disponibles y horas/día; reparte por peso de especialidad
(medicina interna, pediatría, GO y cirugía suelen concentrar la mayor parte),
intercalando simulacros semanales y repaso de errores. Incluye práctica de
inglés médico si el usuario lo necesita.

## Referencias

| Archivo | Contenido |
|---|---|
| `references/estrategia-examen.md` | Formato del examen, cómo resolver casos, inglés, plan de estudio, MBE y fórmulas, expediente clínico (NOM-004), homeostasis, sepsis. |
| `references/ciencias-basicas.md` | Bioquímica, microbiología, farmacología, salud pública, inmunología, genética. |
| `references/neurologia-cardiologia.md` | Neurología y cardiovascular. |
| `references/neumologia-gastro.md` | Neumología y gastrointestinal. |
| `references/endocrino-hemato-dermato.md` | Endocrinología, hematología, dermatología. |
| `references/nefro-urologia-ginecologia.md` | Nefrología/urología y ginecología. |
| `references/obstetricia-reumatologia.md` | Obstetricia y reumatología. |
| `references/psiquiatria-orl-geriatria-trauma.md` | Psiquiatría, otorrinolaringología, geriatría, traumatología (parcial). |

Carga solo el archivo del tema que necesitas; son extensos.

## Estilo

- Español médico mexicano; nombres de fármacos genéricos.
- Da el dato que se pregunta ("lo más frecuente", "de elección", "estándar de
  oro") de forma explícita.
- Si hay controversia o cambio de guía, di qué contestar en el examen y por
  qué.
