# Checklist — Fase G (Cap. 5 + anexos + referencias)

**LaTeX:** `../../latex/chapters/cap05-administracion/` · `../../latex/anexos/` · `../../latex/frontmatter/referencias.tex`  
**PDF:** `../../latex/build/Plan_Tesis_Grupo9.2.pdf` (~55 pp.)  
**Estado Fase G:** ✅ **cerrada** (2026-05-28)

**Prerequisitos:** Fases 0, B, C, D, E, F ✅

---

## Resumen

| Ítem | Progreso |
|------|----------|
| Cap. 5 §5.1–§5.5 | ✅ |
| Tabla 9 cronograma | ✅ `tables/tab09-cronograma.tex` |
| Tabla riesgos + presupuesto | ✅ `tables/tab10-riesgos.tex` |
| Anexo A — string búsqueda | ✅ `anexos/anexo-a.tex` |
| Anexo B — matriz papers | ✅ LaTeX + Excel |
| Anexo C — matriz consistencia | ✅ LaTeX + Excel |
| Anexo D — operación ratios + factores | ✅ `tab-anexo-d-operacion.tex` |
| Anexo E — diseño factorial N/A | ✅ `anexo-e.tex` |
| Anexo F — ejemplos OpenAPI/BIAN | ✅ (I5) |
| Referencias bibliográficas | ✅ `frontmatter/referencias.tex` + `referencias.bib` |
| Compilación PDF | ✅ |

---

## Capítulo 5

- [x] §5.1 Cronograma (Tabla 9)
- [x] §5.2 Recursos humanos, software, bibliográficos
- [x] §5.3 Roles del equipo (Tabla roles)
- [x] §5.4 Riesgos (Tabla 10)
- [x] §5.5 Presupuesto (costo cero + impresión opcional)

---

## Anexos LaTeX

- [x] A — Cadenas de búsqueda + criterios inclusión/exclusión
- [x] B — Resumen 14 papers (`build_anexos_latex.py` → `tab-anexo-b-resumen.tex`)
- [x] C — Resumen 5 fases + trazabilidad OE
- [x] D — Operación de ratios + factores S/E/C + factores por OE
- [x] E — No aplica (justificación; terminología factores PI-11)
- [x] F — Ejemplo reducido + ampliado (YAML + tablas BIAN/S/E/C)

---

## Referencias

- [x] Lista APA en PDF (`referencias.tex` — 18 entradas citadas Cap. 1–3)
- [x] `referencias.bib` para carga en plataforma / Zotero
- [ ] Sincronizar metadatos exactos con Zotero del equipo (DOI/volúmenes finales)
- [ ] Verificar papers de contexto (`bibliografia/contexto-openapi-bian/`) cuando PDFs disponibles

---

## Entrega plataforma (PI-03)

- [ ] Subir PDF `Plan_Tesis_Grupo9.2.pdf`
- [ ] Subir `referencias.bib` o export Zotero
- [ ] Subir al menos 1 paper clave (p. ej. Casas 2021)
- [ ] Opcional: Excel Anexos B y C + `figuras_alineacion_openapi_bian.pdf`

Ubicación: **Aula virtual → Productos y entregables → Presentación de propuesta**

---

## Comandos

```bash
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_anexos_latex.py
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_matriz_papers.py
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_matriz_consistencia.py
cd plan-tesis/latex && make pdf
```

---

## Siguiente fase

**Fase H** — Turnitin 2 · entrega aula virtual · revisión cierre docente
