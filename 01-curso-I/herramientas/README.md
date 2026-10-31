# Herramientas

| Ruta | Uso |
|------|-----|
| `.venv-excel/` | Entorno Python con `openpyxl`, `matplotlib` |
| `scripts/build_figuras_fase_b.py` | Genera Figuras 1 y 2 (PNG + SVG) |
| `scripts/build_figuras_fase_cd.py` | Genera Figuras 4, 5 y 6 (Cap. 2–3) |
| `scripts/build_matriz_papers.py` | Genera Anexo B + fichas stub (Fase 0) |
| `scripts/build_matriz_consistencia.py` | Genera Anexo C — Matriz de consistencia (Excel) |
| `scripts/build_anexos_latex.py` | Genera tablas LaTeX Anexos B, C, D |
| `scripts/build_entrega_guia01.py` | Empaqueta carpeta Informe Guía 1 (Google Drive) |
| `scripts/papers_estado_del_arte.py` | Catálogo de los 14 papers (datos) |

**Documento del plan:** LaTeX en `plan-tesis/latex/` → `make pdf` (no hay generadores Word).

```bash
# Desde 01-curso-I/
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_figuras_fase_b.py
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_figuras_fase_cd.py
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_matriz_papers.py
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_matriz_consistencia.py
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_anexos_latex.py
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_entrega_guia01.py
cd plan-tesis/latex && make pdf
```

Salidas:
- Plan de tesis PDF → `plan-tesis/latex/build/Plan_Tesis_Grupo10.pdf`
- Figuras Cap. 1 → `plan-tesis/figuras/cap01/` (vía symlinks desde Fase B)
- Figuras Cap. 2–3 → `plan-tesis/figuras/cap02/`, `cap03/` (Fase C/D/E)
- Fase 0 → `plan-tesis/fases/fase-0-bibliografia/fichas/` + `plan-tesis/anexos/Matriz_Papers_EstadoDelArte_Grupo10.xlsx`
- Anexo C → `plan-tesis/anexos/Matriz_Consistencia_Grupo10.xlsx`
- Entrega Guía 1 → `plan-tesis/entrega/Informe_Guia1_Grupo10/` (+ `.zip`)
