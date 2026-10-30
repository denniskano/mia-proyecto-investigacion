# Santos y Casas, 2025 — A catalog of API Gateway metrics and its quantitative evaluation

| Campo | Contenido |
|-------|-----------|
| **ID** | E1-03 |
| **Eje** | E1 — OpenAPI como estándar *(contexto periférico: API Gateway)*
| **Tipo** | research article |
| **PDF** | `bibliografia/estado-del-arte/Santos y Casas - 2025 - A catalog of API Gateway metrics and its quantitative evaluation.pdf` |
| **Estado ficha** | completada |

## 1. Referencia

- **Autores:** Eder dos Santos, Sandra Casas
- **Año:** 2025
- **Título:** A catalog of API Gateway metrics and its quantitative evaluation
- **Venue / DOI:** Revista DYNA (Universidad Nacional de Colombia), Vol. 92(237), pp. 106–114 · DOI 10.15446/dyna.v92n237.118741

## 2. Objetivo del estudio

Construir, mediante Design Science Research, un **catálogo de métricas de API Gateway** y analizar cuantitativamente cómo los productos de la industria exponen o soportan esas métricas.

## 3. Dominio y fuente de datos

- **Dominio:** gestión y operación de APIs en producción (API Gateways).
- **Corpus:** literatura previa + informes Gartner/industria + documentación técnica de **68 productos** API Gateway.

## 4. Técnicas usadas

- Design Science Research (DSR).
- Elaboración iterativa de catálogo de métricas (31 iniciales → 59 finales).
- Categorización y análisis cuantitativo de cobertura por producto.

## 5. Métricas de evaluación

- Catálogo de **59 métricas** (latencia, tiempo de respuesta, errores, tráfico, etc.).
- Análisis de frecuencia/cobertura en productos comerciales; métricas de caché y salud del sistema poco representadas.

## 6. Limitaciones (según autores)

- Métricas de **runtime/operación**, no de coherencia documental OpenAPI ↔ modelo de negocio.
- Sesgo hacia documentación de productos; dominio emergente con pocos estudios previos (~20 sobre calidad en API management).
- No evalúa alineación semántica ni estructural de contratos.

## 7. Vacío u oportunidad para OpenAPI–BIAN

Delimita el **borde del problema** (rol: **exclusión explícita**): métricas de **runtime/gateway** ≠ **AlignmentScore** documental OpenAPI–BIAN. No describe usos documentales de OpenAPI como estándar.

## 8. Cita para el plan de tesis

- **Usar en:** §3.5 (E1 — métricas de ecosistema API) · §1.6 / §3.6 (delimitación: fuera del foco métricas runtime)
- **Frase clave (1 línea):** Las métricas de API Gateway miden desempeño operativo, no la alineación entre un contrato OpenAPI y un modelo BIAN de referencia.

## 9. Notas de lectura (opcional, no va al documento final)

- ¿Aporta técnica para S, E o C? **No** — métricas operativas de gateway.
- ¿Menciona OpenAPI + ontología/esquema? **OpenAPI** en contexto de gestión; **no** ontología ni BIAN.
