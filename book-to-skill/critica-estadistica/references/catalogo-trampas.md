# Catálogo de trampas

Diez familias, siguiendo los capítulos del libro. Para cada una: qué es,
señales de alerta, cómo corregir, ejemplo del libro (parafraseado) y un
equivalente en laboratorio o ciencia de datos.

---

## 1. Muestra con sesgo incorporado

**Qué es.** El resultado de un muestreo no es mejor que la muestra. Una muestra
sesgada, pequeña o ambas puede ser peor que una buena estimación a ojo, pero se
ve "científica".

**Fuentes de sesgo.**
- *Autoselección / no respuesta*: responde quien quiere (o quien tiene algo que
  presumir). Encuesta a exalumnos: los que no se encuentran o no contestan
  suelen ganar menos → el ingreso "promedio" sale inflado.
- *Marco muestral no representativo*: la encuesta de *Literary Digest* (1936)
  usó listas de dueños de teléfono y suscriptores → predijo mal la elección.
- *Población de conveniencia*: el psiquiatra que concluye que "casi todos son
  neuróticos" observando a sus propios pacientes.
- *Decir ≠ hacer*: la gente reporta lo socialmente aceptable (revistas que
  "lee", frecuencia de baño o de cepillado).
- *Efecto del entrevistador*: el mismo cuestionario da resultados distintos
  según quién pregunta.
- *Registros reconstruidos hacia atrás*: datos históricos recuperados después
  pierden a quienes se fueron o murieron → mejora falsa de supervivencia.
- *Sesgo del muestreador*: al elegir a quién entrevistar, se tiende a gente más
  accesible, educada y "presentable".
- *Muestreo estratificado con proporciones o clasificaciones erróneas*.

**Prueba de aleatoriedad.** ¿Cada elemento del universo tuvo la misma
probabilidad de entrar en la muestra?

**Señales de alerta.** No se dice cómo se eligió la muestra; tasa de respuesta
baja o ausente; preguntas sobre temas íntimos o con respuesta "correcta";
cifras sorprendentemente precisas o favorables.

**Corrección.** Reportar marco muestral, método de selección, tasa de
respuesta y comparación de respondientes vs no respondientes; medir conducta
en vez de preguntar cuando se pueda.

**Laboratorio.** Valores de referencia calculados solo con pacientes que
acudieron por síntomas; controles de calidad elegidos "cuando la corrida salió
bien"; estudios con pérdida de seguimiento no reportada; muestras hemolizadas
o rechazadas excluidas sin decirlo.

---

## 2. El promedio bien escogido

**Qué es.** "Promedio" puede ser media, mediana o moda. Con distribuciones
simétricas (estatura) coinciden; con distribuciones sesgadas (ingresos,
concentraciones, tiempos de respuesta) difieren mucho, y quien reporta elige
el que le conviene.

**Ejemplos del libro.** El mismo vecindario tiene ingreso "promedio" alto
(media, inflada por tres millonarios) o bajo (mediana), según convenga. Una
empresa mezcla el sueldo de los dueños con el de los obreros y reporta la
media. Un ingreso "familiar" calculado como ingreso per cápita × 4.

**Señales de alerta.** "Promedio" sin especificar en datos que suelen ser
asimétricos; cambiar de tipo de promedio entre dos comparaciones; mezclar
grupos heterogéneos en un solo promedio.

**Corrección.** Nombrar el estadístico; para datos asimétricos usar mediana y
rango intercuartílico; mostrar el histograma; separar subgrupos.

**Laboratorio.** Concentraciones de biomarcadores, cargas virales, títulos y
tiempos de entrega de resultados suelen ser log-normales → reportar mediana o
media geométrica, no media aritmética.

---

## 3. Las cifras pequeñas que no están

**Qué es.** El dato que falta cambia todo: tamaño de muestra, significancia,
rango, unidades, grupo de comparación.

**Formas.**
- *Muestra diminuta + repetir hasta que salga*: con 12 personas, tarde o
  temprano un grupo muestra "23 % menos caries" por azar; se publican solo los
  intentos favorables. (Hoy: *p-hacking*, sesgo de publicación).
- *Evento raro con muestra insuficiente*: un ensayo de vacuna con ~1 100 niños
  en el que se esperaban ~2 casos no podía mostrar nada; hacían falta 15–25
  veces más niños.
- *Sin significancia*: no se dice qué probabilidad hay de que el resultado sea
  azar.
- *Sin rango*: "familia promedio de 3.6 personas" → se construyeron casas para
  una familia que es minoría; "el niño se sienta a los X meses" → la mitad de
  los padres se alarma sin razón. Una temperatura media de 61 °F puede esconder
  15–104 °F.
- *Palabras vagas*: "disponible", "triplica la dureza" (¿de qué, comparado con
  qué?).
- *Gráficas sin números en los ejes*.

