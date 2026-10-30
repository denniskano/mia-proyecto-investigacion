# Revisión cruzada — Fase C (§3.5–§3.6)

**Fecha:** 2026-05-28  
**Revisor:** Alex Mancilla → Cap. 3 §3.5–§3.6 (Jack)  
**Validación:** Jack Paitan → correcciones aplicadas  
**Criterios:** `CHECKLIST.md`, `CAPITULO_03_ESTADO_DEL_ARTE.md`, `EJES_ESTADO_DEL_ARTE.md`, Cap. 1

---

## Resumen ejecutivo

| Revisor | Veredicto | Correcciones |
|---------|-----------|--------------|
| Alex → Jack | **Aprobado** (tras P1) | 5 en LaTeX |
| Jack → Alex | **Aprobado** | — |

**Veredicto global:** Fase C **cerrada** para §3.5–§3.6. Pendiente: revisión docente · citas Zotero (Fase G). §3.1–§3.4 cerrados en **Fase E** ✅.

---

## Alex revisa §3.5–§3.6

| Ítem | Veredicto | Observación |
|------|-----------|-------------|
| Fidelidad borrador MD | ✅ | LaTeX isomórfico al borrador |
| Ejes E1–E6 + conclusiones | ✅ | Subsecciones 3.5.1–3.5.6 |
| Tabla 6 | ✅ | `tab06-sintesis-ejes.tex` |
| S/E/C (convención equipo) | ⚠️→✅ | Mainas matizado: representación ≠ SemanticScore |
| E4 en tabla | ⚠️→✅ | «E contextual» aclarado |
| V1–V5 | ⚠️→✅ | Celdas V1/V2/V5 restauradas |
| Guía 1/2 §3.6.3 | ✅ | Coherente con `\Cref{sec:alcances}` |
| Sin objetivos / sin piloto | ✅ | |
| Figura 6 | ⚠️→✅ | PNG regenerado en `figuras/cap03/` |

---

## Correcciones aplicadas

| ID | Archivo | Cambio |
|----|---------|--------|
| P1-1 | `05-estado-arte.tex` | Mainas: representación/normalización candidata, no S predefinido |
| P1-2 | `tab06-sintesis-ejes.tex` | E4: contexto dominio→interfaz |
| P1-3 | `figuras/cap03/` | `Figura_06_Brecha.png` vía `build_figuras_fase_cd.py` |
| P2-1–3 | `tab06-vacios.tex` | V1 objeto explícito; V2 «producto original»; V5 certificación |
| P2-4–5 | `06-alcances.tex`, `05/06-brecha.tex` | `\label{sec:alcances}` + `\Cref` |

---

## Acuerdos de equipo

1. **Mainas (E1):** aporta representación semántica OpenAPI; el cálculo de S queda en el diseño propio (Cap. 4).
2. **E5/E6:** rol de delimitación, no solución parcial.
3. §3.1–§3.4 cerrados en **Fase E** ✅ (2026-05-28).

---

*Revisión asistida por agente (Alex simulado); sustituir por firma Alex/Jack en entrega formal.*
