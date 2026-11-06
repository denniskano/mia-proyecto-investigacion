---
title: "Sesión 5 — Operacionalización, instrumentos y EDA del piloto OFB"
author: "Grupo 10 · Alex Mancilla Antay · Dennis Jack Paitan Cano"
subtitle: "Objeto: OpenAPI bancario ↔ BIAN · Piloto: Open Finance Brasil"
lang: es
---

# Sesión 5 — Operacionalización e instrumentos · EDA del piloto OFB

**Grupo 10** · Alex Mancilla Antay · Dennis Jack Paitan Cano  
**Programa:** Maestría en Inteligencia Artificial · UNI · MIA 403  
**Objeto de la tesis:** contratos **OpenAPI bancarios** frente a Service Domains BIAN.  
**Piloto de esta sesión:** catálogo **Open Finance Brasil (OFB)** + tres SD BIAN v14.  
**Dataset:** `../piloto/` (`fuentes/ofb/` + `fuentes/bian/`).

Este documento **no sustituye** el plan LaTeX ni el Plan v2. Cierra la operacionalización y el EDA **antes** del matching OE2–OE4.

---

## 0. Encaje en el ciclo

| Bloque | Actividad | Estado |
|--------|-----------|--------|
| S1–S2 | Pares contrato × SD | **Hecho en el piloto:** OFB × 3 SD BIAN |
| S3–S4 | Parser OpenAPI 3.x | **Hecho** (`procesar_openapi.py`) |
| **S5–S6** | Limpieza, normalización, EDA | **Esta sesión** |
| S7–S8 | Matching E y S | Pendiente |
| S9–S10 | C + AlignmentScore | Pendiente |
| S11–S12 | Validación y artículo | Pendiente |

**Frase de ancla:** el objeto de la tesis no es OFB. OFB es la **muestra** con la que se ejecuta el procedimiento.  
**Frase oral:** parser al 100 % **no** implica AlignmentScore Alto.

---

## Parte A. Operacionalización e instrumentos

### A.1 Variables

**Base de medición (OG):** instancia `contrato OpenAPI bancario × Service Domain BIAN`.  
**En el piloto:** p. ej. `OFB_accounts_2.4.2 × SavingsAccount_14.0.0`.

**Fórmula:** AlignmentScore = αS + βE + γC, α+β+γ=1. Línea base 1/3.  
**Clasificación (§1.4):** Alta ≥ 0,80 · Media 0,60–0,79 · Baja 0,40–0,59 · Nula < 0,40.

| Constructo | Definición conceptual | Definición operacional | Escala |
|------------|----------------------|------------------------|--------|
| **S** SemanticScore | ¿Los conceptos significan lo mismo? | Similitud (léxica o embeddings) sobre corpus emparejado | [0, 1] |
| **E** StructuralScore | ¿La jerarquía REST refleja el SD? | Matriz de pares + media (ops sin par aportan 0) | [0, 1] |
| **C** CoverageScore | ¿Cuánto del SD cubre el contrato? | Conceptos BIAN (tags CR + BQ, sin doble conteo) con ≥ 1 par | [0, 1] |
| **AlignmentScore** | Alineación global | αS+βE+γC — **VD del artefacto** | [0, 1] |
| **Clasificación** | Nivel interpretable | Umbrales fijos | Nominal 4 |
| Completitud OE1 | ¿El parser recuperó el YAML? | Extraídos / esperados | Ratio |

**Factores:** esquema intermedio (tabular); estrategia de matching; técnica semántica; pesos.  
**No es variable:** tráfico runtime, encuestas, etiquetas de ML supervisado.

Hipótesis (Cap. 2): H1 normalización habilita S/E/C; H2 schema matching produce E; H3 similitud produce S; H4 la agregación es clasificable.

### A.2 Fuentes e instrumentos

| Elemento | Tesis | Piloto (esta sesión) |
|----------|-------|----------------------|
| Objeto | Contrato OpenAPI **bancario** | No cambia |
| Muestra | Contratos bancarios parseables | **38 APIs OFB** (última estable) |
| Referencia | Service Domain BIAN | SavingsAccount, CurrentAccount, PaymentOrderInitiation v14 |
| Unidad | endpoint/schema ↔ Behavior/BO/BQ | Igual; matching aún no calculado |
| Instancia | `{fuente}_{api}_{versión} × {sd}_{versión}` | p. ej. `OFB_payments_4.0.0 × PaymentOrderInitiation_14.0.0` |
| Instrumento OE1 | Parser OpenAPI 3.x | `procesar_openapi.py` |

**Fuentes oficiales**

- OFB: <https://github.com/OpenBanking-Brasil/openapi> (`swagger-apis`)
- BIAN: <https://github.com/bian-official/public> (`release14.0.0/semantic-apis`)

Criterios de inclusión: OpenAPI 3.x parseable; ≥ 1 operación y esquema; BIAN legible; sin PII (Ley 29733). OFB y BIAN son públicos.

### A.3 OE ↔ indicadores

| OE | Indicador | Evidencia | Estado |
|----|-----------|-----------|--------|
| Fase 1 | Definición S/E/C, fórmula, umbrales | Plan Guía 1 + Plan v2 | Cumplido |
| **OE1** | Completitud; CSV normalizados | `resultado/inventario.json` | **41 contratos parseados**; falta firmar completitud por YAML |
| **OE2** | StructuralScore E | Matriz de pares I1–I6 | Pendiente |
| **OE3** | SemanticScore S | Matriz de similitud | Pendiente |
| **OE4** | C + AlignmentScore + nivel | Informe por instancia | Pendiente |

---

