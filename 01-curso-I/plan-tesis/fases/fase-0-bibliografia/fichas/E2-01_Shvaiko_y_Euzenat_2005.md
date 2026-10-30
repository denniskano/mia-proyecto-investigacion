# Shvaiko y Euzenat, 2005 — A Survey of Schema-Based Matching Approaches

| Campo | Contenido |
|-------|-----------|
| **ID** | E2-01 |
| **Eje** | E2 — Matching estructural |
| **Tipo** | survey |
| **PDF** | `bibliografia/estado-del-arte/Shvaiko y Euzenat - 2005 - A Survey of Schema-Based Matching Approaches.pdf` |
| **Estado ficha** | completada |

## 1. Referencia

- **Autores:** Pavel Shvaiko, Jérôme Euzenat
- **Año:** 2005
- **Título:** A Survey of Schema-Based Matching Approaches
- **Venue / DOI:** Journal on Data Semantics IV, LNCS 3730, Springer, pp. 146–171 · DOI 10.1007/11552262_7

## 2. Objetivo del estudio

Presentar una **clasificación unificada** de técnicas de *schema matching* (esquemas y ontologías) que sirva para comparar matchers existentes y diseñar nuevos, integrando perspectivas de bases de datos, sistemas de información e IA.

## 3. Dominio y fuente de datos

- **Dominio:** integración de esquemas XML/relacionales, ontologías, data warehouses, e-commerce.
- **Corpus:** revisión comparativa de sistemas y técnicas recientes (sin evaluación empírica unificada); solo información a nivel de **esquema** (sin datos de instancia).

## 4. Técnicas usadas

- Taxonomía multidimensional: **aproximado vs exacto** (nivel esquema); **sintáctico, semántico, externo** (nivel elemento/estructura).
- Revisión de matchers elementales y sistemas compuestos; mapeo al espacio de soluciones.
- Enfoque *schema-based*: explota únicamente metadatos del esquema.

## 5. Métricas de evaluación

- Survey conceptual: compara cobertura del espacio de técnicas, no reporta precision/recall agregados.
- Discute métricas usadas por sistemas revisados de forma cualitativa.

## 6. Limitaciones (según autores)

- Predating OpenAPI/JSON Schema; no aborda contratos REST ni dominios bancarios.
- Clasificación no validada empíricamente; exclusión de matching basado en instancias.
- Ontology vs schema matching tratados juntos pero con matices no unificados del todo.

## 7. Vacío u oportunidad para OpenAPI–BIAN

Base teórica para **StructuralScore (E)**: correspondencias paths/operations/schemas ↔ behaviors/business objects BIAN como problema de matching estructural. No contempla OpenAPI ni BIAN; la tesis aplica la taxonomía a artefactos bancarios concretos.

## 8. Cita para el plan de tesis

- **Usar en:** §3.4 (bases teóricas matching estructural) · §3.5 (E2) · §4.4 (StructuralScore)
- **Frase clave (1 línea):** Shvaiko y Euzenat clasifican técnicas de correspondencia entre esquemas, base para formalizar la dimensión estructural de la alineación OpenAPI–BIAN.

## 9. Notas de lectura (opcional, no va al documento final)

- ¿Aporta técnica para S, E o C? **E** (matching estructural); **S** parcial (técnicas semánticas en taxonomía).
- ¿Menciona OpenAPI + ontología/esquema? **Esquema/ontología sí**; OpenAPI **no**.
