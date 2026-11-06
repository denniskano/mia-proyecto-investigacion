# Cierre del piloto OFB × BIAN (P4 / baseline v0)

- Fecha: `2026-11-06T21:00:02Z`
- Commit: `ec2b2ad58b3936c4fabb7d81ce2fde5d017cf747`
- Parser: `procesar_openapi.py`
- Semántica: `tfidf+jaccard-lexical-v0` (embeddings de frase = semana 11)

## Qué faltaba y qué se cierra aquí

| Entregable | Estado |
|------------|--------|
| OE1 firmado (ops/schemas = 1.00) | Sí |
| Matching v0 I1 e I4 (mínimo P4) | Sí |
| Scores v0 de las 7 instancias (baseline léxico) | Sí |
| Catálogo BIAN v14 (258 OpenAPI oficiales) | Sí |
| Mapa extra OFB → SD oficial (sin inventar SD) | Sí (`catalogo/`) |
| Embeddings MiniLM sobre pares OE2 de I1–I6 | Sí (`matching_s1/`) |
| Discusión P5 / borrador P7 | Pendiente (tesis, no piloto) |

## OE1 — completitud

Meta: ratio 1.00 en operaciones y schemas. Propiedades firmadas sobre `properties` directas.

| Archivo | Ops esp/ext | Schemas esp/ext | Props dir. | Firmado |
|---------|-------------|-----------------|------------|---------|
| `OFB_accounts_2.4.2.yml` | 6/6 | 31/31 | 86/86 | sí |
| `OFB_automatic-payments_2.0.0.yml` | 7/7 | 72/72 | 225/225 | sí |
| `OFB_credit-cards_2.3.1.yml` | 7/7 | 40/40 | 127/127 | sí |
| `OFB_enrollments_2.1.0.yml` | 8/8 | 36/36 | 52/52 | sí |
| `OFB_loans_2.5.0.yml` | 5/5 | 42/42 | 112/112 | sí |
| `OFB_opendata-accounts_1.0.1.yml` | 2/2 | 32/32 | 92/92 | sí |
| `OFB_payments_4.0.0.yml` | 6/6 | 56/56 | 119/119 | sí |
| `CreditCard.yaml` | 28/28 | 237/237 | 1054/1054 | sí |
| `CurrentAccount.yaml` | 34/34 | 256/256 | 1266/1266 | sí |
| `Loan.yaml` | 24/24 | 200/200 | 823/823 | sí |
| `PaymentOrderInitiation.yaml` | 7/7 | 137/137 | 522/522 | sí |
| `SavingsAccount.yaml` | 34/34 | 251/251 | 1282/1282 | sí |

Inventario completo: **296/296** YAML firmados (38 OFB + 258 Service Domains BIAN v14). I1–I6 no se reemplazan; el resto de OFB se mapea a un SD oficial (`resultado/matching/catalogo/`).

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

El nivel **Nula/Baja no invalida** el piloto: valida que el score es computable, interpretable y sin leakage. C bajo en cuentas es hallazgo (pocos GET OFB vs 1 CR + varios BQ). I6 en 0 pares es hallazgo: enrollments/FIDO no comparte recurso léxico con PaymentOrderInitiation. S≈0 es el techo del baseline PT×EN; MiniLM ya corre sobre los mismos pares (`matching_s1/`).

## Catálogo extra (no sustituye I1–I6)

Con los 258 YAML oficiales, loans y credit-cards ya tienen SD BIAN (`Loan.yaml`, `CreditCard.yaml`). No se inventó un Service Domain. No se puntúa el producto cartesiano 38 × 258.

| OFB | BIAN oficial | Pares | Score v0 |
|-----|--------------|-------|----------|
| credit-cards | CreditCard | 7/7 | Baja (0,46) |
| loans | Loan | 4/5 | Nula (0,27) |
| opendata-loans | Loan | 2/2 | Nula (0,28) |
| opendata-creditcards | CreditCard | 2/2 | Nula (0,30) |
| investments | InvestmentAccount | 2/5 | Nula (0,19) |

Detalle: `catalogo/MAPA.md`.

## Lo que sigue (ya no es cierre de piloto P4)

1. MiniLM I1–I6 ya está en `matching_s1/` (S sobre pares OE2 congelados).
2. Semana 12 (P5): discusión de tipologías contra literatura.
3. No puntuar 38 OFB × 258 SD. No inventar un SD. I1–I6 siguen siendo n = 7.
