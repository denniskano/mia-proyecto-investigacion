# Chandrasekaran y Mago, 2022 — Evolution of Semantic Similarity: A Survey

| Campo | Contenido |
|-------|-----------|
| **ID** | E3-02 |
| **Eje** | E3 — Matching semántico / ontologías |
| **Tipo** | survey |
| **PDF** | `bibliografia/estado-del-arte/Chandrasekaran y Mago - 2022 - Evolution of Semantic Similarity—A Survey.pdf` |
| **Estado ficha** | completada |

## 1. Referencia

- **Autores:** Dhivya Chandrasekaran, Vijay Mago
- **Año:** 2021 (publicación ACM CSur feb. 2021; catalogado como 2022 en el repositorio)
- **Título:** Evolution of Semantic Similarity: A Survey
- **Venue / DOI:** ACM Computing Surveys, Vol. 54, No. 2, Article 41 · DOI 10.1145/3440755

## 2. Objetivo del estudio

Trazar la evolución de métodos de **similitud semántica** desde enfoques basados en conocimiento y corpus hasta redes neuronales y transformers, categorizando fortalezas y debilidades de cada paradigma.

## 3. Dominio y fuente de datos

- **Dominio:** NLP, Semantic Textual Similarity (STS), aplicaciones generales de comparación de significado.
- **Corpus:** revisión de métodos knowledge-based (WordNet), corpus-based (TF-IDF, LSA), deep learning (Word2Vec, BERT) e híbridos; benchmarks STS2012–2014 y afines.

## 4. Técnicas usadas

- Taxonomía de métodos de similitud semántica por paradigma y época.
- Análisis comparativo cualitativo; referencia a datasets y métricas estándar de STS.
- Discusión de tendencias hacia embeddings contextuales (transformers).

## 5. Métricas de evaluación

- Correlación con juicios humanos en benchmarks STS (Pearson/Spearman según dataset).
- Comparación de desempeño relativo por familia de métodos en tareas de similitud textual.

## 6. Limitaciones (según autores)

- Foco en **texto/NLP**, no en nombres de campos OpenAPI ni IRIs ontológicos directamente.
- Campo en rápida obsolescencia post-BERT; no cubre LLMs recientes en detalle.
- No aborda integración multi-métrica (estructural + semántica + cobertura).

## 7. Vacío u oportunidad para OpenAPI–BIAN

Fundamenta opciones para **SemanticScore (S)** (embeddings/similitud entre etiquetas y descripciones OpenAPI y términos BIAN). No menciona OpenAPI, REST ni BIAN; la tesis adapta estas técnicas al dominio bancario documental.

## 8. Cita para el plan de tesis

- **Usar en:** §3.4 (similitud semántica) · §3.5 (E3) · §4.4 (cálculo de S)
- **Frase clave (1 línea):** Los métodos de similitud semántica evolucionan hacia embeddings contextuales, aplicables a comparar vocabulario OpenAPI con conceptos BIAN, pero sin propuesta integrada de alineación bancaria.

## 9. Notas de lectura (opcional, no va al documento final)

- ¿Aporta técnica para S, E o C? **S** principalmente.
- ¿Menciona OpenAPI + ontología/esquema? **No** directamente.
