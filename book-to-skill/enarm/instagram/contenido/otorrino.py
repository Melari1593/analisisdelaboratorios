from generar import h2, card, muted, lista, dos, tabla, acr, rima

ESPECIALIDADES = {
    "otorrino": {
        "nombre": "Otorrinolaringología",
        "temas": [
            ("Otitis media vs. externa", "¿Duele al jalar la oreja? Es de afuera", [
                h2("¿Duele al jalar la oreja?", "Es de afuera", 58),
                dos(card(lista("Niño tras infección respiratoria", "Membrana <b>abombada</b> y roja", "Neumococo, <i>H. influenzae</i>, <i>Moraxella</i>", "<b>Amoxicilina</b> a dosis altas"), tag="Otitis media aguda", big="Adentro abomba"),
                    card(lista("Nadador, cotonete, humedad", "Dolor al jalar el pabellón o presionar el trago", "<i>Pseudomonas</i>", "<b>Gotas</b> de ciprofloxacino"), tag="Otitis externa", big="Afuera arde")),
                rima("Diabético mayor con otorrea y tejido de granulación: otitis externa <b>maligna</b>. TAC y antipseudomonas IV."),
            ]),
            ("Faringoamigdalitis", "Las 5 T de McIsaac", [
                h2("Las 5 T", "de McIsaac"),
                acr(("T", "Tos <strong>ausente</strong>"),
                    ("T", "Temperatura &gt;38 °C"),
                    ("T", "Tonsilas (amígdalas) con exudado o crecidas"),
                    ("T", "Tumefacción de ganglios cervicales anteriores"),
                    ("T", "Tiempo de vida: 3–14 años +1 · ≥45 años −1")),
                card("0–1 punto: sin antibiótico ni prueba. 2–3: prueba rápida o cultivo. ≥4: alta probabilidad de estreptococo; trata.",
                     big="Suma y decide"),
                rima("Penicilina G benzatínica IM dosis única o amoxicilina 10&nbsp;días: previene la fiebre reumática."),
            ]),
            ("Epistaxis", "Adelante el niño, atrás el abuelo", [
                h2("Adelante el niño,", "atrás el abuelo"),
                tabla(["", "Anterior", "Posterior"], [
                    ["<b>Frecuencia</b>", '<span class="wk">~90 %</span>', "La minoría, más grave"],
                    ["<b>Origen</b>", "Plexo de Kiesselbach", "Arteria esfenopalatina"],
                    ["<b>Paciente</b>", "Niño que se rasca", "Adulto mayor, hipertenso o anticoagulado"],
                    ["<b>Manejo</b>", "Compresión, cauterio, tapón anterior", "Tapón posterior o globo; ligadura o embolización"]]),
                rima("“Cabeza hacia adelante y aprieta 10 minutos.” Nunca hacia atrás: se traga la sangre."),
            ]),
            ("Hipoacusia: Rinne y Weber", "Weber: conductiva al culpable, sensorial al sano", [
                h2("Weber: Conductiva al Culpable,", "Sensorial al Sano", 52),
                tabla(["Tipo", "Rinne (oído afectado)", "Weber"], [
                    ["<b>Normal</b>", "Positivo: aire&nbsp;&gt;&nbsp;hueso", "Al centro"],
                    ["<b>Conductiva</b>", '<b class="g">Negativo</b>: hueso&nbsp;&gt;&nbsp;aire', "Hacia el oído <b>enfermo</b>"],
                    ["<b>Neurosensorial</b>", "Positivo", "Hacia el oído <b>sano</b>"]]),
                card("Conductiva: cerumen, otitis con derrame, otosclerosis. Neurosensorial: presbiacusia, ruido, Ménière; si es unilateral, RM para descartar schwannoma vestibular.",
                     big="¿Y la causa?"),
                rima("“En el Rinne, el aire le gana al hueso… hasta que el oído se tapa.”"),
            ]),
            ("Vértigo periférico", "Segundos, horas, días", [
                h2("Segundos, horas, días:", "el reloj del vértigo"),
                tabla(["Cuadro", "Dura", "Clave y tratamiento"], [
                    ["<b>VPPB</b>", '<span class="wk">Seg.</span>', "Al girar la cabeza. Dix‑Hallpike y <b>Epley</b>"],
                    ["<b>Ménière</b>", '<span class="wk">Horas</span>', "Acúfeno, plenitud, hipoacusia. Poca sal"],
                    ["<b>Neuritis vestibular</b>", '<span class="wk">Días</span>', "Posviral, <b>sin</b> hipoacusia. Esteroide"]]),
                card("Con hipoacusia ya no es neuritis: es <b>laberintitis</b>. Con datos neurológicos, piensa en EVC.",
                     big="Oye mal = laberintitis"),
                rima("“Ménière trae su trío: zumbido, oído lleno y sordera que va y viene.”"),
            ]),
        ],
    },
}
