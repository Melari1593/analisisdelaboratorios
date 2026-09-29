from generar import h2, card, muted, lista, dos, tabla, acr, rima

ESPECIALIDADES = {
    "urologia": {
        "nombre": "Urología",
        "temas": [
            ("Litiasis urinaria", "5 sale, 10 se empuja, 20 se rompe", [
                h2("5 sale, 10 se empuja,", "20 se rompe", 56),
                tabla(["Tamaño (mm)", "Manejo"], [
                    ['<span class="wk">&lt;5</span>', "Sale solo: líquidos y <b>AINE</b>"],
                    ['<span class="wk">5–10</span>', "<b>Tamsulosina</b> (expulsiva, uréter distal)"],
                    ['<span class="wk">10–20</span>', "<b>LEOC</b> (ondas de choque) o ureteroscopia"],
                    ['<span class="wk">&gt;20</span>', "<b>Nefrolitotomía percutánea</b> (renal)"]]),
                card("Estudio de elección: <b>TAC simple</b> de abdomen y pelvis. Con fiebre y obstrucción: catéter JJ o nefrostomía + antibiótico.",
                     big="Sin contraste se ve la piedra"),
                rima("“Piedra que tapa y da fiebre,<br>se drena antes de que se quiebre.”"),
            ]),
            ("Hiperplasia prostática", "Alfa afloja; finasterida achica", [
                h2("Alfa afloja;", "finasterida achica"),
                dos(card(lista("Tamsulosina, doxazosina", "Relaja el cuello vesical", "Efecto en <b>días</b>", "Ojo: hipotensión ortostática"), tag="Alfabloqueador", big="Afloja"),
                    card(lista("Finasterida, dutasterida", "Reduce el volumen prostático", "Efecto en <b>~6 meses</b>", "Baja el APE a la <b>mitad</b>"), tag="Inhibidor 5α-reductasa", big="Achica")),
                card("Retención urinaria recurrente, IVU de repetición, litiasis vesical, hematuria recurrente o daño renal. Estándar: <b>RTUP</b>.",
                     tag="Cirugía si hay complicaciones"),
                rima("“Con finasterida, el APE que ves, multiplícalo por dos.”"),
            ]),
            ("Cáncer de próstata", "Nariz, hiperplasia; frente, cáncer", [
                h2("Nariz, hiperplasia;", "frente, cáncer"),
                card("Al tacto la HPB es ahulada como la punta de la nariz; el cáncer es pétreo como la frente.", big="Toca y compara"),
                tabla(["Dato", "Clave"], [
                    ["<b>Zona</b>", "<b>Periférica</b> (la HPB: transicional)"],
                    ["<b>APE</b>", "&gt;4 ng/mL o nódulo: estudiar"],
                    ["<b>Diagnóstico</b>", "<b>Biopsia</b> guiada por ultrasonido (RM previa si hay)"],
                    ["<b>Pronóstico</b>", "Gleason / grupo ISUP"],
                    ["<b>Metástasis</b>", "Hueso <b>osteoblástico</b>, columna"]]),
                rima("“El cáncer de próstata construye hueso: metástasis blásticas.”"),
            ]),
            ("Torsión testicular vs. epididimitis", "Torsión: 6 horas; Prehn positivo, infección", [
                h2("Torsión:", "el reloj de 6 horas"),
                dos(card(lista("Adolescente, dolor <b>súbito</b>", "Testículo alto y horizontal", "Sin reflejo cremastérico", "Prehn negativo", "<b>Cirugía en &lt;6 h</b>"), tag="Torsión"),
                    card(lista("Dolor <b>gradual</b> y fiebre", "Cremastérico presente", "Prehn <b>positivo</b>", "&lt;35: clamidia, gonococo", "&gt;35: <i>E. coli</i>"), tag="Epididimitis")),
                card("Torsión: detorsión y fijación de <b>ambos</b> testículos. Epididimitis &lt;35 años: ceftriaxona 500 mg IM + doxiciclina 10 días."),
                rima("“Prehn Positivo, Proceso infeccioso.”<br>¿Torsión? Al quirófano sin esperar el Doppler."),
            ]),
            ("IVU y pielonefritis", "Cistitis 5-1-3; bacteriuria: solo las 2 E", [
                h2("Cistitis:", "5 · 1 · 3"),
                tabla(["Fármaco", "Duración"], [
                    ["<b>Nitrofurantoína</b> 100 mg c/12 h", '<span class="wk">5 días</span>'],
                    ["<b>Fosfomicina</b> 3 g", '<span class="wk">1 dosis</span>'],
                    ["<b>TMP-SMX</b> (si resistencia &lt;20 %)", '<span class="wk">3 días</span>']]),
                card("Fiebre, dolor lumbar, Giordano positivo y <b>cilindros leucocitarios</b>. Ciprofloxacino 7 días o ceftriaxona; hospitaliza si está grave.",
                     tag="Pielonefritis", big="Si hay fiebre, subió al riñón"),
                rima("“Bacteriuria sin síntomas se trata solo en las 2 E:<br>Embarazo y Endoscopia urológica.”"),
            ]),
        ],
    },
}
