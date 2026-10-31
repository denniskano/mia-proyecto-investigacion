---
title: "Plan de tesis v2 — Alineación OpenAPI bancario ↔ BIAN (piloto OFB)"
author: "Grupo 10 · Alex Mancilla Antay · Jack Paitan Cano"
subtitle: "MIA 403 · Proyecto de Investigación II · 2026-2"
lang: es
---

# Plan de tesis v2

**Título (tesis):** Alineación entre contratos OpenAPI bancarios y modelos de referencia BIAN, mediante análisis estructural y similitud semántica.  
**Piloto (MIA 403):** catálogo **Open Finance Brasil (OFB)** × tres Service Domains BIAN v14. OFB no sustituye el objeto: es la **muestra empírica** con la que se ejecuta el procedimiento.

**Autores:** Alex Mancilla Antay · Jack Paitan Cano  
**Programa:** Maestría en Inteligencia Artificial · UNI · MIA 403 (2026-2)  
**Prerrequisito:** Plan Guía 1 (`../../01-curso-I/plan-tesis/latex/`, Grupo 10)  
**Producto de curso:** Plan de Tesis para trámite + protocolo empírico + evidencia piloto (P4, semanas 8–9)

---

## 1. Continuidad Guía 1 → Guía 2

La Guía 1 documentó el **diseño** del modelo S/E/C → AlignmentScore y dejó fuera la construcción del artefacto y la experimentación a escala (§1.6 del plan v1). El sílabo MIA 403 exige ahora **ejecutar** el procedimiento, producir evidencia y llegar a un **borrador integral de tesis**.

| Dimensión | Guía 1 (MIA 303) | Guía 2 / Plan v2 (MIA 403) |
|-----------|------------------|----------------------------|
| Naturaleza | Diseño del procedimiento | Diseño **+** piloto **+** ejecución empírica |
| Objeto de estudio | Contrato OpenAPI **bancario** | El **mismo** (no se estrecha a OFB) |
| Referencia | Service Domain BIAN | Service Domain BIAN v14 (tres SD del piloto) |
| Muestra / piloto | Ejemplos ilustrativos (Anexo F) | 38 APIs **OFB** + 3 SD BIAN |
| VD del artefacto | AlignmentScore + clasificación (definida) | AlignmentScore + clasificación (**calculada** en el piloto OFB × BIAN) |
| Software | Fuera de alcance | Parser OE1 hecho; matching OE2–OE4 a construir |

**Qué se hereda sin reescribir:** título, objeto (OpenAPI bancario), planteamiento tecnológico, P1–P4, modelo S/E/C, umbrales, tipologías, estado del arte (14 papers), Anexo C/D, distinción objeto / unidad / producto.

**Qué cambia:** se **ejecuta** el procedimiento sobre un piloto. La muestra de este curso es OFB (estándar multi-institución de open finance brasileño, no el YAML de un banco emisor). En MIA 403 no se añaden Nordea, CommBank ni Open Banking UK; eso no convierte a OFB en el objeto de la tesis. Un contrato de otro banco quedaría dentro del objeto y fuera de **este** piloto.

---

## 2. Diagnóstico (semana 1)

### 2.1 Lo que ya está cerrado

- Problema tecnológico, preguntas P1–P4, OG y OE1–OE4 (diseño).
- Operacionalización conceptual (Anexo D; Sesión 5).
- Matriz de consistencia v2 institucional (8 columnas).
- Parser OpenAPI 3.x (`procesar_openapi.py`) sobre el piloto.
- EDA del piloto: origen, faltantes, sesgos, *leakage* (Sesión 5).

### 2.2 Lo que falta para el borrador de tesis

| Brecha | Semana sílabo | Acción |
|--------|---------------|--------|
| Capítulo I: objeto intacto + piloto OFB | 2 | Este plan, §3–4 |
| Matriz de antecedentes actualizada | 3 | Reusar Anexo B; añadir fila OFB vs. open banking |
| Capítulo II (modelo conceptual OFB × BIAN) | 4 | §5 |
| Matriz consistencia + operacionalización OFB | 5 | `matriz-consistencia-ofb.md` |
| Capítulo III ejecutable | 6 | §7 |
| Protocolo, baselines, métricas | 7 | `protocolo-empirico.md` |
| Matching S/E/C y AlignmentScore | 8–11 | OE2–OE4 |
| Resultados, discusión, borrador | 12–16 | Fuera de este documento (se ejecutan después) |

