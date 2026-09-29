from generar import h2, card, muted, lista, dos, tabla, acr, rima

ESPECIALIDADES = {
    "endocrinologia": {
        "nombre": "Endocrinología",
        "temas": [
            ("Diagnóstico de diabetes", "126 en ayuno, 6.5 de A1c, 200 con carga", [
                h2("126 en ayuno,", "6.5 y 200"),
                tabla(["Prueba", "Prediabetes", "Diabetes"], [
                    ["<b>Glucosa en ayuno</b>", "100–125", '<span class="wk">≥126</span>'],
                    ["<b>HbA1c</b>", "5.7–6.4 %", '<span class="wk">≥6.5 %</span>'],
                    ["<b>CTGO 75 g (2 h)</b>", "140–199", '<span class="wk">≥200</span>'],
                    ["<b>Al azar + síntomas</b>", "—", '<span class="wk">≥200</span>']]),
                card("Una cifra sola no basta: confirma con otra prueba alterada. Inicio en DM2: estilo de vida + <b>metformina</b>.",
                     big='Sin síntomas, <span class="g">repite</span>'),
                rima("“Ayuno de 126, A1c de 6.5,<br>y 200 si hay carga o si hay síntomas.”"),
            ]),
            ("Cetoacidosis vs. hiperosmolar", "Potasio menor de 3.3: insulina en pausa", [
                h2("Suero, potasio", "y luego insulina"),
                tabla(["Dato", "Cetoacidosis", "Hiperosmolar"], [
                    ["<b>Glucosa</b>", '<span class="wk">&gt;250</span>', '<span class="wk">&gt;600</span>'],
                    ["<b>pH</b>", "&lt;7.30", "&gt;7.30"],
                    ["<b>Cetonas</b>", "Positivas", "Mínimas"],
                    ["<b>Osmolaridad</b>", "Variable", "&gt;320"],
                    ["<b>Típico</b>", "DM1 · horas", "DM2 mayor · días"]]),
                card("Primero solución salina 0.9 %; con K &lt;3.3, repón antes de la insulina.",
                     big='K &lt;3.3 = insulina <span class="g">en pausa</span>'),
                rima("“Primero el agua, luego el potasio y al final la insulina.”"),
            ]),
            ("Hipo vs. hipertiroidismo", "PTU: Primer Trimestre Únicamente", [
                h2("La TSH", "siempre va al revés"),
                dos(card(lista("TSH ↑ · T4 libre ↓", "Frío, piel seca, estreñimiento, bradicardia",
                               "Hashimoto: anti-TPO", "<b>Levotiroxina</b> en ayuno"), tag="Hipotiroidismo", big="Todo lento"),
                    card(lista("TSH ↓ · T4 libre ↑", "Calor, baja de peso, taquicardia",
                               "Graves: anticuerpos contra el receptor de TSH, exoftalmos", "<b>Metimazol</b>"), tag="Hipertiroidismo", big="Todo rápido")),
                rima("“La hipófisis grita cuando la tiroides no trabaja.”<br>PTU = <b>P</b>rimer <b>T</b>rimestre <b>Ú</b>nicamente (y tormenta tiroidea)."),
            ]),
            ("Cushing vs. Addison", "Cushing: 3 C; Addison: adiós, sodio", [
                h2("Cushing engorda;", "Addison se broncea"),
                dos(card(lista("Causa más común: <b>esteroides</b> exógenos", "Endógeno: adenoma hipofisario",
                               "Tamizaje: supresión con 1 mg de dexametasona o cortisol libre urinario"),
                         tag="Cushing", big="Las 3 C"),
                    card(lista("Hiperpigmentación (ACTH alta)", "Na ↓, K ↑, hipotensión, hipoglucemia",
                               "Dx: estimulación con ACTH", "Hidrocortisona + fludrocortisona"),
                         tag="Addison", big="Adiós, sodio")),
                rima("“<b>C</b>ara de luna, <b>C</b>uello de búfalo y <b>C</b>intura con estrías violáceas.”<br>Crisis suprarrenal: hidrocortisona IV sin esperar resultados."),
            ]),
            ("Nódulo y cáncer de tiroides", "Papilar Popular; Folicular Fluye por sangre", [
                h2("Papilar es Popular;", "Folicular Fluye", 60),
                tabla(["Tipo", "Truco", "Clave"], [
                    ["<b>Papilar</b>", '<b class="g">Popular</b>', "El más común; ganglios; psamomas"],
                    ["<b>Folicular</b>", '<b class="g">Fluye</b>', "Por sangre a hueso y pulmón"],
                    ["<b>Medular</b>", '<b class="g">Marca</b>', "Calcitonina; MEN 2 (RET)"],
                    ["<b>Anaplásico</b>", '<b class="g">Anciano</b>', "El más agresivo"]]),
                card("Primero TSH y ultrasonido; la <b>BAAF</b> decide. Si la TSH está baja, gammagrama: el nódulo caliente casi nunca es maligno.",
                     big='Nódulo: la <span class="g">BAAF</span> decide'),
                rima("“Medular antes de operar: busca feocromocitoma (MEN 2).”"),
            ]),
        ],
    },
}
