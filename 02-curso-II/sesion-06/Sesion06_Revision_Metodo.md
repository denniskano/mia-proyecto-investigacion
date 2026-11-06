---
title: "Sesión 6 — Revisión del método (Capítulo III)"
author: "Grupo 10 · Alex Mancilla Antay · Dennis Jack Paitan Cano"
subtitle: "Objeto: OpenAPI bancario ↔ BIAN · Piloto: Open Finance Brasil"
lang: es
---

# Sesión 6 — Revisión del método

**Grupo 10** · Alex Mancilla Antay · Dennis Jack Paitan Cano  
**Programa:** Maestría en Inteligencia Artificial · UNI · MIA 403  
**Objeto de la tesis:** contratos **OpenAPI bancarios** frente a Service Domains BIAN.  
**Piloto:** catálogo **Open Finance Brasil (OFB)** × tres SD BIAN v14.  
**Lámina del aula:** `image.png` (cinco puntos de revisión).

Esta sesión **revisa** el Capítulo III. No calcula todavía AlignmentScore. La evidencia de viabilidad es el EDA y el parser de la Sesión 5.

**Frase de ancla:** el objeto no es OFB. OFB es la **muestra** con la que se ejecuta el procedimiento.  
**Frase oral:** parser al 100 % **no** implica AlignmentScore Alto.

---

## 0. Encaje en el ciclo

| Bloque | Actividad | Estado |
|--------|-----------|--------|
| S1–S4 | Pares + parser | Hecho (Sesión 5) |
| S5 | Operacionalización + EDA | Hecho |
| **S6** | Revisión de población, instrumentos, procedimiento y viabilidad | **Esta sesión** |
| S7 | Protocolo v1 + baseline estructural | Pendiente |
| S8–S9 | P4 + defensa (I1 e I4 con score v0) | Pendiente |
| S10–S16 | Siete instancias, discusión, borrador | Pendiente |

Producto sílabo asociado: **P3** (marco + consistencia + método, semana 6).

---

## 1. Población, muestra y criterios de selección

### 1.1 Tres capas (no confundir)

| Capa | Qué es | Qué no es |
|------|--------|-----------|
| **Población (tesis)** | Pares posibles *contrato OpenAPI bancario × Service Domain BIAN* | Un estándar de un país |
| **Universo del piloto** | 38 APIs OFB (última estable) + 3 SD BIAN v14 | Todo el catálogo BIAN |
| **Muestra empírica** | 7 instancias de medición I1–I6 | Las otras 33 APIs OFB (solo inventario OE1) |

OFB es un **estándar de industria**, no el YAML de un banco emisor. Entra como corpus del piloto, no como redefinición del objeto.

### 1.2 Fuentes

