from generar import h2, card, muted, lista, dos, tabla, acr, rima

ESPECIALIDADES = {
    "ginecologia": {
        "nombre": "Ginecología",
        "temas": [
            ("Tamizaje de cáncer cervicouterino", "25 citología, 35 el virus, 64 te jubilas", [
                h2("25 citología, 35 el virus,", "64 te jubilas", 56),
                tabla(["Edad", "Prueba", "Frecuencia"], [
                    ['<span class="wk" style="white-space:nowrap">25–34</span>', "<b>Citología</b>", "Anual; tras 2 normales, cada 3 años"],
                    ['<span class="wk" style="white-space:nowrap">35–64</span>', "<b>VPH</b> (si sale +, citología)", "Cada 5 años si es negativa"]]),
                card("VPH 16 y 18 causan ~70 %. Tipo más común: <b>epidermoide</b>, en la zona de transformación. Citología anormal: <b>colposcopia</b>.",
                     big="El virus es la causa necesaria"),
                rima("“A los 25 te raspan, a los 35 te buscan el virus,<br>a los 64 te jubilas.”"),
            ]),
            ("Cáncer de mama", "BI-RADS 3 espera; 4 y 5, aguja", [
                h2("20 te tocas, 25 te tocan,", "40 te aprietan", 56),
                card("Autoexploración desde los <b>20</b>, examen clínico anual desde los <b>25</b> y mastografía cada 2 años de <b>40 a 69</b> (NOM-041)."),
                tabla(["BI-RADS", "Qué hacer"], [
                    ['<span class="wk">0</span>', "Incompleto: más imagen"],
                    ['<span class="wk">1–2</span>', "Negativo o benigno: tamizaje normal"],
                    ['<span class="wk">3</span>', "Probablemente benigno: control en 6 meses"],
                    ['<span class="wk">4–5</span>', "Sospechoso: <b>biopsia</b>"],
                    ['<span class="wk">6</span>', "Cáncer ya confirmado por biopsia"]]),
                rima("“BI-RADS 3, espera;<br>4 y 5, aguja.”"),
            ]),
            ("Síndrome de ovario poliquístico", "Rotterdam pide 2 de 3 R", [
                h2("Rotterdam pide", "2 de 3 R"),
                acr(("R", "Reglas raras: oligo o anovulación"),
                    ("R", "Rasgos de andrógenos: hirsutismo, acné, testosterona ↑"),
                    ("R", "Racimo: ≥20 folículos por ovario o ≥10 mL")),
                card("Descarta antes hipotiroidismo, hiperprolactinemia e hiperplasia suprarrenal. Tratamiento: bajar de peso y <b>anticonceptivos combinados</b>; para embarazo, <b>letrozol</b>.",
                     big="Diagnóstico de exclusión"),
                rima("“Dos erres bastan: el ultrasonido no es obligatorio.”"),
            ]),
            ("Endometriosis", "Las 3 D y la I", [
                h2("Endometriosis:", "las 3 D y la I"),
                acr(("D", "Dismenorrea secundaria y progresiva"),
                    ("D", "Dispareunia profunda"),
                    ("D", "Disquecia: duele al evacuar"),
                    ("I", "Infertilidad")),
                card("Sitio más común: <b>ovario</b> (endometrioma, “quiste de chocolate”). Estándar de oro: <b>laparoscopia</b> con biopsia. Primera línea: AINE + progestágeno o anticonceptivo.",
                     big="Endometrio fuera de casa"),
                rima("“Tejido que menstrúa donde no debe,<br>duele en la regla, en la cama y en el baño.”"),
            ]),
            ("Vaginitis", "Queso, fresa y pescado", [
                h2("Queso, fresa", "y pescado"),
                tabla(["Agente", "Flujo", "pH", "Tratamiento"], [
                    ["<b>Cándida</b>", "Grumoso, pica, sin olor", '<span class="wk">&lt;4.5</span>', "Fluconazol 150 mg, 1 dosis"],
                    ["<b>Tricomonas</b>", "Espumoso, cérvix en <b>fresa</b>", '<span class="wk">&gt;4.5</span>', "Metronidazol + <b>pareja</b>"],
                    ["<b>Vaginosis</b>", "Gris, olor a <b>pescado</b>", '<span class="wk">&gt;4.5</span>', "Metronidazol 7 días"]]),
                card("Flujo gris homogéneo, pH &gt;4.5, prueba de aminas positiva y <b>células clave</b>.",
                     tag="Vaginosis: Amsel 3 de 4"),
                rima("“Solo la cándida conserva el pH ácido;<br>en la vaginosis, la pareja no se trata.”"),
            ]),
        ],
    },
}
