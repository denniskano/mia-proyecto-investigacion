# Piloto OFB × BIAN v14

**Muestra:** 38 APIs Open Finance Brasil (última estable).  
**Referencia:** 3 Service Domains BIAN v14 (completos).  
**No hay** recorte de 12 operaciones ni YAML de un banco emisor.

Plan vigente: `../../../plan-tesis-v2/PLAN_TESIS_V2.pdf`.  
Objeto de la tesis (no cambia): OpenAPI bancario. OFB es solo este piloto.

## Totales

| | BIAN v14 | Open Finance Brasil | Total |
|--|----------|---------------------|-------|
| Contratos | 3 | **38** | **41** |
| Operaciones | 75 | **160** | **235** |
| Propiedades | — | — | **6746** |
| Corpus | — | — | **10906** |

```
piloto_ofb_bian/
  fuentes/ofb/     38 YAML OFB_*
  fuentes/bian/    SavingsAccount, CurrentAccount, PaymentOrderInitiation
  resultado/       CSV + inventario.json
  procesar_openapi.py
```

Fuente OFB: [OpenBanking-Brasil/openapi](https://github.com/OpenBanking-Brasil/openapi) · `swagger-apis`.  
Criterio: última versión estable por API (solo `payroll-credit-portability` es beta).  
Fuente BIAN: [bian-official/public](https://github.com/bian-official/public) · release 14.0.0.

## Referencia BIAN

| Contrato | Ops |
|----------|-----|
| SavingsAccount v14.0.0 | 34 |
| CurrentAccount v14.0.0 | 34 |
| PaymentOrderInitiation v14.0.0 | 7 |

## Pares naturales (OE2–OE4)

| Open Finance Brasil | BIAN |
|---------------------|------|
| accounts + opendata-accounts | SavingsAccount, CurrentAccount |
| payments + automatic-payments + enrollments | PaymentOrderInitiation |
| loans / financings / credit-cards | *sin SD en este piloto* |

## Regenerar CSV

```
python3 procesar_openapi.py --fuentes fuentes resultado
```
