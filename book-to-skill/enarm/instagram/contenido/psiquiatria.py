from generar import h2, card, muted, lista, dos, tabla, acr, rima

ESPECIALIDADES = {
    "psiquiatria": {
        "nombre": "Psiquiatría",
        "temas": [
            ("Depresión mayor", "La CAMPESINA triste: 5 de 9 por 2 semanas", [
                h2("La CAMPESINA triste:", "5 de 9 por 2 semanas", 58),
                acr(("<span style=\"font-size:38px\">CA</span>", "Culpa excesiva · Apetito o peso que cambia"),
                    ("<span style=\"font-size:38px\">MP</span>", "Muerte (ideas) · Psicomotor: lento o agitado"),
                    ("<span style=\"font-size:38px\">ES</span>", "Energía baja · Sueño: insomnio o hipersomnia"),
                    ("<span style=\"font-size:38px\">IN</span>", "Interés perdido (anhedonia) · No se concentra"),
                    ("A", "Ánimo deprimido")),
                card("Uno de los 5 debe ser <b>ánimo deprimido</b> o <b>anhedonia</b>. Siempre pregunta por ideas de muerte: preguntar no induce el suicidio.",
                     big='Ánimo o Interés: <span class="g">obligatorio</span>'),
                rima("Primera línea: ISRS (sertralina, fluoxetina, escitalopram). El efecto tarda 4–6 semanas."),
            ]),
            ("Trastorno bipolar y litio", "LITIO: 0.6 a 1.2; tóxico arriba de 1.5", [
                h2("Litio: ventana estrecha,", "0.6 a 1.2 mEq/L", 58),
                acr(("L", "Leucocitosis benigna"),
                    ("I", "Insípida nefrogénica: poliuria y sed"),
                    ("T", "Tiroides lenta (hipotiroidismo) y temblor fino"),
                    ("I", "Infante con anomalía de Ebstein (teratógeno)"),
                    ("O", "Ojo: AINE, IECA y tiazidas suben el litio")),
                card("Temblor grueso, ataxia, confusión, vómito y diarrea (&gt;1.5&nbsp;mEq/L). Grave o con falla renal: <b>hemodiálisis</b>.",
                     tag="Intoxicación", big="Del temblor fino al grueso"),
                rima("“Manía: una semana; hipomanía: cuatro días.”<br>El litio es el estabilizador que más reduce el suicidio."),
            ]),
            ("Neuroléptico maligno vs. serotoninérgico", "Neuroléptico: plomo lento; serotonina: saltarina", [
                h2("Neuroléptico: plomo lento;", "serotonina: saltarina", 56),
                dos(card(lista("Antipsicótico (haloperidol)", "Inicia en <b>días</b>", "Rigidez en <b>tubo de plomo</b>", "Reflejos lentos", "CK muy alta, fiebre", "Dantroleno o bromocriptina"), tag="Neuroléptico maligno"),
                    card(lista("ISRS + IMAO, tramadol, linezolid", "Inicia en <b>horas</b>", "<b>Clonus</b> e hiperreflexia", "Midriasis y diarrea", "Fiebre, agitación", "Ciproheptadina y benzodiacepina"), tag="Serotoninérgico")),
                rima("“El de plomo tarda y se pone tieso; el serotoninérgico brinca y llega rápido.” En ambos: suspende el fármaco."),
            ]),
            ("Esquizofrenia", "Positivo suma, negativo resta: las 5 A", [
                h2("Positivo suma,", "negativo resta"),
                acr(("A", "Abulia: sin voluntad"),
                    ("A", "Alogia: pobreza del habla"),
                    ("A", "Anhedonia"),
                    ("A", "Aplanamiento afectivo"),
                    ("A", "Asocialidad")),
                tabla(["Duración", "Diagnóstico"], [
                    ['<span class="wk">&lt;1 mes</span>', "Trastorno psicótico breve"],
                    ['<span class="wk">1–6 meses</span>', "Esquizofreniforme"],
                    ['<span class="wk">≥6 meses</span>', "<b>Esquizofrenia</b>"]]),
                rima("“Uno y seis.” Resistente a 2 antipsicóticos: <b>clozapina</b>, vigilando neutrófilos."),
            ]),
            ("Abstinencia alcohólica y Wernicke", "Tiamina antes que glucosa: Wernicke es un CAOs", [
                h2("Tiamina antes que glucosa:", "Wernicke es un CAOs", 56),
                tabla(["Tras la última copa", "Qué aparece"], [
                    ['<span class="wk">6–24 h</span>', "Temblor, ansiedad, taquicardia"],
                    ['<span class="wk">12–48 h</span>', "Convulsiones y alucinosis"],
                    ['<span class="wk">48–96 h</span>', "<b>Delirium tremens</b>"]]),
                acr(("C", "Confusión"), ("A", "Ataxia"), ("O", "Oftalmoplejía, nistagmo")),
                rima("Abstinencia: <b>benzodiacepinas</b> (lorazepam si hay daño hepático). Korsakoff: amnesia y confabulación."),
            ]),
        ],
    },
}
