# Retroalimentación docente — Grupo 9.2

**Fuente principal:** exposición en clase · transcripción `transcriptions/MAE SE-A PI-10.txt`  
**Tema expuesto:** alineación OpenAPI ↔ BIAN en APIs bancarias · matriz de consistencia  
**Integrantes:** Alex Mancilla · Jack Paitan  
**Seguimiento:** Fases B–D (`CHECKLIST.md`, `REVISION_CRUZADA.md`) · `planificacion/PLAN_ELABORACION_PLAN_TESIS.md`  
**Última actualización pendientes:** 2026-07-02

> **Decisión de equipo (2026-05-28):** Este repositorio cubre **solo el plan de tesis (Guía N°01)**. No se redactará contenido para Guía N°02 / tesis de investigación (otro curso). La experimentación y construcción del artefacto se **delimitan como fuera de alcance** en §1.6; no habrá sección dedicada en Cap. 4.

> **Nota sobre PI-09:** al final de `MAE SE-A PI-09.txt` aparece «grupo 9-2» por un cambio de turno (problemas técnicos de otro equipo). Esa retroalimentación corresponde a **otro tema** (ciclo de requerimientos / agentes en empresa). **No aplica** a OpenAPI–BIAN. Este documento usa solo **PI-10**.

---

## 1. Lo que el docente validó

| # | Comentario docente | Implicación |
|---|-------------------|-------------|
| V1 | «Está clarísimo, está muy bien explicado» (contexto problema + diagrama bancario) | Mantener el hilo problema → objeto → referencia BIAN en exposición y §1.1–1.3 |
| V2 | Objeto de estudio = contratos OpenAPI 3.x del sector bancario; BIAN como contraste/referencia | **Confirmado:** objeto = OpenAPI bancario; BIAN = modelo de referencia |
| V3 | Cada objetivo = transformador (máquina entrada → salida) | ✅ Cap. 2 (Fase D): OE1–OE4 + Fig. 4 |

---

## 2. Sugerencias y correcciones (PI-10)

### A. Matriz de consistencia

| ID | Sugerencia del docente | Estado |
|----|------------------------|--------|
| M1 | **Fila Fase 1:** el «problema» de diseñar procedimiento es el **problema general / marco metodológico**, no el «problema 1» de una fila experimental | ✅ Fase 1 = marco de diseño (Excel + Anexo C) |
| M2 | **Fase 1** = solo **diseño**; **Fase 2** = **transformador** que normaliza artefactos | ✅ Matriz 5 fases |
| M3 | **Fase 4 vs Fase 5:** diferencia semántica vs integración/score global | ✅ S, E, C → AlignmentScore |
| M4 | **Eliminar Fase 6 / piloto Payment Execution** | ✅ Eliminado |
| M5 | **Validación / experimentación** fuera de matriz (no como OE de este plan) | ✅ §1.6 + matriz · sin sección Guía 2 |
| M6 | Las fases son **transformadores**, no generadores abstractos de «datos» | ✅ Cap. 2 (Fase D) |

### B. Objeto de estudio y unidad de análisis

| ID | Sugerencia del docente | Estado |
|----|------------------------|--------|
| O1 | Objeto = **contrato OpenAPI**; unidad atómica = pares endpoint/schema ↔ behavior/business object | ✅ §1.4 |
| O2 | Ejemplos concretos de **endpoints** en el informe | ✅ Tabla 1.4 §1.4 |
| O3 | Área concreta solo para ilustrar, **sin** piloto fijo en matriz | ✅ Dominio pagos genérico |
| O4 | Analogía objeto / unidad que procesa la máquina | ✅ §1.4 |

### C. Introducción y marco conceptual

| ID | Sugerencia del docente | Estado |
|----|------------------------|--------|
| I1 | Definir **contrato OpenAPI** antes de usarlo | ✅ §1.1 |
| I2 | **Conceptos primero, papers después** | ✅ §1.1 reordenado |
| I3 | Explicar **qué es BIAN** antes de usarlo | ✅ §1.1 |
| I4 | Redactar para lector sin background | ✅ §1.1 (revisión continua) |
| I5 | **Ejemplo chico + ejemplo más grande** del contrato | ✅ Tabla 1.4 · Anexo F · §4.6 |
| I6 | **Conceptualizaciones de papers** en el documento | ✅ §3.3 glosario + §3.4 bases teóricas (Fase E) |

