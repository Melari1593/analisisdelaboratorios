from generar import h2, card, muted, lista, dos, tabla, acr, rima

ESPECIALIDADES = {
    "neumologia": {
        "nombre": "Neumología",
        "temas": [
            ("Asma: escalones GINA", "Salbutamol solo, nunca solo", [
                h2("Salbutamol solo,", "nunca solo"),
                tabla(["Escalón", "Vía preferida (GINA)"], [
                    ['<span class="wk">1–2</span>', "Budesonida-formoterol <b>a demanda</b>"],
                    ['<span class="wk">3</span>', "Dosis baja diaria + rescate con el mismo inhalador"],
                    ['<span class="wk">4</span>', "Dosis media de mantenimiento y rescate"],
                    ['<span class="wk">5</span>', "+ Tiotropio; fenotipar y valorar biológico"]]),
                card("Crisis: salbutamol + esteroide sistémico + O₂ (SatO₂ 93–95 %). Sin sibilancias ni aire: paro inminente.",
                     big='Tórax <span class="g">silencioso</span> = alarma'),
                rima("“Salbutamol sin esteroide: rescate sin control.”"),
            ]),
            ("EPOC: GOLD", "Cinco-cinco u ocho-ocho: oxígeno", [
                h2("Setenta que no revierte", "es EPOC", 60),
                tabla(["GOLD", "FEV₁ (% del predicho)"], [
                    ["<b>1</b> · leve", '<span class="wk">≥80 %</span>'],
                    ["<b>2</b> · moderada", '<span class="wk">50–79 %</span>'],
                    ["<b>3</b> · grave", '<span class="wk">30–49 %</span>'],
                    ["<b>4</b> · muy grave", '<span class="wk">&lt;30 %</span>']]),
                card("Diagnóstico: FEV₁/FVC &lt;0.70 tras broncodilatador. Grupos B y E: LABA + LAMA.",
                     big='La <span class="g">E</span> es de Exacerbador'),
                rima("“Cinco-cinco u ocho-ocho: oxígeno ≥15 h al día.”<br>PaO₂ ≤55 mmHg o SatO₂ ≤88 %."),
            ]),
            ("Tromboembolia pulmonar", "Dímero D descarta, no confirma", [
                h2("Dímero D", "Descarta, no confirma"),
                tabla(["Wells", "Siguiente paso"], [
                    ["<b>≤4</b> · poco probable", "Dímero D: si es negativo, se descarta"],
                    ["<b>&gt;4</b> · probable", "<b>AngioTAC</b> directa"],
                    ["<b>Con choque</b>", "Ecocardiograma y <b>trombólisis</b>"]]),
                card("En el ECG lo más frecuente es la taquicardia sinusal; el S1Q3T3 es clásico, pero raro. Estable: anticoagula.",
                     big='Taquicardia, no <span class="g">S1Q3T3</span>'),
                rima("“Poco probable, pide el dímero;<br>probable, directo a la tomografía.”"),
            ]),
            ("Neumonía: CURB-65", "0–1 a casa, 2 a la cama, 3 a terapia", [
                h2("CURB-65:", "cada letra, un punto"),
                acr(("C", "Confusión"), ("U", "Urea &gt;42 mg/dL (BUN &gt;19)"), ("R", "Respiración ≥30 por minuto"),
                    ("B", "Baja presión: PAS &lt;90 o PAD ≤60"), ("65", "Edad ≥65 años")),
                card("Ambulatorio sin comorbilidad: amoxicilina o macrólido. Hospitalizado: betalactámico + macrólido o quinolona respiratoria.",
                     big='El culpable: <span class="g">neumococo</span>'),
                rima("“Cero-uno, a casa; dos, a la cama;<br>tres o más, grave: piensa en terapia.”"),
            ]),
            ("Derrame pleural: Light", "Con un criterio de Light basta: exudado", [
                h2("Light: con uno basta", "para ser exudado", 60),
                tabla(["Criterio", "Exudado si…"], [
                    ["<b>Proteína</b> pleura/suero", '<span class="wk">&gt;0.5</span>'],
                    ["<b>DHL</b> pleura/suero", '<span class="wk">&gt;0.6</span>'],
                    ["<b>DHL</b> pleural", '<span class="wk">&gt;2/3</span> del límite sérico']]),
                card("Transudado: insuficiencia cardiaca (la más común), cirrosis, nefrótico. Exudado: neumonía, cáncer y tuberculosis (ADA &gt;40 U/L).",
                     big='Transudado = <span class="g">corazón, hígado, riñón</span>'),
                rima("“Medio, seis décimos y dos tercios.”<br>pH &lt;7.2, glucosa &lt;60 o pus: sonda pleural."),
            ]),
        ],
    },
}
