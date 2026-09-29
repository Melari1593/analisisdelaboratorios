from generar import h2, card, muted, lista, dos, tabla, acr, rima

ESPECIALIDADES = {
    "oftalmologia": {
        "nombre": "Oftalmología",
        "temas": [
            ("Ojo rojo", "Ojo rojo que duele y ve mal: urgencia", [
                h2("Ojo rojo que duele", "y ve mal: urgencia"),
                tabla(["", "Conjuntivitis", "Glaucoma agudo", "Uveítis anterior"], [
                    ["<b>Visión</b>", "Normal", "↓ con halos", "↓"],
                    ["<b>Dolor</b>", "Arenilla", '<b class="g">Intenso</b>, vómito', "Fotofobia"],
                    ["<b>Pupila</b>", "Normal", "<b>Media fija</b>", "<b>Miosis</b>"],
                    ["<b>Pista</b>", "Secreción", "Córnea turbia, ojo duro", "Tyndall, hipopión"]]),
                card("Rojo periférico que palidece hacia la córnea: conjuntivitis. Rojo alrededor de la córnea (periquerático): glaucoma, uveítis o queratitis.",
                     big="¿Dónde está lo rojo?"),
                rima("“Pupila chica, uveítis; pupila a media asta y ojo de piedra, glaucoma.”"),
            ]),
            ("Glaucoma", "Crónico roba en silencio; agudo asalta de golpe", [
                h2("Glaucoma crónico:", "ladrón silencioso"),
                dos(card(lista("Sin síntomas hasta muy tarde", "Pierde visión <b>periférica</b>: visión en túnel", "Excavación de papila ↑", "1.ª línea: <b>prostaglandina</b> (latanoprost)"), tag="Ángulo abierto", big="Roba en silencio"),
                    card(lista("Luz tenue o midriático", "Dolor, halos, vómito", "Pupila media fija, PIO muy alta", "Acetazolamida, timolol, pilocarpina, manitol"), tag="Ángulo cerrado", big="Asalta de golpe")),
                rima("Cierre angular: baja la presión y haz <b>iridotomía láser en ambos ojos</b>. Evita los midriáticos."),
            ]),
            ("Retinopatía diabética", "Vaso nuevo, problema nuevo", [
                h2("Vaso nuevo,", "problema nuevo"),
                tabla(["Etapa", "Fondo de ojo"], [
                    ["<b>No proliferativa</b>", "<b>Microaneurismas</b> (1.er signo), hemorragias, exudados, manchas algodonosas"],
                    ["<b>Proliferativa</b>", "<b>Neovasos</b>: hemorragia vítrea y desprendimiento traccional"],
                    ["<b>Edema macular</b>", "Principal causa de baja visual en el diabético"]]),
                card("DM2: fondo de ojo <b>al diagnóstico</b>. DM1: a los 5 años. Luego, cada año. Tratamiento: anti-VEGF y láser.",
                     big="¿Cuándo revisar?"),
                rima("“Micro primero, neo al final: cuando la retina hace vasos nuevos, pide láser.”"),
            ]),
            ("Desprendimiento de retina", "Moscas, destellos y se cierra el telón", [
                h2("Moscas, destellos", "y se cierra el telón"),
                tabla(["Síntoma", "Qué significa"], [
                    ['<b class="g">Moscas</b>', "Miodesopsias: sangre o pigmento en el vítreo"],
                    ['<b class="g">Destellos</b>', "Fotopsias: el vítreo tracciona la retina"],
                    ['<b class="g">Telón</b>', "Sombra o cortina que avanza: ya se desprendió"]]),
                card("Miopía alta, cirugía de catarata previa o trauma. Fondo de ojo: retina gris que ondula; si no se ve, ultrasonido.",
                     tag="Factores de riesgo", big="El miope es el candidato"),
                rima("“Mácula pegada, cirugía volada.” Es urgencia quirúrgica: operar antes de que se desprenda la mácula."),
            ]),
            ("Oclusión vascular de la retina", "Arteria: cereza; vena: tormenta", [
                h2("Arteria: cereza;", "vena: tormenta"),
                dos(card(lista("Pérdida súbita e <b>indolora</b>", "Retina pálida y <b>mancha rojo cereza</b>", "Émbolo de carótida o corazón", "Es un EVC: estudia carótidas"), tag="Arteria central", big="Apagón"),
                    card(lista("Baja visual súbita, menos brusca", "Hemorragias en llama por todo el fondo", "Hipertensión, diabetes, glaucoma", "Anti-VEGF si hay edema macular"), tag="Vena central", big="Salsa de tomate")),
                rima("Mayor de 50 con ceguera súbita: pide VSG y PCR. Si es arteritis de células gigantes, esteroide ya."),
            ]),
        ],
    },
}
