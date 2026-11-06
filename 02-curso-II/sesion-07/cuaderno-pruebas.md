# Cuaderno de pruebas — piloto OFB × BIAN

**Grupo 10** · Alex Mancilla Antay · Dennis Jack Paitan Cano  
**Fecha de esta entrada:** 30 oct 2026  
**Corrida:** `procesar_openapi.py` sobre `../piloto/`  
**Commit de referencia:** el de `inventario.json` (41 / 235 / 6 746 / 10 906)

Este cuaderno registra las **primeras pruebas** (OE1 + EDA). No hay AlignmentScore todavía.

---

## Entrada 1 — Parser OE1

**Comando**

```
python3 procesar_openapi.py --fuentes fuentes resultado
```

**Totales**

| | BIAN | OFB | Total |
|--|------|-----|-------|
| Contratos | 3 | 38 | **41** |
| Operaciones | 75 | 160 | **235** |
| Propiedades | — | — | **6 746** |
| Corpus | — | — | **10 906** |

**Versiones congeladas (pares de score)**

- `OFB_accounts_2.4.2.yml` — 6 GET
- `OFB_opendata-accounts_1.0.1.yml`
- `OFB_payments_4.0.0.yml`
- `OFB_automatic-payments_2.0.0.yml`
- `OFB_enrollments_2.1.0.yml`
- BIAN v14: SavingsAccount (34), CurrentAccount (34), PaymentOrderInitiation (7)

**Qué funcionó:** YAML 3.x; `$ref` anidados en requestBody/response; prefijos `InCR`/`ReBQ` limpios; CSV con BOM UTF-8 (`utf-8-sig`).

**Qué falta firmar:** completitud OE1 = extraídos / esperados **por YAML**. Meta: 1,00 en ops y schemas.

---

## Entrada 2 — EDA (prueba de calidad del corpus)

| Prueba | Resultado | Lectura |
|--------|-----------|---------|
| Métodos HTTP OFB | GET 130 / POST 22 / PATCH 7 / DELETE 1 / PUT 0 | REST de consulta |
| Métodos HTTP BIAN | PUT 36 / GET 22 / POST 17 | Control / Update |
| Props sin *description* | 61,9 % (BIAN 90,4 %; OFB 38,1 %) | S de atributos BIAN cae sobre el nombre |
| BIAN summary = description | 75 / 75 | Una sola copia en el corpus |
| Tags CR/BQ en OFB | 0 | No imputar (leakage) |
| Paths / operationId duplicados | 0 en consolidado | OK |
| Loans / cards / financings | sin SD BIAN en el piloto | *Gap*, no se puntúa |

**Hipótesis H1 (parcial):** la normalización a CSV **sí** permite calcular S/E/C de forma sistemática. Aún no se calcula E/S/C.

---

## Entrada 3 — Lo que *no* se corrió (a propósito)

- Matching estructural (OE2) — semana 7–8.
- Similitud semántica (OE3) — v0 léxico en semana 8; embeddings en semana 11.
- AlignmentScore (OE4) — I1 e I4 en semana 8; las 7 instancias en semana 11.
- Autoalineación BIAN↔BIAN — **prohibida** como resultado.

**Próxima entrada del cuaderno:** scores v0 de I1 (`accounts` × SavingsAccount) e I4 (`payments` × PaymentOrderInitiation).

---

## Entrada 4 — Catálogo BIAN v14 completo (6 nov 2026)

**Comando**

```
python3 descargar_bian.py
.venv/bin/python procesar_openapi.py --fuentes fuentes resultado
.venv/bin/python matching_v0.py
.venv/bin/python mapa_ofb_bian.py
```

**Totales** (`resultado/inventario.json`)

| | BIAN | OFB | Total |
|--|------|-----|-------|
| Contratos | **258** | 38 | **296** |
| Operaciones | 4 580 | 160 | **4 740** |
| Propiedades | — | — | **67 388** |
| Corpus | — | — | **100 328** |

OE1: **296/296** firmados (`resultado/matching/oe1_firma.json`).

**Qué cambió:** el hueco de loans/cards era de disco (solo 3 YAML BIAN), no de BIAN. Ahora hay SD oficiales:

| OFB | BIAN oficial | Pares v0 | Nivel |
|-----|--------------|----------|-------|
| credit-cards | CreditCard | 7/7 | Baja (0,46) |
| loans | Loan | 4/5 | Nula (0,27) |

I1–I6 **no** se reemplazan. No se puntúa 38 × 258. No se inventa un SD.

Mapa: `../piloto/resultado/matching/catalogo/MAPA.md`.
