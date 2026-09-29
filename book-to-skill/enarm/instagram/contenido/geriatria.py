from generar import h2, card, muted, lista, dos, tabla, acr, rima

ESPECIALIDADES = {
    "geriatria": {
        "nombre": "Geriatría",
        "temas": [
            ("Delirium vs. demencia", "Delirium llega de golpe y fluctúa; CAM 1+2+(3 o 4)", [
                h2("Delirium llega de golpe;", "la demencia, despacio", 56),
                tabla(["", "Delirium", "Demencia"], [
                    ["<b>Inicio</b>", "Horas a días", "Meses a años"],
                    ["<b>Curso</b>", "<b>Fluctuante</b>", "Progresivo"],
                    ["<b>Atención</b>", "<b>Alterada</b>", "Conservada al inicio"],
                    ["<b>¿Reversible?</b>", "Casi siempre", "No"]]),
                card("<b>1</b> inicio agudo y fluctuante + <b>2</b> inatención + <b>3</b> pensamiento desorganizado <b>o 4</b> conciencia alterada.",
                     tag="CAM", big='1 + 2 + <span class="g">(3 o 4)</span>'),
                rima("Busca la causa: infección, fármacos, globo vesical.<br>Primero, medidas no farmacológicas."),
            ]),
            ("Síndromes geriátricos y funcionalidad", "5 gigantes con I; Katz cuida el cuerpo", [
                h2("Los 5 gigantes", "empiezan con I"),
                card('<span class="g" style="font-weight:800">I</span>nmovilidad · <span class="g" style="font-weight:800">I</span>nestabilidad y caídas · <span class="g" style="font-weight:800">I</span>ncontinencia · <span class="g" style="font-weight:800">I</span>ntelecto deteriorado · <span class="g" style="font-weight:800">I</span>atrogenia',
                     big="Tras una caída, busca las otras 4"),
                dos(card(muted("Básicas: bañarse, vestirse, usar el baño, moverse, continencia y comer."), tag="Katz", big="Cuida el cuerpo"),
                    card(muted("Instrumentales: teléfono, compras, cocina, dinero, medicamentos, transporte."), tag="Lawton", big="Lleva la logística")),
                rima("“Katz para el cuerpo, Lawton para la calle.” Lo instrumental se pierde primero."),
            ]),
            ("Polifarmacia y criterios de Beers", "¡BASTA! de pastillas en el adulto mayor", [
                h2("Beers te dice:", "¡BASTA!"),
                acr(("B", "Benzodiacepinas: caídas, fracturas, delirium"),
                    ("A", "Anticolinérgicos: difenhidramina, clorfenamina"),
                    ("S", "Sulfonilureas: glibenclamida (hipoglucemia)"),
                    ("T", "Tricíclicos: amitriptilina"),
                    ("A", "AINE de uso crónico: sangrado y daño renal")),
                card("Polifarmacia: <b>5 o más</b> fármacos. Cada pastilla nueva se justifica; cada vieja se revisa.",
                     big='Antes de sumar, <span class="g">resta</span>'),
                rima("“Si el abuelo se cae o se confunde, revisa primero la bolsa de medicinas.”"),
            ]),
            ("Incontinencia urinaria", "Ríe, corre, se derrama o no llega", [
                h2("Ríe, corre,", "se derrama o no llega"),
                tabla(["Tipo", "Pista", "Tratamiento"], [
                    ["<b>Esfuerzo</b>", "Se escapa al <b>reír</b> o toser", "Ejercicios de piso pélvico"],
                    ["<b>Urgencia</b>", "<b>Corre</b> al baño; detrusor hiperactivo", "Entrenamiento vesical; mirabegrón"],
                    ["<b>Rebosamiento</b>", "Gotea: vejiga <b>llena</b> (próstata, diabetes)", "Sonda y tratar la causa"],
                    ["<b>Funcional</b>", "<b>No llega</b>: movilidad o cognición", "Baño cerca y horario"]]),
                rima("Rebosamiento: residuo posmiccional alto. En el adulto mayor, evita antimuscarínicos como oxibutinina."),
            ]),
            ("Úlceras por presión", "Rojo, ampolla, grasa y hueso", [
                h2("Rojo, ampolla,", "grasa y hueso"),
                tabla(["Estadio", "Qué ves"], [
                    ['<span class="wk">1</span>', "Eritema que <b>no blanquea</b>, piel íntegra"],
                    ['<span class="wk">2</span>', "Pérdida parcial: <b>ampolla</b> o dermis expuesta"],
                    ['<span class="wk">3</span>', "Pérdida total de piel: se ve <b>grasa</b>"],
                    ['<span class="wk">4</span>', "Se ve <b>hueso</b>, tendón o músculo"]]),
                card("Si una escara o esfacelo cubre el fondo, es <b>no estadificable</b>. Riesgo con escala de <b>Braden</b>: menor puntaje, mayor riesgo.",
                     big='Sin fondo visible, <span class="g">sin número</span>'),
                rima("“Del rojo al hueso.”<br>Prevención: cambios de posición cada 2 h."),
            ]),
        ],
    },
}
