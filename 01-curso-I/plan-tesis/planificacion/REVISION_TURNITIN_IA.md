# Revisión Turnitin — detección de IA (49% total)

**Contexto:** el docente reportó **2% similitud** (OK) y **49% texto con patrones de IA** (revisar).  
**Limitación:** no hay desglose por sección; se trabaja sobre el **documento completo** con prioridades por tipo de contenido.

> **Principio:** reescritura propia del equipo a partir de fichas, matrices, exposiciones PI-10/PI-11 y Anexo F.  
> **No usar:** parafraseadores automáticos ni «humanizadores» de IA.

---

## Meta realista

No existe un umbral oficial publicado por Turnitin. Objetivo práctico tras una pasada seria:

- Bajar el indicador de IA de forma visible en un **segundo envío**.
- Poder **defender oralmente** cada sección sin leer párrafos genéricos.

---

## Orden de trabajo (prioridad)

| Orden | Archivo LaTeX | Por qué |
|-------|---------------|---------|
| 1 | `frontmatter/resumen.tex` + `abstract.tex` | Pocas líneas, mucho peso relativo; suelen marcar alto |
| 2 | `cap01-planteamiento/01-introduccion.tex` | Definiciones enciclopédicas |
| 3 | `cap01-planteamiento/02-problematica.tex` | Mantener casos TSB/CMA; acortar generalidades |
| 4 | `cap01-planteamiento/03-planteamiento.tex` | Ya reestructurado PI-11; revisar tono |
| 5 | `cap02-objetivos/_cap02.tex` | Objetivo superior + OG: voz del grupo |
| 6 | `cap03-marco/01-antecedentes.tex` … `06-brecha.tex` | Un párrafo = una ficha leída |
| 7 | `cap03-marco/05-estado-arte.tex` | Mayor volumen narrativo |
| 8 | Cap. 4 metodología | ✅ Fase F · PI-11 |
| 9 | `cap05-administracion/` | Menor prioridad (tablas) |

---

## Checklist por párrafo (aplicar en cada revisión)

- [ ] ¿Puedo citar **una decisión del Grupo 9.2** (matriz, Anexo F, feedback docente)?
- [ ] ¿Hay al menos **un dato, tabla, figura o cita** anclada al proyecto?
- [ ] ¿Varío longitud de oraciones (cortas + largas)?
- [ ] ¿Evité encadenar «Sin embargo / Además / Por tanto / En este sentido»?
- [ ] ¿Lo escribí **después** de mirar la ficha o el paper, no el párrafo anterior del plan?
- [ ] ¿Alex y Jack **cruzaron** este bloque? (actualizar `REVISION_CRUZADA.md`)

---

## Fuentes obligatorias al reescribir

| Fuente | Uso |
|--------|-----|
| `fases/fase-0-bibliografia/fichas/*.md` | Estado del arte |
| `FEEDBACK_DOCENTE_PI10.md` / `PI11.md` | Planteamiento y niveles |
| `anexos/Matriz_Consistencia_Grupo9.2.xlsx` | Objetivos y fases |
| `datos-objeto-estudio/` + Anexo F | Ejemplos concretos |
| Transcripciones PI-10, PI-11 | Formulaciones usadas en exposición oral |

---

## División sugerida Alex ↔ Jack

| Integrante | Bloques |
|------------|---------|
| Alex | Cap. 1 §1.1–§1.3, Cap. 3 §3.1–§3.4 |
| Jack | Resumen/Abstract, Cap. 2, Cap. 3 §3.5–§3.6 |

Intercambiar archivos y releer en voz alta antes de recompilar PDF.

---

## Después de cada tanda

```bash
cd plan-tesis/latex && make pdf
```

Subir PDF actualizado a Turnitin **solo** cuando hayan reescrito un bloque entero (capítulo o frontmatter), no frases sueltas.

---

## Seguimiento

| Fecha | Acción | Responsable |
|-------|--------|-------------|
| 2026-07-02 | Guía + reescritura resumen/abstract/§1.1 | — |
| 2026-07-02 | **Revisión cruzada 2 agentes:** Cap. 1 (A) + Cap. 2–3 (B) | Ver `REVISION_CRUZADA_TURNITIN.md` |
| | Relectura oral Alex ↔ Jack | ✅ |
| | Segundo reporte Turnitin | ⏳ |
