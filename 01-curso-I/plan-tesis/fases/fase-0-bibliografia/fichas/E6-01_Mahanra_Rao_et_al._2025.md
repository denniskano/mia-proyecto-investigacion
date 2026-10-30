# Mahanra Rao et al., 2025 — BERT-Based Web Service Selection and Recommendation

| Campo | Contenido |
|-------|-----------|
| **ID** | E6-01 |
| **Eje** | E6 — Selección/recomendación servicios |
| **Tipo** | systematic review |
| **PDF** | `bibliografia/estado-del-arte/Mahanra Rao et al. - 2025 - BERT-Based Approaches for Web Service Selection and Recommendation A Systematic Review with a Focus.pdf` |
| **Estado ficha** | completada |

## 1. Referencia

- **Autores:** Vijayalakshmi Mahanra Rao, R Kanesaraj Ramasamy, Md Shohel Sayeed
- **Año:** 2025
- **Título:** BERT-Based Approaches for Web Service Selection and Recommendation: A Systematic Review with a Focus on QoS Prediction
- **Venue / DOI:** Future Internet (MDPI), Vol. 17, 543 · DOI 10.3390/fi17120543

## 2. Objetivo del estudio

Revisar sistemáticamente (PRISMA, **25 papers**, 2020–2024) enfoques **BERT/transformers** para **selección y recomendación de servicios web**, con foco en predicción de **QoS**.

## 3. Dominio y fuente de datos

- **Dominio:** service selection/recommendation en ecosistemas de servicios web (WSDL/REST, catálogos).
- **Corpus:** 25 estudios primarios sobre representación semántica de descripciones de servicio + predicción QoS; modelos híbridos semántico–numéricos.

## 4. Técnicas usadas

- Systematic review (PRISMA).
- BERT y variantes para embeddings de descripciones de servicios; ranking y predicción QoS.
- Síntesis de mitigación cold-start y sparsity en matrices QoS.

## 5. Métricas de evaluación

- Precisión de predicción QoS, calidad de ranking/recomendación (métricas varían por estudio).
- Comparación de overhead computacional e interpretabilidad de modelos BERT.

## 6. Limitaciones (según autores)

- Datasets benchmark limitados; **alto costo computacional** de BERT.
- **Interpretabilidad** reducida; poca pre-training específica de dominio bancario.
- Objetivo = seleccionar servicio por QoS/descripción, no alinear contrato con modelo de referencia.

## 7. Vacío u oportunidad para OpenAPI–BIAN

Contexto **E6** (rol: **exclusión explícita**): similitud semántica de descripciones optimiza **selección/recomendación** con QoS, no **conformidad** de un contrato OpenAPI bancario frente a un **Service Domain BIAN**.

## 8. Cita para el plan de tesis

- **Usar en:** §3.5 (E6 — contexto semántico de servicios) · §3.6 (diferencia: recomendación ≠ alineación documental)
- **Frase clave (1 línea):** BERT mejora selección semántica de servicios web con QoS, pero no propone alineación OpenAPI–BIAN con métricas S, E y C integradas.

## 9. Notas de lectura (opcional, no va al documento final)

- ¿Aporta técnica para S, E o C? **S** parcial (embeddings de descripción); **E/C** no.
- ¿Menciona OpenAPI + ontología/esquema? **Servicios web/REST** en corpus; **OpenAPI/BIAN** no como par de alineación.
