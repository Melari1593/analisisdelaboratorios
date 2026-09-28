# Gráficas, pictogramas y mapas honestos

## Trampas

| Trampa | Cómo engaña | Cómo detectarla |
|---|---|---|
| **Eje truncado** | Quitar la parte baja del eje hace que un aumento de 10 % ocupe media gráfica. | El eje de valores no empieza en cero y no hay corte marcado. Calcula el cambio relativo real con los números del eje. |
| **Escala estirada** | Cambiar la proporción alto/ancho (cada marca vale menos) vuelve dramática una pendiente suave. | Compara el cambio relativo con la inclinación visual. |
| **Barras cortadas** | Eliminar el tramo medio de las barras exagera la diferencia entre ellas. | Barras cuyo largo no es proporcional al valor. |
| **Sin números** | Una línea que sube sin valores puede ser +1 $ o +1 M$. | Ejes sin escala ni unidades. |
| **Pictograma escalado en altura** | Duplicar la altura de un ícono cuadruplica su área y octuplica su volumen aparente: se dice "2×" y se ve "4–8×". | Íconos de distinto tamaño en vez de repetidos. |
| **Ícono que sugiere otra cosa** | Una vaca más grande sugiere vacas más grandes, no más vacas. | Tamaño de objeto usado para representar cantidad. |
| **Mapa sombreado por área** | Colorear estados extensos y poco poblados hace que una proporción de ingreso o población parezca enorme. | La variable no es territorial pero se representa con superficie. |
| **Dos gráficas, dos historias** | Montos absolutos vs cambio porcentual de los mismos datos llevan a conclusiones opuestas. | Pregunta qué pasaría con la otra representación; a menudo conviene mostrar ambas. |
| **Barras de ancho variable** | Cambiar ancho y largo para un solo factor. | Ancho no constante. |
| **Objetos en 3D** | Volúmenes imposibles de comparar a ojo. | Efectos 3D en datos 1D. |

## Reglas para producir gráficas

1. **Barras y áreas empiezan en cero, siempre.** La longitud o el área codifica
   el valor.
2. **Líneas pueden no empezar en cero** si el interés es la variación (p. ej.
   temperatura corporal, pH), pero entonces:
   - dilo en el eje o en una nota, y
   - no titules con el cambio visual ("se dispara") sino con el real ("+10 %").
3. Si cortas un eje, **marca el corte** (símbolo de quiebre) de forma visible.
4. **Proporción de aspecto neutral**: la pendiente debe verse como lo que es;
   no ajustes el alto para exagerar.
5. **Pictogramas**: repite íconos del mismo tamaño (1 ícono = N unidades) o, si
   escalas uno, escálalo por **área** (lado × √razón), nunca por altura.
6. **Mapas coropléticos**: usa tasas (por habitante, por muestra), no conteos;
   considera cartogramas si la superficie distrae.
7. **Muestra números**: etiquetas de valor o ejes con escala y unidades;
   incluye n.
8. **Incertidumbre visible**: barras de error o bandas de IC; di qué
   representan (DE, EE, IC 95 %).
9. **Mismas escalas** al comparar paneles (ejes compartidos).
10. **Rango y distribución** cuando el promedio no basta: boxplots, puntos
    individuales, histogramas.

## Chequeo rápido en código

matplotlib:

```python
ax.set_ylim(bottom=0)                     # barras / áreas
ax.bar(x, y); ax.bar_label(ax.containers[0])  # valores visibles
ax.errorbar(x, y, yerr=ic, fmt="none", capsize=3)
fig, axs = plt.subplots(1, 2, sharey=True)    # escalas comparables
```

plotly:

```python
fig.update_yaxes(rangemode="tozero")
fig.update_traces(texttemplate="%{y}", textposition="outside")
```

Al revisar una gráfica ajena, recalcula: *cambio real = (final − inicial) /
inicial* y compáralo con la impresión visual. Si la gráfica "dice" 3× y el
número dice 1.04×, repórtalo.
