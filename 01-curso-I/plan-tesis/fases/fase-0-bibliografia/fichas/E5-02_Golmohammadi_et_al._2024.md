# Golmohammadi et al., 2024 — Testing RESTful APIs: A Survey

| Campo | Contenido |
|-------|-----------|
| **ID** | E5-02 |
| **Eje** | E5 — Testing y calidad API (borde) |
| **Tipo** | survey |
| **PDF** | `bibliografia/estado-del-arte/Golmohammadi et al. - 2024 - Testing RESTful APIs A Survey.pdf` |
| **Estado ficha** | completada |

## 1. Referencia

- **Autores:** Amid Golmohammadi, Man Zhang, Andrea Arcuri
- **Año:** 2023 (ACM TOSEM nov. 2023; catalogado 2024 en repositorio)
- **Título:** Testing RESTful APIs: A Survey
- **Venue / DOI:** ACM Transactions on Software Engineering and Methodology, Vol. 33, No. 1, Article 27 · DOI 10.1145/3617175

## 2. Objetivo del estudio

Survey comprehensivo de **testing de APIs RESTful** a partir de **92 papers**, respondiendo 12 preguntas de investigación sobre tendencias, técnicas, herramientas y desafíos abiertos.

## 3. Dominio y fuente de datos

- **Dominio:** pruebas automatizadas de servicios REST.
- **Corpus:** 92 estudios primarios (snowballing + 7 bases de datos); herramientas fuzzing, search-based, model-based, property-based; muchas usan OpenAPI como entrada.

## 4. Técnicas usadas

- Revisión estructurada con taxonomía de técnicas y herramientas.
- Análisis bibliométrico temporal y por venue.
- Síntesis de desafíos (costo, servicios en vivo, casos reales limitados).

## 5. Métricas de evaluación

- Métricas de efectividad en corpus: cobertura, faults encontrados, etc. (varía por estudio).
- Conteos por categoría de técnica y año de publicación.

## 6. Limitaciones (según autores)

- Persisten **desafíos abiertos** en testing REST a escala industrial.
- Alto costo de probar servicios desplegados; pocos estudios de caso en algunos subdominios.
- No aborda alineación con modelos de referencia de negocio.

## 7. Vacío u oportunidad para OpenAPI–BIAN

Confirma que OpenAPI impulsa **herramientas de test**, pero ninguna línea revisada mide **coherencia OpenAPI ↔ BIAN**. Refuerza delimitación E5 en §3.6 frente al producto central AlignmentScore.

## 8. Cita para el plan de tesis

- **Usar en:** §3.5 (E5) · §1.6 (límite testing)
- **Frase clave (1 línea):** El estado del arte en testing REST es extenso y OpenAPI-centric, pero orthogonal a la alineación documental con Service Domains BIAN.

## 9. Notas de lectura (opcional, no va al documento final)

- ¿Aporta técnica para S, E o C? **No**.
- ¿Menciona OpenAPI + ontología/esquema? **OpenAPI** (black-box testing); **no** BIAN/ontología de negocio.
