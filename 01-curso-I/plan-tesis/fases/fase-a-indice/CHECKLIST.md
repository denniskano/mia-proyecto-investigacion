# Checklist — Fase A (Índice y esqueleto)

**Alcance:** armar la **estructura** del plan de tesis (capítulos, placeholders, preliminares, índices automáticos) — **no** redactar contenido de otras fases.

**Entregable Fase A:** esqueleto LaTeX en `../../latex/` que compila a PDF con secciones vacías numeradas.

**Estado Fase A:** ✅ cerrada (pendiente menor: portada exacta Guía N°01)

---

## Qué es — y qué no es — Fase A

| Sí es Fase A | No es Fase A (ver otra fase) |
|--------------|------------------------------|
| `main.tex` + carpetas `chapters/`, `frontmatter/`, `anexos/` | Cap. 1 redactado → **Fase B** (`../fase-b-planteamiento/CHECKLIST.md`) |
| Títulos §1.1–§5.x con `[Por redactar — Fase X]` | Cap. 1–3 redactados → **Fases B–E** ✅ |
| Índice, lista de figuras y tablas **generados al compilar** | Cap. 1–5 ✅ · ver `../../planificacion/ESTADO_INFORME.md` |
| Portada, resumen/abstract **borrador** | Metodología Cap. 4 → **Fase F** |
| Metadatos título + macros S/E/C en `config/` | Fichas / Anexo B → **Fase 0** |
| Plan maestro: figuras y tablas en estructura | Ver `../../figuras/README.md` · `../../planificacion/PLAN_ELABORACION_PLAN_TESIS.md` |

> Si ves Cap. 1 completo o figuras del modelo en el PDF, es **trabajo posterior** integrado en el mismo LaTeX — no cuenta como criterio de cierre de Fase A.

---

## Criterios de cierre Fase A

- [x] Proyecto `../../latex/` con `main.tex` colaborativo
- [x] Preliminares: portada (borrador), resumen, abstract
- [x] Capítulos 1–5 presentes con placeholders por fase de redacción
- [x] Anexos A–F listados con placeholders
- [x] `\tableofcontents`, `\listoffigures`, `\listoftablas` operativos
- [x] Título unificado en `config/metadata.tex`
- [x] Índice de figuras (8) y tablas (9) definidos en el plan maestro (`../../planificacion/PLAN_ELABORACION_PLAN_TESIS.md`)
- [x] `make pdf` genera PDF sin errores
- [x] Portada con formato **exacto** Guía N°01 (`frontmatter/portada.tex`)

---

## Comando

```bash
cd plan-tesis/latex && make pdf
```

---

## Documento vivo (otras fases)

El PDF actual incluye más que el esqueleto puro porque el LaTeX es el **documento único** del equipo. Seguimiento por fase:

| Fase | Checklist |
|------|-----------|
| 0 | `../fase-0-bibliografia/CHECKLIST.md` |
| B | `../fase-b-planteamiento/CHECKLIST.md` |
| C | `../fase-c-marco-teorico/CHECKLIST.md` |
| D | `../fase-d-objetivos/CHECKLIST.md` |
| E | `../fase-e-marco-teorico/CHECKLIST.md` |
| F–H | `../../planificacion/PLAN_ELABORACION_PLAN_TESIS.md` |
| G | `../fase-g-administracion/CHECKLIST.md` |

Figuras y tablas (plan maestro completo): `../../figuras/README.md` · `../../latex/README.md`

---

## Siguiente paso del proyecto (no Fase A)

1. **Fase H** — Turnitin 2 · aula virtual · repaso hilo conductor  
2. Ver `../../planificacion/ESTADO_INFORME.md`