**Corrección.** Siempre n, intervalo/p, rango o percentiles; definir cada
término; declarar todos los análisis hechos, no solo el que salió.

**Laboratorio.** "El nuevo método mejora la sensibilidad" sin n, sin IC y sin
decir contra qué referencia; reportar el promedio de un control sin su CV;
declarar un resultado "normal" sin dar el intervalo de referencia.

---

## 4. Mucho ruido por casi nada

**Qué es.** Tratar diferencias dentro del error de medición como reales, o
exagerar diferencias reales pero triviales.

**Ejemplos del libro.** CI de 98 vs 101 con error probable de ±3: no se puede
decir quién es "más inteligente". Un editor que exige más artículos como el
que tuvo 40 % de lectura masculina vs 35 %, con un puñado de hombres en la
muestra. Una marca de cigarros que resultó "la más baja" en un análisis donde
todas eran prácticamente idénticas, y lo convirtió en campaña publicitaria.

**Regla.** Piensa en rangos, no en puntos. "Una diferencia solo es diferencia
si hace una diferencia": significancia estadística ≠ relevancia práctica.

**Corrección.** Reportar IC de la diferencia; definir de antemano la
diferencia mínima relevante; no rankear elementos cuyos intervalos se traslapan.

**Laboratorio.** Dos resultados seriados de creatinina que difieren menos que
el *valor de referencia de cambio* (RCV, que combina variación analítica y
biológica) no indican cambio real; un proveedor "mejor" por 0.1 % de sesgo con
IC que incluye cero.

---

## 5. La gráfica "¡guau!"

Ver `graficas.md`. Resumen: truncar el eje vertical o estirar su escala
convierte un 10 % en una escalada dramática sin cambiar ningún número.

---

## 6. La imagen unidimensional

Ver `graficas.md`. Resumen: dibujar un ícono el doble de alto lo hace 4 veces
más grande en área y 8 veces en volumen aparente; además puede sugerir que el
objeto mismo creció (vacas más grandes).

---

## 7. La cifra semiatada

**Qué es.** Si no puedes probar lo que quieres, prueba otra cosa y preséntala
como si fuera lo mismo.

**Formas.**
- *Proxy irrelevante*: el antiséptico mata X gérmenes en un tubo de ensayo →
  "cura resfriados". "27 % de los médicos fuma esta marca" → ¿y qué?
- *Comparación con un referente débil*: "26 % más jugo"… que un exprimidor
  manual.
- *Conteos sin tasa (sin denominador)*: más muertes a las 7 p.m. que a las
  7 a.m., o en días despejados que con niebla → simplemente hay más gente
  manejando / más días despejados. Pide la tasa por exposición (por millón de
  pasajero-km).
- *Grupos no comparables*: la mortalidad de la Marina (hombres jóvenes y sanos)
  vs la de la población civil (incluye bebés, ancianos, enfermos).
- *Cambios en el registro*: más casos reportados por mayor conciencia,
  diagnóstico, incentivos económicos o nuevas obligaciones de notificación; una
  enfermedad "desaparece" cuando se exige confirmación. A veces las muertes
  son mejor indicador que los casos porque se registran mejor.
- *Pregunta que mide otra cosa*: quienes tienen más prejuicio responden que
  hay igualdad de oportunidades → una encuesta que "mejora" cuando la
  situación empeora.
- *Reetiquetar*: sumar quejas menores y llamarlo "oposición"; esconder
  utilidades como depreciación o reservas.
- *Elegir la expresión*: el mismo resultado es 1 % sobre ventas, 15 % sobre
  inversión, +40 % contra un periodo base, o −60 % contra el año anterior.
- *Antes y después con otras variables cambiadas*: el mínimo rural de antes vs
  el rango urbano de después; la foto con otra luz y otra sonrisa.

**Corrección.** Preguntar "¿qué se midió exactamente?" y "¿qué se concluye?";
exigir tasas con denominador de exposición; comparar grupos equivalentes
(estandarizar por edad, etc.).

**Laboratorio.** Actividad in vitro presentada como eficacia clínica; "más
pruebas positivas este mes" cuando aumentó el número de pruebas realizadas
(reportar tasa de positividad); cambio de reactivo, calibrador o punto de
corte entre periodos comparados.

---

## 8. Post hoc (correlación ≠ causa)

**Qué es.** "B vino después de A (o junto con A), luego A causó B".

**Tipos de correlación a distinguir.**
1. *Por azar*: con muestras pequeñas y muchos intentos, siempre aparece alguna.
2. *Real, pero con dirección incierta o bidireccional* (ingreso ↔ acciones).
3. *Real, sin causalidad directa: un tercer factor causa ambas* — el caso más
   común y más explotado. Salarios de ministros y precio del ron suben juntos
   por la inflación; el cáncer es más frecuente donde se toma más leche porque
   allí la gente vive más años; las mujeres mayores caminan con los pies más
   abiertos porque así se les enseñó de jóvenes (efecto de cohorte, no de edad).
