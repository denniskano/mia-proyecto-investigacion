# Retroalimentación docente — Grupo 9.2 (PI-12 + PI-13 + PI-14)

**Fuentes:**
- `transcriptions/MAE SE-A PI-12.txt` — redacción, IA generativa, estructura del documento
- `transcriptions/MAE SE-A PI-13.txt` — criterios de exposición documento (semana 13)
- `transcriptions/MAE SE-A PI-14.txt` — exposiciones continuación; calendario y rúbrica final

**Complementa:** `FEEDBACK_DOCENTE_PI10.md`, `FEEDBACK_DOCENTE_PI11.md`  
**Integrantes:** Alex Mancilla · Jack Paitan  
**Última actualización:** 2026-07-22

> **PI-14 — Grupo 9.2:** El docente llamó al grupo pero **no hubo exposición** (ausentes en el turno). Los criterios de PI-14 aplican igual para las fechas **23 y 30 julio**.

---

## 1. Mensajes centrales (nuevos vs PI-10/11)

| # | Idea del docente | Implicación Grupo 9.2 |
|---|------------------|------------------------|
| R1 | Texto bien escrito ≠ bien razonado; detecta **IA** por párrafos largos, generalidades y palabras rebuscadas | Pulir §1.2–§1.3; segundo Turnitin; redacción propia por sección |
| R2 | **Párrafos cortos:** 1 oración + complemento; oraciones 20–30 palabras; máx. 5–6 líneas | Acortar bloques en `02-problematica.tex`, §3.5 |
| R3 | **Enunciativo/declarativo** con evidencia; no estilo ensayo ni imperativo | Mantener afirmaciones + cita en problemática y marco |
| R4 | **Al inicio y cierre de cada sección:** qué se hará / qué se expuso | Cap. 2, 3, 4 (aplicado 2026-07-22) |
| R5 | **Metodología ↔ objetivos:** cada OE con paso metodológico en **verbo** | §4.2 + nueva §4.2.1 tabla OE↔fase↔producto |
| R6 | **Referencias trazables:** Zotero ↔ bibliografía ↔ cita; leer el paper antes de citar | Auditoría `referencias.tex`; 2 papers en exposición |
| R7 | **Figuras propias** + «ver Figura X»; ontología interna como diagrama, no sección publicada | Fig. ontología §1.4 (TikZ, elaboración propia) |
| R8 | **Tres problemas** en intro sucinta; definir conceptos antes de problemática | §1.1 ya cumple; no redefinir en §1.2 |
| R9 | No decir «no existe»; decir **insuficiente / no adaptado** | §1.3 reformulado |
| R10 | **23 y 30 jul:** exposición **con nota** (rúbrica); 30 jul **con PPT**; sin reprogramación arbitraria | Ver `exposicion/GUIA_EXPOSICION_JULIO.md` |

---

## 2. Criterios de exposición (PI-13 + PI-14)

| Criterio | Qué pide el docente | Evidencia en nuestro plan |
|----------|---------------------|---------------------------|
| Referencias | Mostrar ≥2 citas y el **pasaje** en el paper | Casas (2021) · Shvaiko & Euzenat (2005) |
| Párrafos | Cortos, una idea por bloque | Revisión §1.2 post-edición |
| Figuras/tablas | Elaboración propia; citar fuente si vienen de paper | Fig. 1–7 + ontología TikZ |
| Numeración | Todas las secciones numeradas | LaTeX `\setcounter{secnumdepth}{3}` |
| Conceptos centrales | Definidos al inicio (intro §1.1) | OpenAPI, BIAN, alineación, S/E/C |
| Tres problemas | Real → subyacente → técnico | §1.2 → §1.4 → §1.3 |
| Variables | Objetivos e hipótesis con factores/ratios | Cap. 2 §2.5–§2.6 · Tabla 5 |
| Metodología | Explica **cómo** se logra cada objetivo | §4.2.1 |
| Oral | **Marcar** la idea al hablar (como «mudo que señala») | Guía exposición §4 |

---

## 3. Mapeo docente → LaTeX (acciones)

