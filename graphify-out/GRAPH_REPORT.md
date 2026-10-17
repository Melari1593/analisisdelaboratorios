# Graph Report - analisisdelaboratorios  (2026-10-17)

## Corpus Check
- Large corpus: 264 files · ~3,139,797 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 1368 nodes · 2119 edges · 81 communities (79 shown, 2 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 323 edges (avg confidence: 0.86)
- Token cost: 1,378,585 input · 0 output

## Community Hubs (Navigation)
- Cardio and Obstetric Carousels
- Anemias and Hematology
- Nephrology and Pulmonology Slides
- Graph Project Adoption
- Diabetes Diagnosis
- Arrhythmias and AV Blocks
- ENT Otitis
- Obstetrics Caption Mnemonics
- Surgery Carousel
- Rheumatoid Arthritis
- Urinary Stones and Urology
- Statistical Calculations (references)
- verificar.py CLI Commands
- Graph Algorithms (skill copy)
- Depression and Psychiatry
- Compartment Syndrome and Trauma
- Red Eye and Ophthalmology
- Acute Kidney Injury
- Repaso ENARM Web App JS
- Pediatric Febrile Illnesses
- Cardiology Carousel
- Magnesium Sulfate and Eclampsia
- Gynecology Screening
- Lab Report Server
- Superficial Mycoses
- ENARM Build Script
- Neuro-Cardio Notes
- Nephro-Uro-Gyn Notes (skill copy)
- Lab Web App UI
- Infectology and Pediatrics Captions
- Molar Pregnancy and Prenatal Screening
- Endocrine-Hemato-Derm Notes (copy)
- Pulmonary-GI Notes (copy)
- Fraud Detection Recipe
- Critica Estadistica Skill
- Nephrology Carousel Mnemonics
- Ophthalmology Carousel Mnemonics
- ENARM Exam Strategy
- Neuro-Cardio Notes (copy)
- Psych-ENT-Geriatrics Notes (copy)
- Trauma Captions
- Irritable Bowel and Pancreatitis
- Obstetric-Rheum Notes Updates
- Lab Upload Client JS
- Statistical Calculations (skill)
- Cardiology Captions
- Psychiatry Captions
- Rheumatology Captions
- Lab App Package Config
- Evidence-Based Medicine
- Pulmonology Captions
- Geriatric Giants and Beers
- ENARM Skill Modes
- Endocrine-Hemato-Derm Notes
- Pulmonary-GI Notes
- Psych-ENT-Geriatrics Notes
- Statistical Traps Catalog
- Honest Charts
- Nephrology Captions
- Urology Captions
- Geriatric Scales
- Basic Sciences Notes
- Nephro-Uro-Gyn Notes
- Hematology Carousel
- Neurology Carousel
- Surgery Captions
- Dermatology Captions
- Gastro Captions
- Neurology Captions
- Ophthalmology Captions
- ENT Captions
- Variceal Bleeding
- Clinical Case Method
- Infectology Carousel
- Pulmonology Carousel
- ENT Carousel
- Geriatrics Captions
- Gynecology Captions
- Crohn vs Ulcerative Colitis
- Delirium vs Dementia
- Slide Renderer

## God Nodes (most connected - your core abstractions)
1. `Material de estudio; verifica con GPC vigentes` - 17 edges
2. `h2()` - 15 edges
3. `Nefrología, urología y ginecología — apuntes ENARM` - 15 edges
4. `Neumología y gastroenterología — apuntes ENARM` - 15 edges
5. `Neurología y cardiología — apuntes ENARM` - 15 edges
6. `Algoritmos de grafos y Neo4j GDS` - 15 edges
7. `card()` - 14 edges
8. `muted()` - 14 edges
9. `lista()` - 14 edges
10. `dos()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Datos de relleno (identificadores falsos)` --semantically_similar_to--> `Muestra con sesgo incorporado`  [INFERRED] [semantically similar]
  .claude/skills/graph-data-science/references/receta-fraude.md → book-to-skill/critica-estadistica/references/catalogo-trampas.md
- `Fuga de información (mulesNearby)` --semantically_similar_to--> `Las cifras pequenas que no estan`  [INFERRED] [semantically similar]
  .claude/skills/graph-data-science/references/receta-fraude.md → book-to-skill/critica-estadistica/references/catalogo-trampas.md
- `Disclaimer: material de estudio, no sustituye GPC` --semantically_similar_to--> `Disclaimer: material de estudio, no sustituye GPC`  [INFERRED] [semantically similar]
  book-to-skill/enarm/instagram/pie-de-foto.txt → book-to-skill/enarm/instagram/pie-de-foto-infectologia.txt
- `Disclaimer: material de estudio, no sustituye GPC` --semantically_similar_to--> `Disclaimer: material de estudio, no sustituye GPC`  [INFERRED] [semantically similar]
  book-to-skill/enarm/instagram/pie-de-foto-nefrologia.txt → book-to-skill/enarm/instagram/pie-de-foto-infectologia.txt
- `Disclaimer: material de estudio, no sustituye GPC` --semantically_similar_to--> `Disclaimer: material de estudio, no sustituye GPC`  [INFERRED] [semantically similar]
  book-to-skill/enarm/instagram/pie-de-foto-neumologia.txt → book-to-skill/enarm/instagram/pie-de-foto-infectologia.txt

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Trampas de How to Lie with Statistics aplicadas a reporte honesto** — _claude_skills_critica_estadistica_skill_how_to_lie_with_statistics, _claude_skills_critica_estadistica_references_catalogo_trampas, _claude_skills_critica_estadistica_references_graficas, _claude_skills_critica_estadistica_references_calculos, _claude_skills_critica_estadistica_skill_modo_b_reportar_resultados [EXTRACTED 1.00]
- **Bioestadistica y MBE para el ENARM** — _claude_skills_enarm_references_estrategia_examen_mbe, _claude_skills_enarm_references_estrategia_examen_tabla_2x2, _claude_skills_enarm_references_estrategia_examen_nnt_rr_or, _claude_skills_enarm_references_estrategia_examen_pregunta_pico, _claude_skills_enarm_references_estrategia_examen_niveles_de_evidencia [EXTRACTED 1.00]
- **Receta de deteccion por identificadores compartidos (outliers, WCC, betweenness, features ML)** — _claude_skills_graph_data_science_skill_outliers_topologicos, _claude_skills_graph_data_science_references_algoritmos_centralidad, _claude_skills_graph_data_science_references_algoritmos_deteccion_de_comunidades, _claude_skills_graph_data_science_references_conceptos_ingenieria_de_features_de_grafo, _claude_skills_graph_data_science_skill_receta_fraude [INFERRED 0.85]
- **Pipeline GDS de deteccion de fraude** — _claude_skills_graph_data_science_references_receta_fraude_degree_centrality, _claude_skills_graph_data_science_references_receta_fraude_datos_de_relleno__identificadores_falsos_, _claude_skills_graph_data_science_references_receta_fraude_weakly_connected_components__wcc_, _claude_skills_graph_data_science_references_receta_fraude_betweenness_centrality, _claude_skills_graph_data_science_references_receta_fraude_features_de_grafo_para_clasificador_binario [EXTRACTED 1.00]
- **Skill critica-estadistica y sus referencias** — book_to_skill_critica_estadistica_skill, book_to_skill_critica_estadistica_references_catalogo_trampas, book_to_skill_critica_estadistica_references_graficas, book_to_skill_critica_estadistica_references_calculos, book_to_skill_critica_estadistica_skill_scripts_verificar_py [EXTRACTED 1.00]
- **Generacion de carruseles ENARM** — book_to_skill_enarm_instagram_readme, book_to_skill_enarm_instagram_generar, book_to_skill_enarm_instagram_readme_render_js__playwright_, book_to_skill_enarm_instagram_cardiologia, book_to_skill_enarm_instagram_carrusel, book_to_skill_enarm_instagram_cirugia, book_to_skill_enarm_instagram_dermatologia [INFERRED 0.85]
- **ENARM Instagram carousel + caption publishing set** — book_to_skill_enarm_instagram_pie_de_foto_hematologia, book_to_skill_enarm_instagram_hematologia_carrusel, book_to_skill_enarm_instagram_hematologia_gpc_disclaimer, book_to_skill_enarm_instagram_pie_de_foto_cardiologia_hashtags_enarm, book_to_skill_enarm_instagram_generar [INFERRED 0.85]
- **Time-window emergency mnemonics (needle/balloon/benzo)** — book_to_skill_enarm_instagram_neurologia_mnemotecnia_evc_isquemico, book_to_skill_enarm_instagram_neurologia_mnemotecnia_estado_epileptico, book_to_skill_enarm_instagram_pie_de_foto_cardiologia_mnemotecnia_infarto_con_elevacion_del_st, book_to_skill_enarm_instagram_pediatria_mnemotecnia_reanimacion_neonatal [INFERRED 0.75]
- **Especialidades digest reuses per-specialty mnemonics** — book_to_skill_enarm_instagram_pie_de_foto_especialidades_mnemotecnia_cardiologia, book_to_skill_enarm_instagram_pie_de_foto_especialidades_mnemotecnia_neurologia, book_to_skill_enarm_instagram_pie_de_foto_especialidades_mnemotecnia_gastroenterologia, book_to_skill_enarm_instagram_pie_de_foto_especialidades_mnemotecnia_dermatologia, book_to_skill_enarm_instagram_pie_de_foto_especialidades_mnemotecnia_cirugia, book_to_skill_enarm_instagram_pie_de_foto_cardiologia_mnemotecnia_arritmias_y_bloqueos_av, book_to_skill_enarm_instagram_pie_de_foto_gastro_mnemotecnia_hepatitis_b, book_to_skill_enarm_instagram_pie_de_foto_dermatologia_mnemotecnia_melanoma, book_to_skill_enarm_instagram_pie_de_foto_cirugia_mnemotecnia_fiebre_posoperatoria, book_to_skill_enarm_instagram_neurologia_mnemotecnia_escala_de_glasgow [INFERRED 0.95]
- **Serie de carruseles Instagram de mnemotecnias ENARM por especialidad** — book_to_skill_enarm_instagram_pie_de_foto_infectologia_caption, book_to_skill_enarm_instagram_pie_de_foto_nefrologia_caption, book_to_skill_enarm_instagram_pie_de_foto_neumologia_caption, book_to_skill_enarm_instagram_pie_de_foto_neurologia_caption, book_to_skill_enarm_instagram_pie_de_foto_oftalmologia_caption, book_to_skill_enarm_instagram_pie_de_foto_otorrino_caption, book_to_skill_enarm_instagram_pie_de_foto_pediatria_caption, book_to_skill_enarm_instagram_pie_de_foto_psiquiatria_caption, book_to_skill_enarm_instagram_pie_de_foto_reumatologia_caption, book_to_skill_enarm_instagram_pie_de_foto_traumatologia_caption, book_to_skill_enarm_instagram_pie_de_foto_urologia_caption, book_to_skill_enarm_instagram_pie_de_foto_caption [INFERRED 0.85]
- **Pares pie de foto + carrusel HTML (psiquiatría, reumatología, traumatología, urología)** — book_to_skill_enarm_instagram_pie_de_foto_psiquiatria_caption, book_to_skill_enarm_instagram_pie_de_foto_reumatologia_caption, book_to_skill_enarm_instagram_pie_de_foto_traumatologia_caption, book_to_skill_enarm_instagram_pie_de_foto_urologia_caption, book_to_skill_enarm_instagram_psiquiatria_carousel, book_to_skill_enarm_instagram_reumatologia_carousel, book_to_skill_enarm_instagram_traumatologia_carousel, book_to_skill_enarm_instagram_urologia_carousel [INFERRED 0.85]
- **Bioestadística y epidemiología de examen** — book_to_skill_enarm_references_ciencias_basicas_tabla_2x2_y_medidas_de_asociacion__rr__rm__nnt_, book_to_skill_enarm_references_ciencias_basicas_pruebas_diagnosticas__sensibilidad__especificidad__vpp__vpn, book_to_skill_enarm_references_ciencias_basicas_diseno_de_estudios_epidemiologicos, book_to_skill_enarm_references_ciencias_basicas_niveles_de_prevencion_de_leavell_y_clark [INFERRED 0.85]
- **Receta de fraude: grado → excluir outliers → WCC → betweenness → features ML** — book_to_skill_graph_data_science_references_algoritmos_degree_centrality, book_to_skill_graph_data_science_references_receta_fraude_outliers_topol_gicos__datos_de_relleno_, book_to_skill_graph_data_science_references_algoritmos_wcc, book_to_skill_graph_data_science_references_algoritmos_betweenness_centrality, book_to_skill_graph_data_science_references_receta_fraude_features_de_grafo_para_clasificador_binario [EXTRACTED 1.00]
- **Empaquetado offline de Repaso ENARM** — book_to_skill_enarm_webapp_build, book_to_skill_enarm_webapp_readme_banco_de_reactivos__banco___json_, book_to_skill_enarm_webapp_index_enarm_data_json_embebido, book_to_skill_enarm_webapp_readme_dist_repaso_enarm_html, book_to_skill_enarm_webapp_readme_dist_artifact_html [INFERRED 0.85]
- **Apuntes ENARM derivados del libro 2015 con actualizaciones** — book_to_skill_enarm_references_endocrino_hemato_dermato_libro_de_preparaci_n_enarm__2015_, book_to_skill_enarm_references_endocrino_hemato_dermato_l_nea____actualizaci_n, book_to_skill_enarm_references_endocrino_hemato_dermato_endocrinolog_a__hematolog_a_y_dermatolog_a___apuntes_enarm, book_to_skill_enarm_references_nefro_urologia_ginecologia_nefrolog_a__urolog_a_y_ginecolog_a___apuntes_enarm, book_to_skill_enarm_references_neumologia_gastro_neumolog_a_y_gastroenterolog_a___apuntes_enarm, book_to_skill_enarm_references_neurologia_cardiologia_neurolog_a_y_cardiolog_a___apuntes_enarm, book_to_skill_enarm_references_obstetricia_reumatologia_obstetricia_y_reumatolog_a___apuntes_enarm, book_to_skill_enarm_references_psiquiatria_orl_geriatria_trauma_psiquiatr_a__orl__geriatr_a_y_traumatolog_a___apuntes_enarm [EXTRACTED 1.00]
- **Carrusel Cardiología ENARM mnemotecnias** — book_to_skill_enarm_instagram_png_cardiologia_01_carrusel_cardiolog_a_enarm, book_to_skill_enarm_instagram_png_cardiologia_02_mnemotecnia_pr_que_se_alarga_se_deja__pr_fijo_que_falla_marcapasos, book_to_skill_enarm_instagram_png_cardiologia_03_mnemotecnia_30_para_la_aguja_90_para_el_balon, book_to_skill_enarm_instagram_png_cardiologia_04_mnemotecnia_asi_5_3_2, book_to_skill_enarm_instagram_png_cardiologia_05_mnemotecnia_sabe, book_to_skill_enarm_instagram_png_cardiologia_06_contraindicaciones_farmacologicas_cardiologia [EXTRACTED 1.00]
- **Carrusel Cirugía ENARM mnemotecnias** — book_to_skill_enarm_instagram_png_cirugia_01_carrusel_cirug_a_enarm, book_to_skill_enarm_instagram_png_cirugia_02_mnemotecnia_5_p_fiebre_posoperatoria, book_to_skill_enarm_instagram_png_cirugia_03_mnemotecnia_mantrels, book_to_skill_enarm_instagram_png_cirugia_04_triada_de_charcot_3_c, book_to_skill_enarm_instagram_png_cirugia_05_abcde_atls, book_to_skill_enarm_instagram_png_cirugia_06_mnemotecnia_directa_va_derecho_indirecta_da_la_vuelta [EXTRACTED 1.00]
- **Carrusel Dermatología ENARM mnemotecnias** — book_to_skill_enarm_instagram_png_dermatologia_01_carrusel_dermatolog_a_enarm, book_to_skill_enarm_instagram_png_dermatologia_02_abcde_del_melanoma, book_to_skill_enarm_instagram_png_dermatologia_03_mnemotecnia_baso_es_bonito_espino_se_esparce, book_to_skill_enarm_instagram_png_dermatologia_04_mnemotecnia_psoriasis_extiende_atopia_flexiona, book_to_skill_enarm_instagram_png_dermatologia_05_mnemotecnia_el_oide_es_el_abuelito [EXTRACTED 1.00]
- **Patron de carrusel: portada + 5 mnemotecnias + resumen 'Las 5 frases para el examen'** — book_to_skill_enarm_instagram_png_dermatologia_07_resumen_dermatologia, book_to_skill_enarm_instagram_png_endocrinologia_07_resumen_endocrinologia, book_to_skill_enarm_instagram_png_especialidades_07_resumen_especialidades, book_to_skill_enarm_instagram_png_endocrinologia_01_portada, book_to_skill_enarm_instagram_png_especialidades_01_portada, book_to_skill_enarm_instagram_png_gastro_01_portada [INFERRED 0.85]
- **Tipos de cancer de tiroides en la mnemotecnia Papilar-Folicular-Medular-Anaplasico** — book_to_skill_enarm_instagram_png_endocrinologia_06_cancer_papilar_de_tiroides, book_to_skill_enarm_instagram_png_endocrinologia_06_cancer_folicular_de_tiroides, book_to_skill_enarm_instagram_png_endocrinologia_06_cancer_medular_de_tiroides, book_to_skill_enarm_instagram_png_endocrinologia_06_cancer_anaplasico_de_tiroides, book_to_skill_enarm_instagram_png_endocrinologia_06_mnemotecnia_papilar_popular_folicular_fluye_medular_marca_anaplasico_anciano [EXTRACTED 1.00]
- **Micosis superficiales: oral para pelo/una, topico para piel** — book_to_skill_enarm_instagram_png_dermatologia_06_mnemotecnia_la_crema_no_llega_a_la_raiz, book_to_skill_enarm_instagram_png_dermatologia_06_tina_capitis, book_to_skill_enarm_instagram_png_dermatologia_06_onicomicosis, book_to_skill_enarm_instagram_png_dermatologia_06_pitiriasis_versicolor, book_to_skill_enarm_instagram_png_dermatologia_06_candidosis_cutanea, book_to_skill_enarm_instagram_png_dermatologia_06_griseofulvina, book_to_skill_enarm_instagram_png_dermatologia_06_terbinafina, book_to_skill_enarm_instagram_png_dermatologia_06_ketoconazol_topico [EXTRACTED 1.00]
- **Manejo de sangrado variceal VASO** — book_to_skill_enarm_instagram_png_gastro_04_vaso, book_to_skill_enarm_instagram_png_gastro_04_octreotido_terlipresina, book_to_skill_enarm_instagram_png_gastro_04_ceftriaxona_profilaxis, book_to_skill_enarm_instagram_png_gastro_04_transfusion_restrictiva_hb7, book_to_skill_enarm_instagram_png_gastro_04_ligadura_endoscopica [EXTRACTED 1.00]
- **Cinco mnemotecnias de geriatria ENARM** — book_to_skill_enarm_instagram_png_geriatria_02_cam_1_2_3o4, book_to_skill_enarm_instagram_png_geriatria_03_5_gigantes_i, book_to_skill_enarm_instagram_png_geriatria_04_basta_beers, book_to_skill_enarm_instagram_png_geriatria_05_tipos_incontinencia, book_to_skill_enarm_instagram_png_geriatria_06_estadios_ulcera_presion [EXTRACTED 1.00]
- **Cinco mnemotecnias de ginecologia ENARM** — book_to_skill_enarm_instagram_png_ginecologia_02_tamizaje_cacu_25_35_64, book_to_skill_enarm_instagram_png_ginecologia_03_bi_rads, book_to_skill_enarm_instagram_png_ginecologia_04_rotterdam_2_de_3_r, book_to_skill_enarm_instagram_png_ginecologia_05_3d_y_la_i, book_to_skill_enarm_instagram_png_ginecologia_06_queso_fresa_pescado [EXTRACTED 1.00]
- **Letter-acronym mnemonics (TICS, RIPE, LUCES, AEIOU)** — book_to_skill_enarm_instagram_png_hematologia_02_mnemonic_tics, book_to_skill_enarm_instagram_png_infectologia_03_mnemonic_ripe, book_to_skill_enarm_instagram_png_nefrologia_06_mnemonic_luces, book_to_skill_enarm_instagram_png_nefrologia_05_mnemonic_aeiou_dialisis [INFERRED 0.85]
- **Numeric threshold-ladder mnemonics (CD4 200/100/50, TFG resta 15, VCM 80/100)** — book_to_skill_enarm_instagram_png_infectologia_02_mnemonic_200_100_50, book_to_skill_enarm_instagram_png_nefrologia_05_mnemonic_60_resta_15, book_to_skill_enarm_instagram_png_hematologia_02_mnemonic_tics [INFERRED 0.75]
- **Consumptive/thrombotic platelet disorders and triggers** — book_to_skill_enarm_instagram_png_hematologia_04_cid, book_to_skill_enarm_instagram_png_hematologia_04_ptt, book_to_skill_enarm_instagram_png_hematologia_04_pti, book_to_skill_enarm_instagram_png_hematologia_05_leucemia_promielocitica_m3 [INFERRED 0.85]
- **Numeric staged-threshold mnemonics (time/score ladders)** — book_to_skill_enarm_instagram_png_neurologia_05_5_benzo_20_carga_40_anestesia, book_to_skill_enarm_instagram_png_obstetricia_04_37_34_30_26_semanas_de_interrupcion, book_to_skill_enarm_instagram_png_neumologia_05_cero_uno_a_casa_dos_a_la_cama_tres_terapia, book_to_skill_enarm_instagram_png_neurologia_03_tiempo_es_cerebro_4_5_para_la_aguja, book_to_skill_enarm_instagram_png_neumologia_02_salbutamol_solo_nunca_solo [INFERRED 0.75]
- **Neumologia ENARM carousel (portada, 5 temas, resumen)** — book_to_skill_enarm_instagram_png_neumologia_01_portada_neumologia_5_mnemotecnias, book_to_skill_enarm_instagram_png_neumologia_02_asma_escalones_gina, book_to_skill_enarm_instagram_png_neumologia_03_epoc_gold, book_to_skill_enarm_instagram_png_neumologia_04_tromboembolia_pulmonar, book_to_skill_enarm_instagram_png_neumologia_05_neumonia_curb_65, book_to_skill_enarm_instagram_png_neumologia_06_derrame_pleural_light, book_to_skill_enarm_instagram_png_neumologia_07_resumen_neumologia_5_frases_para_el_examen [EXTRACTED 1.00]
- **Neurologia ENARM carousel (portada, 5 temas, resumen)** — book_to_skill_enarm_instagram_png_neurologia_01_portada_neurologia_5_mnemotecnias, book_to_skill_enarm_instagram_png_neurologia_02_escala_de_glasgow, book_to_skill_enarm_instagram_png_neurologia_03_evc_isquemico, book_to_skill_enarm_instagram_png_neurologia_04_cefaleas, book_to_skill_enarm_instagram_png_neurologia_05_estado_epileptico, book_to_skill_enarm_instagram_png_neurologia_06_guillain_barre_vs_miastenia, book_to_skill_enarm_instagram_png_neurologia_07_resumen_neurologia_5_frases_para_el_examen [EXTRACTED 1.00]
- **Reloj del vertigo: segundos, horas, dias** — book_to_skill_enarm_instagram_png_otorrino_06_vppb, book_to_skill_enarm_instagram_png_otorrino_06_enfermedad_de_meniere, book_to_skill_enarm_instagram_png_otorrino_06_neuritis_vestibular, book_to_skill_enarm_instagram_png_otorrino_06_laberintitis [EXTRACTED 1.00]
- **Diagnostico diferencial de ojo rojo** — book_to_skill_enarm_instagram_png_oftalmologia_02_conjuntivitis, book_to_skill_enarm_instagram_png_oftalmologia_02_glaucoma_agudo, book_to_skill_enarm_instagram_png_oftalmologia_02_uveitis_anterior [EXTRACTED 1.00]
- **Manejo uterotonico de hemorragia posparto** — book_to_skill_enarm_instagram_png_obstetricia_06_oxitocina, book_to_skill_enarm_instagram_png_obstetricia_06_misoprostol, book_to_skill_enarm_instagram_png_obstetricia_06_acido_tranexamico, book_to_skill_enarm_instagram_png_obstetricia_06_hemorragia_posparto [EXTRACTED 1.00]
- **Carrusel Psiquiatria ENARM: 5 mnemotecnias** — book_to_skill_enarm_instagram_png_psiquiatria_02_mnemotecnia_campesina, book_to_skill_enarm_instagram_png_psiquiatria_03_mnemotecnia_litio, book_to_skill_enarm_instagram_png_psiquiatria_04_mnemotecnia_plomo_lento_serotonina_saltarina, book_to_skill_enarm_instagram_png_psiquiatria_05_mnemotecnia_5a_sintomas_negativos, book_to_skill_enarm_instagram_png_psiquiatria_06_mnemotecnia_caos_wernicke [EXTRACTED 1.00]
- **Carrusel Reumatologia ENARM: 5 mnemotecnias** — book_to_skill_enarm_instagram_png_reumatologia_02_mnemotecnia_reumatoide_respeta_punta_dedo, book_to_skill_enarm_instagram_png_reumatologia_03_mnemotecnia_ana_abre_sm_dna_cierran, book_to_skill_enarm_instagram_png_reumatologia_04_mnemotecnia_gota_aguja_negativa, book_to_skill_enarm_instagram_png_reumatologia_05_mnemotecnia_pera, book_to_skill_enarm_instagram_png_reumatologia_06_mnemotecnia_50_cmop [EXTRACTED 1.00]
- **Carrusel Pediatria ENARM: 5 frases para el examen** — book_to_skill_enarm_instagram_png_pediatria_07_piloro_frase, book_to_skill_enarm_instagram_png_pediatria_03_mnemotecnia_corta, book_to_skill_enarm_instagram_png_pediatria_04_mnemotecnia_rose_ola, book_to_skill_enarm_instagram_png_pediatria_05_mnemotecnia_cien_aire_sesenta_manos, book_to_skill_enarm_instagram_png_pediatria_06_prednisona_primero_biopsia_si_persiste [EXTRACTED 1.00]
- **Traumatologia y ortopedia ENARM - 5 mnemotecnias** — book_to_skill_enarm_instagram_png_traumatologia_01_portada, book_to_skill_enarm_instagram_png_traumatologia_02_sindrome_compartimental, book_to_skill_enarm_instagram_png_traumatologia_03_salter_harris, book_to_skill_enarm_instagram_png_traumatologia_04_fractura_cadera, book_to_skill_enarm_instagram_png_traumatologia_05_lesiones_rodilla, book_to_skill_enarm_instagram_png_traumatologia_06_displasia_cadera, book_to_skill_enarm_instagram_png_traumatologia_07_resumen [EXTRACTED 1.00]
- **Urologia ENARM - 5 mnemotecnias** — book_to_skill_enarm_instagram_png_urologia_01_portada, book_to_skill_enarm_instagram_png_urologia_02_litiasis_urinaria, book_to_skill_enarm_instagram_png_urologia_03_hiperplasia_prostatica, book_to_skill_enarm_instagram_png_urologia_04_cancer_prostata, book_to_skill_enarm_instagram_png_urologia_05_torsion_vs_epididimitis, book_to_skill_enarm_instagram_png_urologia_06_ivu_pielonefritis, book_to_skill_enarm_instagram_png_urologia_07_resumen [EXTRACTED 1.00]
- **Urgencias quirurgicas tiempo-dependientes (no esperar signo tardio/estudio)** — book_to_skill_enarm_instagram_png_traumatologia_02_sindrome_compartimental, book_to_skill_enarm_instagram_png_urologia_05_torsion_testicular, book_to_skill_enarm_instagram_png_traumatologia_04_fractura_cadera, book_to_skill_enarm_instagram_png_urologia_02_litiasis_urinaria [INFERRED 0.75]

## Communities (81 total, 2 thin omitted)

### Community 0 - "Cardio and Obstetric Carousels"
Cohesion: 0.08
Nodes (52): Carrusel mnemotecnias cardiologia, Arritmias y bloqueos AV, Infarto con elevacion del ST, Insuficiencia cardiaca: SABE, Carrusel mnemotecnias obstetricia, Hemorragia posparto, RCIU protocolo de Barcelona, Sulfato de magnesio (+44 more)

### Community 1 - "Anemias and Hematology"
Cohesion: 0.06
Nodes (57): Anemia ferropenica (la mas comun), Anemia macrocitica por B12 o folato, Anemia sideroblastica (plomo, alcohol, isoniazida), Mnemotecnia TICS (anemia microcitica), Slide: Anemias por VCM (La microcitica tiene TICS), Talasemia (hierro normal, Mentzer <13), Anemia de enfermedad cronica (ferritina normal/alta), Ferritina = el almacen (<15 confirma ferropenia) (+49 more)

### Community 2 - "Nephrology and Pulmonology Slides"
Cohesion: 0.05
Nodes (55): Anion gap alto: prende las LUCES, Enfermedad renal cronica: Del 60 para abajo, resta 15, Hiperkalemia: Protege, mete, saca, Lesion renal aguda: Prerrenal ahorra, la NTA derrocha, Nefritico vs nefrotico: La O de prOteina, la I de Inflamacion, Resumen Nefrologia: 5 frases para el examen, Portada Neumologia: 5 mnemotecnias, Asma: escalones GINA (+47 more)

### Community 3 - "Graph Project Adoption"
Cohesion: 0.06
Nodes (46): Equipo punta de lanza, Llevar un proyecto de grafos de la idea a producción, Medir el ROI, Neo4j GraphAcademy, Prueba de concepto (POC), Adamic-Adar, Algoritmos de grafos y Neo4j GDS, Búsqueda de caminos (+38 more)

### Community 4 - "Diabetes Diagnosis"
Cohesion: 0.08
Nodes (36): Endocrinologia ENARM portada: 5 mnemotecnias que no se te olvidan, CTGO 75 g, Diagnostico de diabetes mellitus, Glucosa en ayuno, HbA1c, Metformina, Prediabetes, Endocrinologia 2/7: 126 en ayuno, 6.5 y 200 (+28 more)

### Community 5 - "Arrhythmias and AV Blocks"
Cohesion: 0.08
Nodes (32): Especialidades ENARM portada: 5 especialidades, 5 mnemotecnias, Bloqueo AV de tercer grado, Bloqueo AV Mobitz I, Bloqueo AV Mobitz II, Cardioversion sincronizada, Desfibrilacion, Marcapasos, Especialidades 2/7: Inestable? Electricidad (+24 more)

### Community 6 - "ENT Otitis"
Cohesion: 0.07
Nodes (40): Portada: Otorrinolaringologia ENARM - 5 mnemotecnias, Amoxicilina, Otitis externa, Otitis externa maligna, Otitis media aguda, Pseudomonas, Slide 2/7: Otitis media vs externa - Duele al jalar la oreja es de afuera, Faringoamigdalitis estreptococica (+32 more)

### Community 7 - "Obstetrics Caption Mnemonics"
Cohesion: 0.06
Nodes (38): Pie de foto Instagram Obstetricia, Mnemotecnia: VIH: CD4 y profilaxis — 200 neumo, 100 toxo, 50 MAC, Mnemotecnia: Doppler en RCIU — ausente 34, reversa 30, ductus a reversa 26, Mnemotecnia: Mola — COMpleta COpia de papá, PARcial PAR de espermatozoides, Mnemotecnia: Sulfato de magnesio — rodilla, respiración, ritmo; rescata el calcio, Mnemotecnia: Tamiz prenatal — en Down la hCG sube, Mnemotecnia: Uterotónicos en hipertensa — ni ERGO ni CARBÓN; OXI y MISO, Ciencias básicas — apuntes ENARM (+30 more)

### Community 8 - "Surgery Carousel"
Cohesion: 0.09
Nodes (21): Carrusel Cirugía · 5 mnemotecnias ENARM, Fiebre posoperatoria, Slide Cirugía: Las 5 P, en orden de días, Apendicitis escala de Alvarado, Slide Cirugía: Alvarado: MANTRELS, Colangitis, Slide Cirugía: Charcot son 3 C; Reynolds son 5, Slide Cirugía: Lo que mata primero se trata primero (+13 more)

### Community 9 - "Rheumatoid Arthritis"
Cohesion: 0.11
Nodes (27): Carrusel Reumatologia ENARM, Reumatologia 1/7: Portada - 5 mnemotecnias que no se te olvidan, Anti-CCP, Artritis reumatoide, Metotrexato (ancla de tratamiento AR), Osteoartritis, Reumatologia 2/7: Artritis reumatoide vs osteoartritis, Anti-Ro (lupus neonatal, bloqueo AV congenito) (+19 more)

### Community 10 - "Urinary Stones and Urology"
Cohesion: 0.09
Nodes (29): Fasciotomia urgente (presion >30 mmHg o delta diastolica <=30 mmHg), Urologia ENARM - 5 mnemotecnias (portada carrusel), LEOC o ureteroscopia (10-20 mm); nefrolitotomia percutanea >20 mm, Litiasis urinaria, Litiasis urinaria - slide mnemotecnia, TAC simple de abdomen y pelvis (estudio de eleccion), Terapia expulsiva con tamsulosina (5-10 mm), Alfabloqueadores (tamsulosina, doxazosina): relajan cuello vesical, efecto en dias (+21 more)

### Community 11 - "Statistical Calculations (references)"
Cohesion: 0.08
Nodes (26): Calculos que conviene rehacer, Eventos raros y tamano de muestra, Extrapolacion fuera de rango, Incertidumbre de una estimacion (IC de proporcion), Indices aritmetico vs geometrico, Precision falsa, Puntos porcentuales vs porcentaje (base cambiante), Catalogo de trampas (10 familias) (+18 more)

### Community 12 - "verificar.py CLI Commands"
Cohesion: 0.13
Nodes (24): cmd_cambio(), cmd_descuentos(), cmd_diferencia(), cmd_ganancia(), cmd_indice(), cmd_prestamo(), cmd_proporcion(), cmd_raro() (+16 more)

### Community 13 - "Graph Algorithms (skill copy)"
Cohesion: 0.09
Nodes (27): Llevar un proyecto de grafos a produccion (10 pasos), Equipo punta de lanza, Medir el ROI, Neo4j GraphAcademy, Prueba de concepto (POC), Algoritmos de grafos y Neo4j GDS, Busqueda de caminos (Dijkstra, BFS, A*), Centralidad (Degree, PageRank, Betweenness) (+19 more)

### Community 14 - "Depression and Psychiatry"
Cohesion: 0.12
Nodes (25): Carrusel Psiquiatria ENARM, Psiquiatria 1/7: Portada - 5 mnemotecnias que no se te olvidan, Depresion mayor, ISRS (sertralina, fluoxetina, escitalopram), Psiquiatria 2/7: Depresion mayor, Hemodialisis, Intoxicacion por litio (>1.5 mEq/L), Litio (ventana 0.6-1.2 mEq/L) (+17 more)

### Community 15 - "Compartment Syndrome and Trauma"
Cohesion: 0.11
Nodes (24): Traumatologia y ortopedia ENARM - 5 mnemotecnias (portada carrusel), 5 P: Pain, Parestesias, Palidez, Paralisis, Pulso ausente (tardio), Sindrome compartimental, Sindrome compartimental - slide mnemotecnia, Reduccion anatomica abierta con fijacion (tipos III y IV), Fracturas fisarias: Salter-Harris, SALTR (Separada, Arriba, hacia La articulacion, Todo, Reventada), Fracturas fisarias: Salter-Harris - slide mnemotecnia (+16 more)

### Community 16 - "Red Eye and Ophthalmology"
Cohesion: 0.13
Nodes (24): Portada: Oftalmologia ENARM - 5 mnemotecnias, Conjuntivitis, Glaucoma agudo, Ojo rojo, Slide 2/7: Ojo rojo que duele y ve mal - urgencia, Uveitis anterior, Glaucoma de angulo abierto, Glaucoma de angulo cerrado (+16 more)

### Community 17 - "Acute Kidney Injury"
Cohesion: 0.14
Nodes (24): Slide: Portada Nefrologia ENARM - 5 mnemotecnias, FENa (<1% prerrenal, >2% NTA), Definicion KDIGO de lesion renal aguda, Mnemotecnia Prerrenal ahorra; la NTA derrocha, Necrosis tubular aguda (cilindros granulosos cafe lodoso), Slide: Lesion renal aguda (Prerrenal ahorra; la NTA derrocha), C3 bajo vs normal (postestreptococica/lupus vs IgA Berger), Mnemotecnia La O de prOteina; la I de Inflamacion (+16 more)

### Community 18 - "Repaso ENARM Web App JS"
Cohesion: 0.18
Nodes (21): abrir(), calcular(), candidatos(), construir(), disponibles(), filas(), get(), iniciar() (+13 more)

### Community 19 - "Pediatric Febrile Illnesses"
Cohesion: 0.14
Nodes (16): Crisis febril simple, Pediatria 3/7: Crisis febril simple, Escarlatina, Parvovirus B19 (quinta enfermedad), Roseola (HHV-6), Sarampion, Pediatria 4/7: Exantemas, Adrenalina (+8 more)

### Community 20 - "Cardiology Carousel"
Cohesion: 0.17
Nodes (12): Carrusel Cardiología · 5 mnemotecnias ENARM, Arritmias y bloqueos AV, Slide Cardiología: ¿Inestable? Electricidad, Infarto con elevación del ST, Slide Cardiología: 30 para la aguja, 90 para el balón, Estenosis aórtica y soplos, Slide Cardiología: Estenosis aórtica: ASI y 5-3-2, Insuficiencia cardiaca con FE reducida (+4 more)

### Community 21 - "Magnesium Sulfate and Eclampsia"
Cohesion: 0.18
Nodes (12): Gluconato de calcio 1 g IV, Slide 5/7: Sulfato de magnesio - Las 3 R de la intoxicacion, Sulfato de magnesio, Acido tranexamico, Carbetocina, Estudio WOMAN, Hemorragia posparto, Metilergonovina (+4 more)

### Community 22 - "Gynecology Screening"
Cohesion: 0.14
Nodes (17): Ginecologia ENARM: 5 mnemotecnias que no se te olvidan, Ginecologia slide 2: 25 citologia, 35 el virus, 64 te jubilas, Tamizaje CaCU: 25 citologia, 35 el virus, 64 te jubilas, VPH 16 y 18 (~70% de CaCU), BI-RADS: 3 espera; 4 y 5 aguja, NOM-041 (cancer de mama), Ginecologia slide 3: 20 te tocas, 25 te tocan, 40 te aprietan, Tamizaje cancer de mama: 20 te tocas, 25 te tocan, 40 te aprietan (+9 more)

### Community 23 - "Lab Report Server"
Cohesion: 0.15
Nodes (8): createApp(), here, SCHEMA, send(), sample, withServer(), TYPES, validFile()

### Community 24 - "Superficial Mycoses"
Cohesion: 0.20
Nodes (11): Candidosis cutanea, Griseofulvina, Ketoconazol topico, Onicomicosis, Pitiriasis versicolor, Dermatologia 6/7: Tina de cabeza - la crema no llega a la raiz, Terbinafina, Tina capitis (+3 more)

### Community 25 - "ENARM Build Script"
Cohesion: 0.19
Nodes (12): cargar_banco(), main(), enarm-data JSON embebido, Repaso ENARM page, Vista Estudiar, Vista Progreso, Vista Simulacro, app.js (+4 more)

### Community 26 - "Neuro-Cardio Notes"
Cohesion: 0.15
Nodes (14): Neurologia y cardiologia (apuntes ENARM), Cardiovascular, Enfermedad vascular cerebral, Hipertension arterial sistemica, Neurologia, RCP (AHA 2010), Cardiopatia isquemica / SCA, Obstetricia y reumatologia (apuntes ENARM) (+6 more)

### Community 27 - "Nephro-Uro-Gyn Notes (skill copy)"
Cohesion: 0.14
Nodes (14): Anticoncepción, Cáncer cervicouterino, Cáncer de mama, Cáncer de próstata, Enfermedad renal crónica, Ginecología, Lesión renal aguda, Nefrología, urología y ginecología — apuntes ENARM (+6 more)

### Community 28 - "Lab Web App UI"
Cohesion: 0.21
Nodes (14): app.js, Campo clave de acceso, Campo de contexto clínico, Clara page, Dropzone de archivos, Sección de resultado (resumen, hallazgos, preguntas, límites), Selector tipo de estudio (laboratorio/ecografía), ACCESS_TOKEN (+6 more)

### Community 29 - "Infectology and Pediatrics Captions"
Cohesion: 0.17
Nodes (9): Pie de foto Instagram Infectología, Mnemotecnia: Dengue — cuando baja la fiebre, llega el peligro, Mnemotecnia: Meningitis — la bacteria se come el azúcar, Mnemotecnia: Tuberculosis — 2 meses con 4, 4 meses con 2, Pie de foto Instagram Pediatría, Mnemotecnia: Crisis febril simple — si es CORTA no se estudia, Mnemotecnia: Estenosis de píloro — HIPO-HIPO-ALCA, Mnemotecnia: Reanimación neonatal — cien aire, sesenta manos, sesenta jeringa (+1 more)

### Community 30 - "Molar Pregnancy and Prenatal Screening"
Cohesion: 0.23
Nodes (13): Portada Obstetricia: 5 mnemotecnias, COMpleta = COpia de papa (46,XX), Enfermedad trofoblastica: Mola completa vs parcial, hCG en mola, PARcial = PAR de espermatozoides (69,XXY), AFP que sube, tubo que se abre; AFP que baja, piensa en el 21, En Down, la hCG es la que sube, Tamiz prenatal (+5 more)

### Community 31 - "Endocrine-Hemato-Derm Notes (copy)"
Cohesion: 0.15
Nodes (13): Cetoacidosis diabética y estado hiperosmolar, Dermatología, Diabetes mellitus tipo 2, Endocrinología, Endocrinología, hematología y dermatología — apuntes ENARM, Hematología, Hipotiroidismo, Leucemia linfoblástica aguda (+5 more)

### Community 32 - "Pulmonary-GI Notes (copy)"
Cohesion: 0.15
Nodes (13): Asma, Cáncer colorrectal, Cirrosis y hepatopatía alcohólica, Enfermedad inflamatoria intestinal, Enfermedad tromboembólica venosa, EPOC, Gastrointestinal, Hemorragia de tubo digestivo alto (+5 more)

### Community 33 - "Fraud Detection Recipe"
Cohesion: 0.27
Nodes (10): Receta: detectar entidades sospechosas por identificadores compartidos, Betweenness Centrality, Datos de relleno (identificadores falsos), Degree Centrality, Fraude de primera parte, Mula (Mule), Neo4j Graph Data Science (GDS), SharedId (+2 more)

### Community 34 - "Critica Estadistica Skill"
Cohesion: 0.20
Nodes (10): Como responderle a una estadistica, Skill critica-estadistica, Cinco preguntas para auditar una cifra, Modo A: auditar una cifra ajena, Modo B: reportar resultados sin enganar, scripts/verificar.py, book-to-skill, CAM Curso de Actualizacion Medica ENARM (McGraw-Hill 2015) (+2 more)

### Community 35 - "Nephrology Carousel Mnemonics"
Cohesion: 0.17
Nodes (12): Carrusel mnemotecnias Nefrología (ENARM), Acidosis metabólica y anion gap: "Anion gap alto: prende las LUCES", Enfermedad renal crónica: "Del 60 para abajo, resta 15", Hiperkalemia: "Protege, mete, saca", Lesión renal aguda: "Prerrenal ahorra; la NTA derrocha", Nefrítico vs. nefrótico: "La O de prOteína; la I de Inflamación", Carrusel mnemotecnias Pediatría (ENARM), Crisis febril simple: "Si es CORTA, no se estudia" (+4 more)

### Community 36 - "Ophthalmology Carousel Mnemonics"
Cohesion: 0.17
Nodes (12): Carrusel mnemotecnias Oftalmología (ENARM), Desprendimiento de retina: "Moscas, destellos y se cierra el telón", Glaucoma: "Glaucoma crónico: ladrón silencioso", Oclusión vascular de la retina: "Arteria: cereza; vena: tormenta", Ojo rojo: "Ojo rojo que duele y ve mal: urgencia", Retinopatía diabética: "Vaso nuevo, problema nuevo", Pie de foto Instagram: endocrinologia, Cáncer de tiroides: Papilar Popular; Folicular Fluye por sangre (+4 more)

### Community 37 - "ENARM Exam Strategy"
Cohesion: 0.21
Nodes (9): CIFRHS, ENARM, Estrategia de examen, MBE y expediente clínico, Guías de Práctica Clínica (GPC/CENETEC), Homeostasis y respuesta a la agresión, Medicina basada en evidencias (MBE), NOM-004-SSA3-2012 (expediente clínico), Sección en inglés del ENARM (+1 more)

### Community 38 - "Neuro-Cardio Notes (copy)"
Cohesion: 0.17
Nodes (12): Arritmias y bloqueos, Cardiovascular, Enfermedad vascular cerebral, Epilepsia, Esclerosis múltiple, Hipertensión arterial, Insuficiencia cardiaca, Meningitis bacteriana (+4 more)

### Community 39 - "Psych-ENT-Geriatrics Notes (copy)"
Cohesion: 0.17
Nodes (12): Demencias y Alzheimer, Demencia/Alzheimer en geriatría, Depresión mayor, Esquizofrenia, Fracturas expuestas, Geriatría, Otitis media aguda, Otorrinolaringología (+4 more)

### Community 40 - "Trauma Captions"
Cohesion: 0.27
Nodes (9): Pie de foto Instagram Traumatología y ortopedia, Mnemotecnia: Displasia de cadera — Barlow la bota, Ortolani la regresa, Mnemotecnia: Fractura de cadera — adentro se cambia, afuera se fija, Mnemotecnia: Lesiones de rodilla — Lachman con LCA, McMurray con menisco, Mnemotecnia: Salter-Harris — SALTR: entre más alto, peor, Mnemotecnia: Síndrome compartimental — primero el dolor, al final el pulso, Carrusel Instagram mnemotecnias Traumatología y ortopedia (7 slides), Fractura de cadera intracapsular (artroplastia/tornillos) vs extracapsular (osteosíntesis) (+1 more)

### Community 41 - "Irritable Bowel and Pancreatitis"
Cohesion: 0.18
Nodes (11): Datos de alarma (no es funcional), Criterios Roma IV 1-3-2 (SII), Sindrome de intestino irritable, Gastro slide 6: Roma IV 1-3-2, Hepatitis B: Antigeno S = Si esta; anticuerpo S = Salvado, Pancreatitis aguda: Tres veces tres, Gastro slide 7: Resumen - 5 frases para el examen, Letrozol para embarazo en SOP (+3 more)

### Community 42 - "Obstetric-Rheum Notes Updates"
Cohesion: 0.18
Nodes (10): Artritis reumatoide, Control prenatal, Estados hipertensivos del embarazo, Gota e hiperuricemia, Hemorragia posparto, Lupus eritematoso sistémico, Obstetricia, Obstetricia y reumatología — apuntes ENARM (+2 more)

### Community 43 - "Lab Upload Client JS"
Cohesion: 0.25
Nodes (8): addFiles(), allowed, drop, mime(), readFile(), renderFiles(), selected, status()

### Community 44 - "Statistical Calculations (skill)"
Cohesion: 0.20
Nodes (10): Cuentas que conviene rehacer, Base cambiante, Eventos raros y regla del 3, Extrapolacion, Indices: media aritmetica vs geometrica, Intervalo de Wilson para proporcion, Precision falsa, Puntos porcentuales vs porcentaje (+2 more)

### Community 45 - "Cardiology Captions"
Cohesion: 0.22
Nodes (10): Escala de Glasgow: "Ojos 4, Voz 5, Movimiento 6", Pie de foto Instagram: cardiologia, Hashtags #ENARM #ENARM2026 #Mnemotecnias #RepasoENARM, Arritmias y bloqueos AV: PR que se alarga, se deja; PR fijo que falla, marcapasos, Estenosis aórtica y soplos: ASI y 5-3-2, Fármacos con trampa: Nitrato con sildenafil, presión que se desploma, Insuficiencia cardiaca con FE reducida: El que SABE, sobrevive, Pie de foto Instagram: especialidades (+2 more)

### Community 46 - "Psychiatry Captions"
Cohesion: 0.33
Nodes (9): Pie de foto Instagram Psiquiatría, Mnemotecnia: Depresión mayor — la CAMPESINA triste: 5 de 9 por 2 semanas, Mnemotecnia: Esquizofrenia — positivo suma, negativo resta: las 5 A, Mnemotecnia: Litio — 0.6 a 1.2; tóxico arriba de 1.5, Mnemotecnia: Neuroléptico maligno vs serotoninérgico — plomo lento vs saltarina, Mnemotecnia: Wernicke — tiamina antes que glucosa: CAOs, Carrusel Instagram mnemotecnias Psiquiatría (7 slides), ISRS primera línea en depresión (efecto 4-6 semanas) (+1 more)

### Community 47 - "Rheumatology Captions"
Cohesion: 0.31
Nodes (8): Pie de foto Instagram Reumatología, Mnemotecnia: AR vs osteoartritis — la reumatoide respeta la punta del dedo, Mnemotecnia: Arteritis de células gigantes — más de 50, VSG de 50: prednisona ya, Mnemotecnia: Espondiloartritis — HLA-B27 es una PERA, Mnemotecnia: Gota — aguja negativa; meta menor de 6, Mnemotecnia: LES — ANA abre la puerta; Sm y DNA la cierran, Arteritis de células gigantes: 50-C-M-O-P, esteroide antes que biopsia, Carrusel Instagram mnemotecnias Reumatología (7 slides)

### Community 48 - "Lab App Package Config"
Cohesion: 0.20
Nodes (9): engines, node, name, private, scripts, start, test, type (+1 more)

### Community 49 - "Evidence-Based Medicine"
Cohesion: 0.28
Nodes (9): Post hoc: correlacion no es causa, Estrategia de examen, MBE y expediente clinico (apuntes ENARM), CIFRHS, Medicina basada en evidencias (MBE), Niveles de evidencia (USPSTF, Oxford, GRADE), NOM-004-SSA3-2012 expediente clinico, Pregunta PICO, Sepsis / falla organica multiple (+1 more)

### Community 50 - "Pulmonology Captions"
Cohesion: 0.22
Nodes (8): Mnemotecnia: Sífilis — VDRL vigila, FTA firma, Pie de foto Instagram Neumología, Mnemotecnia: Asma GINA — salbutamol solo, nunca solo, Mnemotecnia: Derrame pleural — un criterio de Light basta: exudado, Mnemotecnia: EPOC GOLD — cinco-cinco u ocho-ocho: oxígeno, Mnemotecnia: Neumonía CURB-65 — 0-1 casa, 2 cama, 3 terapia, Mnemotecnia: TEP — dímero D descarta, no confirma, Pruebas diagnósticas: sensibilidad, especificidad, VPP, VPN

### Community 51 - "Geriatric Giants and Beers"
Cohesion: 0.31
Nodes (9): Los 5 gigantes geriatricos con I, Mnemotecnia BASTA (criterios de Beers), Criterios de Beers, Polifarmacia (>=5 farmacos), Evitar antimuscarinicos (oxibutinina) en adulto mayor, Mirabegron para incontinencia de urgencia, Geriatria slide 5: Rie, corre, se derrama o no llega, Mnemotecnia Rie, corre, se derrama o no llega (incontinencia urinaria) (+1 more)

### Community 52 - "ENARM Skill Modes"
Cohesion: 0.28
Nodes (8): Skill ENARM, Bioestadistica y MBE, CIFRHS, Generar casos / simulacro, Plan de estudio, references/estrategia-examen.md, Repaso de un tema, Resolver caso clinico

### Community 53 - "Endocrine-Hemato-Derm Notes"
Cohesion: 0.25
Nodes (8): Endocrinologia, hematologia y dermatologia (apuntes ENARM), Cetoacidosis diabetica y estado hiperosmolar, Dermatologia, Diabetes mellitus tipo 2, Endocrinologia, Hematologia, Hipotiroidismo, Diabetes mellitus gestacional

### Community 54 - "Pulmonary-GI Notes"
Cohesion: 0.25
Nodes (8): Neumologia y gastroenterologia (apuntes ENARM), Enfermedad inflamatoria intestinal, EPOC, Gastrointestinal, Neumologia, Pancreatitis aguda, Tuberculosis pulmonar, Enfermedad tromboembolica venosa

### Community 55 - "Psych-ENT-Geriatrics Notes"
Cohesion: 0.25
Nodes (8): Demencias / Alzheimer, Psiquiatria, ORL, geriatria y traumatologia (apuntes ENARM), Trastorno depresivo mayor, Geriatria, Otorrinolaringologia, Psiquiatria, Sindrome demencial y Alzheimer (geriatria), Traumatologia y ortopedia

### Community 56 - "Statistical Traps Catalog"
Cohesion: 0.25
Nodes (8): Catalogo de trampas, Como estadisticular, El promedio bien escogido, La cifra semiatada, Literary Digest 1936, Muestra con sesgo incorporado, Post hoc: correlacion no es causa, Tercer factor (confusor)

### Community 57 - "Honest Charts"
Cohesion: 0.32
Nodes (8): La grafica guau, La imagen unidimensional, Graficas, pictogramas y mapas honestos, Chequeo en matplotlib/plotly, Eje truncado, Mapa coropletico por tasas, Pictograma escalado en altura, Reglas para producir graficas

### Community 58 - "Nephrology Captions"
Cohesion: 0.25
Nodes (7): Pie de foto Instagram Nefrología, Mnemotecnia: Anion gap alto — prende las LUCES, Mnemotecnia: Enfermedad renal crónica — del 60 para abajo resta 15, Mnemotecnia: Hiperkalemia — protege, mete, saca, Mnemotecnia: Lesión renal aguda — prerrenal ahorra, NTA derrocha, Mnemotecnia: Nefrítico vs nefrótico — O de prOteína, I de Inflamación, Mnemotecnia: Síndrome nefrótico infantil — prednisona primero, biopsia si persiste

### Community 59 - "Urology Captions"
Cohesion: 0.43
Nodes (7): Pie de foto Instagram Urología, Mnemotecnia: Cáncer de próstata — nariz hiperplasia, frente cáncer, Mnemotecnia: Hiperplasia prostática — alfa afloja, finasterida achica, Mnemotecnia: IVU — cistitis 5-1-3; bacteriuria solo las 2 E, Mnemotecnia: Litiasis urinaria — 5 sale, 10 se empuja, 20 se rompe, Mnemotecnia: Torsión testicular vs epididimitis — 6 horas; Prehn positivo infección, Carrusel Instagram mnemotecnias Urología (7 slides)

### Community 60 - "Geriatric Scales"
Cohesion: 0.29
Nodes (8): Geriatria ENARM: 5 mnemotecnias que no se te olvidan, Indice de Katz (ABVD: cuida el cuerpo), Escala de Lawton (AIVD: lleva la logistica), Geriatria slide 3: Los 5 gigantes empiezan con I, Geriatria slide 4: Beers te dice BASTA, Escala de Braden (menor puntaje, mayor riesgo), Estadios de ulcera por presion: rojo, ampolla, grasa y hueso, Geriatria slide 6: Rojo, ampolla, grasa y hueso

### Community 61 - "Basic Sciences Notes"
Cohesion: 0.29
Nodes (7): Ciencias basicas (bioquimica, micro, farmaco, salud publica, inmuno, genetica) (apuntes ENARM), Bioquimica, Farmacologia, Genetica, Inmunologia (Gell y Coombs), Microbiologia, CAM. Curso de Actualizacion Medica (McGraw-Hill, 2015)

### Community 62 - "Nephro-Uro-Gyn Notes"
Cohesion: 0.29
Nodes (7): Nefrologia, urologia y ginecologia (apuntes ENARM), Cancer cervicouterino, Cancer de mama, Enfermedad renal cronica, Ginecologia, Nefrologia y urologia, Trastornos acido-base

### Community 63 - "Hematology Carousel"
Cohesion: 0.52
Nodes (7): Carrusel mnemotecnias Hematología (ENARM), Anemias por VCM: "La microcítica tiene TICS", Anticoagulantes y antídotos: "Heparina, protamina; warfarina, vitamina", Ferropenia vs. enfermedad crónica: "Almacén vacío o almacén con candado", Leucemias por edad: "La LLA va al kínder; la LLC, al asilo", PTI, PTT y CID: "A la PTT no le des plaquetas: dale plasma", Pie de foto Instagram: hematologia

### Community 64 - "Neurology Carousel"
Cohesion: 0.29
Nodes (6): Carrusel mnemotecnias Neurología (ENARM), Cefaleas: "La migraña PULSA", Estado epiléptico: "Benzo, carga, coma (5-20-40)", EVC isquémico: "Tiempo es cerebro: 4.5 para la aguja", Guillain-Barré vs. miastenia: "Guillain sube; la miastenia se cansa", Infarto con elevación del ST: 30 para la aguja, 90 para el balón

### Community 65 - "Surgery Captions"
Cohesion: 0.29
Nodes (7): Pie de foto Instagram: cirugia, Apendicitis (Alvarado): MANTRELS, Colangitis: Charcot son 3 C; Reynolds son 5, Fiebre posoperatoria: Pulmón, pipí, piernas, piel, pastillas, Hernias inguinales: La Directa va Derecho; la Indirecta da la vuelta, Trauma ATLS: Lo que mata primero se trata primero, Cirugía: fiebre posoperatoria 5 P

### Community 66 - "Dermatology Captions"
Cohesion: 0.29
Nodes (7): Pie de foto Instagram: dermatologia, Basocelular vs. espinocelular: Baso es Bonito y Bueno; Espino se Esparce, Melanoma: ABCDE; Breslow = pronóstico, Micosis superficiales: La crema no llega a la raíz, Pénfigo vs. penfigoide: El oide es el abuelito, Psoriasis: Psoriasis Extiende; atopia Flexiona, Dermatología: ABCDE del melanoma

### Community 67 - "Gastro Captions"
Cohesion: 0.29
Nodes (7): Gastroenterología: hepatitis B antígeno S = Sí está; anticuerpo S = Salvado, Pie de foto Instagram: gastro, Crohn vs. CUCI: Las 5 C del Crohn, Hepatitis B: Antígeno S = Sí está; anticuerpo S = Salvado, Intestino irritable: Roma 1, 3, 2, Pancreatitis aguda: Tres veces tres, Sangrado por várices: VASO

### Community 68 - "Neurology Captions"
Cohesion: 0.29
Nodes (6): Pie de foto Instagram Neurología, Mnemotecnia: Cefaleas — la migraña PULSA, Mnemotecnia: Escala de Glasgow — ojos 4, voz 5, movimiento 6; con ocho intubo, Mnemotecnia: Estado epiléptico — 5 benzo, 20 carga, 40 anestesia, Mnemotecnia: EVC isquémico — TAC sin contraste; 4.5 para la aguja, Mnemotecnia: Guillain-Barré vs miastenia — Guillain sube, miastenia se cansa

### Community 69 - "Ophthalmology Captions"
Cohesion: 0.29
Nodes (6): Pie de foto Instagram Oftalmología, Mnemotecnia: Desprendimiento de retina — moscas, destellos y telón, Mnemotecnia: Glaucoma — crónico roba en silencio, agudo asalta, Mnemotecnia: Oclusión vascular retiniana — arteria cereza, vena tormenta, Mnemotecnia: Ojo rojo — duele y ve mal: urgencia, Mnemotecnia: Retinopatía diabética — vaso nuevo, problema nuevo

### Community 70 - "ENT Captions"
Cohesion: 0.29
Nodes (6): Pie de foto Instagram Otorrinolaringología, Mnemotecnia: Epistaxis — adelante el niño, atrás el abuelo, Mnemotecnia: Faringoamigdalitis — las 5 T de McIsaac, Mnemotecnia: Hipoacusia Rinne y Weber, Mnemotecnia: Otitis media vs externa — duele al jalar la oreja: de afuera, Mnemotecnia: Vértigo periférico — segundos, horas, días

### Community 71 - "Variceal Bleeding"
Cohesion: 0.29
Nodes (7): Ceftriaxona profilactica en cirrotico que sangra, Ligadura endoscopica en primeras 12 h, Octreotido / terlipresina (vasoactivo), Gastro slide 4: Varices sangrando - llena el VASO, Transfusion restrictiva Hb <7 (meta 7-8 g/dL), Ulcera peptica sangrante: IBP IV + endoscopia <24 h, Mnemotecnia VASO (sangrado variceal)

### Community 73 - "Infectology Carousel"
Cohesion: 0.33
Nodes (6): Carrusel mnemotecnias Infectología (ENARM), Dengue: "Cuando baja la fiebre, llega el peligro", Meningitis: LCR: "La bacteria se come el azúcar", Sífilis: "Uno no duele, dos mancha, tres destruye", Tuberculosis: "2 meses con 4, 4 meses con 2 (RIPE)", VIH: CD4 y profilaxis: "CD4 a la mitad, bicho nuevo"

### Community 74 - "Pulmonology Carousel"
Cohesion: 0.33
Nodes (6): Carrusel mnemotecnias Neumología (ENARM), Asma: escalones GINA: "Salbutamol solo, nunca solo", Derrame pleural: Light: "Light: con uno basta para ser exudado", EPOC: GOLD: "Setenta que no revierte es EPOC", Neumonía: CURB-65: "CURB-65: cada letra, un punto", Tromboembolia pulmonar: "Dímero D Descarta, no confirma"

### Community 75 - "ENT Carousel"
Cohesion: 0.33
Nodes (6): Carrusel mnemotecnias Otorrinolaringología (ENARM), Epistaxis: "Adelante el niño, atrás el abuelo", Faringoamigdalitis: "Las 5 T de McIsaac", Hipoacusia: Rinne y Weber: "Weber: Conductiva al Culpable, Sensorial al Sano", Otitis media vs. externa: "¿Duele al jalar la oreja? Es de afuera", Vértigo periférico: "Segundos, horas, días: el reloj del vértigo"

### Community 76 - "Geriatrics Captions"
Cohesion: 0.33
Nodes (6): Pie de foto Instagram: geriatria, Delirium vs. demencia: CAM 1+2+(3 o 4), Incontinencia urinaria: Ríe, corre, se derrama o no llega, Polifarmacia y criterios de Beers: ¡BASTA!, Síndromes geriátricos: 5 gigantes con I; Katz, Úlceras por presión: Rojo, ampolla, grasa y hueso

### Community 77 - "Gynecology Captions"
Cohesion: 0.33
Nodes (6): Pie de foto Instagram: ginecologia, Cáncer de mama: BI-RADS 3 espera; 4 y 5, aguja, Endometriosis: Las 3 D y la I, SOP: Rotterdam pide 2 de 3 R, Tamizaje CaCu: 25 citología, 35 el virus, 64 te jubilas, Vaginitis: Queso, fresa y pescado

### Community 78 - "Crohn vs Ulcerative Colitis"
Cohesion: 0.50
Nodes (5): Mnemotecnia Las 5 C del Crohn, Colangitis esclerosante primaria, CUCI (colitis ulcerosa cronica idiopatica), Enfermedad de Crohn, Gastro slide 5: Las 5 C del Crohn

### Community 79 - "Delirium vs Dementia"
Cohesion: 0.60
Nodes (5): Busca la causa: infeccion, farmacos, globo vesical, CAM 1+2+(3 o 4), Delirium, Demencia, Geriatria slide 2: Delirium llega de golpe; la demencia, despacio

## Ambiguous Edges - Review These
- `Modo B: reportar resultados propios sin enganar (checklist)` → `Ingenieria de features de grafo`  [AMBIGUOUS]
  .claude/skills/graph-data-science/references/conceptos.md · relation: conceptually_related_to
- `NOM-004-SSA3-2012 (expediente clínico)` → `Pacientes duplicados por expediente`  [AMBIGUOUS]
  book-to-skill/graph-data-science/references/receta-fraude.md · relation: conceptually_related_to
- `Anemia macrocitica por B12 o folato` → `Isoniazida (neuropatia, piridoxina)`  [AMBIGUOUS]
  book-to-skill/enarm/instagram/png/hematologia-02.png · relation: conceptually_related_to

## Knowledge Gaps
- **374 isolated node(s):** `How to Lie with Statistics (Darrell Huff, 1954)`, `Indices aritmetico vs geometrico`, `Precision falsa`, `Extrapolacion fuera de rango`, `El promedio bien escogido (media/mediana/moda)` (+369 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 432 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Estrategia de examen, MBE y expediente clínico` connect `ENARM Exam Strategy` to `ENARM Build Script`, `Endocrine-Hemato-Derm Notes (copy)`?**
  _High betweenness centrality (0.022) - this node is a cross-community bridge._
- **Are the 16 inferred relationships involving `Material de estudio; verifica con GPC vigentes` (e.g. with `Carrusel mnemotecnias Infectología (ENARM)` and `Carrusel mnemotecnias Nefrología (ENARM)`) actually correct?**
  _`Material de estudio; verifica con GPC vigentes` has 16 INFERRED edges - model-reasoned connections that need verification._
- **What connects `How to Lie with Statistics (Darrell Huff, 1954)`, `Indices aritmetico vs geometrico`, `Precision falsa` to the rest of the system?**
  _374 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Cardio and Obstetric Carousels` be split into smaller, more focused modules?**
  _Cohesion score 0.07887323943661972 - nodes in this community are weakly interconnected._
- **Why does `Carruseles de Instagram: mnemotecnias ENARM` connect `Cardio and Obstetric Carousels` to `ENARM Skill Modes`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Modo B: reportar resultados propios sin enganar (checklist)` and `Ingenieria de features de grafo`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `NOM-004-SSA3-2012 (expediente clínico)` and `Pacientes duplicados por expediente`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._