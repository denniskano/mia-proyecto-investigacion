# Exposición Beamer — presentación oficial

PDF oficial del Grupo 9.2: **`../Exposicion_Plan_Tesis_Grupo9.2-beamer.pdf`** (**22 slides**; slides **2** y **3** no oral · punto rojo).

**Guiones:** [`../LIBRETO_EXPOSICION_COMPLETO.md`](../LIBRETO_EXPOSICION_COMPLETO.md) · [`../ppt/GUION_15MIN_AMPLIADO.md`](../ppt/GUION_15MIN_AMPLIADO.md)

## Compilar

```bash
cd plan-tesis/exposicion/latex
make pdf          # extrae figuras del PPT + compila PDF
make open
make clean
```

Requisitos: MacTeX/TeX Live + `../ppt/.venv` (python-pptx).

## Figuras

| Slides Beamer | Origen |
|---------------|--------|
| 4–10, 17 | Imágenes extraídas de `../ppt/Exposicion_Plan_Tesis_Grupo9.2.pptx` → `ppt-images/` |
| 13, 19 | Informe: `../../figuras/cap02/Figura_04_Cadena_Objetivos.png`, `../../figuras/cap03/Figura_06_Brecha.png` |

Extracción automática PPT vía `extract_ppt_images.py`.

## Estructura (22 slides)

| Slide | Contenido | Oral |
|-------|-----------|------|
| 1 | Portada | ✅ |
| 2 | Fuentes Drive + Zotero | ⛔ |
| 3 | Intro §1.1 escrita | ⛔ |
| 4 | Ontología (figura informe) | ⛔ |
| 5–22 | Problemática → referencias | ✅ (ver guion) |

Navegación en clase: **1 → 5 → … → 22**.

## Fuentes LaTeX

- `exposicion_beamer.tex` — contenido
- `beamer-preamble.tex` — estilo
- `../../latex/config/metadata.tex` — título idéntico al plan de tesis
