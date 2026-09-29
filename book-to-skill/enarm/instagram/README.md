# Carruseles de Instagram: mnemotecnias ENARM

Láminas de 1080×1350 (formato 4:5), listas para subir en orden.

| Carrusel | Fuente | Imágenes | Pie de foto | Zip |
|---|---|---|---|---|
| Obstetricia | `carrusel.html` | `png/obstetricia-01…07.png` | `pie-de-foto.txt` | `carrusel-obstetricia-enarm.zip` |
| Pediatría | `pediatria.html` | `png/pediatria-01…07.png` | `pie-de-foto-pediatria.txt` | `carrusel-pediatria-enarm.zip` |
| Cardio, neuro, gastro, dermato y cirugía | `especialidades.html` | `png/especialidades-01…07.png` | `pie-de-foto-especialidades.txt` | `carrusel-especialidades-enarm.zip` |

`fuentes/` contiene Montserrat y Plus Jakarta Sans (licencia OFL).

Para regenerar las imágenes después de editar (usa Playwright):

```
node render.js                              # obstetricia
node render.js pediatria.html pediatria     # pediatría
node render.js especialidades.html especialidades
```
