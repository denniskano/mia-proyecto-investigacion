# Ehsan et al., 2022 — RESTful API Testing Methodologies

| Campo | Contenido |
|-------|-----------|
| **ID** | E5-01 |
| **Eje** | E5 — Testing y calidad API (borde) |
| **Tipo** | systematic literature review |
| **PDF** | `bibliografia/estado-del-arte/Ehsan et al. - 2022 - RESTful API Testing Methodologies Rationale, Challenges, and Solution Directions.pdf` |
| **Estado ficha** | completada |

## 1. Referencia

- **Autores:** Adeel Ehsan, Mohammed Ahmad M. E. Abuhaliqa, Cagatay Catal, Deepti Mishra
- **Año:** 2022
- **Título:** RESTful API Testing Methodologies: Rationale, Challenges, and Solution Directions
- **Venue / DOI:** Applied Sciences (MDPI), Vol. 12, 4369 · DOI 10.3390/app12094369

## 2. Objetivo del estudio

Revisar sistemáticamente metodologías de **testing de APIs RESTful** y generación de pruebas unitarias, identificando problemas, desafíos y direcciones de solución.

## 3. Dominio y fuente de datos

- **Dominio:** ingeniería de software, pruebas de APIs REST.
- **Corpus:** **16 artículos** incluidos en SLR; bases académicas principales.

## 4. Técnicas usadas

- Systematic Literature Review.
- Categorización de enfoques de generación de tests (black-box, white-box, model-based, etc.).
- Análisis de soporte a autenticación, cobertura y desafíos (especificaciones incompletas, statefulness).

## 5. Métricas de evaluación

- **Code coverage** como métrica principal de efectividad en trabajos revisados.
- Síntesis cualitativa de retos: especificaciones OpenAPI incompletas, oráculos, flujos con estado.

## 6. Limitaciones (según autores)

- Corpus reducido (16 papers); amenazas a validez de SLR.
- Foco en **verificación runtime**, no en alineación documental con modelos de negocio.
- No distingue calidad semántica de contrato vs conformidad funcional.

## 7. Vacío u oportunidad para OpenAPI–BIAN

Delimita el **borde E5**: testing ≠ **AlignmentScore**. OpenAPI aparece como entrada para pruebas, no como artefacto a alinear con BIAN. Cita en §1.6 y §3.6 para excluir testing como foco principal.

## 8. Cita para el plan de tesis

- **Usar en:** §3.5 (E5 — delimitación) · §1.6 (limitación: no foco testing)
- **Frase clave (1 línea):** La literatura de testing REST usa OpenAPI como especificación de prueba, no evalúa su alineación semántica con modelos BIAN.

## 9. Notas de lectura (opcional, no va al documento final)

- ¿Aporta técnica para S, E o C? **No** — testing/coverage.
- ¿Menciona OpenAPI + ontología/esquema? **OpenAPI** como spec de test; **no** ontología/BIAN.
