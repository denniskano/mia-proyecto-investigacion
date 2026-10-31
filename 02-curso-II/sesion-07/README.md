# Sesión 7 — Revisión de avances (salas)

Documento de curso (Guía 2 / desarrollo) Grupo 10. Revisión en salas: Trello, primeros resultados, métricas y revistas.

**Las presentaciones de sesión son PDF (Beamer). No se genera PPTX.**

| Archivo | Formato |
|---------|---------|
| `image.png` | Lámina oficial del aula |
| `Sesion07_Revision_Avances.md` | Fuente escrita |
| `Sesion07_Revision_Avances.pdf` | Informe (pandoc) |
| `cuaderno-pruebas.md` | Cuaderno de las primeras pruebas (OE1 + EDA) |
| `Sesion07_Revision_Avances_slides.tex` | Fuente de la presentación |
| `Sesion07_Revision_Avances_slides.pdf` | **Presentación** |

**Trello / 12 semanas:** `../plan-tesis-v2/cronograma-sprints.md`  
**Protocolo:** `../plan-tesis-v2/protocolo-empirico.md`  
**EDA:** `../sesion-05/`

```bash
pdflatex Sesion07_Revision_Avances_slides.tex

pandoc Sesion07_Revision_Avances.md \
  -o Sesion07_Revision_Avances.pdf \
  --pdf-engine=xelatex \
  --toc --toc-depth=2 \
  -V geometry:margin=2.1cm \
  -V fontsize=11pt \
  -V colorlinks=true \
  -V lang=es \
  -V mainfont="Times New Roman"
```
