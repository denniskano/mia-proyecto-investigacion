# Checklist — Fase 0 (Bibliografía y fichas)

**Estado:** fichas + Excel ✅ · síntesis §3.5–§3.6 ✅ · integrado LaTeX §3.5–§3.6 ✅ · revisión cruzada ✅

---

## Resumen

| Ítem | Progreso |
|------|----------|
| PDFs en `bibliografia/estado-del-arte/` | 14 / 14 ✅ |
| Fichas `fichas/*.md` (estado **completada**) | 14 / 14 ✅ |
| Mapa de ejes (`EJES_ESTADO_DEL_ARTE.md`) | ✅ |
| Plantilla (`PLANTILLA_FICHA.md`) | ✅ |
| Excel Anexo B (`anexos/Matriz_Papers_EstadoDelArte_Grupo9.2.xlsx`) | ✅ sincronizado desde fichas |
| Borrador §3.5–3.6 | ✅ `EJES_ESTADO_DEL_ARTE.md` + `../fase-c-marco-teorico/CAPITULO_03_ESTADO_DEL_ARTE.md` |

---

## Progreso por paper

| ID | Paper | Eje | PDF | Ficha | Excel |
|----|-------|-----|-----|-------|-------|
| E1-01 | Casas et al., 2021 | E1 | [x] | [x] | [x] |
| E1-02 | Mainas et al., 2023 | E1 | [x] | [x] | [x] |
| E1-03 | Santos y Casas, 2025 | E1 | [x] | [x] | [x] |
| E2-01 | Shvaiko y Euzenat, 2005 | E2 | [x] | [x] | [x] |
| E3-01 | El Bayadh et al., 2015 | E3 | [x] | [x] | [x] |
| E3-02 | Chandrasekaran y Mago, 2022 | E3 | [x] | [x] | [x] |
| E3-03 | Santos Sousa et al., 2026 | E3 | [x] | [x] | [x] |
| E4-01 | Schmidt y Thiry, 2020 | E4 | [x] | [x] | [x] |
| E5-01 | Ehsan et al., 2022 | E5 | [x] | [x] | [x] |
| E5-02 | Golmohammadi et al., 2024 | E5 | [x] | [x] | [x] |
| E5-03 | Otieno y Araka, 2026 | E5 | [x] | [x] | [x] |
| E5-04 | Tanveer et al., 2025 | E5 | [x] | [x] | [x] |
| E5-05 | Vitorino et al., 2025 | E5 | [x] | [x] | [x] |
| E6-01 | Mahanra Rao et al., 2025 | E6 | [x] | [x] | [x] |

---

## Progreso por eje (§3.5.1)

| Eje | Papers | Fichas | Vacío OpenAPI–BIAN en fichas |
|-----|--------|--------|------------------------------|
| **E1** OpenAPI como estándar | 3 | [x] 3/3 | ✅ §7 en E1-01, E1-02, E1-03 |
| **E2** Matching estructural | 1 | [x] 1/1 | ✅ E2-01 |
| **E3** Matching semántico | 3 | [x] 3/3 | ✅ E3-01, E3-02, E3-03 |
| **E4** Microservicios / interfaces | 1 | [x] 1/1 | ✅ E4-01 |
| **E5** Testing (borde) | 5 | [x] 5/5 | ✅ delimitación en E5-01…E5-05 |
| **E6** Selección de servicios | 1 | [x] 1/1 | ✅ E6-01 |

**Brecha transversal (§3.6):** ningún paper propone S + E + C → AlignmentScore para OpenAPI bancario ↔ BIAN — ver párrafo final de `EJES_ESTADO_DEL_ARTE.md`.

---

## División sugerida (revisión cruzada)

| Integrante | Papers | IDs | Revisión |
|------------|--------|-----|----------|
| Alex | 7 | E1-01, E1-03, E3-01, E3-03, E5-02, E5-04, E6-01 | [x] |
| Jack | 7 | E1-02, E2-01, E3-02, E4-01, E5-01, E5-03, E5-05 | [x] |

---

## Criterios de cierre Fase 0

- [x] 14 PDFs disponibles en `bibliografia/estado-del-arte/`
- [x] 14 fichas en `fichas/` con estado **completada** (§1–9 según `PLANTILLA_FICHA.md`)
- [x] Cada ficha incluye vacío/oportunidad OpenAPI–BIAN (§7) y aporte S/E/C (§9)
- [x] Mapa E1–E6 actualizado en `EJES_ESTADO_DEL_ARTE.md`
- [x] Regenerar Excel: `build_matriz_papers.py`
- [x] Columnas 6–11 del Anexo B rellenadas desde fichas (objetivo, dominio, técnicas, métricas, limitaciones, vacío)
- [x] Columna «Estado ficha» = completada en Excel
- [x] Hoja «Por eje» revisada
- [x] Revisión cruzada Alex ↔ Jack de fichas asignadas al otro (`REVISION_CRUZADA.md`)
- [x] Borrador §3.6 listo para Fase C (expandir brecha de `EJES_ESTADO_DEL_ARTE.md`)

---

## Comandos

```bash
# Generar Excel Anexo B (no sobrescribe fichas .md existentes)
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_matriz_papers.py
```

---

## Siguiente fase

**Fase F** — Cap. 4 metodología · **Fase G** — anexos LaTeX + Zotero · subir PDF al aula virtual

**Referencia cruzada:** Cap. 1–3 cerrados (Fases B–E) · Matriz consistencia Anexo C ✅ · Fig. 1–7 en PDF.
