# Plan de tesis — Grupo 10

**PDF Guía 1:** `latex/build/Plan_Tesis_Grupo10.pdf` (57 pp.)  
**Plan v2 (MIA 403):** [`../../02-curso-II/plan-tesis-v2/`](../../02-curso-II/plan-tesis-v2/) · objeto = OpenAPI bancario · piloto = OFB
**Plan maestro:** `planificacion/PLAN_ELABORACION_PLAN_TESIS.md`  
**Estado consolidado:** `planificacion/ESTADO_INFORME.md`

## Avance Guía 1 (Tesis 1)

| Dimensión | % |
|-----------|---|
| Contenido informe (LaTeX) | **~98%** |
| Cierre curso (Turnitin + aula) | **~70%** |

**Alcance:** solo diseño del plan · **no** Tesis 2 (construcción/experimento).

## Estado por fase

| Fase | Estado | Checklist |
|------|--------|-----------|
| 0 — Bibliografía | ✅ | `fases/fase-0-bibliografia/CHECKLIST.md` |
| A — Esqueleto LaTeX | ✅ | `fases/fase-a-indice/CHECKLIST.md` |
| B — Cap. 1 | ✅ | `fases/fase-b-planteamiento/CHECKLIST.md` |
| C — §3.5–§3.6 | ✅ | `fases/fase-c-marco-teorico/CHECKLIST.md` |
| D — Cap. 2 | ✅ | `fases/fase-d-objetivos/CHECKLIST.md` |
| E — §3.1–§3.4 | ✅ | `fases/fase-e-marco-teorico/CHECKLIST.md` |
| G — Cap. 5 + anexos | ✅ | `fases/fase-g-administracion/CHECKLIST.md` |
| F — Cap. 4 | ✅ | §4.1–§4.8 · PI-11 adquisición datos |
| H — Cierre | ⏳ | Turnitin 2 · subir aula virtual |

**Feedback PI-10:** `fases/fase-b-planteamiento/FEEDBACK_DOCENTE_PI10.md`  
**Feedback PI-11 + Clase 04:** `fases/FEEDBACK_DOCENTE_PI11.md`  
**Revisión Turnitin (IA):** `planificacion/REVISION_TURNITIN_IA.md`

## Carpetas

| Ruta | Contenido |
|------|-----------|
| `planificacion/` | Plan maestro de elaboración |
| `latex/` | Documento maestro LaTeX |
| `figuras/` | Fig. 1–7 (`figuras/README.md`) |
| `fases/` | Checklists y borradores por fase |
| `exposicion/` | Guion, checklist y PPT (23/30 jul) |
| `anexos/` | Matrices Excel + PDF modelo S/E/C |
| `../../02-curso-II/plan-tesis-v2/` | **Segundo curso (MIA 403):** plan ejecutable; objeto OpenAPI bancario; piloto OFB |

## Compilar

Requisitos: MacTeX o TeX Live (`pdflatex`, `latexmk`).

```bash
cd latex && make pdf
# Salida: build/Plan_Tesis_Grupo10.pdf (copia de main.pdf; no usar latexmk sin make)
```

## Repositorio Git

La raíz del repo es **`plan-tesis/`** (no solo `latex/`). Para compilar hacen falta:

| Carpeta | Contenido |
|---------|-----------|
| `latex/` | Fuente LaTeX, tablas, anexos |
| `figuras/` | Fig. 1–7 y apoyos S/C |
| `fases/fase-b-planteamiento/figuras/` | Fuente SVG/PNG Fig. 1–2 (regenerar) |
| `anexos/` | PDF modelo S/E/C; Excel Anexos B/C |

Los PNG de `figuras/cap01/` son **copias** de las Fig. 1–2 (sin symlinks; compatibles con Windows).

```bash
git clone <url> plan-tesis
cd plan-tesis/latex && make pdf
```

`latex/build/` está en `.gitignore`. Scripts Python para regenerar tablas/figuras: `../../herramientas/scripts/` (repo v3, fuera de este Git).

### Entrega Informe Guía 1 (Google Drive)

```bash
python3 herramientas/scripts/build_entrega_guia01.py
```

Genera `entrega/Informe_Guia1_Grupo10/` (5 carpetas, sin README internos) y `.zip`.

## Capítulos en LaTeX

| Cap. | Carpeta | Estado |
|------|---------|--------|
| 1 | `latex/chapters/cap01-planteamiento/` | ✅ |
| 2 | `latex/chapters/cap02-objetivos/` | ✅ |
| 3 | `latex/chapters/cap03-marco/` | ✅ §3.1–§3.6 |
| 4 | `latex/chapters/cap04-metodologia/` | ✅ |
| 5 | `latex/chapters/cap05-administracion/` | ✅ |

## Ver también

- `latex/README.md`
- `../README.md` (raíz v3)
