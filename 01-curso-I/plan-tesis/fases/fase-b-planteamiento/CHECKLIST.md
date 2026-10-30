# Checklist — Fase B (Capítulo 1)

**Fuente del Cap. 1:** `../../latex/chapters/cap01-planteamiento/`  
**Compilar:** `cd ../../latex && make pdf`  
**Estado Fase B:** ✅ **cerrada** (2026-05-28 · revisión cruzada en `REVISION_CRUZADA.md`)

## Contenido

- [x] §1.1 Introducción — definiciones OpenAPI/BIAN/alineación → contexto → puente (sin problemática)
- [x] §1.2 Problemática — fragmentación, deriva documental
- [x] §1.3 Planteamiento — problema + P1–P4 + Tabla 2 tipologías
- [x] §1.4 Objeto de estudio — contratos OpenAPI; objeto vs unidad; Tabla 1.4 ejemplo genérico; modelo S/E/C
- [x] §1.5 Ámbito y delimitación
- [x] §1.6 Alcances y limitaciones (Tabla 1.7) — incluye Guía 1 vs Guía 2 + prosa §1.6
- [x] §1.7 Justificación
- [x] §1.8 Clasificación IEEE/ACM
- [x] §1.9 Tipo de investigación
- [x] Problema formulado como **preguntas**, no como objetivos

## Retroalimentación docente (PI-10)

- [x] Acta en `FEEDBACK_DOCENTE_PI10.md` (§2 aplicado en Cap. 1)
- [x] Cap. 1: definiciones §1.1, unidad de análisis + Tabla 1.4 §1.4, Guía 1/2 §1.6
- [x] Matriz: Fase 1 = diseño; 5 fases; sin piloto; puente textual §1.4
- [x] Revisión cruzada Alex ↔ Jack → `REVISION_CRUZADA.md`
- [x] PI-11 aplicado en Cap. 1 (2026-05-28 · relectura oral 2026-07-02)
- [x] Pendientes PI-10 post–Fase B cerrados en Cap. 2 y Cap. 4 → `FEEDBACK_DOCENTE_PI10.md` §4
- [ ] PPT exposición (E1–E3) — no es contenido LaTeX

## Figuras

- [x] Fig. 1–3 en LaTeX (`../../figuras/cap01/` + `../../figuras/modelo-alineacion/`)
- [x] PNG fuente Fig. 1–2: `figuras/` (regenerar con `build_figuras_fase_b.py`)

## Coherencia docente

| Criterio | Estado |
|----------|--------|
| Problema ≠ objetivo | ✅ |
| Objeto de estudio = contratos OpenAPI bancarios | ✅ |
| Producto central = modelo de alineación + AlignmentScore | ✅ |
| Matriz consistencia + título unificado | ✅ |
| Referencias PI-XX solo en plan interno | ✅ |

## Comandos

```bash
cd plan-tesis/latex && make pdf
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_figuras_fase_b.py
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_matriz_consistencia.py
```

## Siguiente fase

**Fase H** — cierre curso · Turnitin 2 · aula virtual
