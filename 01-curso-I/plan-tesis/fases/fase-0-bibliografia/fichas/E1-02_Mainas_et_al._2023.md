# Mainas et al., 2023 — Annotated OpenAPI Descriptions and Ontology for REST Services

| Campo | Contenido |
|-------|-----------|
| **ID** | E1-02 |
| **Eje** | E1 — OpenAPI como estándar |
| **Tipo** | research article |
| **PDF** | `bibliografia/estado-del-arte/Mainas et al. - 2023 - Annotated OpenAPI Descriptions and Ontology for REST Services.pdf` |
| **Estado ficha** | completada |

## 1. Referencia

- **Autores:** Nikolaos Mainas, Fotios Bouraimis, Aikaterini Karavisileiou, Euripides G. M. Petrakis
- **Año:** 2023
- **Título:** Annotated OpenAPI Descriptions and Ontology for REST Services
- **Venue / DOI:** International Journal on Artificial Intelligence Tools (IJAIT), Vol. 32, No. 6 · DOI 10.1142/S0218213023500173

## 2. Objetivo del estudio

Proponer una **ontología de referencia para servicios REST** y un **procedimiento formal** para convertir descripciones OpenAPI en instancias de esa ontología, enriquecidas con anotaciones semánticas que superen la ambigüedad de los contratos OpenAPI estándar.

## 3. Dominio y fuente de datos

- **Dominio:** APIs REST/OpenAPI 3.x en la Web; ecosistema de publicación y descubrimiento de servicios.
- **Corpus:** más de 300 descripciones OpenAPI de SwaggerHub; evaluación con triple store Virtuoso y aplicación web pública de búsqueda semántica.

## 4. Técnicas usadas

- Extensiones de anotación OpenAPI (`x-refersTo`, `x-kindOf`, `x-mapsTo`, `x-collectionOn`, `x-onResource`, `x-operationType`).
- Ontología REST basada en **Hydra**; restricciones **SHACL**; algoritmos de traducción OpenAPI → RDF (Algoritmos 1–7).
- Consultas **SPARQL** sobre instancias materializadas; criterios de calidad ontológica (Raad & Cruz, 2015).

## 5. Métricas de evaluación

- Tiempo de traducción: >1 s para YAML de >200 líneas.
- Tiempos de respuesta SPARQL: consulta simple ~2,2 s; compleja ~8,3 s.
- Evaluación task-based sobre corpus real de OpenAPI; criterios de exactitud/completitud de la ontología.

## 6. Limitaciones (según autores)

- No cubre aún **Webhooks, Links ni Callbacks** de OpenAPI 3.x (trabajo futuro).
- Evaluación exhaustiva cualitativa con expertos pendiente; foco en eficiencia y tareas de búsqueda.
- Ontología genérica REST, no específica de dominio bancario ni BIAN.

## 7. Vacío u oportunidad para OpenAPI–BIAN

Aporta **enriquecimiento semántico de OpenAPI** vía ontología y anotaciones, útil para **normalización** e inspirar el cálculo de **SemanticScore (S)** — no un score de similitud predefinido — pero **no contrasta** contratos con **Service Domains BIAN** ni calcula alineación estructural/cobertura.

## 8. Cita para el plan de tesis

- **Usar en:** §3.5 (E1 — OpenAPI semántico) · §4.4 (técnica de referencia para representación semántica; también en `bibliografia/aporte/`)
- **Frase clave (1 línea):** Mainas et al. convierten OpenAPI anotado en ontología RDF consultable, pero no evalúan alineación con modelos de negocio de referencia como BIAN.

## 9. Notas de lectura (opcional, no va al documento final)

- ¿Aporta técnica para S, E o C? **S** (representación/normalización semántica; base para cálculo de S); **E** parcial (mapeo esquema→RDF); **C** no.
- ¿Menciona OpenAPI + ontología/esquema? **Sí** — núcleo del paper.
