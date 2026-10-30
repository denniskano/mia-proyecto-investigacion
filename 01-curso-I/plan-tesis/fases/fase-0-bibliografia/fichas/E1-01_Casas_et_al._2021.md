# Casas et al., 2021 — Uses and applications of the OpenAPI/Swagger specification

| Campo | Contenido |
|-------|-----------|
| **ID** | E1-01 |
| **Eje** | E1 — OpenAPI como estándar |
| **Tipo** | systematic mapping |
| **PDF** | `bibliografia/estado-del-arte/Casas et al. - 2021 - Uses and applications of the OpenAPISwagger specification a systematic mapping of the literature.pdf` |
| **Estado ficha** | completada |

## 1. Referencia

- **Autores:** Sandra Casas, Diana Cruz, Graciela Vidal, Marcela Constanzo
- **Año:** 2021
- **Título:** Uses and applications of the OpenAPI/Swagger specification: a systematic mapping of the literature
- **Venue / DOI:** 40th International Conference of the Chilean Computer Science Society (SCCC), IEEE · DOI 10.1109/SCCC54552.2021.9650408

## 2. Objetivo del estudio

Sintetizar los usos y aplicaciones de la especificación OpenAPI/Swagger más allá de la documentación: identificar actividades de desarrollo beneficiadas, tipos de artefactos generados, métodos de validación y dominios de aplicación cubiertos por la literatura (2011–2020).

## 3. Dominio y fuente de datos

- **Dominio:** desarrollo de software con APIs web (REST/RESTful); aplicaciones en IoT, microservicios, nube, entre otros.
- **Corpus:** 47 artículos primarios seleccionados de ACM, IEEE, Science Direct y Springer (2011–2020), mediante cadena de búsqueda sobre actividades de desarrollo, artefactos generados y dominios cubiertos.

## 4. Técnicas usadas

- Estudio de mapeo sistemático (lineamientos Petersen/Kitchenham).
- Cadena de búsqueda, criterios de inclusión/exclusión y evaluación de calidad.
- Clasificación temática por fase de desarrollo, tipo de artefacto, validación y dominio.
- Síntesis cuantitativa de frecuencias (documentación, automatización, procedimientos, etc.).

## 5. Métricas de evaluación

- Conteos y porcentajes sobre el corpus: p. ej. 43 % mejora de documentación; 68 % propone herramientas/automatización; 77 % orientado a consumidores de API; 40 % dominio específico.
- En trabajos mapeados aparecen métricas de mantenibilidad de OpenAPI (p. ej. conjuntos de métricas estáticas en estudios secundarios citados).
- Validación predominante mediante ejemplos ilustrativos (~47 %).

## 6. Limitaciones (según autores)

- Ventana temporal 2011–2020; idioma inglés; posible sesgo de la cadena de búsqueda.
- Estudios primarios a menudo poco teóricos y orientados a tecnología.
- Recomiendan revisiones más focalizadas, especialmente en **testing de APIs** y **métricas de calidad de APIs web**.

## 7. Vacío u oportunidad para OpenAPI–BIAN

No aborda modelos de referencia de negocio bancario ni BIAN. Mapea usos de OpenAPI pero **no propone alineación** entre contratos OpenAPI y modelos de dominio externos. La brecha OpenAPI ↔ Service Domain BIAN queda fuera del alcance del estudio; aporta contexto de adopción y gobernanza documental (§3.5 E1).

## 8. Cita para el plan de tesis

- **Usar en:** §3.5 (tabla E1 — uso del estándar OpenAPI) · §3.6 (brecha: estándar técnico sin vínculo con modelos de negocio BIAN)
- **Frase clave (1 línea):** OpenAPI se consolida como estándar de facto para describir APIs REST, pero la literatura mapeada no aborda su alineación con modelos de referencia de negocio como BIAN.

## 9. Notas de lectura (opcional, no va al documento final)

- ¿Aporta técnica para S, E o C? **No directamente** — contexto de estándar y artefactos derivados.
- ¿Menciona OpenAPI + ontología/esquema? **OpenAPI sí**; ontologías solo en papers citados (p. ej. Mainas), no como foco propio.