| ID | Acción | Archivo | Estado |
|----|--------|---------|--------|
| A1 | Partir párrafo largo Casas/Golmohammadi | `02-problematica.tex` | ✅ 2026-07-22 |
| A2 | «Insuficiente/no adaptado» en problema tecnológico | `03-planteamiento.tex` | ✅ 2026-07-22 |
| A3 | Figura ontología conceptual + `\Cref` | `fig-ontologia.tex`, `04-objeto-estudio.tex` | ✅ 2026-07-22 |
| A4 | Apertura/cierre Cap. 2, 3, 4 | `_cap02.tex`, `_cap03.tex`, `_cap04.tex` | ✅ 2026-07-22 |
| A5 | Tabla OE ↔ fase ↔ verbo ↔ producto | `47-objetivos-metodologia.tex` | ✅ 2026-07-22 |
| A6 | Pasos metodológicos con verbos | `42-procedimiento.tex` | ✅ 2026-07-22 |
| A7 | Hipótesis ↔ factor/ratio explícito | `_cap02.tex` | ✅ 2026-07-22 |
| A8 | Guía exposición julio | `exposicion/GUIA_EXPOSICION_JULIO.md` | ✅ 2026-07-22 |
| A9 | Auditoría referencias (19 entradas ↔ citas autor-año) | `referencias.tex` + nota §5 | ✅ verificado |
| A10 | Pasada redacción PI-12 (Cap. 1–3, resumen, abstract) | múltiples `.tex` | ✅ 2026-07-22 |

---

## 4. Lo que **no** cambia (ya cubierto PI-10/11)

- Objeto = contrato OpenAPI bancario; BIAN = referencia  
- Objetivo superior vs OG técnico  
- Matriz 5 fases · OE transformadores  
- Alcance Guía 1 (§1.6)  
- Anexo F · adquisición datos Clase 04  

---

## 5. Auditoría bibliográfica (PI-12/13)

El documento usa **autor-año manual** en el cuerpo (no `\cite{}`). Las **19** entradas de `referencias.tex` cubren las citas del Cap. 1–5 verificadas en revisión cruzada.

| Verificación | Resultado |
|--------------|-----------|
| Casas et al. (2021) | DOI en bibliografía ✅ |
| CMA (2016), UK Treasury TSB (2018) | Informes oficiales ✅ |
| Shvaiko & Euzenat (2005) | Revista acotada ✅ |
| Informes sin DOI (Bhatia, Santos, Farzi, Shabbir) | Etiquetados como informe de contexto ✅ |

**Pendiente operativo:** export Zotero → verificar metadatos DOI antes de exposición con nota.

---

## 6. Citas textuales de referencia

**PI-12:**
- «Redactar no es escribir… el problema es que no hay **lógica**, no hay rigor.»
- «Un párrafo contiene primariamente **una oración** y un complemento.»
- «Al comenzar **cada sección**, expliquen brevemente qué van a hacer.»
- «La metodología tiene que decir **qué se hace en el objetivo uno, dos…**»
- «La ontología **nunca la muestras**; es para ustedes.»

**PI-13:**
- «Muéstrame **dos referencias** y el documento donde está lo que citan.»
- «**Marque** la idea que quiere transmitir.»
- «El 23 y el 30 **con nota**.»

**PI-14:**
- «Voy a empezar por la **metodología** e ir como el cangrejo hacia atrás.»
- «Pasos metodológicos deben ser **acciones**, verbos.»
- «Máximo **6 a 7** subsecciones en metodología; no 21.»

---

## 7. Seguimiento priorizado

### P0 — antes del 23 jul

| # | Tarea |
|---|-------|
| 1 | Ensayar exposición con guía `exposicion/GUIA_EXPOSICION_JULIO.md` |
| 2 | Confirmar fecha asignada (23 o 30) |
| 3 | Segundo Turnitin |
| 4 | PDF actualizado en aula virtual |

### P1 — exposición final (30 jul)

| # | Tarea |
|---|-------|
| 5 | PPT: dos casitos + modelo S/E/C + diagrama ontología |
| 6 | Ensayo sin leer: señalar PDF al hablar |

---

*Documento interno Grupo 9.2 — acta PI-12/13/14. Complementa checklists Fase H y `ESTADO_INFORME.md`.*
