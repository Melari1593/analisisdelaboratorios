from generar import h2, card, muted, lista, dos, tabla, acr, rima

ESPECIALIDADES = {
    "reumatologia": {
        "nombre": "Reumatología",
        "temas": [
            ("Artritis reumatoide vs. osteoartritis", "La reumatoide respeta la punta del dedo", [
                h2("La reumatoide respeta", "la punta del dedo", 58),
                tabla(["", "Artritis reumatoide", "Osteoartritis"], [
                    ["<b>Dedos</b>", "MCF, IFP y muñecas, simétrica", "<b>IFD</b>, IFP, rodilla, cadera"],
                    ["<b>Rigidez</b>", '<span class="wk">&gt;1 h</span> matutina', '<span class="wk">&lt;30 min</span>'],
                    ["<b>Laboratorio</b>", "FR y <b>anti-CCP</b> (el más específico)", "Normal"],
                    ["<b>Rx</b>", "Erosiones, osteopenia yuxtaarticular", "Osteofitos, pinzamiento asimétrico"]]),
                card("Tratamiento de primera línea en AR: <b>metotrexato</b> desde el diagnóstico, con esteroide corto como puente.",
                     big='<span class="g">Metotrexato</span> es el ancla'),
                rima("“Bouchard en la base (IFP), Heberden hasta arriba (IFD).”"),
            ]),
            ("Lupus eritematoso sistémico", "ANA abre la puerta; Sm y DNA la cierran", [
                h2("ANA abre la puerta;", "Sm y DNA la cierran", 58),
                tabla(["Anticuerpo", "Pista"], [
                    ["<b>ANA ≥1:80</b>", "Tamiz sensible; requisito para clasificar"],
                    ["<b style=\"white-space:nowrap\">Anti-DNAdc</b>", "Específico; sube con la actividad y la nefritis"],
                    ["<b>Anti-Sm</b>", "El más específico"],
                    ["<b style=\"white-space:nowrap\">Anti-histona</b>", "Lupus inducido por fármacos"],
                    ["<b>Anti-Ro</b>", "Lupus neonatal y bloqueo AV congénito"]]),
                card("Brote: <b>C3 y C4 bajos</b> con anti-DNAdc alto. <b>Hidroxicloroquina</b> para todos.",
                     big="Complemento baja, lupus sube"),
                rima("“Lupus por fármacos da HIP: Hidralazina, Isoniazida, Procainamida.”"),
            ]),
            ("Gota", "Gota: aguja negativa; meta menor de 6", [
                h2("Gota: aguja negativa,", "meta menor de 6", 58),
                tabla(["Cristal", "Forma", "Birrefringencia"], [
                    ["<b>Gota</b> (urato monosódico)", "Aguja", '<span class="wk">Negativa</span>'],
                    ["<b>Pseudogota</b> (pirofosfato de calcio)", "Romboide", '<span class="wk">Positiva</span>']]),
                dos(card(muted("Colchicina, AINE o esteroide. Si ya toma alopurinol, <b>no</b> lo suspendas."), tag="Crisis aguda", big="Apaga el fuego"),
                    card(muted("Alopurinol hasta ácido úrico &lt;6 mg/dL (&lt;5 con tofos), con colchicina profiláctica al inicio."), tag="Crónica", big="Baja el nivel")),
                rima("“La gota pica como aguja y es negativa.”<br>Clásico: podagra (1.ª metatarsofalángica)."),
            ]),
            ("Espondiloartritis", "HLA-B27 es una PERA", [
                h2("HLA-B27", "es una PERA"),
                acr(("P", "Psoriásica: dactilitis, dedos en salchicha"),
                    ("E", "Enteropática: Crohn y CUCI"),
                    ("R", "Reactiva: no ve, no orina, no camina"),
                    ("A", "Anquilosante: hombre joven, sacroileítis bilateral")),
                card("Dolor lumbar <b>inflamatorio</b>: inicio &lt;40 años, mejora con ejercicio y no con reposo, despierta en la noche. Uveítis anterior asociada.",
                     big="Mejora al moverse"),
                rima("“Columna de bambú, Schober que no se estira.” Tratamiento: AINE y ejercicio; si fallan, anti-TNF."),
            ]),
            ("Arteritis de células gigantes", "Más de 50, VSG de 50: prednisona ya", [
                h2("Más de 50 años,", "VSG más de 50"),
                acr(("50", "Edad ≥50 al inicio"),
                    ("C", "Cefalea nueva, temporal"),
                    ("M", "Mandíbula que duele al masticar (claudicación)"),
                    ("O", "Ojo: amaurosis, riesgo de ceguera"),
                    ("P", "Polimialgia reumática asociada")),
                card("Da <b>prednisona</b> ante la sospecha, sin esperar la biopsia. La biopsia de arteria temporal es el estándar de oro y sigue siendo útil en las primeras 2 semanas.",
                     big='Primero el esteroide, <span class="g">luego la biopsia</span>'),
                rima("“Si mastica y le duele y la vista se le va: prednisona ya.”"),
            ]),
        ],
    },
}
