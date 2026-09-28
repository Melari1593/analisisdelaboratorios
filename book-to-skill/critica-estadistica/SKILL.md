---
name: critica-estadistica
description: Detecta y evita estadísticas engañosas — muestras sesgadas, promedios mal elegidos, cifras sin margen de error ni tamaño de muestra, diferencias insignificantes presentadas como hallazgos, gráficas con ejes truncados o pictogramas desproporcionados, cifras "semiatadas" que prueban otra cosa, correlación confundida con causa, porcentajes con base cambiante, índices manipulables y extrapolaciones absurdas. Úsalo SIEMPRE que el usuario pida revisar, auditar o interpretar un dato, estudio, encuesta, reporte, anuncio, paper, gráfica o dashboard ("¿esto es cierto?", "¿qué tan confiable es este estudio?", "revisa esta gráfica", "¿este resultado es significativo?"), y también cuando TÚ vayas a reportar resultados, promedios, porcentajes o gráficas (reportes de laboratorio, análisis de datos, presentaciones) para no caer en las mismas trampas — aunque el usuario no diga "estadística". NO usar para enseñar fórmulas estadísticas desde cero ni para diseñar un análisis estadístico formal completo (potencia, modelos) — este skill es de pensamiento crítico y reporte honesto.
---

# Crítica estadística

Skill destilado de *How to Lie with Statistics* (Darrell Huff, 1954). El
contenido está reescrito y resumido; los ejemplos se parafrasean y se agregan
equivalentes de laboratorio y ciencia de datos.

## Idea central

Una cifra puede ser correcta y aun así engañar. Casi nunca hace falta mentir:
basta con elegir la muestra, el tipo de promedio, la base del porcentaje, el
eje de la gráfica o la comparación que convienen, y omitir el dato que lo
delataría. Los errores "honestos" también engañan, y cuando todos favorecen a
quien los publica, ya no parecen accidentes.

No se trata de desconfiar de toda estadística, sino de mirarla dos veces.

## Dos modos de uso

### Modo A — Auditar una cifra ajena

Aplica las **cinco preguntas** en orden y reporta lo que encuentres:

1. **¿Quién lo dice?** ¿Tiene interés en el resultado (ventas, reputación,
   financiamiento, una buena nota periodística)? ¿Se usa un "nombre de
   autoridad" (universidad, laboratorio, médicos) que aportó los datos pero no
   la conclusión?
2. **¿Cómo lo sabe?** ¿De qué muestra sale? ¿Es aleatoria o se autoseleccionó
   (quien respondió la encuesta, quien llegó a consulta)? ¿Es suficientemente
   grande? ¿Se midió lo que la gente *hace* o lo que *dice* que hace?
3. **¿Qué falta?** Tamaño de muestra, margen de error o significancia, tipo de
   promedio, rango o dispersión, cifras absolutas detrás de los porcentajes,
   grupo de comparación, base del índice, otros factores que explican el
   cambio.
4. **¿Cambió el tema?** ¿La conclusión habla de algo distinto a lo que se
   midió? (casos *reportados* ≠ casos reales; matar gérmenes in vitro ≠ curar
   resfriados; correlación ≠ causa; cambio en la definición o en la forma de
   registrar).
5. **¿Tiene sentido?** Haz la cuenta de orden de magnitud. ¿La precisión es
   creíble (¿$40.13?)? ¿La extrapolación lleva a un absurdo si la estiras?

Cierra con un veredicto: qué *sí* se puede concluir, qué no, y qué dato haría
falta para decidirlo.

### Modo B — Reportar tus propios resultados sin engañar

Antes de entregar un número, tabla o gráfica, verifica:

- [ ] Digo qué promedio uso (media, mediana, moda) y elegí el adecuado a la
      forma de la distribución; si es asimétrica, reporto la mediana.
- [ ] Doy n, y un intervalo o error (± / IC 95 %) junto a cada estimación.
- [ ] Doy rango o dispersión, no solo el centro.
- [ ] Porcentajes acompañados de la cifra absoluta; nada de "33 %" con n = 3.
- [ ] Distingo *puntos porcentuales* de *porcentaje*; declaro la base de cada
      cambio porcentual.
- [ ] No declaro "diferencia" entre valores que caen dentro del error.
- [ ] Una diferencia significativa también debe ser relevante (tamaño de
      efecto).
- [ ] La precisión reportada no excede la de la medición.
- [ ] No infiero causa de una correlación sin diseño que lo respalde; menciono
      terceros factores plausibles.
- [ ] No extrapolo fuera del rango de los datos sin decirlo.
- [ ] Gráficas: eje de magnitudes desde cero (o corte marcado), proporciones
      honestas, pictogramas escalados por área, números visibles.
- [ ] Comparaciones con el mismo periodo, definición y método de registro.

## Referencias

| Archivo | Cuándo leerlo |
|---|---|
| `references/catalogo-trampas.md` | Identificar y nombrar la trampa concreta (10 familias), con señales de alerta, corrección y ejemplo de laboratorio. |
| `references/graficas.md` | Revisar o producir gráficas, pictogramas y mapas; incluye reglas para matplotlib/plotly. |
| `references/calculos.md` | Porcentajes, base cambiante, puntos porcentuales, descuentos encadenados, índices, márgenes de error, eventos raros, intereses. |
| `scripts/verificar.py` | Recalcular rápido: cambio %, IC de una proporción, tamaño de muestra para eventos raros, índices aritmético vs geométrico, descuentos encadenados, ganancia sobre costo vs precio. |

Uso del script:

```bash
python scripts/verificar.py --help
python scripts/verificar.py proporcion 9 12          # IC 95 % de 9/12
python scripts/verificar.py raro 0.002 2              # n para esperar 2 casos si p=0.2 %
python scripts/verificar.py cambio 3 6                # 3 % → 6 %: +3 pp, +100 %
```

## Tono

Sé específico y sin sarcasmo: nombra la trampa, muestra la cuenta, di qué dato
falta. Si la cifra resiste el escrutinio, dilo también — rechazar la
estadística en bloque es tan irracional como aceptarla en bloque.
