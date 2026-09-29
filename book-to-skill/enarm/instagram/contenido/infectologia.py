from generar import h2, card, muted, lista, dos, tabla, acr, rima

ESPECIALIDADES = {
    "infectologia": {
        "nombre": "Infectología",
        "temas": [
            ("VIH: CD4 y profilaxis", "200 neumo, 100 toxo, 50 MAC", [
                h2("CD4 a la mitad,", "bicho nuevo"),
                tabla(["CD4", "Oportunista", "Profilaxis"], [
                    ['<span class="wk">&lt;200</span>', "<b>Pneumocystis</b>", "TMP-SMX"],
                    ['<span class="wk">&lt;100</span>', "<b>Toxoplasma</b> (IgG&nbsp;+)", "TMP-SMX"],
                    ['<span class="wk">&lt;50</span>', "<b>MAC</b> y CMV", "Azitromicina solo si no inicia TAR"]]),
                card("Tamizaje con prueba de <b>4.ª generación</b> (antígeno p24 + anticuerpos) y prueba confirmatoria. Tratamiento antirretroviral a <b>todos</b>, sin importar los CD4.",
                     big="Diagnóstico: tamiza y confirma"),
                rima("“Doscientos, cien, cincuenta: cada mitad trae su cuenta.” El TMP-SMX cubre los dos primeros."),
            ]),
            ("Tuberculosis", "2 meses con 4, 4 meses con 2", [
                h2("2 meses con 4,", "4 meses con 2"),
                acr(("R", "Rifampicina: <strong>Rojo</strong> naranja en orina y lágrimas; hepatotóxica"),
                    ("I", "Isoniazida: <strong>Inerva mal</strong> (neuropatía): dale piridoxina"),
                    ("P", "Pirazinamida: <strong>Podagra</strong> (ácido úrico ↑, gota)"),
                    ("E", "Etambutol: <strong>Enceguece</strong> (neuritis óptica, rojo-verde)")),
                card("Baciloscopia seriada o PCR (Xpert MTB/RIF); el <b>cultivo</b> es el estándar de oro. Fase intensiva HRZE y sostén con HR.",
                     big="Diagnóstico y esquema"),
                rima("“Rifampicina pinta, isoniazida adormece, pirazinamida hincha el dedo y etambutol apaga el verde.”"),
            ]),
            ("Dengue", "Cuando baja la fiebre, llega el peligro", [
                h2("Cuando baja la fiebre,", "llega el peligro", 58),
                tabla(["Fase", "Qué pasa"], [
                    ["<b>Febril</b> (2–7 días)", "Fiebre, dolor retroocular; NS1 +"],
                    ['<b>Crítica</b> <span style="white-space:nowrap">(24–48 h)</span>', "Al ceder la fiebre: <b>fuga de plasma</b> y choque"],
                    ["<b>Recuperación</b>", "Reabsorbe líquidos: cuidado con la sobrecarga"]]),
                card("Dolor abdominal intenso, vómito persistente, líquido en serosas, sangrado de mucosas, letargia, hígado &gt;2 cm, hematocrito ↑ con plaquetas ↓.",
                     tag="Signos de alarma", big="Con alarma, hospitaliza"),
                rima("“Si el termómetro baja y el hematocrito sube, vigila.” Solo paracetamol: nada de AINE."),
            ]),
            ("Meningitis: LCR", "La bacteria se come el azúcar", [
                h2("La bacteria", "se come el azúcar"),
                tabla(["LCR", "Bacteriana", "Viral", "Tuberculosa"], [
                    ["<b>Células</b>", "Neutrófilos", "Linfocitos", "Linfocitos"],
                    ["<b>Glucosa</b>", '<b class="g">Muy baja</b>', "Normal", "Baja"],
                    ["<b>Proteínas</b>", "Muy altas", "Normales o ↑ leve", "Muy altas"],
                    ["<b>Pista</b>", "Turbio", "Claro", "ADA ↑, nervios craneales"]]),
                card("Ceftriaxona + vancomicina + dexametasona. Suma <b>ampicilina</b> (Listeria) en &gt;50 años e inmunosuprimidos.",
                     big="Empírico: no esperes al cultivo"),
                rima("“El virus deja el azúcar; la bacteria se la acaba; la TB se la come despacio.”"),
            ]),
            ("Sífilis", "VDRL vigila, FTA firma", [
                h2("Uno no duele, dos mancha,", "tres destruye", 54),
                tabla(["Etapa", "Clave"], [
                    ["<b>Primaria</b>", "Chancro <b>indoloro</b>, bordes duros, adenopatía"],
                    ["<b>Secundaria</b>", "Roséola en <b>palmas y plantas</b>, condiloma plano"],
                    ["<b>Terciaria</b>", "Gomas, aortitis, tabes dorsal"]]),
                card("La no treponémica (VDRL o RPR) sirve para tamizar y seguir la respuesta. La treponémica (FTA-ABS) confirma y queda positiva de por vida.",
                     big='<span class="g">V</span>DRL <span class="g">V</span>igila, <span class="g">F</span>TA <span class="g">F</span>irma'),
                rima("Temprana: penicilina G benzatínica 2.4 millones UI IM, dosis única. Neurosífilis: penicilina cristalina IV."),
            ]),
        ],
    },
}
