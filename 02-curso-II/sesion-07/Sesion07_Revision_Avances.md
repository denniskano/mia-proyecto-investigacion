---
title: "Sesión 7 — Revisión de avances"
author: "Grupo 10 · Alex Mancilla Antay · Dennis Jack Paitan Cano"
subtitle: "Trello · primeros resultados · métricas · revistas"
lang: es
---

# Sesión 7 — Revisión de avances

**Grupo 10** · Alex Mancilla Antay · Dennis Jack Paitan Cano  
**Programa:** Maestría en Inteligencia Artificial · UNI · MIA 403  
**Objeto de la tesis:** contratos **OpenAPI bancarios** frente a Service Domains BIAN.  
**Piloto:** Open Finance Brasil × 3 SD BIAN v14.  
**Lámina del aula:** `image.png` (salas de revisión).

**Frase de ancla:** la tesis mide OpenAPI bancario ↔ BIAN; OFB es el piloto.  
**Frase oral:** parser al 100 % **no** implica AlignmentScore Alto.

---

## 0. Encaje

Esta sesión abre **salas** para revisar avances. No sustituye el matching de la semana 8. Producto sílabo en puerta: **P4** (semanas 8–9).

| Punto de la lámina | Dónde se responde |
|--------------------|-------------------|
| Plan de 12 semanas en Trello | §1 · `../plan-tesis-v2/cronograma-sprints.md` |
| Primeros resultados en cuadernos | §2 · `cuaderno-pruebas.md` |
| Métricas y criterios de éxito | §3 |
| Dos revistas para el artículo | §4 |

---

## 1. Plan de trabajo del ciclo (12 semanas) — Trello

El ciclo empírico de 12 semanas se **superpone** a las semanas 5–16 del sílabo. S1–S4 de ese ciclo ya ocurrieron en la Sesión 5 (pares + parser + EDA).

**Tablero:** `Backlog` → `Semana actual` → `En curso (WIP=2)` → `Revisión pareja` → `Hecho` → `Bloqueado`  
**Etiquetas:** `P1`–`P7` · `OE1`–`OE4` · `OFB` · `BIAN` · `defensa`

### 1.1 Las 12 semanas empíricas

| Sem. ciclo | Sem. sílabo | Tarjeta | Estado |
|------------|-------------|---------|--------|
| S1–S2 | 5 | Pares I1–I6 (n = 7) | **Hecho** |
| S3–S4 | 5 | Parser OpenAPI 3.x | **Hecho** |
| S5–S6 | 5–6 | EDA + revisión del método | **Hecho** |
| **S7** | **7** | Protocolo congelado + este cuaderno | **Esta sesión** |
| S8 | 8 | P4: scores v0 de I1 e I4 | Pendiente |
| S9 | 9 | Defensa intermedia | Pendiente |
| S10 | 10 | E de las 7 instancias | Pendiente |
| S11 | 11 | S + C + AlignmentScore (7) | Pendiente |
| S12 | 12–16 | P5–P7 discusión y borrador | Pendiente |

### 1.2 Tarjetas permanentes (no borrar)

- `LEAKAGE` — no copiar CR/BQ a OFB; no puntuar BIAN↔BIAN.
- `VERSIONES` — accounts 2.4.2, payments 4.0.0, BIAN 14.0.0.
- `PARES` — solo I1–I6 reciben AlignmentScore.
- `SIN-ML` — no etiquetar Alta/Media/Baja a mano.

### 1.3 Dueños

| Quién | Tarjetas |
|-------|----------|
| Alex | Cap. I, exposición, validez de propósito, discusión (P5) |
| Jack | Dataset, parser, protocolo, matching, resultados |
| Ambos | P4, defensas 9 y 16, Turnitin |

Detalle de las 16 semanas del sílabo: `../plan-tesis-v2/cronograma-sprints.md`.

---

## 2. Primeros resultados (cuaderno)

Fuente: `cuaderno-pruebas.md` + `inventario.json`. Son pruebas de **extracción y calidad**, no de AlignmentScore.

### 2.1 Lo que ya se midió

| Indicador | Valor | Lectura |
|-----------|-------|---------|
| Contratos parseados | 41 (38 OFB + 3 BIAN) | OE1 ejecutable |
| Operaciones | 235 (160 + 75) | Inventario cerrado |
| Propiedades / corpus | 6 746 / 10 906 | Listo para matching |
| GET en OFB | 130 / 160 | REST de consulta |
| PUT en BIAN | 36 / 75 | Control / Update |
| Props sin *description* | 61,9 % | S cae sobre el nombre (BIAN 90,4 %) |
| BIAN summary = description | 75 / 75 | Una copia |
| I1 accounts | 6 GET vs 1 CR + 9 BQ | C de I1 será baja |

### 2.2 Hipótesis tocada

**H1** (normalización habilita S/E/C): **soportada a nivel de extracción**. H2–H4 esperan I1 e I4.

### 2.3 Lo que el cuaderno *no* muestra aún

Scores S, E, C ni AlignmentScore. Eso es la **próxima** entrada (semana 8): I1 e I4 v0.

---

## 3. Métricas y criterios de éxito

Las métricas son las del artefacto, no accuracy de un clasificador.

