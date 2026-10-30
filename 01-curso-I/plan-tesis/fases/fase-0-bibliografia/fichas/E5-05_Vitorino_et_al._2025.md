# Vitorino et al., 2025 — Constrained adversarial learning for automated software testing

| Campo | Contenido |
|-------|-----------|
| **ID** | E5-05 |
| **Eje** | E5 — Testing y calidad API (borde) |
| **Tipo** | literature review |
| **PDF** | `bibliografia/estado-del-arte/Vitorino et al. - 2025 - Constrained adversarial learning for automated software testing a literature review.pdf` |
| **Estado ficha** | completada |

## 1. Referencia

- **Autores:** João Vitorino, Tiago Dias, Tiago Fonseca, Eva Maia, Isabel Praça (ISEP / GECAD, Portugal)
- **Año:** 2025
- **Título:** Constrained adversarial learning for automated software testing: a literature review
- **Venue / DOI:** Discover Applied Sciences, Vol. 7, Article 547 · DOI 10.1007/s42452-025-07073-3

## 2. Objetivo del estudio

Revisar cómo el **aprendizaje adversarial con restricciones** puede mejorar la **generación de datos de prueba** automatizada en cajas blanca, gris y negra.

## 3. Dominio y fuente de datos

- **Dominio:** testing automatizado de software en general; menciones incidentales a REST/API (OpenAPI, mutación).
- **Corpus:** literatura sobre GANs, VAEs, CGAN, WGAN y algoritmos genéticos con restricciones en generación de inputs.

## 4. Técnicas usadas

- Literature review de enfoques adversarial + constrained generation.
- Análisis por tipo de caja (white/grey/black) y ventajas/limitaciones.
- Referencias cruzadas a testing de APIs vía OpenAPI en trabajos secundarios citados.

## 5. Métricas de evaluación

- Evaluación cualitativa por enfoque; métricas de testing (cobertura, diversidad de inputs) según papers revisados, sin meta-análisis cuantitativo unificado.

## 6. Limitaciones (según autores)

- Pocos trabajos integran adversarial ML + restricciones para testing de forma madura.
- API testing no es núcleo del review; cobertura periférica de OpenAPI.

## 7. Vacío u oportunidad para OpenAPI–BIAN

E5 periférico: **SLR de adversarial ML** con cobertura marginal de API testing — no alineación OpenAPI–BIAN. Refuerza exclusión de foco en calidad de testing (Cap. 1.6) frente al modelo S/E/C.

## 8. Cita para el plan de tesis

- **Usar en:** §3.5 (E5 — borde testing/ML)
- **Frase clave (1 línea):** Las técnicas adversariales constrained apoyan testing automatizado, sin abordar alineación de contratos OpenAPI con Service Domains BIAN.

## 9. Notas de lectura (opcional, no va al documento final)

- ¿Aporta técnica para S, E o C? **No**.
- ¿Menciona OpenAPI + ontología/esquema? **OpenAPI** mencionado marginalmente; **no** ontología BIAN.
