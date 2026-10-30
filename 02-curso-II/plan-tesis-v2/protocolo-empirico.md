# Protocolo empírico — OFB × BIAN (semana 7 en adelante)

**Grupo 9.2** · MIA 403 · Plan de tesis v2  
**Objeto de la tesis:** contrato OpenAPI **bancario**  
**Referencia:** Service Domain **BIAN v14** (SavingsAccount, CurrentAccount, PaymentOrderInitiation)  
**Muestra / piloto:** catálogo **Open Finance Brasil**  
**Dataset:** `../sesion-05/data/piloto_ofb_bian/`

Este protocolo ejecuta el Anexo C de Guía 1 sobre el corpus OFB ya parseado. No introduce otros emisores en **este** piloto; eso no reduce el objeto de la tesis a OFB.

---

## 0. Congelación (hacer una vez)

| Lado | Artefacto | Versión |
|------|-----------|---------|
| OFB I1 / I2 | `OFB_accounts_2.4.2.yml` | 2.4.2 |
| OFB I3 | `OFB_opendata-accounts_1.0.1.yml` | 1.0.1 |
| OFB I4 | `OFB_payments_4.0.0.yml` | 4.0.0 |
| OFB I5 | `OFB_automatic-payments_2.0.0.yml` | 2.0.0 |
| OFB I6 | `OFB_enrollments_2.1.0.yml` | 2.1.0 |
| BIAN | `SavingsAccount.yaml` · `CurrentAccount.yaml` · `PaymentOrderInitiation.yaml` | 14.0.0 |
| Parser | `procesar_openapi.py` | hash Git de la corrida |

Registrar en bitácora: commit, fecha, comando `run_batch`, totales de `inventario.json` (41 / 235 / 6746 / 10906).

Si se re-parsea, **no** se mezclan CSV de corridas distintas.

---

## 1. OE1 — Completitud (ya extraído; falta firmar)

Por cada YAML de I1–I6 y de los 3 SD:

1. Contar en el YAML fuente: paths × methods, schemas en `components`, propiedades (tras resolver `$ref` anidados).
2. Comparar con `por_contrato/<id>/estadisticas.json`.
3. Completitud = extraídos / esperados. Meta: 1,00 en ops y schemas; propiedades pueden diferir si hay `allOf`/`oneOf` documentado.

**Informe OE1 (1 página):** tabla contrato × (ops, schemas, props, textos) × (esperados, extraídos, ratio).  
Solo YAML en `fuentes/ofb/` y `fuentes/bian/`.

---

## 2. Unidades que se emparejan

| Lado OFB (muestra del piloto) | Lado BIAN (referencia) |
|-------------------|------------------------|
| `operation_id` + `method` + `path` | Behavior (operation) del SD |
| schema de request/response (nombre limpio) | Business Object / CR / BQ |
| propiedad (nombre) | atributo del BO |

OFB **no** trae tags CR/BQ. El matching asigna un elemento BIAN; no escribe el tag en el CSV OFB.

Normalización de nombres (igual que el parser): quitar prefijos `InCR`, `ReBQ`, camelCase → tokens, minúsculas, sin stopwords técnicas (`get`, `retrieve`, `id` al final).

---

## 3. OE2 — StructuralScore E

**Entrada:** `operaciones_estructuradas.csv` + `propiedades_esquemas.csv` de ambos lados de la instancia.

**Baseline (semana 7–8, sin embeddings)**

Para cada operación OFB, candidato BIAN si:

1. Jaccard de tokens del `operation_id` / nombre ≥ 0,40, **o**
2. Último segmento del `path` coincide con el recurso BIAN (p. ej. `accounts` ↔ `SavingsAccountFacility`), **o**
3. Mismo verbo HTTP **y** Jaccard ≥ 0,25.

Cada par recibe `e_pair` ∈ [0, 1]:

```
e_pair = 0,40·jaccard_nombre + 0,25·sim_path + 0,20·http_igual + 0,15·profundidad
```

`http_igual` = 1 si el verbo coincide, 0,5 si ambos son lectura (GET↔Retrieve) o escritura (PUT/POST/PATCH↔Update/Initiate/Execute), 0 si no.

`profundidad` = 1 − |prof_OFB − prof_BIAN| / max(prof), acotado a [0, 1].

**Agregación E de la instancia**

- Quedarse con el mejor par por operación OFB (greedy, sin reutilizar el mismo Behavior BIAN).
- E oficial = (suma de `e_pair` + 0 por cada operación OFB sin par) / (número de operaciones OFB de la instancia).
- Reportar también E* = promedio solo sobre las emparejadas (diagnóstico; no es el E oficial).

**Prohibido:** exigir que OFB tenga tantos PUT como BIAN. El EDA mostró GET 130/160 en OFB vs. PUT dominante en BIAN.

---

## 4. OE3 — SemanticScore S