4. *Causalidad invertida*: en las Nuevas Hébridas "los piojos dan salud" —
   en realidad, la fiebre ahuyenta a los piojos.

**Otras advertencias.**
- *Extrapolar la correlación fuera del rango*: más lluvia → más cosecha, hasta
  que el exceso la arruina.
- *Aplicar una tendencia de grupo a un individuo*: una correlación real puede
  servir de poco para decidir un caso particular.
- *Tendencias de época*: cualquier par de series que crecen con el tiempo
  correlacionan.
- *Datos transversales para conclusiones longitudinales*: comparar grupos de
  edad hoy no dice cómo cambia una persona al envejecer.

**Corrección.** Buscar confusores y cohortes; ver si la relación se sostiene
dentro de subgrupos; preferir diseños experimentales o longitudinales; decir
explícitamente "asociación, no causalidad demostrada".

**Laboratorio.** Un marcador que "predice" mortalidad porque se pide más en
pacientes graves (sesgo de indicación); relación dosis-respuesta extrapolada
fuera del rango estudiado; muestras procesadas por lote donde el lote confunde
el efecto.

---

## 9. Cómo "estadisticular" (manipulación y error)

Ver `calculos.md` para las cuentas. Familias:

- *Mapas* que sombrean áreas grandes y poco pobladas para exagerar
  (ver `graficas.md`).
- *Promedios fabricados*: per cápita × tamaño de familia.
- *Precisión falsa*: 7.831 horas de sueño a partir de estimaciones al cuarto de
  hora; decimales sobre supuestos redondeados.
- *Porcentajes sobre n minúsculo*: 4.9 % = 2 de 41.
- *Confusión de base*: "ahorre 100 %", reducciones de más de 100 %, ganancia
  de 3 800 %.
- *Base cambiante*: recortar 20 % y "devolver una cuarta parte" con +5 %.
- *Error de escala*: 0.00063 cuando es 0.063 %.
- *Descuentos encadenados*: 50 % + 20 % = 60 %, no 70 %.
- *Sumar lo que no se suma*: horas de sueño + comida + vacaciones que dejan sin
  días de escuela; aumentos porcentuales de partidas de costo que se "suman".
- *Promedios sin ponderar*: promediar tarifas horarias distintas sin pesos.
- *Puntos porcentuales vs porcentaje*.
- *Percentiles*: separan mucho en los extremos y casi nada en el centro.
- *Elegir el año base favorable* para comparar productividad o salarios.
- *Dos gráficas con los mismos datos*: montos absolutos vs cambios porcentuales
  cuentan historias opuestas.
- *Índices*: con los mismos precios, según la base y el tipo de promedio, el
  costo de vida sube 25 %, baja 25 % o no cambia.

El libro insiste en que no todo es mala fe; pero cuando todos los errores
caen del mismo lado, es difícil llamarlos accidentes.

---

## 10. Cómo responderle a una estadística

Las cinco preguntas del SKILL.md, con ejemplos adicionales de lo que suele
faltar:

- *Solo porcentaje*: "33 % de las mujeres se casó con profesores" = 1 de 3.
- *Promedio que oculta concentración*: 3 003 accionistas con 660 acciones en
  promedio, pero tres personas tienen tres cuartas partes.
- *Sin punto de comparación*: "la mitad de las madres tenía 35 años o más" —
  ¿cuál es la proporción en la población general?
- *Sin contexto temporal*: un pico de mortalidad semanal sin saber la variación
  normal ni si después hubo un descenso compensatorio.
- *Sin el factor que explica el cambio*: ventas de abril mayores… porque la
  Pascua cayó en abril.
- *Cambio de definición*: "más granjas" porque cambió la definición de granja.
- *Redondeo y amontonamiento*: más personas de 35 que de 34 o 36 años (se
  redondea a múltiplos de 5); pedir fecha de nacimiento.
- *Incentivos para declarar*: un censo para impuestos vs otro para ayuda
  alimentaria dan poblaciones muy distintas.
- *Comparación de costos distintos*: costo total de un preso vs solo la tarifa
  del hotel.
- *"Primero en…"* cualquier cosa si se define bien la categoría.
- *Tasas de interés* "6 %" que en realidad son ~12 % o ~48 % anual.
- *Palabras eufemísticas* ("utilidades retenidas" por "superávit").
- *Fórmulas que reducen juicio a número* sin validar el supuesto (índices de
  legibilidad).
- *Cifras imposibles*: más casos estimados que personas susceptibles.
- *Esperanza de vida al nacer* confundida con edad típica de muerte de adultos.
- *Extrapolación sin control*: televisores por familia, población, o el río
  Mississippi de Mark Twain que en el pasado medía más de un millón de millas.
