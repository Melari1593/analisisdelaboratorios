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
| Endocrinología (5 temas) | `contenido/endocrinologia.py` | `png/endocrinologia-01…07.png` | `pie-de-foto-endocrinologia.txt` | `carrusel-endocrinologia-enarm.zip` |
| Geriatría (5 temas) | `contenido/geriatria.py` | `png/geriatria-01…07.png` | `pie-de-foto-geriatria.txt` | `carrusel-geriatria-enarm.zip` |
| Ginecología (5 temas) | `contenido/ginecologia.py` | `png/ginecologia-01…07.png` | `pie-de-foto-ginecologia.txt` | `carrusel-ginecologia-enarm.zip` |
| Hematología (5 temas) | `contenido/hematologia.py` | `png/hematologia-01…07.png` | `pie-de-foto-hematologia.txt` | `carrusel-hematologia-enarm.zip` |
| Infectología (5 temas) | `contenido/infectologia.py` | `png/infectologia-01…07.png` | `pie-de-foto-infectologia.txt` | `carrusel-infectologia-enarm.zip` |
| Nefrología (5 temas) | `contenido/nefrologia.py` | `png/nefrologia-01…07.png` | `pie-de-foto-nefrologia.txt` | `carrusel-nefrologia-enarm.zip` |
| Neumología (5 temas) | `contenido/neumologia.py` | `png/neumologia-01…07.png` | `pie-de-foto-neumologia.txt` | `carrusel-neumologia-enarm.zip` |
| Oftalmología (5 temas) | `contenido/oftalmologia.py` | `png/oftalmologia-01…07.png` | `pie-de-foto-oftalmologia.txt` | `carrusel-oftalmologia-enarm.zip` |
| Otorrinolaringología (5 temas) | `contenido/otorrino.py` | `png/otorrino-01…07.png` | `pie-de-foto-otorrino.txt` | `carrusel-otorrino-enarm.zip` |
| Psiquiatría (5 temas) | `contenido/psiquiatria.py` | `png/psiquiatria-01…07.png` | `pie-de-foto-psiquiatria.txt` | `carrusel-psiquiatria-enarm.zip` |
| Reumatología (5 temas) | `contenido/reumatologia.py` | `png/reumatologia-01…07.png` | `pie-de-foto-reumatologia.txt` | `carrusel-reumatologia-enarm.zip` |
| Traumatología y ortopedia (5 temas) | `contenido/traumatologia.py` | `png/traumatologia-01…07.png` | `pie-de-foto-traumatologia.txt` | `carrusel-traumatologia-enarm.zip` |
| Urología (5 temas) | `contenido/urologia.py` | `png/urologia-01…07.png` | `pie-de-foto-urologia.txt` | `carrusel-urologia-enarm.zip` |

`fuentes/` contiene Montserrat y Plus Jakarta Sans (licencia OFL).

Los carruseles por especialidad se generan desde `generar.py`. El contenido de cardio, neuro, gastro, dermato y cirugía está en ese archivo; el de las demás, en `contenido/<especialidad>.py`:

```
python3 generar.py            # todas; o: python3 generar.py neumologia hematologia
node render.js neumologia.html neumologia   # una por una
```

Para regenerar las imágenes después de editar (usa Playwright):

```
node render.js                              # obstetricia
node render.js pediatria.html pediatria     # pediatría
node render.js especialidades.html especialidades
```
