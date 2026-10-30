# Ejes del estado del arte — Grupo 9.2

Mapa y **síntesis por eje** para Cap. 3 §3.5–3.6.  
Detalle paper a paper: `fichas/` y Anexo B (`Matriz_Papers_EstadoDelArte_Grupo9.2.xlsx`).  
Borrador narrativo Fase C: `../fase-c-marco-teorico/CAPITULO_03_ESTADO_DEL_ARTE.md`.

---

## Mapa de ejes (§3.5.1)

| Eje | Pregunta | Papers asignados |
|-----|----------|------------------|
| **E1 — OpenAPI como estándar** | ¿Cómo se describe y usa OpenAPI? | Casas 2021, Mainas 2023, Santos y Casas 2025 |
| **E2 — Matching estructural** | ¿Cómo se formaliza la correspondencia entre esquemas? | Shvaiko 2005 |
| **E3 — Matching semántico / ontologías** | ¿Qué técnicas de similitud existen? | El Bayadh 2015, Chandrasekaran 2022, Santos Sousa 2026 |
| **E4 — Microservicios / interfaces** | ¿Cómo se vincula modelo de dominio e interfaces? | Schmidt 2020 |
| **E5 — Testing y calidad API (borde)** | Delimita qué **no** es el foco de la tesis | Ehsan 2022, Golmohammadi 2024, Otieno 2026, Tanveer 2025, Vitorino 2025 |
| **E6 — Selección/recomendación servicios** | Contexto semántico de servicios | Mahanra Rao 2025 |

**Nota:** Mainas 2023 está también en `bibliografia/aporte/`; en estado del arte se cita como referencia semántica OpenAPI (E1).

---

## Síntesis por eje (insumo §3.5)

### E1 — OpenAPI como estándar

OpenAPI/Swagger es el estándar de facto para APIs REST (Casas et al., 2021): documentación, generación, pruebas y gobernanza. Mainas et al. (2023) enriquecen contratos con **ontología y anotaciones semánticas** (OpenAPI → RDF), útil para normalización y **S**. Santos y Casas (2025) miden **métricas de gateway** (runtime), no alineación documental.

- **Aporte S/E/C:** S (Mainas); contexto de artefacto (E1 en general).
- **Vacío:** ningún paper liga OpenAPI con **Service Domains BIAN** ni sector bancario como par de evaluación.

### E2 — Matching estructural

Shvaiko y Euzenat (2005) clasifican técnicas de **schema matching** (sintáctico, semántico, externo; elemento y estructura). Base teórica para mapear paths/schemas OpenAPI a *behaviors*/*business objects* BIAN.

- **Aporte S/E/C:** **E** (StructuralScore).
- **Vacío:** sin OpenAPI, REST ni dominio bancario.

### E3 — Matching semántico / ontologías

El Bayadh et al. (2015) sintetizan **alineación ontológica** por familias de medidas. Chandrasekaran y Mago (2022) revisan **similitud semántica** (WordNet → embeddings/transformers). Santos Sousa et al. (2026) catalogan **embeddings en ontology matching** (supervisión, escalabilidad, correspondencias complejas).

- **Aporte S/E/C:** **S** principal; **C** parcial vía cobertura ontológica.
- **Vacío:** sin contratos OpenAPI ni BIAN; sin score integrado.

### E4 — Microservicios / interfaces

Schmidt y Thiry (2020) relacionan **MDE/DDD** con descomposición en microservicios: capacidades de dominio → límites de servicio. Contexto para entender BIAN como referencia de negocio frente a APIs expuestas.

- **Aporte S/E/C:** **E** contextual (dominio → interfaz).
- **Vacío:** sin métrica de alineación OpenAPI–BIAN.

### E5 — Testing y calidad API (borde)

Cinco surveys confirman un cuerpo extenso en **testing REST**, ML para pruebas, **vulnerabilidades** y generación adversarial. OpenAPI es input de verificación, no objeto de alineación con modelos de negocio.

- **Aporte S/E/C:** **delimitación** — fuera del foco (Cap. 1.6).
- **Vacío:** orthogonal al AlignmentScore documental.

### E6 — Selección/recomendación de servicios

Mahanra Rao et al. (2025) revisan **BERT** para selección de servicios y QoS. Semántica de descripciones de servicio, no validación contra Service Domain BIAN.

- **Aporte S/E/C:** **S** parcial (embeddings de descripción).
- **Vacío:** recomendación/QoS ≠ alineación OpenAPI ↔ BIAN.

---

## Hallazgos transversales

| # | Hallazgo |
|---|----------|
| H1 | OpenAPI está maduro como especificación técnica; la literatura **no** estandariza su coherencia con modelos de negocio bancarios. |
| H2 | Existen técnicas de matching **estructural** (E2) y **semántico** (E3) aplicables por separado, no integradas para OpenAPI–BIAN. |
| H3 | Trabajos de **testing/seguridad** (E5) y **selección de servicios** (E6) usan OpenAPI con otros fines. |
| H4 | Ningún paper revisado define **S + E + C → AlignmentScore** sobre contratos OpenAPI bancarios vs. Service Domains BIAN. |

---

## Brecha y oportunidad (§3.6)

**Brecha central:** la intersección **OpenAPI bancario ↔ BIAN** carece de un **modelo de alineación reproducible** que integre similitud semántica, correspondencia estructural y cobertura de conceptos en un **AlignmentScore** clasificable.

| Vacío | Descripción breve |
|-------|-------------------|
| **V1** | Sin estudios que tomen ambos artefactos en banca |
| **V2** | Sin métrica integrada S, E, C |
| **V3** | Sin CoverageScore sobre *business objects* BIAN |
| **V4** | Sin procedimiento documentado comparable al pipeline propuesto |
| **V5** | Confusión frecuente con calidad runtime (E5/E6) vs. coherencia documental |

**Oportunidad:** diseñar el modelo de alineación y el procedimiento de cálculo (plan de tesis, Guía 1); construcción y experimentación a escala → tesis 2 (Guía 2).

Redacción extendida: `../fase-c-marco-teorico/CAPITULO_03_ESTADO_DEL_ARTE.md` §3.6.

---

*Actualizado tras completar 14 fichas (Fase 0) — listo como base para Fase C/E.*