### 3.1 Selección (adecuadas a la tarea)

| Métrica | Pregunta que responde | Por qué entra |
|---------|----------------------|---------------|
| Completitud OE1 | ¿El parser recuperó el YAML? | Condición de reproducibilidad |
| StructuralScore E | ¿La jerarquía REST refleja el SD? | P1 / H2 |
| SemanticScore S | ¿Los conceptos significan lo mismo? | P2 / H3 |
| CoverageScore C | ¿Cuánto del SD cubre el contrato? | Insumo de P3/P4 |
| AlignmentScore | ¿Cuánto se alinea la instancia? | **VD** · P4 / H4 |
| Nivel | ¿Es interpretable? | Umbrales fijos, no ML |

No se usan: F1 supervisado, encuestas, latencia runtime, “número de PUT iguales”.

### 3.2 Cómo se calculan e interpretan

**Unidad:** instancia `contrato OFB × SD BIAN` (p. ej. I1 = accounts 2.4.2 × SavingsAccount 14.0.0).

```
E  = (Σ e_pair + 0·ops_sin_par) / n_ops_OFB
S  = promedio de similitud de los pares oficiales de E
C  = (CR+BQ con >= 1 par) / (CR+BQ del SD)
AlignmentScore = (S + E + C) / 3     # oficial; sensibilidad aparte
```

| AlignmentScore | Nivel | Cómo se lee |
|----------------|-------|-------------|
| ≥ 0,80 | Alta | El contrato cubre el SD de forma usable |
| 0,60–0,79 | Media | Alineación parcial; tipología a declarar |
| 0,40–0,59 | Baja | Desalineación dominante (p. ej. GET vs CR/BQ) |
| < 0,40 | Nula | Casi sin correspondencia defendible |

**Interpretación que ya adelanta el EDA:** I1 tiende a **Baja/Nula en C** (6 GET vs 10 conceptos BIAN). Eso es hallazgo.

Baseline semana 8: E por Jaccard/path/HTTP; S léxico/TF-IDF. Semana 11: S con embeddings. Detalle: `../plan-tesis-v2/protocolo-empirico.md`.

### 3.3 Criterios verificables de éxito

| Hito | Criterio (sí / no) | Evidencia |
|------|--------------------|-----------|
| Hoy (S7) | 41 YAML parseados; cuaderno con EDA; protocolo v1 en git | `inventario.json` · este folder |
| Semana 8 (P4) | OE1 firmado **y** I1 e I4 con S, E, C, AlignmentScore v0 | `scores.json` de I1 e I4 |
| Semana 9 | Defensa 8–10 min con EDA + 2 instancias | Slides del cronograma |
| Semana 11 | Las **7** instancias con S/E/C + sensibilidad de pesos | `resumen_instancias.csv` |
| Semana 12 (P5) | Discusión: tipologías, literatura, limitaciones | Capítulo |
| Semana 16 (P7) | Borrador v2 + repo; piloto OFB **no** se vende como toda la tesis | PDF + git |

Un criterio **falla** si: se reporta BIAN↔BIAN como banco; se inventa un SD para loans; no hay commit de la corrida.

---

## 4. Dos revistas para el artículo

Candidatas ya fijadas en el Plan v2 §9. Se envía **después** de tener scores (insumo P5), no esta semana.

| # | Revista | Por qué encaja | Qué enviaría el grupo |
|---|---------|----------------|------------------------|
| 1 | *[Journal of Web Semantics](https://www.sciencedirect.com/journal/journal-of-web-semantics)* (Elsevier) | Schema/ontology matching, servicios semánticos, alineación de especificaciones | AlignmentScore sobre contratos OpenAPI × BIAN; tipologías de desalineación |
| 2 | *[Semantic Web Journal](https://www.semantic-web-journal.net/)* (IOS Press, open access) | Web semántica aplicada, ontologías, reproducibilidad | Piloto OFB público + procedimiento S/E/C reproducible |

**No son candidatas de primer envío:** revistas de *fuzzing* o seguridad de APIs (el objeto no es vulnerabilidades) ni revistas solo de open banking regulatorio (el objeto no es OFB).

Alcance del paper: procedimiento + evidencia del piloto. Limitación obligatoria: 3 SD y un estándar de industria, no un banco peruano.

---

## 5. Qué pedimos en la sala

1. El Trello de 12 semanas es coherente con el sílabo (P4 en semana 8).
2. El cuaderno de pruebas (OE1 + EDA) cuenta como **primer resultado**, no como score final.
3. Las métricas S/E/C/AlignmentScore son las adecuadas; no se pide un clasificador.
4. Las dos revistas quedan nominadas; el envío espera a P5.

---

## Referencias internas

| Documento | Uso |
|-----------|-----|
| `image.png` | Lámina oficial |
| `cuaderno-pruebas.md` | Primeras pruebas |
| `../plan-tesis-v2/cronograma-sprints.md` | Trello 16 semanas |
| `../plan-tesis-v2/protocolo-empirico.md` | Cálculo de S/E/C |
| `../sesion-05/` | EDA y dataset |
| `../sesion-06/` | Revisión del método |

*Grupo 10 · Sesión 7 · revisión de avances · objeto OpenAPI bancario · piloto OFB · octubre 2026.*
