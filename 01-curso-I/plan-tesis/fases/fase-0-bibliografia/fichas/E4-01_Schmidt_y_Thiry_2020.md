# Schmidt y Thiry, 2020 — Microservices identification strategies (MDE & DDD)

| Campo | Contenido |
|-------|-----------|
| **ID** | E4-01 |
| **Eje** | E4 — Microservicios / interfaces |
| **Tipo** | systematic literature review |
| **PDF** | `bibliografia/estado-del-arte/Schmidt y Thiry - 2020 - Microservices identification strategies  A review focused on Model-Driven Engineering and Domain Dr.pdf` |
| **Estado ficha** | completada |

## 1. Referencia

- **Autores:** Roger Anderson Schmidt, Marcello Thiry
- **Año:** 2020
- **Título:** Microservices identification strategies: A review focused on Model-Driven Engineering and Domain Driven Design
- **Venue / DOI:** 15th Iberian Conference on Information Systems and Technologies (CISTI 2020) · ISBN 978-989-54659-0-3

## 2. Objetivo del estudio

Realizar una revisión sistemática (2013–2019) de estrategias de **identificación y descomposición de microservicios**, con énfasis en **Model-Driven Engineering (MDE)** y **Domain-Driven Design (DDD)** para definir granularidad óptima.

## 3. Dominio y fuente de datos

- **Dominio:** arquitecturas de microservicios, ingeniería dirigida por modelos, diseño orientado al dominio.
- **Corpus:** **27 estudios primarios** seleccionados de 715 registros (Kitchenham SLR, marco PICO).

## 4. Técnicas usadas

- Systematic Literature Review (SLR).
- Análisis de RQ sobre estrategias, roles, uso de MDE y cobertura DDD.
- Síntesis cualitativa de enfoques estáticos, dinámicos (runtime) y basados en modelos de negocio.

## 5. Métricas de evaluación

- Conteos y categorización de estrategias (p. ej. resolución de dependencias, tiempo de respuesta en enfoques dinámicos).
- No hay métrica unificada de alineación; evaluación heterogénea en estudios primarios.

## 6. Limitaciones (según autores)

- Pocos trabajos integran **MDE + DDD** conjuntamente.
- Corte temporal hasta 2019; granularidad de microservicios aún poco consensuada.
- No aborda contratos OpenAPI ni estándares de arquitectura bancaria (BIAN).

## 7. Vacío u oportunidad para OpenAPI–BIAN

Contextualiza cómo **capacidades de negocio** (similar espíritu a Service Domains) se traducen en límites de servicio/API. No propone medir coherencia OpenAPI ↔ BIAN; aporta marco DDD/MDE para §3.5 E4 y justificar mapeo dominio–interfaz.

## 8. Cita para el plan de tesis

- **Usar en:** §3.5 (E4 — dominio e interfaces) · §3.2 (coherencia arquitectura negocio–servicios)
- **Frase clave (1 línea):** La descomposición en microservicios desde modelos de dominio (DDD/MDE) relaciona capacidades de negocio con servicios, pero no cuantifica alineación OpenAPI–BIAN.

## 9. Notas de lectura (opcional, no va al documento final)

- ¿Aporta técnica para S, E o C? **E** contextual (estructura dominio→servicio); no scores.
- ¿Menciona OpenAPI + ontología/esquema? **No** OpenAPI; modelos de dominio sí.