### D. Exposición oral

| ID | Sugerencia del docente | Estado |
|----|------------------------|--------|
| E1 | **Ejemplo concreto** en ppt: «dos casitos» | ⏳ Slide pendiente |
| E2 | Mostrar **avance del documento** (plan de tesis) | ⏳ Subir PDF LaTeX al aula virtual |
| E3 | Explicar **modelo de scores** | ⏳ Usar PDF anexo en ppt |

### E. Alcance del plan (interpretación PI-10)

| ID | Sugerencia del docente | Estado |
|----|------------------------|--------|
| G1 | **Este plan:** diseño del artefacto y procedimiento | ✅ §1.6 · Cap. 4 ✅ |
| G2 | No incluir **experimentación/construcción** como objetivo del plan | ✅ §1.6 Tabla 1.7 · fuera de matriz |
| G3 | AS-IS, estado del arte → plan de tesis, no filas de matriz | ✅ §3.1–§3.6 LaTeX |

---

## 3. Citas textuales de referencia (PI-10)

- «Más bien les recomiendo que cuando ustedes hagan su presentación, coloquen un **ejemplo concreto**.»
- «Ok, me parece que es el **problema general**. Es el procedimiento, no es la solución.»
- «**El objetivo 6 desaparezca, no va ahí.**»
- «El **objeto de estudio es aquella unidad que va a pasar por la máquina**.»
- «Colóquenme por favor **ejemplos concretos de esos endpoints**.»
- «**Define** el contrato OpenAPI **antes**. Conceptos primero, papers después.»
- «No se coloca un objetivo vinculado directamente a esa actividad de **verificación y validación**… en la etapa ponen la **experimentación**.»

---

## 4. Seguimiento de pendientes

### Cerrados (implementados en LaTeX / matriz)

| ID | Qué | Evidencia |
|----|-----|-----------|
| V3, M6 | Cap. 2 objetivos = transformadores S/E/C | `latex/chapters/cap02-objetivos/` · Fase D ✅ |
| — | Fig. 1–3 en PDF del plan | `latex/build/Plan_Tesis_Grupo9.2.pdf` |
| — | Fig. 4 cadena objetivos | `figuras/cap02/` · Cap. 2 §2.6 |
| — | Fig. 6 brecha estado del arte | `figuras/cap03/` · Cap. 3 §3.6 |
| I6 (parcial) | Estado del arte sistematizado por ejes | Cap. 3 §3.5–§3.6 · Fase C ✅ |
| G3 | Cap. 3 completo §3.1–§3.6 (antecedentes + estado del arte + brecha) | Fase C + E ✅ |
| I6 | Glosario 18 términos + bases teóricas | §3.3 Tabla 7 · §3.4 · Fig. 5 |
| G3 | Cap. 5 + anexos A–F + referencias | Fase G ✅ |
| G1 | Cap. 4 metodología completa | Fase F ✅ 2026-07-02 |
| M5, G2 | Experimentación/construcción fuera de alcance del plan | §1.6 · matriz sin OE experimental |

### Abiertos — prioridad P1 (contenido del plan)

*Ninguno — informe LaTeX completo para Guía 1.*

### Abiertos — prioridad P2 (entrega / oral)

| Prioridad | Qué | Dónde | IDs |
|-----------|-----|-------|-----|
| **P2** | Subir **plan de tesis (PDF)** al aula virtual | Entrega PI-03 | E2 |
| **P2** | Slide **«dos casitos»** concretos | PPT | E1 |
| **P2** | Explicar **modelo S/E/C** en exposición | PPT + `figuras_alineacion_openapi_bian.pdf` | E3 |

### Abiertos — revisión y cierre curso

| Qué | Dónde |
|-----|-------|
| Revisión docente Cap. 1–4 | Tras subir PDF / próxima sesión |
| Zotero metadatos finos (DOI) | Fase G · verificar |
| Checklist cierre PI-08 | Fase H · ver `ESTADO_INFORME.md` |
| Portada exacta Guía N°01 | Fase A (menor) |

---

*Documento interno Grupo 9.2 — acta PI-10 + seguimiento vivo. Complementa `NOTAS_EQUIPO.md` y checklists por fase.*
