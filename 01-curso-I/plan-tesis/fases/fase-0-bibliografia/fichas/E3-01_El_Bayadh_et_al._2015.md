# El Bayadh et al., 2015 — Ontology-Alignment Techniques: Survey and Analysis

| Campo | Contenido |
|-------|-----------|
| **ID** | E3-01 |
| **Eje** | E3 — Matching semántico / ontologías |
| **Tipo** | survey |
| **PDF** | `bibliografia/estado-del-arte/Univ Ctr of El Bayadh, Inst. Science and Technology, Algeria et al. - 2015 - Ontology-Alignment Techniques Survey and Analysis.pdf` |
| **Estado ficha** | completada |

## 1. Referencia

- **Autores:** Fatima Ardjani, Djelloul Bouchiha, Mimoun Malki (Université Centre El Bayadh, Argelia)
- **Año:** 2015
- **Título:** Ontology-Alignment Techniques: Survey and Analysis
- **Venue / DOI:** I.J. Modern Education and Computer Science (MECS), Vol. 7, No. 11, pp. 67–78 · DOI 10.5815/ijmecs.2015.11.08

## 2. Objetivo del estudio

Revisar y analizar enfoques de **alineación de ontologías**, clasificándolos en métodos **terminológicos, estructurales, extensionales y semánticos**, para orientar la selección de técnicas según el escenario.

## 3. Dominio y fuente de datos

- **Dominio:** Semantic Web, integración de ontologías, sistemas heterogéneos.
- **Corpus:** literatura sobre ontology matching/alignment; síntesis cualitativa y estadística de frecuencia de tipos de medidas.

## 4. Técnicas usadas

- Survey bibliográfico con categorización en cuatro familias de técnicas de alineación.
- Análisis comparativo de combinaciones de medidas (terminológicas + estructurales + extensionales + semánticas).
- Discusión de ventajas/limitaciones por familia.

## 5. Métricas de evaluación

- Estadísticas de uso relativo de tipos de medidas en enfoques revisados.
- Referencia a métricas clásicas de evaluación de alineaciones (precision, recall, F-measure) en trabajos citados, sin meta-análisis unificado.

## 6. Limitaciones (según autores)

- Ninguna medida aislada es suficiente; combinaciones fijas pueden ser subóptimas.
- Literatura previa a 2015; sin foco en APIs REST/OpenAPI.
- No aborda modelos de referencia sectoriales (p. ej. BIAN).

## 7. Vacío u oportunidad para OpenAPI–BIAN

Proporciona vocabulario de **alineación ontológica** aplicable a **SemanticScore (S)** al contrastar conceptos OpenAPI con *business objects* BIAN, pero **no estudia contratos OpenAPI** ni dominio bancario. La tesis operacionaliza estas familias sobre artefactos documentales bancarios.

## 8. Cita para el plan de tesis

- **Usar en:** §3.4 (bases de alineación ontológica) · §3.5 (E3)
- **Frase clave (1 línea):** La alineación ontológica combina medidas terminológicas, estructurales y semánticas — marco conceptual para la similitud OpenAPI–BIAN, aún no aplicado a Service Domains bancarios.

## 9. Notas de lectura (opcional, no va al documento final)

- ¿Aporta técnica para S, E o C? **S** (medidas terminológicas/semánticas); **C** indirecto (cobertura en alineación). **No E** del modelo tesis (estructura ontológica ≠ StructuralScore OpenAPI–BIAN).
- ¿Menciona OpenAPI + ontología/esquema? **Ontología sí**; OpenAPI **no**.
