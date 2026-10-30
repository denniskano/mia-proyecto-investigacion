# Revisión cruzada — Capítulo 1 (Grupo 9.2)

**Fecha:** 2026-05-28  
**Revisores:** Alex Mancilla → Cap. 1 LaTeX · Jack Paitan → validación y correcciones  
**Criterios:** `CHECKLIST.md`, `FEEDBACK_DOCENTE_PI10.md`, `NOTAS_EQUIPO.md`  
**Fuente:** `../../latex/chapters/cap01-planteamiento/` · PDF `../../latex/build/Plan_Tesis_Grupo9.2.pdf`

---

## Resumen ejecutivo

| Revisor | Alcance | Veredicto | Correcciones |
|---------|---------|-----------|--------------|
| Alex → Jack | §1.1–§1.9 + figuras 1–3 + tablas | **Aprobado** (condiciones P1) | 3 en LaTeX |
| Jack → Alex | Informe Alex + coherencia matriz | **Aprobado** | — |

**Veredicto global:** Cap. 1 **aprobado para cierre Fase B**. Sin bloqueantes P0. Pendientes PI-10 §4 restantes (Cap. 2, Cap. 4, PPT) son **post–Fase B**.

---

## Alex revisa Cap. 1 (LaTeX)

| § | Veredicto | Observación clave |
|---|-----------|-------------------|
| §1.1 Introducción | ✅ | Definiciones OpenAPI/BIAN/alineación antes de contexto; sin problemática |
| §1.2 Problemática | ✅ | Fragmentación, deriva documental |
| §1.3 Planteamiento | ⚠️→✅ | P4 decía «caso de estudio»; corregido (sin piloto fijo) |
| §1.4 Objeto de estudio | ⚠️→✅ | Objeto/unidad/producto claro; Tabla 1.4 endpoints; puente 5 fases añadido |
| §1.5 Ámbito | ✅ | Tabla 1.6 |
| §1.6 Alcances | ⚠️→✅ | Guía 1/2 solo en tabla; prosa introductoria añadida |
| §1.7–§1.9 | ✅ | Justificación, IEEE/ACM, design science |
| Fig. 1–3 | ✅ | Compilan en PDF |
| Coherencia docente | ✅ | Problema ≠ objetivo; BIAN = referencia; sin PI-XX en `.tex` |

**Riesgos transversales:** numeración interna «Tabla 3» en checklist ≠ Tabla 1.4 LaTeX (solo documentación). Anexo C en LaTeX ✅.

---

## Jack valida revisión Alex

| Ítem | Veredicto |
|------|-----------|
| Criterios CHECKLIST §1.1–§1.9 | ✅ |
| PI-10 aplicado en Cap. 1 (I1–I4, O1–O4, G1–G2, M4–M5) | ✅ |
| Correcciones P1 aplicadas en `03`, `04`, `06` | ✅ |
| PDF recompilado sin errores | ✅ |

---

## Correcciones aplicadas

| ID | Archivo | Cambio |
|----|---------|--------|
| P1-1 | `03-planteamiento.tex` | P4: «por caso de estudio» → «por cada instancia evaluada (par contrato OpenAPI bancario — Service Domain BIAN)» |
| P1-2 | `04-objeto-estudio.tex` | Párrafo redundante sustituido por puente a 5 fases + Anexo C + Cap. 2 |
| P1-3 | `06-alcances.tex` | Prosa Guía 1 vs Guía 2 antes de Tabla 1.7 |

**No aplicadas (P2, opcional):** macros `\figCapOne` en Fig. 1; gloss «pipeline» → «procedimiento»; nota pedagógica S/E convención.

---

## Acuerdos de equipo (post-revisión)

1. **Fase B cerrada** con Cap. 1 congelado salvo ajustes docente.
2. **Siguiente prioridad:** Fase F (Cap. 4 metodología) · Fase G (Cap. 5 + anexos LaTeX).
3. **Validación humana:** Alex/Jack confirman en ~10 min la lectura del PDF actualizado.

---

*Revisión asistida por agente especializado (Alex simulado); correcciones aplicadas en repo · sustituir por firma Alex/Jack en entrega formal.*