### 2.3 Riesgos actuales

1. **Asimetría de inventario:** 160 operaciones OFB vs. 75 BIAN (solo 3 SD). No se puede pretender C global sobre las 38 APIs OFB.
2. **Pares naturales limitados:** accounts ↔ Savings/Current; payments ↔ PaymentOrderInitiation. Loans, credit-cards y financings OFB **no** tienen SD BIAN en el piloto.
3. **Piloto ≠ población:** OFB no es un banco peruano ni agota los OpenAPI bancarios; la validez externa del piloto se declara en limitaciones.
4. **BIAN summary = description** (75/75): S se apoyará en nombres y en el texto OFB.
5. **No ML supervisado:** no hay etiquetas Alta/Media/Baja a priori; la clasificación es por umbrales del AlignmentScore.

---

## 3. Planteamiento (Capítulo I reencuadrado)

### 3.1 Problema de investigación

¿En qué medida y bajo qué tipologías se desalinea un **contrato OpenAPI bancario** respecto de un Service Domain BIAN emparejado, y cómo cuantificarlo de forma reproducible con AlignmentScore = α·S + β·E + γ·C?

La primera medición empírica (piloto MIA 403) se hace sobre contratos **Open Finance Brasil**.

### 3.2 Preguntas específicas (se mantienen)

- **P1:** ¿Qué correspondencias estructurales hay entre paths/operations/schemas del contrato bancario y Behavior/Business Object BIAN?
- **P2:** ¿Qué similitud semántica hay entre términos del contrato y conceptos BIAN?
- **P3:** ¿Qué tipologías de desalineación predominan (estructural, semántica, de modelado, REST)?
- **P4:** ¿La agregación S, E y C produce un AlignmentScore interpretable por instancia `contrato_bancario × SD_BIAN`?

### 3.3 Objeto, unidad y producto

| Concepto | Tesis (se mantiene) | Piloto MIA 403 |
|----------|---------------------|----------------|
| **Objeto de estudio** | Contrato OpenAPI **bancario** (artefacto documental) | No cambia |
| **Referencia** | Service Domain BIAN | Tres SD v14 del zip |
| **Muestra** | Contratos bancarios parseables (OpenAPI 3.x) | 38 APIs OFB (p. ej. `accounts` 2.4.2) |
| **Unidad de análisis** | Par elemento contrato ↔ Behavior/BO/BQ | Igual, sobre YAML OFB |
| **Instancia de medición** | `{fuente}_{api}_{versión} × {sd-bian}_{versión}` | p. ej. `OFB_accounts_2.4.2 × SavingsAccount_14.0.0` |
| **Producto** | S, E, C, AlignmentScore y clasificación | Calculado en las 7 instancias I1–I6 |

OFB es un **estándar de industria** (open finance brasileño), no el YAML de Itaú ni de un banco peruano. Entra como **corpus del piloto**, no como redefinición del objeto.

### 3.4 Objetivo general (técnico, ahora verificable)

**Calcular**, sobre instancias `contrato OpenAPI bancario × Service Domain BIAN`, el AlignmentScore en [0, 1] y la clasificación (Alta / Media / Baja / Nula), mediante el procedimiento S/E/C documentado en Guía 1. En este curso la verificación empírica se hace de forma reproducible sobre el **piloto OFB**.

### 3.5 Objetivos específicos (transformaciones a ejecutar)

| ID | Transformación | Entrada | Salida |
|----|----------------|---------|--------|
| **OE1** | Adquirir y normalizar contrato bancario + BIAN | YAML oficiales versionados (piloto: OFB + 3 SD) | Representaciones CSV (hecho en el piloto) + informe de completitud |
| **OE2** | Emparejar estructuras | Representaciones OE1 de **pares declarados** | Matriz de correspondencias + StructuralScore E |
| **OE3** | Calcular similitud semántica | Corpus OE1 de los mismos pares | Matriz semántica + SemanticScore S |
| **OE4** | Integrar y clasificar | E, S, inventario BIAN del SD | C, AlignmentScore, nivel, tipologías |

