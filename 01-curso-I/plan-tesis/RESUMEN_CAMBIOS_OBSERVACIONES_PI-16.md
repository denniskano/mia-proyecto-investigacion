# Resumen de cambios — Grupo 9.2  
**Plan de tesis:** *Alineación entre contratos OpenAPI bancarios y modelos de referencia BIAN*  
**Integrantes:** Alex Mancilla Antay · Jack Paitan Cano  
**Referencia:** observaciones de la sesión de exposición MAE SE-A PI-16  

---

Estimado docente:

En atención a las observaciones formuladas durante nuestra exposición del plan de tesis, el Grupo 9.2 ha actualizado el **informe (Guía 1)** y la **presentación Beamer**. A continuación detallamos los cambios realizados, organizados según los puntos discutidos en la sesión.

---

## 1. Problema tecnológico — redacción explícita y visible

**Observación:** el problema tecnológico debía estar **escrito** en la exposición; no confundirlo con el verbo «diseñar» (objetivo general); lo que vale es lo **escrito**, no solo la explicación oral.

**Cambios realizados:**

- **Presentación (slide 10):** enunciado completo del problema tecnológico como **situación técnica**: ausencia de un procedimiento documentado y reproducible que cuantifique la alineación entre un contrato OpenAPI bancario y un Service Domain BIAN emparejado.
- Recordatorio visible: problemática del sector ≠ problema tecnológico; «diseñar» pertenece al objetivo general.
- **Informe (Cap. 1 §1.3):** se mantiene la formulación como situación a modificar (no como pregunta ni como objetivo).

---

## 2. Objetivo general — base de medición y producto del artefacto

**Observación:** el objetivo general debe precisar **en base a qué se mide**, **cuál es el producto del artefacto** y **con qué variable** se mide el rendimiento; todo debe poder leerse en la diapositiva correspondiente.

**Cambios realizados:**

- **Presentación (slide 11):** bloque autocontenido con:
  - **Insumo / base de medición:** par contrato OpenAPI 3.x + extracto del Service Domain BIAN.
  - **Objetivo general (técnico):** diseñar modelo S/E/C y procedimiento reproducible.
  - **Producto del artefacto:** procedimiento documentado + AlignmentScore ∈ [0,1] + clasificación (Alta / Media / Baja / Nula).
  - **Variable dependiente del artefacto:** AlignmentScore.
  - **Fórmula:** AlignmentScore = α·S + β·E + γ·C (α + β + γ = 1).
  - Distinción explícita del **objetivo superior** (consecuencia en gobernanza, no OG).
- **Informe (Cap. 2 §2.3):** nuevo párrafo **«Base de medición»** que vincula instancia `contrato × Service Domain`, AlignmentScore, clasificación y VD global del artefacto.

---

## 3. Variable dependiente — artefacto completo vs. objetivos específicos

**Observación:** distinguir la VD que mide el **rendimiento global del artefacto** de los productos parciales de OE1–OE4 (p. ej. representación intermedia de OE1).

**Cambios realizados:**

- **Presentación (slide 14):** caja destacada con la **VD del artefacto** (AlignmentScore + clasificación) y tabla separada de **ratios parciales por OE** (completitud, E, S, C).
- **Informe (Tabla 5):** fila **«Artefacto (OG)»** con AlignmentScore + clasificación como VD global; fila OE4 ajustada para indicar que C es ratio parcial que contribuye al AlignmentScore.
- **Informe (Cap. 2):** aclaración de que S, E, C y completitud de normalización son productos parciales, no sustitutos de la VD global.

---

## 4. Técnicas, paradigma y ejemplos numéricos

**Observación:** precisar si el procedimiento usa aprendizaje automático o reglas/métricas; nombrar técnicas en documento y exposición; presentar al menos **tres ejemplos contrastantes** con cálculo visible.

**Cambios realizados:**

