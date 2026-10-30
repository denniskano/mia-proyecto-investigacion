# Otieno y Araka, 2026 — RESTful API Testing Using Machine Learning

| Campo | Contenido |
|-------|-----------|
| **ID** | E5-03 |
| **Eje** | E5 — Testing y calidad API (borde) |
| **Tipo** | systematic literature review |
| **PDF** | `bibliografia/estado-del-arte/Otieno y Araka - 2026 - Systematic Literature Review RESTful API Testing Using Machine Learning Techniques.pdf` |
| **Estado ficha** | completada |

## 1. Referencia

- **Autores:** Bill A. Otieno, Eric Araka (Kenyatta University, Kenya)
- **Año:** 2026
- **Título:** Systematic Literature Review: RESTful API Testing Using Machine Learning Techniques
- **Venue / DOI:** Journal of the Kenya National Commission for UNESCO, Vol. 5, No. 1 · DOI 10.62049/jkncu.v5i1.449

## 2. Objetivo del estudio

Revisar cómo **ML/LLMs** mejoran el testing de APIs RESTful: extracción de restricciones, generación de entradas válidas y exploración adaptativa frente a enfoques black/white/model-based clásicos.

## 3. Dominio y fuente de datos

- **Dominio:** pruebas automatizadas de APIs REST con inteligencia artificial.
- **Corpus:** **24 papers** muestreados (de 98 identificados → 34 preseleccionados); NLP/LLM sobre OpenAPI, RL, grafos de propiedades.

## 4. Técnicas usadas

- Systematic Literature Review.
- Síntesis de LLMs para minar restricciones de OpenAPI, agentes multi-RL, modelos fine-tuned compactos.
- Comparación con testing tradicional.

## 5. Métricas de evaluación

- Cobertura de operaciones/código, tasa de entradas válidas, detección de faults (según estudios incluidos).
- Mejoras reportadas vs baselines en exploración de APIs.

## 6. Limitaciones (según autores)

- Especificaciones incompletas, oráculos semánticos débiles, flujos stateful largos.
- Muestra limitada; despliegue industrial de herramientas ML aún incipiente.
- ML para **test**, no para **alineación de significado de negocio**.

## 7. Vacío u oportunidad para OpenAPI–BIAN

Usa OpenAPI como **artefacto de entrada para pruebas**, no como objeto a contrastar con BIAN. Delimita que técnicas ML del eje E5 no sustituyen SemanticScore orientado a modelos de referencia bancarios.

## 8. Cita para el plan de tesis

- **Usar en:** §3.5 (E5 — frontera ML/testing)
- **Frase clave (1 línea):** El ML aplicado a testing REST explota OpenAPI para generar pruebas, no para medir alineación con modelos BIAN.

## 9. Notas de lectura (opcional, no va al documento final)

- ¿Aporta técnica para S, E o C? **No** (ML para test generation).
- ¿Menciona OpenAPI + ontología/esquema? **OpenAPI sí**; ontología de negocio **no**.
