# Sesión 6 — Revisión del método

Documento de curso (Guía 2 / desarrollo) Grupo 10. Revisa el Capítulo III antes del matching OE2–OE4.

**Las presentaciones de sesión son PDF (Beamer). No se genera PPTX.**

| Archivo | Formato |
|---------|---------|
| `image.png` | Lámina oficial del aula |
| `Sesion06_Revision_Metodo.md` | Fuente escrita |
| `Sesion06_Revision_Metodo.pdf` | Informe (pandoc) |
| `Sesion06_Revision_Metodo_slides.tex` | Fuente de la presentación |
| `Sesion06_Revision_Metodo_slides.pdf` | **Presentación** |
| `LIBRETO_SLIDES.md` | Libreto oral (11 diapositivas, 8–10 min) |
| `REVISION_PARES.md` | Acta de revisión visual |

**Plan v2:** `../plan-tesis-v2/PLAN_TESIS_V2.pdf` §7  
**Protocolo:** `../plan-tesis-v2/protocolo-empirico.md`  
**EDA / dataset:** `../sesion-05/`

```bash
pdflatex Sesion06_Revision_Metodo_slides.tex

pandoc Sesion06_Revision_Metodo.md \
  -o Sesion06_Revision_Metodo.pdf \
  --pdf-engine=xelatex \
  --toc --toc-depth=2 \
  -V geometry:margin=2.1cm \
  -V fontsize=11pt \
  -V colorlinks=true \
  -V lang=es \
  -V mainfont="Times New Roman"
```