### 3.6 Hipótesis

- **H1:** La normalización del contrato OpenAPI bancario y de BIAN a un esquema intermedio común permite calcular S, E y C de forma sistemática (piloto OE1 sobre OFB: **soportada** a nivel de extracción).
- **H2:** El schema matching produce un E que distingue correspondencia REST ↔ CR/BQ.
- **H3:** La similitud semántica produce un S que discrimina alineación de desalineación de modelado (p. ej. *account* vs. *SavingsAccountFacility*).
- **H4:** α·S + β·E + γ·C (α=β=γ=1/3 como línea base) produce un AlignmentScore clasificable por los umbrales §1.4.

### 3.7 Justificación

Sin un score reproducible, la coherencia entre un OpenAPI bancario y BIAN se revisa a mano. El plan v2 aporta (i) un corpus piloto público y legal (OFB, sin PII), (ii) el procedimiento ya operacionalizado y (iii) la primera evidencia empírica, no solo los ejemplos ilustrativos de Guía 1.

### 3.8 Alcance y delimitaciones

**Dentro de la tesis (objeto)**

- Contratos OpenAPI 3.x del sector bancario, contrastados con Service Domains BIAN.
- El procedimiento S/E/C y la VD AlignmentScore + clasificación.

**Dentro del piloto MIA 403 (muestra)**

- 38 APIs OFB (última estable) como **universo del piloto**.
- Tres SD BIAN v14 ya adquiridos.
- Cálculo de S, E, C y AlignmentScore en los **pares declarados** (§4.1; n = 7 instancias).
- Prototipo Python reproducible (parser + matching + agregación).

**Fuera de este piloto (siguen dentro del objeto si se incorporan después)**

- YAML de un banco emisor concreto (p. ej. Itaú, cores peruanos) u otros estándares (Open Banking UK, Berlin Group).
- El resto del catálogo BIAN.

**Fuera de la tesis**

- Despliegue productivo, runtime, seguridad ofensiva.
- Entrenamiento supervisado de un clasificador de niveles.
- Autoalineación (puntuar el mismo YAML BIAN en ambos lados).

---

## 4. Universo del piloto y muestra (Sesión 5)

Fuente: `../sesion-05/data/piloto_ofb_bian/`.

| Lado | Contratos | Operaciones |
|------|-----------|-------------|
| OFB (muestra / piloto) | 38 | 160 |
| BIAN (referencia) | 3 | 75 |
| **Total parseado** | **41** | **235** |

Propiedades extraídas: 6 746. Corpus: 10 906 fragmentos.

### 4.1 Pares declarados (muestra empírica)

| Instancia | OFB | BIAN | Justificación |
|-----------|-----|------|----------------|
| I1 | `accounts` 2.4.2 | SavingsAccount 14.0.0 | OFB cubre poupança / depósito |
| I2 | `accounts` 2.4.2 | CurrentAccount 14.0.0 | OFB cubre cuenta a la vista |
| I3a | `opendata-accounts` 1.0.1 | SavingsAccount 14.0.0 | Catálogo open data de cuentas (poupança) |
| I3b | `opendata-accounts` 1.0.1 | CurrentAccount 14.0.0 | Catálogo open data de cuentas (vista) |
| I4 | `payments` 4.0.0 | PaymentOrderInitiation 14.0.0 | Iniciación de pagos (Anexo F) |
| I5 | `automatic-payments` 2.0.0 | PaymentOrderInitiation 14.0.0 | Pagos recurrentes vs. order initiation |
| I6 | `enrollments` 2.1.0 | PaymentOrderInitiation 14.0.0 | Enrolamiento para iniciación |

Hay **siete** instancias de medición. I1–I6 nombra las familias de pares; I3 se desdobla en I3a e I3b. I1 e I2 (y I3a/I3b) comparten el mismo YAML OFB frente a dos referencias: los scores **no son independientes**. I4–I6 comparten el mismo SD BIAN.

