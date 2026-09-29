# Carruseles de Instagram: mnemotecnias ENARM

Láminas de 1080×1350 (formato 4:5), listas para subir en orden.

| Carrusel | Fuente | Imágenes | Pie de foto | Zip |
|---|---|---|---|---|
| Obstetricia | `carrusel.html` | `png/obstetricia-01…07.png` | `pie-de-foto.txt` | `carrusel-obstetricia-enarm.zip` |
| Pediatría | `pediatria.html` | `png/pediatria-01…07.png` | `pie-de-foto-pediatria.txt` | `carrusel-pediatria-enarm.zip` |
| Cardio, neuro, gastro, dermato y cirugía | `especialidades.html` | `png/especialidades-01…07.png` | `pie-de-foto-especialidades.txt` | `carrusel-especialidades-enarm.zip` |
| Cardiología (5 temas) | `cardiologia.html` | `png/cardiologia-01…07.png` | `pie-de-foto-cardiologia.txt` | `carrusel-cardiologia-enarm.zip` |
| Neurología (5 temas) | `neurologia.html` | `png/neurologia-01…07.png` | `pie-de-foto-neurologia.txt` | `carrusel-neurologia-enarm.zip` |
| Gastroenterología (5 temas) | `gastro.html` | `png/gastro-01…07.png` | `pie-de-foto-gastro.txt` | `carrusel-gastro-enarm.zip` |
| Dermatología (5 temas) | `dermatologia.html` | `png/dermatologia-01…07.png` | `pie-de-foto-dermatologia.txt` | `carrusel-dermatologia-enarm.zip` |
| Cirugía (5 temas) | `cirugia.html` | `png/cirugia-01…07.png` | `pie-de-foto-cirugia.txt` | `carrusel-cirugia-enarm.zip` |

`fuentes/` contiene Montserrat y Plus Jakarta Sans (licencia OFL).

Los carruseles por especialidad se generan desde `generar.py` (contenido y diseño en un solo lugar):

```
python3 generar.py
for e in cardiologia neurologia gastro dermatologia cirugia; do node render.js $e.html $e; done
```

Para regenerar las imágenes después de editar (usa Playwright):

```
node render.js                              # obstetricia
node render.js pediatria.html pediatria     # pediatría
node render.js especialidades.html especialidades
```
