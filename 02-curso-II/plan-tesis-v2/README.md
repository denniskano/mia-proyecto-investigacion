# Plan de tesis v2 — Proyecto de Investigación II (MIA 403)

**Grupo 10** · Alex Mancilla Antay · Dennis Jack Paitan Cano  
**Curso:** MIA 403 · 2026-2  
**Continuidad:** Guía 1 vive en `../../01-curso-I/plan-tesis/` (LaTeX). Esta carpeta es el **plan vigente** del segundo curso: ejecutable + protocolo + evidencia piloto.

| Documento | Uso |
|-----------|-----|
| `PLAN_TESIS_V2.md` / `.pdf` | Plan de tesis del segundo curso (P4, semanas 8–9) |
| `REVISION_PARES.md` | Acta de revisión (30 oct 2026) |
| `diagnostico-guia1-a-guia2.md` | P1 · qué se hereda y qué se ejecuta |
| `cronograma-sprints.md` | Hoja de ruta 16 semanas (Trello) |
| `protocolo-empirico.md` | Protocolo paso a paso (semana 7+) |
| `matriz-consistencia-ofb.md` | Matriz institucional 8 columnas, alcance OFB |
| `Matriz_Consistencia_OFB_Grupo10.xlsx` / `.pdf` | Misma matriz, entrega institucional |

**Objeto de la tesis (se mantiene):** contratos **OpenAPI bancarios** frente a Service Domains BIAN.  
**Piloto MIA 403:** catálogo **Open Finance Brasil (OFB)** — muestra empírica, no redefinición del objeto. En este curso no se añaden YAML de un banco emisor ni Open Banking UK.

**Piloto:** `../piloto/`

Regenerar la matriz (hace falta `openpyxl` del venv de herramientas):

```bash
../../01-curso-I/herramientas/.venv-excel/bin/python build_matriz_ofb.py
```

Acta de revisión de pares: `REVISION_PARES.md`.

Regenerar el PDF del plan:

```bash
pandoc PLAN_TESIS_V2.md -o PLAN_TESIS_V2.pdf --pdf-engine=xelatex \
  --toc --toc-depth=2 -V geometry:margin=2.1cm -V fontsize=11pt \
  -V colorlinks=true -V lang=es -V mainfont="Times New Roman"
```
