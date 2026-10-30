# Checklist — Fase D (Capítulo 2)

**LaTeX:** `../../latex/chapters/cap02-objetivos/_cap02.tex`  
**Matriz:** `../../anexos/Matriz_Consistencia_Grupo9.2.xlsx` (Anexo C)  
**Compilar:** `cd ../../latex && make pdf`  
**Estado Fase D:** ✅ **cerrada** (revisión cruzada · 2026-05-28)

---

## Contenido

- [x] §2.1 Línea de base / datos iniciales
- [x] §2.2 Objetivo general (coherente con matriz OG)
- [x] §2.3 Objetivos específicos OE1–OE4 como transformaciones
- [x] §2.4 Hipótesis H1–H4 (+ Fase 1 diseño en Anexo C)
- [x] §2.5 Variables (`tables/tab05-variables.tex`)
- [x] §2.6 Figura cadena de objetivos (Fig. 4)

## Coherencia docente (PI-10)

- [x] Objetivos = transformadores entrada → salida (V3, M6)
- [x] OE1 normalización · OE2 E · OE3 S · OE4 C + AlignmentScore
- [x] Fase 1 diseño ≠ OE1 (marco metodológico)
- [x] Sin piloto fijo; coherente con Cap. 1

## Retroalimentación y revisión

- [x] Revisión cruzada Alex ↔ Jack → `REVISION_CRUZADA.md`
- [ ] Revisión docente
- [ ] Citas Zotero → Fase G

## Figuras

- [x] Fig. 4 en LaTeX (`../../figuras/cap02/Figura_04_Cadena_Objetivos.png`)
- [x] Regenerar: `build_figuras_fase_cd.py`

---

## Comandos

```bash
cd plan-tesis/latex && make pdf
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_figuras_fase_cd.py
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_matriz_consistencia.py
```

---

## Siguiente fase

**Fase F** — Cap. 4 metodología · revisión docente Cap. 2–3
