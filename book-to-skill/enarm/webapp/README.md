# Repaso ENARM (app web)

App de estudio independiente: apuntes con buscador, 254 reactivos tipo caso
clínico con explicación de cada opción, calculadora de bioestadística y
seguimiento de progreso. No necesita internet, servidor ni cuenta de Claude.

## Usarla

Abre `dist/repaso-enarm.html` con doble clic en cualquier navegador (también en
el teléfono). El progreso se guarda en ese navegador.

## Estructura

| Archivo | Qué es |
|---|---|
| `index.html` | Página y estilos (versión de desarrollo) |
| `app.js` | Lógica: apuntes, simulacro, calculadora, progreso |
| `banco/*.json` | Reactivos por especialidad |
| `../references/*.md` | Apuntes que muestra la app |
| `build.py` | Empaqueta todo en `dist/` |
| `dist/repaso-enarm.html` | Versión autocontenida para abrir sin conexión |
| `dist/artifact.html` | La misma página para publicarla en claude.ai |

## Agregar reactivos o cambiar apuntes

Edita `banco/*.json` o `../references/*.md` y ejecuta `python3 build.py`.
Cada reactivo lleva `id`, `especialidad`, `tema` (igual a un encabezado `###`
de los apuntes), `caso`, `pregunta`, `opciones` A–D, `correcta`,
`explicacion`, `distractores` y `perla`.

Para desarrollo sin empaquetar, sirve la carpeta con un servidor local
(`python3 -m http.server`) y copia o enlaza `../references` como `apuntes/`.