**Entrada:** `corpus_semantico.csv`, campo `normalized_text`. Un texto por elemento (operation o schema). En BIAN, si `summary == description`, usar **una** copia.

**Línea base (semana 8):** similitud léxica (Jaccard / coseno TF-IDF sobre tokens).  
**Línea principal (semana 11):** embeddings de frase (mismo modelo en toda la corrida, p. ej. `paraphrase-multilingual-MiniLM`) + coseno.

Umbral de par semántico: coseno ≥ 0,55 (fijo; se reporta sensibilidad 0,45 / 0,55 / 0,65).

S de la instancia = promedio de similitudes de los pares **oficiales de OE2** (no se buscan pares semánticos sueltos que contradigan E). Si un par OE2 no tiene texto, se usa solo el nombre tokenizado.

---

## 5. OE4 — C, AlignmentScore, nivel

**Catálogo BIAN de la instancia** (denominador de C), sin doble conteo:

- el Control Record del SD (tag `CR - …`)
- los Behavior Qualifiers publicados como tags `BQ - …` en el YAML

Los Business Objects se usan en el matching de esquemas (OE2), no como segunda lista del denominador: el CR ya es el BO de control.

C = (conceptos del catálogo con ≥ 1 par OFB de OE2) / (tamaño del catálogo).

Nota: `accounts` tiene 6 GET y SavingsAccount tiene 1 CR + 9 BQ. C de I1 será probablemente baja; eso es hallazgo, no fallo del parser. `enrollments` (8 ops) vs. PaymentOrderInitiation (7 behaviors) deja al menos una operación OFB sin par bajo la regla greedy 1–1.

```
AlignmentScore = αS + βE + γC
α = β = γ = 1/3   # línea base
```

| AlignmentScore | Nivel |
|----------------|-------|
| ≥ 0,80 | Alta |
| 0,60–0,79 | Media |
| 0,40–0,59 | Baja |
| < 0,40 | Nula |

Sensibilidad: repetir con (0,50 / 0,30 / 0,20) y (0,20 / 0,50 / 0,30). El nivel **oficial** es el de 1/3.

Tipologías (Tabla 2 Guía 1): estructural, semántica, de modelado, REST/contrato. Una instancia puede tener más de una.

---

## 6. Instancias que se reportan

| ID | OFB | BIAN | Prioridad |
|----|-----|------|-----------|
| I1 | accounts 2.4.2 | SavingsAccount | Semana 8 |
| I4 | payments 4.0.0 | PaymentOrderInitiation | Semana 8 |
| I2 | accounts 2.4.2 | CurrentAccount | Semana 10–11 |
| I3a | opendata-accounts 1.0.1 | SavingsAccount | Semana 10–11 |
| I3b | opendata-accounts 1.0.1 | CurrentAccount | Semana 10–11 |
| I5 | automatic-payments 2.0.0 | PaymentOrderInitiation | Semana 10–11 |
| I6 | enrollments 2.1.0 | PaymentOrderInitiation | Semana 10–11 |

Las otras **33** APIs OFB (38 − 5 YAML usados en I1–I6): inventario OE1 y mapa de *gap* (loans, credit-cards, financings sin SD en el piloto). **No** se calcula AlignmentScore inventando un SD.

---

## 7. Controles de leakage y ética

1. No puntuar un YAML BIAN contra sí mismo y llamarlo “banco”.
2. No copiar `CR` / `BQ` al CSV OFB.
3. No usar el nombre interno de un `$ref` BIAN como evidencia OFB.
4. No etiquetar niveles a mano para entrenar un clasificador.
5. Fuentes públicas (OpenBanking-Brasil/openapi, bian-official/public). Sin PII; Ley 29733 no aplica.
6. Citar ambas organizaciones en el informe.

---

## 8. Entregables por corrida

```
resultado/matching/
  I1_accounts_x_SavingsAccount/
    pares_estructurales.csv
    pares_semanticos.csv
    scores.json          # S, E, C, AlignmentScore, nivel, pesos, umbrales
    tipologias.md
  ...
  resumen_instancias.csv
```

`scores.json` debe incluir `git_commit`, `parser_id`, `embedding_model` (o `tfidf`), umbrales y fecha.

---

## 9. Criterio de éxito

| Hito | Mínimo |
|------|--------|
| Semana 8 (P4) | OE1 firmado; I1 e I4 con scores v0 (puede ser solo baseline léxico) |
| Semana 9 | Defensa con EDA + 2 instancias |
| Semana 11 | Siete instancias con S/E/C + sensibilidad de pesos (insumo de Resultados v1) |
| Semana 12 (P5) | Discusión avanzada (sílabo): tipologías, literatura, limitaciones |
| Semana 16 (P7) | Borrador con tablas, tipologías y limitaciones (piloto OFB no agota OpenAPI bancario; 3 SD) |
