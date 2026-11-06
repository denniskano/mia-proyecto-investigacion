# Revisión de pares — Turnitin IA (~50 %)

**Fecha:** 6 nov 2026  
**Qué se revisó:** el plan que ya pasó por Turnitin (**Guía 1** `Plan_Tesis_Grupo10.pdf`) y el **Plan v2** vigente, que comparte el mismo tono.  
**Reporte previo:** 2 % similitud (bien) · **~49–50 % “escrito con IA”** (solo total; sin mapa por sección).  
**Veredicto:** el contenido es del grupo (objeto, S/E/C, matriz, fichas). El porcentaje alto es **estilo de prosa académica genérica**, no copia. Un segundo envío **sin reescribir narrativo** no va a bajarlo.

Turnitin no publica umbral oficial. El 50 % no prueba que “lo escribió ChatGPT”; marca **ritmo, transiciones y simetría** típicos de texto asistido. Tampoco se limpia con un “humanizador”.

---

## Qué sí y qué no explica el 50 %

| El detector **sí** marca | El detector **casi no** marca |
|--------------------------|-------------------------------|
| Párrafos del mismo largo, misma cadencia | Tablas, fórmulas, listas de pares I1–I6 |
| “Esta sección…”, “Sin embargo…”, “no sustituye…” | Citas con cifra (47 papers, 1,9 millones, 61,9 %) |
| Definiciones de libro (OpenAPI, BIAN, design science) | IDs, YAML, `procesar_openapi.py` |
| Cierre de cada eje: “existe X; falta Y” | Anexo C/D, inventario, números del piloto |
| Resumen + Abstract espejo ES/EN | Nombres propios (TSB, CMA, OFB, Grupo 10) |

La similitud al 2 % confirma que **no hay copiar-pegar de papers**. El 50 % de IA está en **cómo** está redactado el planteamiento, la justificación, el estado del arte y los objetivos.

---

## Hallazgos (prioridad de reescritura)

| # | Dónde | Qué se ve | Gravedad |
|---|--------|-----------|----------|
| 1 | Resumen + Abstract Guía 1 | Dos párrafos espejo, simétricos, sin decisión del grupo | Alta (poco texto, mucho peso) |
| 2 | §1.1 Introducción | Tres bloques plantilla: “en banca… / en paralelo BIAN… / llamamos alineación…” | Alta |
| 3 | §1.2 Problemática | Arranca con “Esta sección corresponde a…”. Luego 4 síntomas en viñeta idéntica | Alta |
| 4 | §1.3 Planteamiento | Tres niveles con la misma receta: definición + “no es X” + puente al siguiente | Alta |
| 5 | Cap. 2 Objetivos | “Este capítulo presenta…”. OG y superior en voz de manual | Alta |
| 6 | §3.5 Estado del arte | Cada eje: Papers → resumen → **Conclusión En:** “maduro / falta aplicar a OpenAPI–BIAN” | Alta (más páginas) |
| 7 | §1.7, §3.2, §4.1 | Muletillas: *no sustituye*, *queda fuera de alcance*, *de forma reproducible* | Media |
| 8 | Plan v2 §1, §3.7, §7 | Mismo ADN. Si Turnitin se hace sobre el v2, el % se va a parecer | Media |
| 9 | Tablas, protocolo, EDA | Tono de bitácora; no es el problema | Baja (no reescribir) |

---

## Ejemplos (para que se vea el patrón)

**Plantilla de apertura** (se repite en justificación, problemática, objeto, Cap. 2):

> “Esta sección explica / corresponde / formula…”

**Plantilla de eje** (E1–E6): *paper → cifra → “sin embargo no aborda BIAN” → conclusión con el mismo verbo*.

**Plantilla de delimitación** (intro, OG, método):

> “El plan diseña el procedimiento. La construcción del artefacto queda fuera de alcance (§1.6).”

Eso es correcto de contenido. Como prosa, es **la misma oración tres veces**. El detector la cuenta como IA.

**Lo que ya suena a Grupo 10** (no tocar): TSB 1,9 millones; CMA 2016; Casas 47 estudios / 40 %; “parser al 100 % no implica AlignmentScore Alto”; I3a/I3b; OFB ≠ objeto.

---

## Plan v2 (el documento vigente)

El PDF `PLAN_TESIS_V2.pdf` es más corto y más tabular. Eso **ayuda**. Sigue en riesgo:

- §1 Continuidad (hereda / cambia) en prosa de informe de agente.
- §3.7 Justificación (tres aportes i–ii–iii).
- §7 “Tipo / enfoque / no es / población / muestra” en viñetas simétricas.

Si el trámite pide **Guía 1 LaTeX**, hay que reescribir Cap. 1–3 de ese PDF. Si pide el **v2**, reescribir esas tres secciones basta como primera pasada.

---

## Qué no va a bajar el porcentaje

- Cambiar sinónimos frase a frase (“coherencia” ↔ “alineación”).
- Pasar el PDF por un humanizador o por otra IA.
- Recompilar LaTeX sin tocar el narrativo.
- Reescribir tablas, fórmulas o el protocolo empírico.

---

## Cómo bajarlo (orden)

1. **Resumen + Abstract** — una sola voz, no espejo. En ES: qué va a hacer el Grupo 10 en MIA 403 (piloto OFB, 7 instancias). En EN: no traducir oración por oración.
2. **§1.1 y §1.7** — cortar definiciones de diccionario; arrancar con la decisión (medir OpenAPI × BIAN **antes** de integrar; Guía 1 = diseño).
3. **§1.2** — dejar TSB/CMA/Casas; quitar el párrafo de silos y las cuatro viñetas simétricas (pasar a una tabla o a dos frases desiguales).
4. **Estado del arte** — un eje ≠ una plantilla. Mezclar: un eje con cifra, otro con crítica, otro con “esto no entra (testing)”. Quitar el estribillo “Conclusión En”.
5. **Cap. 2** — el OG ya está en la matriz; no repetir el manual. Una frase del grupo: *diseñar cómo se calcula el score; no construirlo aún*.
6. **Relectura en voz alta** Alex ↔ Jack (como `REVISION_ORAL_ALEX_JACK.md`) **antes** del segundo Turnitin.

Meta práctica: no “0 % IA”. Meta: prosa que el grupo pueda **decir en la defensa** sin leer.

---

**Pasada 6 nov 2026:** reescritos a mano resumen/abstract, §1.1–§1.3, objeto, justificación, Cap. 2 (apertura), E1–E6, brecha, §4.1 y Plan v2 §1 / §3.7 / §7. Cifras y citas no se tocaron. Siguiente: recompilar PDF y **segundo Turnitin**.

---

## Criterio de salida

- [ ] Resumen/Abstract reescritos a mano (no parafraseador)
- [ ] Cap. 1 sin “Esta sección…” en cada apertura
- [ ] E1–E6 sin el mismo cierre
- [ ] Plan v2 §1 / §3.7 / §7 alineados al mismo tono
- [ ] Segundo Turnitin **después** de un capítulo entero, no de tres frases

*Grupo 10 · revisión de pares Turnitin IA · 6 nov 2026.*
