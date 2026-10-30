# Santos Sousa et al., 2026 — Survey on Embedding Methods Applied to Ontology Matching

| Campo | Contenido |
|-------|-----------|
| **ID** | E3-03 |
| **Eje** | E3 — Matching semántico / ontologías |
| **Tipo** | survey |
| **PDF** | `bibliografia/estado-del-arte/Santos Sousa et al. - 2026 - Survey on Embedding Methods Applied to Ontology Matching.pdf` |
| **Estado ficha** | completada |

## 1. Referencia

- **Autores:** Guilherme Santos Sousa, Rinaldo Jose Lima, Cassia Trojahn
- **Año:** 2026
- **Título:** Survey on Embedding Methods Applied to Ontology Matching
- **Venue / DOI:** ACM Computing Surveys · DOI 10.1145/3805799 · CC BY 4.0

## 2. Objetivo del estudio

Revisar sistemáticamente métodos basados en **embeddings** para *ontology matching* a nivel de esquema; proponer marco de clasificación (tipo de embedding, estrategia de entrenamiento, matching simple vs complejo) y responder RQ1–RQ4 sobre representación, estrategias, heterogeneidad y limitaciones.

## 3. Dominio y fuente de datos

- **Dominio:** ontology matching, integración de datos, fusion de conocimiento.
- **Corpus:** **81 estudios** recientes incorporados (extiende trabajo previo de Sousa et al.); benchmarks OAEI y matchers basados en Word2Vec, GloVe, BERT, GNNs e híbridos.

## 4. Técnicas usadas

- Revisión sistemática con taxonomía en tres dimensiones: segmentación léxica, estrategia de entrenamiento, complejidad de correspondencias (simple vs compleja).
- Análisis de matchers embedding-based vs heurísticas léxicas/estructurales clásicas.
- Gap analysis y direcciones futuras (explicabilidad, escalabilidad, supervisión).

## 5. Métricas de evaluación

- Síntesis de métricas en literatura revisada: precision, recall, F-measure, cosine similarity, M-Hits@K en tracks OAEI.
- Identificación de cuellos de botella: ~38 % métodos requieren alineaciones de referencia; ~7 % manejan correspondencias lógicas complejas.

## 6. Limitaciones (según autores)

- **Cuello de botella de supervisión** y escasez de alineaciones gold estándar.
- **Brecha estructural-semántica** en correspondencias complejas; déficit de explicabilidad.
- Trade-off escalabilidad vs ontologías grandes (>100K entidades); sin OpenAPI ni dominio bancario.

## 7. Vacío u oportunidad para OpenAPI–BIAN

Referencia principal para **SemanticScore (S)** con embeddings al comparar entidades OpenAPI normalizadas con conceptos BIAN. Ningún trabajo revisado aborda **contratos OpenAPI bancarios vs Service Domains BIAN** ni un **AlignmentScore** integrado S+E+C.

## 8. Cita para el plan de tesis

- **Usar en:** §3.5 (E3 — embeddings) · §4.4 (SemanticScore; alternativa/complemento a ontología Mainas)
- **Frase clave (1 línea):** Los embeddings permiten similitud semántica robusta en ontology matching, pero la literatura no aplica ese enfoque a la alineación OpenAPI bancario ↔ BIAN con métrica integrada.

## 9. Notas de lectura (opcional, no va al documento final)

- ¿Aporta técnica para S, E o C? **S** (embeddings); **E** parcial (GNNs sobre **grafos ontológicos**, no StructuralScore REST↔BIAN); **C** no explícito.
- ¿Menciona OpenAPI + ontología/esquema? **Ontology matching sí**; OpenAPI **no**.
