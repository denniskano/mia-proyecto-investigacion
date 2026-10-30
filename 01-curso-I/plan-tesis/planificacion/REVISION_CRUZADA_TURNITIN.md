# Revisión cruzada — Turnitin / reducción IA

**Fecha:** 2026-07-02  
**Contexto:** Turnitin 2% similitud · 49% IA (solo total reportado)  
**Agente A (Cap. 1):** §1.2–§1.4 narrativo · §1.7  
**Agente B (Cap. 2–3):** objetivos · §3.1–§3.4 · §3.5–§3.6  

---

## Veredicto

| Bloque | Estado | Notas |
|--------|--------|-------|
| Resumen + Abstract + §1.1 | ✅ | Tanda previa (Jack) |
| §1.2 Problemática | ✅ | Agente A — PI-11, TSB, CMA, tono Grupo 9.2 |
| §1.3 Planteamiento | ✅ | Agente A — tres niveles + matriz vs. brecha |
| §1.4 Objeto (narrativo) | ✅ | Agente A — Anexo F, ontología interna |
| §1.7 Justificación | ✅ | Agente A |
| Cap. 2 Objetivos | ✅ | Agente B — OG superior/técnico, fichas en hipótesis |
| Cap. 3 §3.1–§3.4 | ✅ | Agente B — datos de fichas |
| Cap. 3 §3.5–§3.6 | ✅ | Agente B — encabezados **Papers:** por eje |
| Cap. 4 | ✅ | §4.1–§4.8 redactados (PI-11 adquisición datos) |
| Cap. 5 + anexos técnicos | ⏳ | Baja prioridad Turnitin |

**Coherencia cruzada:** contenido alineado (PI-11, sin piloto fijo, brecha ≠ matriz). **Tono:** Cap. 1–3 ahora más homogéneo y anclado al grupo.

---

## Pendientes menores (post-revisión)

1. ~~Cap. 2 §2.4: factores / ratios (PI-11 M8)~~ ✅ 2026-07-02
2. ~~Relectura oral Alex ↔ Jack~~ ✅ `REVISION_ORAL_ALEX_JACK.md` · 10 correcciones aplicadas
3. ~~Regenerar entrega Drive~~ ✅ `Informe_Guia1_Grupo9.2.zip`

---

## Tanda 2026-07-02 (relectura oral)

- Acta: `REVISION_ORAL_ALEX_JACK.md` — veredicto condicional → **correcciones aplicadas**
- Cap. 1: meta PI-11, §1.7 narrativo, ID instancia, umbrales provisionales, §1.1 LaTeX
- Cap. 2–3: §2.3 oral, Tabla 5 OE1 ratio, §3.2 REST acortado, E5 partido
- PDF recompilado · entrega regenerada (~34 MB)

---

## Tanda 2026-07-02 (continuación)

- Cap. 4 §4.1–§4.8 redactado (adquisición datos Tabla~4.x, protocolo Tesis~2, validez).
- Terminología **factores / ratios** en Cap. 2, Anexo D, Excel matriz.
- PDF: 55 páginas · entrega regenerada.

---

## Comandos

```bash
cd plan-tesis/latex && latexmk -pdf -outdir=build -f main.tex
python3 herramientas/scripts/build_entrega_guia01.py   # si aplica
```

---

## Siguiente paso Turnitin

Subir `latex/build/Plan_Tesis_Grupo9.2.pdf` completo (Cap. 1–3 reescritos). Comparar **solo el total IA** con el 49% inicial.