Las demás **33** APIs OFB (38 − 5 YAML emparejados) entran en **OE1** (inventario y completitud) y en el mapa de *gap*, no en el AlignmentScore salvo ampliación futura de SD BIAN.

### 4.2 Hallazgos EDA que condicionan el método

- OFB es mayormente **GET** (130/160); BIAN concentra **PUT** (Update/Control/Execute). E no puede exigir el mismo estilo REST.
- OFB **no** usa tags CR/BQ: imputarlos sería *leakage*.
- BIAN: *summary = description* en 75/75. S no debe contar el mismo texto dos veces.
- 61,9 % de propiedades del consolidado sin description (BIAN 90,4 %; OFB 38,1 %): el matching de atributos BIAN cae sobre el **nombre**. (La cifra «88 %» de las diapositivas de Sesión 5 era incorrecta.)
- El recorte inicial (12 ops / 5 schemas genéricos) está archivado; no se usa para scores.

---

## 5. Modelo conceptual y variables

```
OFB OpenAPI  --OE1-->  repres. intermedia  --OE2-->  E
                       repres. intermedia  --OE3-->  S
                       inventario BIAN SD  --OE4-->  C
                              E, S, C      --OE4-->  AlignmentScore → {Alta, Media, Baja, Nula}
```

**Fórmula:** AlignmentScore = αS + βE + γC, α+β+γ=1. Línea base α=β=γ=1/3. Umbrales: Alta ≥ 0,80 · Media 0,60–0,79 · Baja 0,40–0,59 · Nula < 0,40.

| Constructo | Definición conceptual | Definición operacional | Escala |
|------------|----------------------|------------------------|--------|
| Completitud OE1 | ¿El parser recuperó el YAML? | extraídos / esperados por contrato | Ratio |
| E | Correspondencia estructural OFB ↔ BIAN | Promedio de pares alineados (nombre, ruta, HTTP, profundidad) | [0,1] |
| S | Equivalencia de significado | Similitud (embeddings + coseno o léxica) sobre corpus emparejado | [0,1] |
| C | Cobertura del SD | Conceptos BIAN del catálogo CR + BQ (sin doble conteo del CR como BO) con al menos un par OFB | [0,1] |
| AlignmentScore | Alineación global de la instancia | αS+βE+γC | [0,1] — **VD** |
| Clasificación | Nivel interpretable | Umbrales fijos | Nominal 4 |

**Factores:** esquema intermedio (tabular en el piloto); estrategia de matching; técnica semántica; pesos.

**Controles:** versión fija de cada YAML; parser fijo; umbrales fijos; no usar tags BIAN en el lado OFB.

---

## 6. Correspondencia OE ↔ indicador

| OE | Indicador | Evidencia | Estado |
|----|-----------|-----------|--------|
| OE1 | Completitud; CSV normalizados | `resultado/inventario.json`, consolidado | Piloto hecho; falta informe de completitud por contrato |
| OE2 | StructuralScore E | Matriz de pares I1–I6 | Pendiente |
| OE3 | SemanticScore S | Matriz de similitud I1–I6 | Pendiente |
| OE4 | C + AlignmentScore + nivel + tipologías | Informe por instancia | Pendiente |

Criterio oral: parser al 100 % **no** implica AlignmentScore Alto.

---

## 7. Diseño metodológico (Capítulo III)

- **Tipo:** investigación tecnológica / *design science*.
- **Enfoque:** cuantitativo sobre artefactos documentales (no encuestas).
- **No** es clasificación supervisada.
- **Población (tesis):** pares posibles contrato OpenAPI bancario × SD BIAN.
- **Muestra (piloto MIA 403):** siete instancias de medición sobre OFB (§4.1: I1, I2, I3a, I3b, I4, I5, I6).
- **Técnicas:** parsing OpenAPI 3.x; schema matching (Shvaiko y Euzenat, 2005); similitud semántica (embeddings/coseno o léxica); agregación lineal.
- **Instrumentos:** `procesar_openapi.py`; matrices CSV; script de matching (a construir); repositorio Git.
- **Ética:** solo YAML públicos; Ley 29733 no aplica (sin PII de clientes). Citar OFB y BIAN.