## Parte B. EDA del piloto OFB × BIAN

Corpus actual: **3 SD BIAN + 38 APIs OFB**. El recorte de 12 operaciones no se usa.

### B.1 Inventario

| Lado | Rol | Contratos | Operaciones |
|------|-----|-----------|-------------|
| Open Finance Brasil | **Muestra / piloto** | 38 | 160 |
| BIAN v14 | **Referencia** | 3 | 75 |
| **Total parseado** | | **41** | **235** |

Propiedades: 6 746. Corpus: 10 906 fragmentos.

**Referencia BIAN**

| SD | Ops |
|----|-----|
| SavingsAccount 14.0.0 | 34 |
| CurrentAccount 14.0.0 | 34 |
| PaymentOrderInitiation 14.0.0 | 7 |

**Pares declarados (muestra de scores; n = 7 instancias)**

| ID | OFB | BIAN |
|----|-----|------|
| I1 | accounts 2.4.2 | SavingsAccount |
| I2 | accounts 2.4.2 | CurrentAccount |
| I3a / I3b | opendata-accounts 1.0.1 | SavingsAccount / CurrentAccount |
| I4 | payments 4.0.0 | PaymentOrderInitiation |
| I5 | automatic-payments 2.0.0 | PaymentOrderInitiation |
| I6 | enrollments 2.1.0 | PaymentOrderInitiation |

Las otras **33** APIs OFB (loans, credit-cards, financings, consents, …) entran en el inventario OE1. No reciben AlignmentScore mientras no haya SD BIAN emparejado.

Catálogo OFB completo: `../piloto/README.md`.

### B.2 Distribuciones

**Métodos HTTP**

| | GET | POST | PUT | PATCH | DELETE | Total |
|--|-----|------|-----|-------|--------|-------|
| OFB | 130 | 22 | 0 | 7 | 1 | 160 |
| BIAN | 22 | 17 | 36 | 0 | 0 | 75 |
| **Total** | **152** | **39** | **36** | **7** | **1** | **235** |

OFB es REST de **consulta**. BIAN concentra **PUT** (Update/Control/Execute). E no puede exigir el mismo verbo.

**Tags (solo BIAN):** 64 BQ + 11 CR. OFB **no** trae tags CR/BQ: imputarlos sería *leakage*.

**Corpus:** property 9 314 · schema 1 253 · operation 339. Prefijos `InCR`/`ReBQ` limpios. BIAN: *summary = description* en **75/75** operaciones (no contar el texto dos veces).

### B.3 Faltantes e inconsistencias

| Fenómeno | Magnitud | Lectura |
|----------|----------|---------|
| Propiedades sin *description* | **61,9 %** del consolidado (BIAN 90,4 %; OFB 38,1 %) | S de atributos BIAN cae sobre el **nombre** |
| BIAN summary = description | 75 / 75 | Una copia en el corpus |
| `$ref` anidados | resueltos por el parser actual | OE1 ya no está bloqueado por requestBody anidado |
| CSV BOM UTF-8 | todos los CSV | Abrir con `utf-8-sig` |
| Loans / cards / financings OFB | 3 familias sin SD en el zip | *Gap* de referencia, no de objeto |

No hay `path` ni `operationId` duplicados en el consolidado de operaciones.

### B.4 Variable objetivo

**VD:** AlignmentScore + {Alta, Media, Baja, Nula}.

Aún **no hay** distribución de clases: no se calculó S/E/C. Los conteos OFB / BQ / CR son **proxy estructural**, no la VD.

Cuando existan scores en I1–I6, los niveles se asignan **después** de los umbrales, no como etiqueta de entrenamiento.

### B.5 Sesgos y *leakage*

| Riesgo | Mitigación |
|--------|------------|
| Evaluar BIAN contra sí mismo | Prohibido como resultado Banco–BIAN |
| Copiar tags CR/BQ a OFB | No imputar |
| Usar el nombre de un `$ref` BIAN como evidencia OFB | No |
| Calibrar α,β,γ en los mismos pares del reporte | Separar calibración y reporte |
| Tratar OFB como si fuera el objeto de la tesis | OFB = piloto; objeto = OpenAPI bancario |
| C global sobre las 38 APIs | C se calcula **por instancia** (I1–I6) |

---

## 5. Qué sigue

| Prioridad | Acción |
|-----------|--------|
| Hecho | 38 APIs OFB + 3 SD BIAN parseados |
| P1 | Firmar completitud OE1 por contrato |
| P2 | Matching I1 e I4 (semana 8); resto I2–I6 (semana 10–11) |
| P2 | No presentar AlignmentScore de autoalineación BIAN↔BIAN |

---

## 6. Checklist

- [x] Conceptual y operacional de S, E, C, AlignmentScore
- [x] Fuentes: objeto = OpenAPI bancario; piloto = OFB
- [x] Tabla OE ↔ indicador
- [x] EDA sobre 41 contratos (38 OFB + 3 BIAN)
- [x] Faltantes reales (61,9 % props sin description)
- [x] Leakage y distinción objeto / muestra
- [ ] Completitud OE1 firmada por YAML
- [ ] Matching y AlignmentScore (S7–S10)

## Referencias

| Documento | Uso |
|-----------|-----|
| `../../01-curso-I/plan-tesis/latex/` | Guía 1 |
| `../plan-tesis-v2/PLAN_TESIS_V2.pdf` | Plan v2 (MIA 403) |
| `../piloto/` | Corpus OFB + BIAN |
| `../piloto/README.md` | Lista de 38 APIs |

*Grupo 10 · Sesión 5 · piloto Open Finance Brasil · objeto OpenAPI bancario · octubre 2026.*
