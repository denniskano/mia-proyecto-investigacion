# Capítulo 3 — Borrador §3.5 y §3.6 (Fase C)

Fuente editable para el estado del arte del plan de tesis.  
Síntesis por eje: `../fase-0-bibliografia/EJES_ESTADO_DEL_ARTE.md` · Detalle por paper: Anexo B y `../fase-0-bibliografia/fichas/`.

---

## 3.5 Estado del arte por ejes temáticos

El estado del arte se organiza en **seis ejes** (E1–E6) que responden a preguntas distintas sobre OpenAPI, matching estructural/semántico, arquitectura de servicios y delimitación del foco investigativo. No se presentan catorce resúmenes aislados: cada eje sintetiza los hallazgos convergentes de los papers asignados (Casas et al., 2021; Mainas et al., 2023; Santos y Casas, 2025; Shvaiko y Euzenat, 2005; El Bayadh et al., 2015; Chandrasekaran y Mago, 2022; Santos Sousa et al., 2026; Schmidt y Thiry, 2020; Ehsan et al., 2022; Golmohammadi et al., 2024; Otieno y Araka, 2026; Tanveer et al., 2025; Vitorino et al., 2025; Mahanra Rao et al., 2025). La Tabla 6 resume por eje; la Tabla 7 remite al Anexo B con la ficha completa de cada paper.

### 3.5.1 Eje E1 — OpenAPI como estándar

La literatura confirma que OpenAPI/Swagger es el **estándar de facto** para describir APIs REST de forma machine-readable (Casas et al., 2021). Los usos mapeados van más allá de la documentación: generación de código, pruebas, gobernanza y automatización, pero **ningún estudio** del eje vincula esos contratos con modelos de referencia de negocio bancario tipo BIAN.

Mainas et al. (2023) avanzan hacia **OpenAPI enriquecido semánticamente**: anotaciones (`x-refersTo`, `x-kindOf`, etc.), ontología REST/Hydra, traducción OpenAPI → RDF y consultas SPARQL. Aporta técnicas aplicables al **SemanticScore (S)** y a la normalización de artefactos, aunque en dominio genérico y sin Service Domains BIAN.

Santos y Casas (2025) catalogan **métricas de API Gateway** (runtime, latencia, tráfico). Delimitan un borde útil: la calidad operativa en producción **no equivale** a la coherencia documental OpenAPI ↔ modelo de negocio.

**Conclusión E1:** OpenAPI está maduro como artefacto técnico; la literatura no resuelve su **alineación** con capacidades de negocio estandarizadas en banca.

### 3.5.2 Eje E2 — Matching estructural

Shvaiko y Euzenat (2005) sistematizan el **schema matching**: técnicas aproximadas/exactas y sintácticas, semánticas o externas a nivel de elemento y estructura. El marco es anterior a OpenAPI y JSON Schema, pero fundamenta el **StructuralScore (E)** al contrastar paths, operations y schemas con la organización de un Service Domain BIAN (*behaviors*, *business objects*).

**Conclusión E2:** Existe base teórica sólida para correspondencias estructurales; falta aplicarla a **pares OpenAPI bancario ↔ BIAN** con métrica reproducible.

### 3.5.3 Eje E3 — Matching semántico y ontologías

Tres líneas convergen. El Bayadh et al. (2015) clasifican **alineación ontológica** (medidas terminológicas, estructurales, extensionales y semánticas). Chandrasekaran y Mago (2022) trazan la evolución de **similitud semántica** desde recursos léxicos hasta embeddings y transformers. Santos Sousa et al. (2026) revisan **embeddings para ontology matching**, con limitaciones de supervisión, escalabilidad y correspondencias complejas.

Ninguno aborda OpenAPI ni BIAN directamente; todos aportan técnicas candidatas para **SemanticScore (S)** y, en parte, cobertura conceptual (**CoverageScore, C**).

**Conclusión E3:** La similitud semántica está bien documentada; no existe propuesta integrada que la aplique a **vocabulario OpenAPI bancario vs. conceptos BIAN** dentro de un modelo de alineación único.

### 3.5.4 Eje E4 — Microservicios e interfaces

Schmidt y Thiry (2020) revisan estrategias de **identificación de microservicios** con MDE y DDD: descomposición desde modelos de dominio hacia límites de servicio. Contextualiza por qué los Service Domains BIAN son referencia de negocio y las APIs su capa de exposición, sin medir coherencia entre ambas.

**Conclusión E4:** La literatura arquitectónica relaciona dominio e interfaces; **no cuantifica** desalineación OpenAPI–BIAN.

### 3.5.5 Eje E5 — Testing y calidad API (borde del estudio)

Cinco revisiones (Ehsan et al., 2022; Golmohammadi et al., 2024; Otieno y Araka, 2026; Tanveer et al., 2025; Vitorino et al., 2025) cubren **testing REST**, ML para pruebas, vulnerabilidades y generación adversarial de datos. OpenAPI aparece como **entrada para verificación runtime**, no como objeto a alinear con modelos BIAN.

**Conclusión E5:** Confirma la delimitación del plan de tesis (Cap. 1.6): testing, seguridad y QoS operativa **quedan fuera** del foco; el producto central es el **AlignmentScore documental**.

