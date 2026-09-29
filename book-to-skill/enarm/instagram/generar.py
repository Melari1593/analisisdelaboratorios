#!/usr/bin/env python3
"""Genera un carrusel HTML (portada + 5 temas + resumen) por especialidad.

Toma el <head> y la portada de especialidades.html y arma cada lámina con
bloques simples. Después se renderiza con: node render.js <archivo> <prefijo>

Uso: python3 generar.py
"""
import pathlib
import re

AQUI = pathlib.Path(__file__).resolve().parent
PIE = '<div class="foot"><span>Material de estudio · verifica con GPC vigentes</span><span class="swipe">→</span></div>'


# ---------- bloques ----------
def card(*partes, tag=None, big=None, cls="", estilo=""):
    attr = ' style="%s"' % estilo if estilo else ""
    h = f'<div class="glass card {cls}"{attr}>'
    if tag:
        h += f'<span class="tag">{tag}</span>'
    if big:
        h += f'<p class="big" style="font-size:44px">{big}</p>'
    for p in partes:
        h += p if p.startswith(("<p", "<ul", "<div", "<table")) else f"<p>{p}</p>"
    return h + "</div>"


def muted(t):
    return f'<p class="muted">{t}</p>'


def lista(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def dos(a, b):
    return f'<div class="two">{a}{b}</div>'


def tabla(encabezado, filas):
    h = '<div class="glass card" style="padding:18px 30px"><table>'
    if encabezado:
        h += "<tr>" + "".join(f"<th>{c}</th>" for c in encabezado) + "</tr>"
    for f in filas:
        h += "<tr>" + "".join(f"<td>{c}</td>" for c in f) + "</tr>"
    return h + "</table></div>"


def acr(*pares):
    h = '<div class="glass card acr">'
    for letra, texto in pares:
        h += f'<b class="g">{letra}</b><span>{texto}</span>'
    return h + "</div>"


def rima(t):
    return f'<div class="rima">{t}</div>'


def h2(negro, color, size=None):
    s = f' style="font-size:{size}px"' if size else ""
    return f'<h2{s}>{negro}<br><span class="g">{color}</span></h2>'


# ---------- contenido ----------
ESPECIALIDADES = {
    "cardiologia": {
        "nombre": "Cardiología",
        "temas": [
            ("Arritmias y bloqueos AV", "PR que se alarga, se deja; PR fijo que falla, marcapasos", [
                h2("¿Inestable?", "Electricidad"),
                dos(card(muted("Cardioversión sincronizada: la descarga cae en la R, no en la T."), tag="Con pulso", big="Sincroniza"),
                    card(muted("FV o TV sin pulso: descarga no sincronizada + RCP."), tag="Sin pulso", big="Desfibrila")),
                tabla(["Bloqueo AV", "PR", "Conducta"], [
                    ["<b>Mobitz I</b>", "Se <b>alarga</b> hasta que falla", "Se deja"],
                    ["<b>Mobitz II</b>", "<b>Fijo</b> y de pronto falla", '<b class="g">Marcapasos</b>'],
                    ["<b>3.er grado</b>", "P y QRS sin relación", '<b class="g">Marcapasos</b>']]),
                rima("“PR que se alarga, se deja;<br>PR fijo que falla, marcapasos.”"),
            ]),
            ("Infarto con elevación del ST", "30 para la aguja, 90 para el balón", [
                h2("30 para la aguja,", "90 para el balón"),
                tabla(["Reperfusión", "Meta"], [
                    ["<b>Fibrinólisis</b> (puerta-aguja)", '<span class="wk">≤30 min</span>'],
                    ["<b>Angioplastia</b> (puerta-balón)", '<span class="wk">≤90 min</span>'],
                    ["Ventana de reperfusión", '<span class="wk">≤12 h</span>']]),
                card("Infarto inferior (II, III, aVF): pide <b>V4R</b>. Si el ventrículo derecho está afectado: <b>volumen</b>, y nada de nitratos, morfina ni diuréticos.",
                     big='Ventrículo <span class="g">D</span>erecho = <span class="g">D</span>ale líquidos'),
                rima("Oxígeno solo si la SatO₂ es menor de 90 %. La angioplastia es preferible si se hace en menos de 120 min."),
            ]),
            ("Estenosis aórtica y soplos", "ASI y 5-3-2", [
                h2("Estenosis aórtica:", "ASI y 5-3-2"),
                tabla(["Síntoma", "Sobrevida sin cirugía"], [
                    ['<b class="g">A</b>ngina', '<span class="wk">5 años</span>'],
                    ['<b class="g">S</b>íncope', '<span class="wk">3 años</span>'],
                    ['<b class="g">I</b>nsuficiencia cardiaca', '<span class="wk">2 años</span>']]),
                card("Soplo sistólico en 2.º espacio intercostal derecho que se irradia a carótidas; pulso <i>parvus et tardus</i>. Con síntomas: cambio valvular.",
                     big="Cuenta regresiva: 5, 3, 2"),
                rima("“Al pujar o ponerse de pie, solo suben dos: la miocardiopatía hipertrófica y el prolapso mitral.”"),
            ]),
            ("Insuficiencia cardiaca con FE reducida", "El que SABE, sobrevive", [
                h2("El que SABE,", "sobrevive"),
                acr(("S", "iSGLT2: dapagliflozina o empagliflozina"),
                    ("A", "ARNI (sacubitrilo-valsartán) o IECA/ARA II"),
                    ("B", "Betabloqueador: metoprolol succinato, bisoprolol, carvedilol"),
                    ("E", "Espironolactona (antagonista mineralocorticoide)")),
                card("Son los 4 pilares que <b>reducen mortalidad</b> con FEVI ≤40 %. Los diuréticos de asa alivian la congestión, pero no alargan la vida.",
                     big="4 pilares, 4 letras"),
                rima("“El diurético quita el agua; el SABE quita la muerte.”"),
            ]),
            ("Fármacos con trampa", "Nitrato con sildenafil, presión que se desploma", [
                h2("Fármacos", "con trampa"),
                tabla(["Fármaco", "Prohibido si…"], [
                    ["<b>Nitratos</b>", "Sildenafil &lt;24 h (tadalafil &lt;48 h), infarto de VD, PAS &lt;90"],
                    ["<b>Verapamilo / diltiazem</b>", "FEVI reducida o FA con WPW"],
                    ["<b>Adenosina</b>", "Asma grave o FA preexcitada"],
                    ["<b>IECA / ARA II</b>", "Embarazo o estenosis renal bilateral"],
                    ["<b>ACOD</b>", "Válvula mecánica o estenosis mitral: solo warfarina"]]),
                rima("“Nitrato con sildenafil, presión que se desploma.”<br>“Verapamilo: ni corazón débil ni vía accesoria.”"),
            ]),
        ],
    },
    "neurologia": {
        "nombre": "Neurología",
        "temas": [
            ("Escala de Glasgow", "Ojos 4, Voz 5, Movimiento 6; con ocho, intubo", [
                h2("Ojos 4, Voz 5,", "Movimiento 6"),
                tabla(["Parte", "Máximo", "Mejor respuesta"], [
                    ["<b>Ocular</b>", '<span class="wk">4</span>', "Abre espontáneamente"],
                    ["<b>Verbal</b>", '<span class="wk">5</span>', "Orientado"],
                    ["<b>Motora</b>", '<span class="wk">6</span>', "Obedece órdenes"]]),
                card("Flexión anormal = motor <b>3</b>. Descerebración = extensión = motor <b>2</b>.",
                     big='DeCORticación = brazos al <span class="g">CORazón</span>'),
                rima("“Con ocho, intubo.” Glasgow ≤8 = grave: asegura la vía aérea. 9–12 moderado · 13–15 leve."),
            ]),
            ("EVC isquémico", "TAC sin contraste; 4.5 para la aguja", [
                h2("Tiempo es cerebro:", "4.5 para la aguja"),
                card("Primero <b>TAC simple</b>: descarta sangre antes de dar trombolítico.", big="Sin contraste, sin sangre, con aguja"),
                tabla(["Número", "Qué significa"], [
                    ['<span class="wk">4.5 h</span>', "Ventana para alteplasa IV"],
                    ['<span class="wk">24 h</span>', "Trombectomía en oclusión de vaso grande (con imagen favorable)"],
                    ['<span class="wk">185/110</span>', "Presión máxima para poder trombolizar"],
                    ['<span class="wk">220/120</span>', "Sin trombólisis, solo se baja por encima de esto"]]),
                rima("“Al cerebro isquémico no le quites presión: déjalo con 220.”"),
            ]),
            ("Cefaleas", "La migraña PULSA", [
                h2("La migraña", "PULSA"),
                acr(("P", "Pulsátil"), ("U", "Unilateral"), ("L", "Luz y sonido molestan"),
                    ("S", "Se agrava con la actividad"), ("A", "Asociada a náusea · dura 4–72 h")),
                dos(card(muted("Hombre, ojo que llora, a la misma hora. Crisis: O₂ al 100 % y sumatriptán."), tag="En racimos", big="Hombre, ojo, reloj"),
                    card(muted("“La peor de mi vida”, súbita. TAC simple; si es normal, punción lumbar."), tag="Hemorragia subaracnoidea", big="Cefalea en trueno")),
                rima("“Si pulsa y te apaga la luz, es migraña; si llora el ojo a la misma hora, es racimo.”"),
            ]),
            ("Estado epiléptico", "5 benzo, 20 carga, 40 anestesia", [
                h2("Crisis de 5 minutos", "ya es estado epiléptico"),
                tabla(["Minuto", "Paso"], [
                    ['<span class="wk">0–5</span>', "ABC, glucosa capilar, acceso IV"],
                    ['<span class="wk">5</span>', "<b>Benzodiacepina</b>: lorazepam o midazolam (diazepam si no hay)"],
                    ['<span class="wk">20</span>', "<b>Carga</b>: fenitoína, levetiracetam o valproato"],
                    ['<span class="wk">40</span>', "<b>Anestesia</b>: intubación y midazolam o propofol en infusión"]]),
                card("Si hay hipoglucemia, primero glucosa (con tiamina en alcohólico).", big='5 <span class="g">benzo</span>, 20 <span class="g">carga</span>, 40 <span class="g">anestesia</span>'),
                rima("“Benzo, carga, coma.”"),
            ]),
            ("Guillain-Barré vs. miastenia", "Guillain sube; la miastenia se cansa", [
                h2("Guillain sube;", "la miastenia se cansa"),
                dos(card(lista("Ascendente, simétrica", "<b>Sin reflejos</b>", "Tras diarrea (Campylobacter) o infección respiratoria", "LCR: proteínas ↑, células normales", "IgIV o plasmaféresis; <b>no</b> esteroides"), tag="Guillain-Barré"),
                    card(lista("Ptosis y diplopía", "<b>Empeora al usarse</b> y por la tarde", "Reflejos normales", "Anticuerpos anti-receptor de acetilcolina", "Piridostigmina; TAC de tórax (timoma)"), tag="Miastenia gravis")),
                rima("“Guillain sube desde los pies y se lleva los reflejos.”<br>“Miastenia: más se usa, más se cansa.”"),
            ]),
        ],
    },
    "gastro": {
        "nombre": "Gastroenterología",
        "temas": [
            ("Hepatitis B", "Antígeno S = Sí está; anticuerpo S = Salvado", [
                h2("Antígeno S = Sí está", "Anticuerpo S = Salvado", 58),
                card("<b>Core = Contacto real:</b> la vacuna solo trae el antígeno S, así que el vacunado <b>nunca</b> tiene anti-HBc.",
                     "<b>IgM = Muy reciente</b> (aguda) · <b>HBeAg = rEplicación</b> (muy contagioso)."),
                tabla(["Situación", "Marcadores"], [
                    ["<b>Vacunado</b>", "Solo anti-HBs"],
                    ["<b>Curado</b>", "Anti-HBs + anti-HBc IgG"],
                    ["<b>Aguda</b>", "HBsAg + anti-HBc <b>IgM</b>"],
                    ["<b>Crónica</b>", "HBsAg <b>&gt;6 meses</b> + anti-HBc IgG"]]),
                rima("“La vacuna solo deja la S; el virus deja la C.”"),
            ]),
            ("Pancreatitis aguda", "Tres veces tres", [
                h2("Pancreatitis:", "tres veces tres"),
                tabla(["El 3", "Qué significa"], [
                    ['<span class="wk">2 de 3</span>', "Dolor típico · lipasa o amilasa · imagen"],
                    ['<span class="wk">×3</span>', "Lipasa o amilasa ≥3 veces el límite normal"],
                    ['<span class="wk">72 h</span>', "TAC solo si hay duda o no mejora tras 72 h"]]),
                card("Litiasis biliar y alcohol explican ~80 %. Después: hipertrigliceridemia (&gt;1 000 mg/dL), CPRE, fármacos.",
                     big='Causas: <span class="g">piedras y copas</span>'),
                rima("Tratamiento: líquidos (Ringer lactato), analgesia y comer temprano por boca. La colecistectomía, en el mismo internamiento si fue biliar."),
            ]),
            ("Sangrado por várices", "VASO", [
                h2("Várices sangrando:", "llena el VASO"),
                acr(("V", "Vasoactivo: octreótido o terlipresina"),
                    ("A", "Antibiótico: ceftriaxona (el cirrótico que sangra se infecta)"),
                    ("S", "Sangre con medida: transfunde si Hb &lt;7"),
                    ("O", "Obliterar: ligadura endoscópica en las primeras 12 h")),
                card("Úlcera péptica: IBP IV y endoscopia en &lt;24 h. En ambos, la meta de Hb es 7–8 g/dL.",
                     big="Hb de 7, transfunde"),
                rima("“Al cirrótico que sangra: vasoactivo, antibiótico y ligadura.”"),
            ]),
            ("Crohn vs. CUCI", "Las 5 C del Crohn", [
                h2("Las 5 C", "del Crohn"),
                acr(("C", "Cualquier parte, de la boca al ano (en parches)"),
                    ("C", "Capas todas: transmural"),
                    ("C", "Cañerías: fístulas y estenosis"),
                    ("C", "Calles empedradas y granulomas"),
                    ("C", "Cigarro lo empeora")),
                card("Empieza en el <b>recto</b> y sube continuo, solo mucosa, con sangre. Se asocia a colangitis esclerosante; el cigarro no lo empeora.",
                     tag="CUCI", big="Continua desde el recto"),
                rima("“Crohn salta y atraviesa; la CUCI sube derechito por la mucosa.”"),
            ]),
            ("Síndrome de intestino irritable", "Roma: 1, 3, 2", [
                h2("Roma IV:", "1 · 3 · 2"),
                tabla(["Número", "Criterio"], [
                    ['<span class="wk">1</span>', "Dolor abdominal al menos 1 día por semana"],
                    ['<span class="wk">3</span>', "En los últimos 3 meses (inicio hace ≥6)"],
                    ['<span class="wk">2</span>', "Con 2 de 3: relación con la evacuación, cambio en frecuencia o en forma"]]),
                card("Sangrado, anemia, baja de peso, inicio después de los 50, síntomas nocturnos o familiar con cáncer de colon.",
                     tag="Datos de alarma", big="Si hay alarma, no es funcional"),
                rima("“Una vez por semana, tres meses de drama, dos de tres criterios… y cero alarmas.”"),
            ]),
        ],
    },
    "dermatologia": {
        "nombre": "Dermatología",
        "temas": [
            ("Melanoma", "ABCDE; Breslow = pronóstico", [
                h2("El ABCDE", "del lunar sospechoso"),
                acr(("A", "Asimetría"), ("B", "Bordes irregulares"), ("C", "Color variado"),
                    ("D", "Diámetro &gt;6 mm (más que la goma de un lápiz)"),
                    ("E", "<strong>Evolución</strong>: cambia de tamaño, forma o color")),
                card(muted("El grosor en milímetros es el factor pronóstico más importante. Diagnóstico: biopsia <b>escisional</b> con margen estrecho."),
                     big='<span class="g">Breslow</span> = profundidad = pronóstico'),
                rima("“La E es la que alarma: lunar que cambia, lunar que se estudia.”"),
            ]),
            ("Basocelular vs. espinocelular", "Baso es Bonito y Bueno; Espino se Esparce", [
                h2("Baso es Bonito;", "Espino se Esparce"),
                dos(card(lista("El cáncer de piel más frecuente", "Pápula <b>perlada</b> con telangiectasias", "Tercio superior de la cara", "Casi <b>nunca</b> metastatiza"), tag="Basocelular", big="Bonito y Bueno"),
                    card(lista("Sobre <b>queratosis actínica</b>", "Placa costrosa o úlcera", "Labio inferior, dorso de manos", "<b>Sí</b> puede dar metástasis"), tag="Espinocelular", big="Espinoso y se Esparce")),
                rima("“La perla es basocelular; la costra que no cierra, espinocelular.” Tratamiento de ambos: resección con márgenes; Mohs en cara."),
            ]),
            ("Psoriasis", "Psoriasis Extiende; atopia Flexiona", [
                h2("Psoriasis Extiende;", "atopia Flexiona"),
                card("Placas eritematosas con escama <b>plateada</b> en codos, rodillas, piel cabelluda y región sacra. Uñas en dedal.",
                     big="Codos y rodillas por fuera"),
                tabla(["Signo", "Cómo recordarlo"], [
                    ["<b>Auspitz</b>", "Raspas la escama y aparece rocío de sangre"],
                    ["<b>Koebner</b>", "Es rencorosa: donde la lastimas, aparece"]]),
                rima("Dermatitis atópica: flexuras (codo y rodilla por dentro), prurito intenso, antecedente de asma o rinitis."),
            ]),
            ("Pénfigo vs. penfigoide", "El “oide” es el abuelito", [
                h2("El “oide”", "es el abuelito"),
                dos(card(lista("Ampollas <b>flácidas</b> que se rompen", "Boca afectada", "Nikolsky <b>positivo</b>", "Intraepidérmico (acantólisis)", "Anti-desmogleína"), tag="Pénfigo vulgar", big="Frágil y en la boca"),
                    card(lista("Ampollas <b>tensas</b>", "Adulto mayor", "Mucosas casi siempre respetadas", "Nikolsky <b>negativo</b>", "Subepidérmico (BP180/230)"), tag="Penfigoide ampolloso", big="Tensa y profunda")),
                rima("“Pénfigo: piel que se despega con el dedo. Penfigoide: ampolla tensa en el abuelo.” Ambos: esteroides."),
            ]),
            ("Micosis superficiales", "La crema no llega a la raíz", [
                h2("Tiña de cabeza:", "la crema no llega a la raíz"),
                tabla(["Micosis", "Clave", "Tratamiento"], [
                    ["<b>Tiña capitis</b>", "Niño, placa con pelos rotos", "<b>Oral</b>: griseofulvina o terbinafina"],
                    ["<b>Onicomicosis</b>", "Uña gruesa y amarilla", "Terbinafina oral (meses)"],
                    ["<b>Pitiriasis versicolor</b>", "Manchas hipo o hiper, Malassezia", "Tópico: ketoconazol o sulfuro de selenio"],
                    ["<b>Candidosis</b>", "Pliegues con lesiones satélite", "Azol tópico"]]),
                rima("“Versicolor al microscopio: espagueti con albóndigas.”<br>“Pelo y uña, por boca; piel, con crema.”"),
            ]),
        ],
    },
    "cirugia": {
        "nombre": "Cirugía",
        "temas": [
            ("Fiebre posoperatoria", "Pulmón, pipí, piernas, piel, pastillas", [
                h2("Las 5 P,", "en orden de días"),
                tabla(["P", "Causa", "Día"], [
                    ['<b class="g" style="font-size:40px">Pulmón</b>', "Atelectasia / neumonía", '<span class="wk">1–2</span>'],
                    ['<b class="g" style="font-size:40px">Pipí</b>', "Infección urinaria (sonda)", '<span class="wk">3–5</span>'],
                    ['<b class="g" style="font-size:40px">Piernas</b>', "Trombosis venosa profunda", '<span class="wk">4–6</span>'],
                    ['<b class="g" style="font-size:40px">Piel</b>', "Infección de la herida", '<span class="wk">5–7</span>'],
                    ['<b class="g" style="font-size:40px">Pastillas</b>', "Fiebre por fármacos", '<span class="wk" style="font-size:28px">Cualquiera</span>']]),
                rima("“Pulmón, pipí, piernas, piel… y si nada cuadra, las pastillas.”<br>Más de 7 días: piensa en absceso o fuga de anastomosis."),
            ]),
            ("Apendicitis: escala de Alvarado", "MANTRELS; los dobles son dolor y leucocitos", [
                h2("Alvarado:", "MANTRELS"),
                tabla(["Letra", "Dato", "Puntos"], [
                    ['<b class="g">M</b>', "Migración del dolor a FID", "1"],
                    ['<b class="g">A</b>', "Anorexia", "1"],
                    ['<b class="g">N</b>', "Náusea o vómito", "1"],
                    ['<b class="g">T</b>', "<b>Dolor en FID</b> (tenderness)", "<b>2</b>"],
                    ['<b class="g">R</b>', "Rebote", "1"],
                    ['<b class="g">E</b>', "Elevación de temperatura ≥37.3 °C", "1"],
                    ['<b class="g">L</b>', "<b>Leucocitosis</b> &gt;10 000", "<b>2</b>"],
                    ['<b class="g">S</b>', "Shift: neutrofilia", "1"]]),
                rima("“Valen doble el dolor y los leucocitos.” ≤4 poco probable · 5–6 posible · ≥7 probable."),
            ]),
            ("Colangitis", "Charcot son 3 C; Reynolds son 5", [
                h2("Charcot son 3 C;", "Reynolds son 5"),
                acr(("C", "Calentura (fiebre)"), ("C", "Color amarillo (ictericia)"), ("C", "Cólico en hipocondrio derecho"),
                    ("C", "+ Choque (hipotensión)"), ("C", "+ Confusión")),
                card("Antibiótico IV y <b>drenaje de la vía biliar por CPRE</b>; urgente si hay datos de Reynolds.",
                     big="Tratamiento: drena la tubería"),
                rima("“Tres C: colangitis. Cinco C: colangitis que se está muriendo.”"),
            ]),
            ("Trauma: ATLS", "Lo que mata primero se trata primero", [
                h2("Lo que mata primero", "se trata primero"),
                acr(("A", "Vía aérea con control de columna cervical"), ("B", "Ventilación (neumotórax a tensión)"),
                    ("C", "Circulación y control de la hemorragia"), ("D", "Déficit neurológico (Glasgow, pupilas)"),
                    ("E", "Exposición y control de temperatura")),
                tabla(["Choque", "Pérdida", "Clave"], [
                    ["<b>I</b>", '<span class="wk">&lt;15 %</span>', "Casi sin cambios"],
                    ["<b>II</b>", '<span class="wk">15–30 %</span>', "Taquicardia"],
                    ["<b>III</b>", '<span class="wk">30–40 %</span>', "<b>Primera en que baja la presión</b>"],
                    ["<b>IV</b>", '<span class="wk">&gt;40 %</span>', "Riesgo de muerte inminente"]]),
            ]),
            ("Hernias inguinales", "La Directa va Derecho; la Indirecta da la vuelta", [
                h2("La Directa va Derecho;", "la Indirecta da la vuelta", 56),
                dos(card(lista("<b>Medial</b> a los vasos epigástricos", "Atraviesa el triángulo de Hesselbach", "Adulto mayor, pared débil"), tag="Directa"),
                    card(lista("<b>Lateral</b> a los vasos epigástricos", "Entra por el anillo profundo", "La más común, también en mujeres y niños"), tag="Indirecta")),
                card("Límites del triángulo de Hesselbach: <b>R</b>ecto (borde lateral), <b>E</b>pigástricos inferiores y <b>L</b>igamento inguinal.",
                     big='Hesselbach es <span class="g">REL</span>'),
                rima("Femoral: debajo del ligamento inguinal, más en mujeres y la que más se estrangula."),
            ]),
        ],
    },
}


def portada(head, nombre, temas):
    h = head.replace('<span class="pill">Cardio · Neuro · Gastro · Dermato · Cirugía</span>', f'<span class="pill">{nombre} · ENARM</span>')
    h = h.replace('<h1><span class="g">5 especialidades,</span><br>5 mnemotecnias</h1>', '<h1><span class="g">5 mnemotecnias</span><br>que no se te olvidan</h1>')
    h = h.replace('Arritmias y bloqueos · Glasgow · Hepatitis B · Melanoma · Fiebre posoperatoria', " · ".join(t[0] for t in temas))
    return re.sub(r"<title>.*?</title>", f"<title>Carrusel mnemotecnias {nombre.lower()}</title>", h)


def construir(clave, datos):
    base = (AQUI / "especialidades.html").read_text(encoding="utf-8")
    head = portada(base[:base.index("<!-- 2 ·")], datos["nombre"], datos["temas"])
    total = len(datos["temas"]) + 2
    partes = [head]
    for i, (titulo, _, bloques) in enumerate(datos["temas"], 2):
        partes.append(f'<section class="slide"><div class="top"><span class="eyebrow">{i - 1:02d} · {titulo}</span>'
                      f'<span class="num">{i} / {total}</span></div>' + "".join(bloques) + PIE + "</section>")
    filas = "".join(f"<tr><td><b>{t}</b></td><td>{f}</td></tr>" for t, f, _ in datos["temas"])
    partes.append(f'<section class="slide"><div class="top"><span class="eyebrow">Resumen · {datos["nombre"]}</span>'
                  f'<span class="num">{total} / {total}</span></div>{h2("Las 5 frases", "para el examen")}'
                  f'<div class="glass card" style="padding:18px 30px"><table>{filas}</table></div>'
                  '<div style="margin-top:auto;display:grid;gap:22px"><span class="pill">Guarda · Comparte con tu grupo de estudio</span>'
                  '<p class="muted" style="font-size:24px">Material de estudio, no sustituye las GPC vigentes ni el juicio clínico.</p></div></section>')
    (AQUI / f"{clave}.html").write_text("\n".join(partes) + "\n</body>\n</html>\n", encoding="utf-8")


def todas():
    """Especialidades de este archivo más las de contenido/*.py (cada una define ESPECIALIDADES)."""
    import importlib.util
    total = dict(ESPECIALIDADES)
    for f in sorted((AQUI / "contenido").glob("*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        total.update(mod.ESPECIALIDADES)
    return total


if __name__ == "__main__":
    import sys
    elegidas = sys.argv[1:]
    for clave, datos in todas().items():
        if elegidas and clave not in elegidas:
            continue
        construir(clave, datos)
        print(clave)
