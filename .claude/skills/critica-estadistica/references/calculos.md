# Cuentas que conviene rehacer

Todas se pueden verificar con `scripts/verificar.py`.

## Porcentajes

**Cambio porcentual:** `(nuevo − viejo) / viejo × 100`. La base es el valor
*anterior*.

**Puntos porcentuales vs porcentaje.** De 3 % a 6 %: +3 puntos porcentuales,
o +100 %. Ambos correctos; usar uno u otro según convenga es manipulación.
Reporta los dos cuando haya duda.

**Base cambiante.** Un recorte de 20 % seguido de un aumento de 5 %:
1.00 → 0.80 → 0.84. Se recuperó 0.04 de 0.20 = una quinta parte, no una cuarta.
Para compensar una caída de 50 % hace falta subir 100 %.

**Reducciones de más de 100 %** son imposibles (salvo que te paguen por
llevártelo). "Ahorre 100 %" en un producto a mitad de precio = 50 % de
descuento, calculado mal sobre el precio nuevo.

**Descuentos encadenados.** 50 % y 20 %: 1 × 0.5 × 0.8 = 0.40 → 60 % de
descuento, no 70 %.

**Sumar aumentos porcentuales de componentes** no da el aumento total. Si cada
partida sube ~10 %, el total sube ~10 % (promedio ponderado por peso de cada
partida), no 30 %.

**Ganancia sobre costo vs sobre precio.** Costo 1.75, precio 40:
- sobre costo: (40 − 1.75) / 1.75 = 2 186 %
- sobre precio (margen): (40 − 1.75) / 40 = 95.6 %
Declara siempre cuál usas.

**Rendimiento sobre ventas vs sobre inversión.** 1 % por venta con rotación
diaria del capital ≈ 365 % anual sobre la inversión.

**Escala del porcentaje.** 4 863 / 7 715 741 = 0.00063 = 0.063 %. Un periódico
lo publicó como "0.00063 %", cien veces menos. Verifica si una fracción ya fue
multiplicada por 100 antes de ponerle el signo %.

**Porcentaje con n pequeño.** 2 de 41 = 4.9 %; 1 de 3 = 33.3 %. Con n < ~30
reporta la fracción, no el porcentaje, y nunca con decimales.

## Promedios

- **Media de tasas no ponderadas** (1 h a 1.50, 1 h a 2.25, 1 h a 3.00 →
  "promedio" 2.25) no significa nada si las horas de cada tipo no son iguales;
  usa el promedio ponderado por cantidad.
- **Per cápita × tamaño de familia** no es ingreso familiar.
- **Media vs mediana** en datos asimétricos: calcula ambas; si difieren mucho,
  la media está dominada por pocos valores extremos.
- **Media geométrica** para razones, índices y datos log-normales.

## Índices

Precios del año 1 → año 2: leche 20 → 10, pan 5 → 10.

| Método | Resultado |
|---|---|
| Media aritmética de relativos, base año 1: (50 + 200)/2 | 125 → "subió 25 %" |
| Media aritmética de relativos, base año 2: (200 + 50)/2 | 125 → "antes era 25 % más caro" |
| Media geométrica de relativos, cualquier base: √(50 × 200) | 100 → "sin cambio" |

Moraleja: pregunta siempre qué base y qué fórmula usa un índice. La media
geométrica es consistente al cambiar la base; la aritmética no. Además, elegir
un año base anormalmente bajo infla cualquier crecimiento posterior.

## Incertidumbre de una estimación

**Proporción** p = x/n. IC 95 % (Wilson, mejor que ±1.96·√(p(1−p)/n) con n
pequeño o p cercano a 0 o 1). Ejemplo: 9/12 = 75 % → IC ≈ 47 %–91 %.

**Diferencia entre dos valores con error.** Si cada valor tiene error estándar
EE, la diferencia tiene EE ≈ √(EE₁² + EE₂²). Si la diferencia es menor que
~2 × ese EE, no es distinguible del azar.

**Error probable vs error estándar.** El error probable (el libro lo usa para
el CI) cubre 50 % de los casos; el error estándar ~68 %; el IC 95 % usa ~1.96
EE. Convierte antes de comparar: EP ≈ 0.674 × EE.

**Laboratorio – valor de referencia de cambio (RCV).**
RCV = √2 × z × √(CVa² + CVi²), con CVa = variación analítica, CVi = variación
biológica intraindividual, z = 1.96 (bilateral, 95 %). Un cambio entre dos
resultados seriados menor que el RCV no es evidencia de cambio real.

## Eventos raros

Si la incidencia es p, en un grupo de n se esperan n·p casos. Con ~2 casos
esperados en el grupo control, ninguna vacuna puede demostrar nada. Para
detectar una reducción razonable se necesitan decenas de eventos esperados en
el grupo control. Calcula primero cuántos eventos esperas.

Regla del 3: si observas 0 eventos en n intentos, el límite superior del IC
95 % de la tasa es ≈ 3/n.

## Precisión falsa

- No reportes más cifras significativas que las de la medición más imprecisa.
- Promediar datos imprecisos no los vuelve precisos si los errores no son
  aleatorios (la gente redondea, exagera o minimiza en una dirección).
- Cálculos largos sobre supuestos redondeados no merecen decimales en el
  resultado.

## Tasas de interés engañosas

"$6 por cada $100" sobre un préstamo que se paga en cuotas mensuales iguales
durante un año equivale a ~11 % anual efectivo, porque en promedio solo tienes
la mitad del dinero. "$12 por cada $100" a seis meses con pagos mensuales
equivale a ~40–48 % anual. Pide la tasa anual efectiva (TAE / CAT).

## Extrapolación

Una tendencia hasta hoy es un hecho; la tendencia futura es una suposición con
"todo lo demás igual" implícito. Estira la extrapolación: si lleva a absurdos
(40 televisores por familia, un río de un millón de millas), el modelo lineal
no aplica. Reporta el rango de validez del ajuste.