### 3.5.6 Eje E6 — Selección y recomendación de servicios

Mahanra Rao et al. (2025) revisan enfoques **BERT** para selección/recomendación de servicios web y predicción de QoS. La representación semántica de descripciones de servicio es adyacente a S, pero el objetivo es **ranking/consumo**, no validar un contrato frente a un Service Domain de referencia.

**Conclusión E6:** Contexto semántico de servicios; **no sustituye** un modelo de alineación OpenAPI ↔ BIAN.

**Tabla 6. Síntesis del estado del arte por ejes (E1–E6)**

| Eje | Papers | Hallazgo principal | Aporte a S / E / C | Vacío respecto a OpenAPI–BIAN |
|-----|--------|-------------------|-------------------|------------------------------|
| **E1** | Casas 2021; Mainas 2023; Santos y Casas 2025 | OpenAPI consolidado; enriquecimiento semántico posible | S (Mainas); contexto estándar | Sin vínculo con Service Domains BIAN |
| **E2** | Shvaiko 2005 | Taxonomía de schema matching | E | Sin aplicación REST/banca/BIAN |
| **E3** | El Bayadh 2015; Chandrasekaran 2022; Santos Sousa 2026 | Ontología matching + embeddings + STS | S; C parcial | Sin contratos OpenAPI ni dominio bancario |
| **E4** | Schmidt 2020 | Dominio (DDD/MDE) → microservicios | E contextual | Sin métrica de alineación |
| **E5** | Ehsan 2022; Golmohammadi 2024; Otieno 2026; Tanveer 2025; Vitorino 2025 | Testing, ML-test, seguridad | Delimitación (fuera de foco) | Orthogonal al AlignmentScore |
| **E6** | Mahanra Rao 2025 | BERT + QoS en selección de servicios | S parcial | Recomendación ≠ alineación BIAN |

La Tabla 7 (Anexo B) detalla objetivo, técnicas, métricas y limitaciones **paper por paper**.

---

## 3.6 Brecha y oportunidad de investigación

### 3.6.1 Qué sí cubre la literatura revisada

De forma transversal, el estado del arte permite afirmar que:

1. **OpenAPI** es el formato dominante para especificar APIs REST y soporta automatización en el ciclo de vida del software (E1).
2. Existen marcos formales para **correspondencia entre esquemas** (E2) y **similitud semántica / alineación ontológica** (E3), incluidos embeddings de última generación.
3. La **arquitectura orientada al dominio** justifica separar modelos de negocio y interfaces técnicas (E4).
4. Un volumen considerable de trabajo aborda **calidad, prueba y seguridad** de APIs (E5), útil para delimitar el problema pero no para resolverlo.
5. La **representación semántica de servicios** se explota en selección y recomendación (E6).

Ninguna de estas líneas, tomadas aisladamente o en conjunto en los catorce papers revisados, responde a la pregunta del plan de tesis: *¿en qué medida un contrato OpenAPI bancario refleja el modelo de negocio de un Service Domain BIAN y cómo cuantificarlo de forma reproducible?*

### 3.6.2 Vacíos identificados

| Vacío | Evidencia en el review | Implicación para la tesis |
|-------|------------------------|---------------------------|
| **V1 — Intersección OpenAPI ∩ BIAN** | Ningún paper estudia ambos artefactos en el sector bancario | El objeto de estudio (contrato OpenAPI bancario vs. SD BIAN) no está cubierto |
| **V2 — Métrica integrada** | E2 y E3 aportan técnicas parciales; E1 no evalúa alineación | Justifica **S**, **E**, **C** y **AlignmentScore** como producto original |
| **V3 — Cobertura de conceptos** | Matching ontológico discute cobertura; no sobre *business objects* BIAN en OpenAPI | Justifica **CoverageScore (C)** |
| **V4 — Procedimiento reproducible** | Mainas propone pipeline RDF; no scores comparables ni clasificación | Justifica diseño metodológico Cap. 4 (Guía 1) |
| **V5 — Gobernanza documental** | E5/E6 abordan runtime o selección, no deriva OpenAPI–modelo de referencia | Motiva alineación previa a despliegue/certificación |

### 3.6.3 Oportunidad de investigación

La brecha abre la oportunidad de **diseñar un modelo de alineación** que, dado un contrato OpenAPI bancario y un Service Domain BIAN emparejado:

- normalice ambos artefactos a representaciones comparables;
- calcule **SemanticScore (S)**, **StructuralScore (E)** y **CoverageScore (C)**;
- integre **AlignmentScore = α·S + β·E + γ·C** con clasificación interpretativa (Alta / Media / Baja / Nula).

Este plan de tesis documenta el **diseño** de ese modelo y del procedimiento de cálculo (Guía 1). La construcción del artefacto software y la experimentación empírica a escala corresponden al trabajo de investigación de tesis 2 (Guía 2), como se delimita en §1.6.

La investigación contribuye al vacío **V1–V4** con un enfoque reproducible sobre **artefactos documentales**, orientado a gobernanza de APIs bancarias y trazabilidad negocio–tecnología, sin sustituir testing operativo ni certificación regulatoria.

---

*Borrador Fase C — integrar en §3.1 (antecedentes narrativos) y redactar §3.2–3.4 en Fase E.*