- **Presentación (slide 13):** variables independientes con técnicas explícitas (*schema matching* según Shvaiko & Euzenat, 2005; similitud semántica por embeddings/ontología) y nota: **no es aprendizaje supervisado**.
- **Presentación (slide 9):** tabla con **tres escenarios** (casos A, B, C: alineación alta, baja y nula) con valores de E, S, C y AlignmentScore; ejemplo E = 7/8 = 0,875; nota sobre validación con *ground truth* en Tesis 2.
- **Informe (§4.4):** párrafo que indica que el procedimiento **no emplea aprendizaje supervisado**.
- **Informe (Anexo F):** nueva sección **«Escenarios numéricos ilustrativos»** con la misma tabla de tres casos y ejemplo de cálculo de E.

---

## 5. Objeto de estudio, referencia BIAN e instrumento

**Observación:** precisar que BIAN entra como **Service Domain** de referencia (behaviors, business objects), no necesariamente como un segundo contrato OpenAPI genérico; definir objeto, unidad de análisis y etapa de aplicación del artefacto.

**Cambios realizados:**

- **Presentación (slides 6–8):** paneles con definiciones escritas de objeto, referencia BIAN, unidad de análisis, producto, instrumento, paradigma y **etapa de uso** (design-first / pre-despliegue).
- **Presentación (slide 7):** ciclo de vida del contrato OpenAPI y punto de aplicación del artefacto.

---

## 6. Metodología y adquisición de datos

**Observación:** la captura/adquisición de datos debe preceder a la normalización; el flujo metodológico debe quedar claro por fases.

**Cambios realizados:**

- **Presentación (slide 15):** Fase 2 renombrada **«Adquirir + Normalizar»** (§4.3), antes de emparejar y calcular scores.
- **Informe (§4.2):** Fase 2 actualizada a **«Adquirir y normalizar artefactos»**; párrafo introductorio que sitúa la adquisición (§4.3) antes del *parsing*.
- **Informe (Tabla OE–metodología, §4.2.1):** acción OE1 = **Adquirir y normalizar**.

---

## 7. Criterio de exposición: slides autocontenidas

**Observación:** cada concepto clave debe poder mostrarse en la diapositiva; no depender de «está en otra parte del documento» ni leer solo imágenes sin texto.

**Cambios realizados:**

- Texto explicativo añadido en slides de problemática, objeto, instrumento, problema tecnológico, objetivo general, variables, metodología y modelo S/E/C.
- La presentación Beamer (22 diapositivas) queda **autocontenida** para defensa oral; el libreto pasa a ser apoyo opcional para ensayo.

---

## Documentos actualizados

| Documento | Ubicación |
|-----------|-----------|
| Presentación Beamer (PDF) | `plan-tesis/exposicion/Exposicion_Plan_Tesis_Grupo9.2-beamer.pdf` |
| Fuente Beamer | `plan-tesis/exposicion/latex/exposicion_beamer.tex` |
| Cap. 2 — Objetivos | `plan-tesis/latex/chapters/cap02-objetivos/_cap02.tex` |
| Tabla 5 — Variables | `plan-tesis/latex/tables/tab05-variables.tex` |
| Cap. 4 — Procedimiento y técnicas | `plan-tesis/latex/chapters/cap04-metodologia/` |
| Anexo F — Ejemplos | `plan-tesis/latex/anexos/anexo-f.tex` |
| Registro de observaciones (interno) | `transcriptions/OBSERVACIONES_PI-16_Profesor.md` |

---

## Pendientes conscientes (alcance Guía 1)

- **Validación empírica a escala** y calibración de umbrales: Tesis 2 (§1.6).
- **Construcción del prototipo software** y contrastación con *ground truth* de especialistas: fuera del alcance del presente plan.
- **Gestión del tiempo** en exposición (15 + 5 min): ensayo cronometrado con la versión actualizada de slides.

---

Quedamos atentos a sus comentarios adicionales.

**Grupo 9.2** · Alex Mancilla · Jack Paitan  
Universidad Nacional de Ingeniería · Maestría en Inteligencia Artificial · Lima, 2026
