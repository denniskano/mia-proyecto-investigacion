# Sesión 6 — Revisión del método

Documento de curso (Guía 2 / desarrollo) Grupo 10. Revisa el Capítulo III antes del matching OE2–OE4.

| Archivo | Formato |
|---------|---------|
| `image.png` | Lámina oficial del aula (5 puntos a revisar) |
| `Sesion06_Revision_Metodo.md` | Fuente escrita |
| `Sesion06_Revision_Metodo.pdf` | Informe (pandoc) |
| `Sesion06_Revision_Metodo.pptx` | Presentación (11 diapositivas) |
| `ppt/build_sesion06.mjs` | Generador del PPTX |

**Plan v2:** `../plan-tesis-v2/PLAN_TESIS_V2.pdf` §7  
**Protocolo:** `../plan-tesis-v2/protocolo-empirico.md`  
**EDA / dataset:** `../sesion-05/`

```bash
node ppt/build_sesion06.mjs

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
