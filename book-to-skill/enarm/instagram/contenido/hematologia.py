from generar import h2, card, muted, lista, dos, tabla, acr, rima

ESPECIALIDADES = {
    "hematologia": {
        "nombre": "Hematología",
        "temas": [
            ("Anemias por VCM", "La microcítica tiene TICS", [
                h2("La microcítica", "tiene TICS"),
                acr(("T", "Talasemia (hierro normal, Mentzer &lt;13)"),
                    ("I", "Insuficiencia de hierro: ferropenia, la más común"),
                    ("C", "Crónica (enfermedad inflamatoria), a veces"),
                    ("S", "Sideroblástica: plomo, alcohol, isoniazida")),
                card("VCM &gt;100: déficit de B12 o folato. Solo la <b>B12</b> daña los nervios; dar folato solo corrige la anemia, pero no el daño neurológico.",
                     big='Macro: <span class="g">B12</span> o folato'),
                rima("“Menos de 80, micro; más de 100, macro.”"),
            ]),
            ("Ferropenia vs. enfermedad crónica", "Almacén vacío o almacén con candado", [
                h2("Almacén vacío", "o almacén con candado"),
                tabla(["Dato", "Ferropénica", "Crónica"], [
                    ["<b>Ferritina</b>", '<span class="wk">Baja</span>', '<span class="wk">Normal o alta</span>'],
                    ["<b>Transferrina</b>", "↑", "↓"],
                    ["<b>Hierro sérico</b>", "↓", "↓"],
                    ["<b>ADE</b>", "↑", "Normal"]]),
                card("Ferritina &lt;15 lo confirma (&lt;30 lo sugiere). Adulto mayor u hombre con ferropenia: busca sangrado digestivo con endoscopia y colonoscopia.",
                     big='Ferritina = <span class="g">el almacén</span>'),
                rima("“En la ferropenia la bodega está vacía;<br>en la crónica está llena, pero la hepcidina la cierra.”"),
            ]),
            ("PTI, PTT y CID", "A la PTT no le des plaquetas: dale plasma", [
                h2("La CID lo consume todo;", "la PTT tapa los vasos", 56),
                tabla(["", "Clave", "Tratamiento"], [
                    ["<b>PTI</b>", "Solo plaquetas bajas; tiempos normales", "Esteroide · IgIV"],
                    ["<b>PTT</b>", "Esquistocitos, fiebre, neuro, riñón; ADAMTS13 ↓", "<b>Recambio plasmático</b>"],
                    ["<b>CID</b>", "TP y TTPa ↑, fibrinógeno ↓, dímero D ↑", "Tratar la causa"]]),
                card("Niño con petequias 2–3 semanas después de una infección viral y solo plaquetas bajas: PTI, que casi siempre se resuelve sola.",
                     big='Niño + virosis = <span class="g">PTI</span>'),
                rima("“A la PTT no le des plaquetas: dale plasma.”"),
            ]),
            ("Leucemias por edad", "La LLA va al kínder; la LLC, al asilo", [
                h2("La LLA va al kínder;", "la LLC, al asilo", 58),
                tabla(["Leucemia", "Edad", "Pista"], [
                    ["<b>LLA</b>", '<span style="white-space:nowrap">2–5 años</span>', "La más común en niños"],
                    ["<b>LMA</b>", "Adultos", "Bastones de Auer"],
                    ["<b>LMC</b>", '<span style="white-space:nowrap">40–60 años</span>', "Filadelfia t(9;22) → imatinib"],
                    ["<b>LLC</b>", "&gt;60 años", "Linfocitosis y sombras de Gumprecht"]]),
                card("Promielocítica (M3): t(15;17), alto riesgo de CID. Tratamiento: ácido transretinoico (ATRA).",
                     big='M3 = <span class="g">CID</span>'),
                rima("“Auer, mieloide aguda; Filadelfia, mieloide crónica.”"),
            ]),
            ("Anticoagulantes y antídotos", "Heparina, protamina; warfarina, vitamina", [
                h2("Heparina: protamina;", "warfarina: vitamina", 60),
                tabla(["Fármaco", "Vigilar", "Antídoto"], [
                    ["<b>Heparina</b>", "TTPa", "Protamina"],
                    ["<b>Enoxaparina</b>", "Anti-Xa", "Protamina (parcial)"],
                    ["<b>Warfarina</b>", "INR", "Vitamina K + CCP"],
                    ["<b>Dabigatrán</b>", "—", "Idarucizumab"],
                    ["<b>Rivaroxabán, apixabán</b>", "—", "Andexanet o CCP"]]),
                rima("“Heparina, TTPa, protamina;<br>warfarina, INR, vitamina.”<br>INR meta 2–3 · CCP = concentrado de complejo protrombínico."),
            ]),
        ],
    },
}