| Lado | Fuente | Criterio de versión |
|------|--------|---------------------|
| Muestra | [OpenBanking-Brasil/openapi](https://github.com/OpenBanking-Brasil/openapi) · `swagger-apis` | Última **estable** por API (solo `payroll-credit-portability` es beta) |
| Referencia | [bian-official/public](https://github.com/bian-official/public) · release 14.0.0 | YAML completo del SD (no el recorte de 12 operaciones) |

Ruta: `../piloto/` (`fuentes/ofb/` + `fuentes/bian/`).

### 1.3 Criterios de inclusión / exclusión

**Incluye**

- OpenAPI 3.x parseable (YAML/JSON).
- ≥ 1 operación y ≥ 1 esquema.
- BIAN con Control Record y Behavior Qualifiers legibles.
- Sin PII de clientes (Ley 29733 no aplica).
- Par **natural** para AlignmentScore: accounts / opendata-accounts / payments / automatic-payments / enrollments frente a SavingsAccount, CurrentAccount o PaymentOrderInitiation.

**Excluye de este piloto (siguen dentro del objeto de la tesis)**

- YAML de un banco emisor (Itaú, cores peruanos) u otros estándares (Open Banking UK, Berlin Group).
- Nordea / CommBank como emisores.
- Inventar un SD BIAN para loans, credit-cards o financings.
- El recorte inicial de 12 operaciones (ya archivado).

### 1.4 Universo parseado y muestra de scores

| Lado | Contratos | Operaciones |
|------|-----------|-------------|
| OFB (universo del piloto) | 38 | 160 |
| BIAN (referencia) | 3 | 75 |
| **Total parseado** | **41** | **235** |

Propiedades: 6 746. Corpus: 10 906 fragmentos.

| ID | OFB | BIAN | Por qué entra |
|----|-----|------|----------------|
| I1 | accounts 2.4.2 | SavingsAccount 14.0.0 | Poupança / depósito |
| I2 | accounts 2.4.2 | CurrentAccount 14.0.0 | Cuenta a la vista |
| I3a | opendata-accounts 1.0.1 | SavingsAccount 14.0.0 | Open data de cuentas |
| I3b | opendata-accounts 1.0.1 | CurrentAccount 14.0.0 | Open data de cuentas |
| I4 | payments 4.0.0 | PaymentOrderInitiation 14.0.0 | Iniciación de pagos |
| I5 | automatic-payments 2.0.0 | PaymentOrderInitiation 14.0.0 | Pagos recurrentes |
| I6 | enrollments 2.1.0 | PaymentOrderInitiation 14.0.0 | Enrolamiento |

n = **7**. I1/I2 e I3a/I3b no son independientes (mismo YAML OFB, dos referencias). Las otras **33** APIs OFB no reciben AlignmentScore.

---

## 2. Técnicas e instrumentos de recolección

No hay encuestas ni runtime. Se recolectan **artefactos documentales** públicos.

| Técnica | Instrumento | Qué recolecta |
|---------|-------------|---------------|
| Adquisición versionada | `git` + YAML oficiales | Contrato OFB y SD BIAN congelados |
| Parsing OpenAPI 3.x | `procesar_openapi.py` | paths, methods, `$ref` anidados, schemas, propiedades, textos |
| Normalización | mismo parser (camelCase, prefijos `InCR`/`ReBQ`) | CSV listos para matching |
| Inventario | `resultado/inventario.json` | 41 / 235 / 6 746 / 10 906 |
| Trazabilidad | repositorio Git | commit, fecha, comando de corrida |

**Salidas OE1 (ya existen)**

- `operaciones_estructuradas.csv`
- `propiedades_esquemas.csv`
- `corpus_semantico.csv`
- `por_contrato/<id>/estadisticas.json`

**Aún no existen** (semana 7+): `pares_estructurales.csv`, `pares_semanticos.csv`, `scores.json`.

Ética: solo YAML públicos; citar Open Finance Brasil y BIAN.

---

## 3. Procedimiento (reproducible)

Tipo: investigación tecnológica / *design science*. Enfoque cuantitativo sobre documentos. **No** es ML supervisado.

```
adquirir YAML  →  parsear / normalizar (OE1)
        →  emparejar estructura (OE2 → E)
        →  similitud semántica (OE3 → S)
        →  cobertura + score (OE4 → C, AlignmentScore, nivel)
```

Pasos congelados:

1. Fijar versiones (accounts 2.4.2, payments 4.0.0, BIAN 14.0.0, parser por hash Git).
2. Correr `python3 procesar_openapi.py --fuentes fuentes resultado`.
3. Firmar completitud OE1 = extraídos / esperados (por YAML).
4. Matching **solo** en I1–I6. Baseline E (semana 7–8): Jaccard de tokens + path + HTTP; ops sin par aportan 0.
5. S v0 (semana 8): léxico / TF-IDF. S v1 (semana 11): embeddings + coseno. Umbral 0,55; sensibilidad 0,45 / 0,65.
6. C = (CR + BQ con ≥ 1 par) / (CR + BQ del SD). Sin contar el CR dos veces como BO.
7. AlignmentScore = (S + E + C) / 3. Sensibilidad de pesos aparte. Nivel oficial = umbrales fijos.
8. Bitácora: commit + `inventario.json`. No mezclar CSV de corridas distintas.

Detalle operativo: `../plan-tesis-v2/protocolo-empirico.md`.

**Prohibido en cualquier corrida**

- Puntuar BIAN contra sí mismo y llamarlo resultado banco–BIAN.
- Copiar tags CR/BQ al CSV OFB.
- Usar el nombre interno de un `$ref` BIAN como evidencia OFB.
- Etiquetar Alta/Media/Baja a mano para entrenar un clasificador.

---

## 4. Técnicas de análisis y correspondencia con objetivos / hipótesis

**VD del artefacto:** AlignmentScore + clasificación {Alta ≥ 0,80 · Media 0,60–0,79 · Baja 0,40–0,59 · Nula < 0,40}.

| Pregunta | OE | Técnica | Hipótesis | Evidencia ahora |
|----------|----|---------|-----------|-----------------|
| P1 correspondencias estructurales | OE2 | Schema matching (Jaccard, path, HTTP) → E | H2 | Pendiente (I1 e I4 en semana 8) |
| P2 similitud de términos | OE3 | Léxico v0 / embeddings v1 → S | H3 | Pendiente |
| P3 tipologías de desalineación | OE4 | Lectura de pares + Tabla 2 Guía 1 | — | Condicionada por EDA (GET vs PUT; *gap* loans) |
| P4 score interpretable | OE4 | αS+βE+γC, pesos 1/3 | H4 | Pendiente |
| (previo) ¿se puede medir? | OE1 | Parser + completitud | H1 | **Soportada** a nivel de extracción (41 YAML) |

Los ratios de OE1–OE3 son **parciales**. No sustituyen la VD.

**Amenazas que el análisis debe declarar**

- Interna: *account* / *payment* ambiguos; BIAN summary = description 75/75; I1/I2 e I3a/I3b no independientes.
- Externa: OFB no es un banco peruano; 3 SD no cubren loans/cards.
- Constructo: un score global puede ocultar un BQ crítico mal cubierto.
- Conclusión: no generalizar a «todo open banking» ni a «todo BIAN».

---

## 5. Evidencia de viabilidad (EDA + piloto)

No hay baseline de AlignmentScore todavía. La viabilidad de **esta** semana es: el procedimiento se puede ejecutar sobre un corpus real, público y ya parseado.

### 5.1 Hecho (Sesión 5)

| Hecho | Dato |
|-------|------|
| Contratos parseados | 41 (38 OFB + 3 BIAN) |
| Operaciones | 235 (160 + 75) |
| Parser | OpenAPI 3.x, `$ref` anidados resueltos |
| OFB | GET 130/160 (REST de consulta) |
| BIAN | PUT 36/75 (Update/Control/Execute) |
| Props sin *description* | 61,9 % (BIAN 90,4 %; OFB 38,1 %) |
| BIAN summary = description | 75/75 |
| Leakage documentado | no copiar CR/BQ; no autoalineación |

### 5.2 Lo que el EDA ya decide

- E **no** puede exigir el mismo verbo HTTP.
- S de atributos BIAN cae sobre el **nombre**.
- C de I1 será probablemente baja (6 GET OFB vs. 1 CR + 9 BQ). Eso es hallazgo, no fallo del parser.
- Loans / cards / financings = *gap* de referencia, no de objeto.

### 5.3 Checklist de la lámina

| Punto del aula | ¿Cubierto? | Dónde |
|----------------|------------|-------|
| Población, muestra, fuentes, criterios | Sí | §1 · Plan v2 §3.3 y §4 |
| Técnicas e instrumentos de recolección | Sí | §2 · parser + CSV |
| Procedimiento claro y reproducible | Sí | §3 · `protocolo-empirico.md` |
| Análisis ↔ objetivos / hipótesis | Sí | §4 · P1–P4, OE1–OE4, H1–H4 |
| Evidencia de viabilidad (EDA / piloto) | Sí, sin scores | §5 · Sesión 5 |

### 5.4 Qué falta para cerrar P3 / abrir P4

- [ ] Firmar completitud OE1 por YAML (semana 7).
- [ ] Script de matching v0 (semana 7).
- [ ] Scores v0 de I1 e I4 (semana 8, P4).
- [ ] Figura Cap. II: OFB (GET) vs BIAN (CR/BQ).

---

## Referencias internas

| Documento | Uso |
|-----------|-----|
| `image.png` | Lámina oficial Sesión 6 |
| `../plan-tesis-v2/PLAN_TESIS_V2.pdf` | Plan vigente · §7 método |
| `../plan-tesis-v2/protocolo-empirico.md` | Pasos OE1–OE4 |
| `../plan-tesis-v2/matriz-consistencia-ofb.md` | 8 columnas |
| `../sesion-05/` | Operacionalización + EDA + dataset |
| `../../01-curso-I/plan-tesis/latex/` | Guía 1 (diseño) |

*Grupo 10 · Sesión 6 · revisión del método · objeto OpenAPI bancario · piloto OFB · octubre 2026.*
