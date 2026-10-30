# Carpeta `ppt/` — fuente de figuras (no presentación oral)

## Presentación oficial (proyectar en clase)

| Archivo | Uso |
|---------|-----|
| **`../Exposicion_Plan_Tesis_Grupo9.2-beamer.pdf`** | **Proyectar en clase** — 22 slides (saltar slides **2** y **3**) |

## Guiones (alineados al Beamer PDF)

| Documento | Uso |
|-----------|-----|
| [`GUION_15MIN_AMPLIADO.md`](GUION_15MIN_AMPLIADO.md) | Timing minuto a minuto (22 slides) |
| [`../LIBRETO_EXPOSICION_COMPLETO.md`](../LIBRETO_EXPOSICION_COMPLETO.md) | Texto oral slide por slide |

## Archivos legacy (no proyectar)

| Archivo | Uso |
|---------|-----|
| `Exposicion_Plan_Tesis_Grupo9.2.pptx` | Fuente de figuras para Beamer (`latex/extract_ppt_images.py`) |
| `Exposicion_Plan_Tesis_Grupo9.2-v2.pptx` | Experimento PptxGenJS (no oficial) |
| `Exposicion_Plan_Tesis_Grupo9.2-ampliado.pptx` | Versión anterior (obsoleta) |

## Regenerar PDF oficial

```bash
cd plan-tesis/exposicion/latex
make pdf
```
