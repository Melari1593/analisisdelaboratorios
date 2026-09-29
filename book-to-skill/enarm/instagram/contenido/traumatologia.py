from generar import h2, card, muted, lista, dos, tabla, acr, rima

ESPECIALIDADES = {
    "traumatologia": {
        "nombre": "Traumatología y ortopedia",
        "temas": [
            ("Síndrome compartimental", "Primero el dolor, al final el pulso", [
                h2("Primero el dolor,", "al final el pulso"),
                acr(("P", "<strong>Pain</strong>: dolor desproporcionado, peor al estirar pasivo (el más temprano)"),
                    ("P", "Parestesias"),
                    ("P", "Palidez"),
                    ("P", "Parálisis"),
                    ("P", "Pulso ausente: signo <strong>tardío</strong>")),
                card("Presión del compartimento &gt;30 mmHg o diferencia con la diastólica ≤30 mmHg: <b>fasciotomía</b> urgente. Antes, quita yesos y vendajes.",
                     big="Tratamiento: abre la caja"),
                rima("“Si esperas a que falte el pulso, llegaste tarde.”"),
            ]),
            ("Fracturas fisarias: Salter-Harris", "SALTR: entre más alto el número, peor", [
                h2("Salter-Harris:", "S · A · L · T · R"),
                acr(("I", "<b>S</b>eparada: solo a través de la fisis"),
                    ("II", "<b>A</b>rriba: fisis + metáfisis (la más común)"),
                    ("III", "hacia <b>L</b>a articulación: fisis + epífisis"),
                    ("IV", "<b>T</b>odo: metáfisis, fisis y epífisis"),
                    ("V", "<b>R</b>eventada: fisis aplastada")),
                card("III y IV entran a la articulación: reducción anatómica, a menudo abierta con fijación. La V frena el crecimiento y se ve tarde.",
                     big="Entre más alto el número, peor"),
                rima("“SALTR: si la fractura salta a la articulación, va al quirófano.”"),
            ]),
            ("Fractura de cadera", "Adentro se cambia, afuera se fija", [
                h2("Adentro se cambia,", "afuera se fija"),
                card("Adulto mayor que cae de su altura: pierna <b>acortada</b> y en <b>rotación externa</b>.", big="La abuelita que no se levanta"),
                dos(card(lista("Cuello femoral", "Riesgo de <b>necrosis avascular</b>", "Desplazada: <b>artroplastia</b>", "No desplazada: tornillos"), tag="Intracapsular"),
                    card(lista("Intertrocantérica", "Buena irrigación, consolida", "<b>Osteosíntesis</b>: clavo o placa", "Sangra más"), tag="Extracapsular")),
                rima("Opera en las primeras 48 h y da tromboprofilaxis: la cama mata más que la fractura."),
            ]),
            ("Lesiones de rodilla", "Lachman con LCA, McMurray con menisco", [
                h2("L con L,", "M con M"),
                tabla(["Prueba", "Lesión", "Pista"], [
                    ["<b>Lachman</b>", '<b class="g">LCA</b>', "La más sensible; giro con “pop”"],
                    ["<b>Cajón anterior</b>", "LCA", "Tibia que se va hacia adelante"],
                    ["<b>Cajón posterior</b>", "LCP", "Golpe en la rodilla contra el tablero"],
                    ["<b>Valgo forzado</b>", "Colateral medial", "Golpe en la cara externa"],
                    ["<b>McMurray</b>", '<b class="g">Menisco</b>', "Chasquido, bloqueo, derrame tardío"]]),
                rima("“Giro, pop y rodilla hinchada en horas: LCA hasta demostrar lo contrario.” Imagen de elección: RM."),
            ]),
            ("Displasia de cadera", "Barlow la bota, Ortolani la regresa", [
                h2("Barlow la bota,", "Ortolani la regresa"),
                tabla(["Maniobra", "Cómo", "Qué hace"], [
                    ["<b>Barlow</b>", "Aducción y empuje hacia atrás", "<b>Luxa</b> una cadera inestable"],
                    ["<b>Ortolani</b>", "Abducción y levanta el trocánter", "<b>Reduce</b> con un “clunk”"]]),
                card("Ultrasonido antes de los 4 meses; después, radiografía (ya aparece el núcleo de osificación). Menor de 6 meses: <b>arnés de Pavlik</b>.",
                     big="Imagen según la edad"),
                rima("Riesgo: niña, primogénita, presentación pélvica y familiar afectado. Tarde: Galeazzi y abducción limitada."),
            ]),
        ],
    },
}