**Amenazas (actualizadas)**

- Interna: ambigüedad léxica *account* / *payment*; summary duplicado BIAN; I1/I2 e I3a/I3b no son independientes (mismo YAML OFB).
- Externa: el piloto OFB no cubre un banco peruano ni todo OpenAPI bancario; 3 SD no cubren loans/cards.
- Constructo: un score global puede ocultar un BQ crítico mal cubierto.
- Conclusión: no generalizar a “todo open banking” ni a “todo BIAN”.

---

## 8. Protocolo (resumen)

El detalle paso a paso está en `protocolo-empirico.md`.

1. Congelar versiones (inventario ya versionado).
2. Recalcular OE1 y firmar completitud.
3. Construir matrices de matching **solo** en I1–I6.
4. Baseline estructural: matching por igualdad de tokens normalizados (sin embeddings).
5. S v0 (semana 8): similitud léxica/TF-IDF. S v1 (semana 11): embeddings de frase sobre `normalized_text`; umbral fijo por corrida.
6. C: catálogo CR + BQ del SD BIAN de la instancia (sin doble conteo del CR).
7. AlignmentScore con pesos 1/3; sensibilidad α,β,γ.
8. Prohibido: reportar BIAN↔BIAN como resultado Banco–BIAN.
9. Bitácora Git + `inventario.json`.

**Criterios de éxito del piloto (examen parcial, semana 8)**

- OE1 reproducible sobre los 41 YAML.
- Al menos I1 e I4 con E, S, C y AlignmentScore calculados (aunque sean v0).
- Documento de amenazas y *leakage* (ya en Sesión 5).

---

## 9. Resultados esperados

- Tablas por instancia I1–I6: S, E, C, AlignmentScore, nivel.
- Informe de tipologías (Tabla 2 Guía 1).
- Análisis de sensibilidad de pesos.
- Discusión: OFB (REST de consulta) vs. BIAN (facility CR/BQ).
- Limitación explícita del catálogo OFB no emparejado.
- Insumo para artículo (revistas candidatas: *Journal of Web Semantics*; *Semantic Web Journal*).

---

## 10. Administración

| Rol | Responsabilidad v2 |
|-----|-------------------|
| Alex Mancilla | Cap. I reencuadre, exposición, validez de propósito |
| Jack Paitan | Dataset, parser, protocolo, matching, Cap. III–resultados |
| Ambos | Matriz, defensa semanas 9 y 16, Turnitin |

Presupuesto: software libre; sin cloud productivo. Tiempo: ~8–10 h/semana × 16 semanas.

Cronograma semanal: `cronograma-sprints.md`.

---

## 11. Trazabilidad sílabo MIA 403

| Producto sílabo | Semana | Cubierto en v2 |
|-----------------|--------|----------------|
| P1 Diagnóstico y hoja de ruta | 1 | §2 + `cronograma-sprints.md` |
| P2 Capítulo I + estado del arte | 3 | §3; estado del arte = Guía 1 Cap. 3 (a reargumentar) |
| P3 Marco + consistencia + método | 6 | §5–7 + `matriz-consistencia-ofb.md` |
| P4 Plan + protocolo | 8–9 | Este documento + `protocolo-empirico.md` |
| P5 Resultados y discusión avanzados | 12 | Ejecución semanas 10–12 |
| P6 Borrador integral v1 | 14 | Integración + Turnitin |
| P7 Borrador integral v2 + defensa | 16 | Cierre |

---

## Referencias internas

- Plan Guía 1: `../../01-curso-I/plan-tesis/latex/`
- Matriz consistencia v2 (Guía 1): `../../01-curso-I/plan-tesis/anexos/`
- Sesión 5: `../sesion-05/`
- Sílabo: `../material-oficial/silabo/MIA-403_Proyecto_de_Investigacion_II_Silabo_v_2.pdf`

*Grupo 10 · Plan de tesis v2 · octubre 2026 · objeto = OpenAPI bancario · referencia = BIAN · piloto = OFB.*
