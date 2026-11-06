# Cierre del piloto OFB × BIAN (P4 / baseline v0)

- Fecha: `2026-11-06T20:09:56Z`
- Commit: `24d1644ed4cdb7fc80da6f88800b9c87225100ed`
- Parser: `procesar_openapi.py`
- Semántica: `tfidf+jaccard-lexical-v0` (embeddings de frase = semana 11)

## Qué faltaba y qué se cierra aquí

| Entregable | Estado |
|------------|--------|
| OE1 firmado (ops/schemas = 1.00) | Sí |
| Matching v0 I1 e I4 (mínimo P4) | Sí |
| Scores v0 de las 7 instancias (baseline léxico) | Sí |
| Embeddings + sensibilidad de umbral S (semana 11) | Pendiente |
| Discusión P5 / borrador P7 | Pendiente (tesis, no piloto) |

## OE1 — completitud

Meta: ratio 1.00 en operaciones y schemas. Propiedades firmadas sobre `properties` directas.

| Archivo | Ops esp/ext | Schemas esp/ext | Props dir. | Firmado |
|---------|-------------|-----------------|------------|---------|
| `OFB_accounts_2.4.2.yml` | 6/6 | 31/31 | 86/86 | sí |
| `OFB_automatic-payments_2.0.0.yml` | 7/7 | 72/72 | 225/225 | sí |
| `OFB_enrollments_2.1.0.yml` | 8/8 | 36/36 | 52/52 | sí |
| `OFB_opendata-accounts_1.0.1.yml` | 2/2 | 32/32 | 92/92 | sí |
| `OFB_payments_4.0.0.yml` | 6/6 | 56/56 | 119/119 | sí |
| `CurrentAccount.yaml` | 34/34 | 256/256 | 1266/1266 | sí |
| `PaymentOrderInitiation.yaml` | 7/7 | 137/137 | 522/522 | sí |
| `SavingsAccount.yaml` | 34/34 | 251/251 | 1282/1282 | sí |

Inventario completo: **41/41** YAML firmados (incluye las 33 APIs OFB que solo entran al inventario, no al AlignmentScore).

## Scores v0

| ID | OFB × BIAN | S | E | C | AlignmentScore | Nivel | Pares |
|----|------------|---|---|---|----------------|-------|-------|
| I1 | `OFB_accounts_2.4.2.yml` × `SavingsAccount.yaml` | 0.01 | 0.35 | 0.40 | **0.26** | Nula | 4/6 |
| I2 | `OFB_accounts_2.4.2.yml` × `CurrentAccount.yaml` | 0.01 | 0.47 | 0.50 | **0.33** | Nula | 5/6 |
| I3a | `OFB_opendata-accounts_1.0.1.yml` × `SavingsAccount.yaml` | 0.00 | 0.56 | 0.20 | **0.25** | Nula | 2/2 |
| I3b | `OFB_opendata-accounts_1.0.1.yml` × `CurrentAccount.yaml` | 0.00 | 0.56 | 0.20 | **0.25** | Nula | 2/2 |
| I4 | `OFB_payments_4.0.0.yml` × `PaymentOrderInitiation.yaml` | 0.00 | 0.29 | 0.25 | **0.18** | Nula | 3/6 |
| I5 | `OFB_automatic-payments_2.0.0.yml` × `PaymentOrderInitiation.yaml` | 0.03 | 0.32 | 0.50 | **0.28** | Nula | 4/7 |
| I6 | `OFB_enrollments_2.1.0.yml` × `PaymentOrderInitiation.yaml` | 0.00 | 0.00 | 0.00 | **0.00** | Nula | 0/8 |

El nivel **Nula/Baja no invalida** el piloto: valida que el score es computable, interpretable y sin leakage. C bajo en cuentas es hallazgo (pocos GET OFB vs 1 CR + varios BQ). I6 en 0 pares es hallazgo: enrollments/FIDO no comparte recurso léxico con PaymentOrderInitiation. S≈0 es el techo del baseline PT×EN; los embeddings de semana 11 existen para eso.

## Lo que sigue (ya no es cierre de piloto P4)

1. Semana 11: S con embeddings (`paraphrase-multilingual-MiniLM`) y sensibilidad 0.45/0.55/0.65.
2. Semana 12 (P5): discusión de tipologías contra literatura.
3. No puntuar loans/cards/financings inventando un SD.
