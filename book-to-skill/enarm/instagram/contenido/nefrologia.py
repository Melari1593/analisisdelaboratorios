from generar import h2, card, muted, lista, dos, tabla, acr, rima

ESPECIALIDADES = {
    "nefrologia": {
        "nombre": "Nefrología",
        "temas": [
            ("Lesión renal aguda", "Prerrenal ahorra; la NTA derrocha", [
                h2("Prerrenal ahorra;", "la NTA derrocha"),
                tabla(["Índice", "Prerrenal", "NTA"], [
                    ["<b>FENa</b>", '<span class="wk">&lt;1 %</span>', '<span class="wk">&gt;2 %</span>'],
                    ["<b>Na urinario</b>", "&lt;20 mEq/L", "&gt;40 mEq/L"],
                    ["<b>Osm. urinaria</b>", "&gt;500 mOsm/kg", "&lt;350 mOsm/kg"],
                    ["<b>BUN/Cr</b>", "&gt;20", "&lt;15"],
                    ["<b>Sedimento</b>", "Cilindros hialinos", "Cilindros granulosos “café lodoso”"]]),
                card("Creatinina ↑ ≥0.3 mg/dL en 48 h, ≥1.5 veces la basal en 7 días o uresis &lt;0.5 mL/kg/h por 6 h.",
                     tag="Definición KDIGO"),
                rima("“El riñón con sed guarda sodio;<br>el túbulo muerto lo tira.”"),
            ]),
            ("Nefrítico vs. nefrótico", "La O de prOteína; la I de Inflamación", [
                h2("La O de prOteína;", "la I de Inflamación"),
                dos(card(lista("Proteinuria <b>&gt;3.5 g/24 h</b>", "Albúmina &lt;3 g/dL", "Edema e hiperlipidemia", "Niño: <b>cambios mínimos</b> (esteroide)", "Adulto: glomerulopatía <b>membranosa</b>"), tag="NefrÓtico"),
                    card(lista("Hematuria con eritrocitos <b>dismórficos</b>", "<b>Cilindros eritrocitarios</b>", "Hipertensión y oliguria", "Proteinuria &lt;3.5 g/24 h", "Postestreptocócica: <b>C3 bajo</b>"), tag="NefrÍtico")),
                card("<b>C3 bajo</b>: postestreptocócica, lupus, membranoproliferativa. <b>C3 normal</b>: IgA (Berger)."),
                rima("“IgA sangra a los días de la faringitis;<br>la postestreptocócica, a las semanas.”"),
            ]),
            ("Hiperkalemia", "Protege, mete, saca", [
                h2("Hiperkalemia:", "protege, mete, saca"),
                tabla(["Paso", "Qué dar"], [
                    ['<b class="g">Protege</b>', "<b>Gluconato de calcio</b> 10 % IV si hay cambios en el ECG"],
                    ['<b class="g">Mete</b>', "<b>Insulina</b> rápida 10 U + glucosa · salbutamol nebulizado · bicarbonato si hay acidosis"],
                    ['<b class="g">Saca</b>', "Diurético de asa · resinas de intercambio · <b>hemodiálisis</b>"]]),
                card("T picudas → P aplanada y PR largo → QRS ancho → onda sinusoidal.",
                     tag="ECG en orden", big="El ECG manda la prisa"),
                rima("“El calcio no baja el potasio:<br>solo le pone escudo al corazón.”"),
            ]),
            ("Enfermedad renal crónica", "Del 60 para abajo, resta 15", [
                h2("Del 60 para abajo,", "resta 15"),
                tabla(["Estadio", "TFG", "Clave"], [
                    ["<b>G1</b>", '<span class="wk">≥90</span>', "Solo cuenta si hay daño renal"],
                    ["<b>G2</b>", '<span class="wk">60–89</span>', "Solo cuenta si hay daño renal"],
                    ["<b>G3</b>", '<span class="wk">30–59</span>', "3a: 45–59 · 3b: 30–44"],
                    ["<b>G4</b>", '<span class="wk">15–29</span>', "Preparar diálisis o trasplante"],
                    ["<b>G5</b>", '<span class="wk">&lt;15</span>', "Falla renal"]]),
                card("TFG &lt;60 o daño renal (albuminuria ≥30 mg/g) por <b>más de 3 meses</b>. Causa n.º 1: diabetes; luego hipertensión."),
                rima("Diálisis urgente, las vocales: <b>A</b>cidosis, <b>E</b>lectrolitos (K⁺),<br><b>I</b>ntoxicación, s<b>O</b>brecarga, <b>U</b>remia."),
            ]),
            ("Acidosis metabólica y anion gap", "Anion gap alto: prende las LUCES", [
                h2("Anion gap alto:", "prende las LUCES"),
                card("Anion gap = Na⁺ − (Cl⁻ + HCO₃⁻). Normal: <b>8–12</b> mEq/L (corrige por albúmina baja).",
                     big="Na menos cloro y bicarbonato"),
                acr(("L", "Láctica (choque, sepsis)"), ("U", "Uremia"), ("C", "Cetoacidosis (diabética, alcohólica, ayuno)"),
                    ("E", "Etilenglicol y mEtanol"), ("S", "Salicilatos")),
                rima("“Anion gap normal, el cloro sube:<br>diarrea o acidosis tubular renal.”"),
            ]),
        ],
    },
}
