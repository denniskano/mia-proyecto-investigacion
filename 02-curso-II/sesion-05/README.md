# Sesión 5 — Operacionalización e instrumentos · EDA

Documento de curso (Guía 2 / desarrollo) Grupo 10. El plan vigente está en `../plan-tesis-v2/`.

| Archivo | Formato |
|---------|---------|
| `Sesion05_Operacionalizacion_y_EDA_slides.pdf` | **Presentación** (PDF) |
| `LIBRETO_SLIDES.md` | Libreto oral (19 diapositivas, 12–14 min) |
| `Sesion05_Operacionalizacion_y_EDA.md` | Fuente escrita (detalle) |
| `Sesion05_Operacionalizacion_y_EDA.pdf` | Informe largo (pandoc) |
| `ppt/build_sesion05.mjs` | Generador del PPTX |
| `data/piloto_ofb_bian/` | Piloto: 38 APIs OFB + 3 SD BIAN |

**Dataset:** `data/piloto_ofb_bian/` (`fuentes/ofb/` + `fuentes/bian/`)  
**Plan v2:** `../plan-tesis-v2/PLAN_TESIS_V2.pdf`

```bash
# Regenerar PPTX
node ppt/build_sesion05.mjs

# Regenerar informe largo
pandoc Sesion05_Operacionalizacion_y_EDA.md \
  -o Sesion05_Operacionalizacion_y_EDA.pdf \
  --pdf-engine=xelatex \
  --toc --toc-depth=2 \
  -V geometry:margin=2.1cm \
  -V fontsize=11pt \
  -V colorlinks=true \
  -V lang=es \
  -V mainfont="Times New Roman"
```
