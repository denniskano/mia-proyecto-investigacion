# Piloto OFB × BIAN v14

**Muestra:** 38 APIs Open Finance Brasil (última estable).  
**Referencia:** **258** Service Domains BIAN v14 (todos los OpenAPI publicados).  
**No hay** recorte de 12 operaciones ni YAML de un banco emisor.  
**No se inventa** un SD: solo YAML de `bian-official/public` release 14.0.0.

Plan vigente: `../plan-tesis-v2/PLAN_TESIS_V2.pdf`.  
Presentación: `Piloto_OFB_BIAN_slides.pdf` (Beamer; no PPTX).  
Objeto de la tesis (no cambia): OpenAPI bancario. OFB es solo este piloto.

## Totales (parser)

| | BIAN v14 | Open Finance Brasil | Total |
|--|----------|---------------------|-------|
| Contratos | **258** | **38** | **296** |
| Operaciones | 4 580 | **160** | **4 740** |
| Propiedades | — | — | **67 388** |
| Corpus | — | — | **100 328** |

```
02-curso-II/piloto/
  fuentes/ofb/      38 YAML OFB_*
  fuentes/bian/     258 YAML BIAN v14
  descargar_bian.py
  procesar_openapi.py
  matching_v0.py    I1–I6 oficiales (baseline léxico)
  matching_s1.py    S MiniLM sobre pares OE2 congelados
  mapa_ofb_bian.py  catálogo extra (loans, cards, …)
```

Fuente OFB: [OpenBanking-Brasil/openapi](https://github.com/OpenBanking-Brasil/openapi).  
Fuente BIAN: [bian-official/public](https://github.com/bian-official/public) · `release14.0.0/semantic-apis/oas3 /yamls`.

OE1: **296/296** firmados (`resultado/matching/oe1_firma.json`).

## Instancias oficiales (protocolo, n = 7)

I1–I6 no se reemplazan. Siguen en `resultado/matching/` y `resultado/matching_s1/`.

## Catálogo extra

`resultado/matching/catalogo/MAPA.md` — OFB contra SD **oficiales** que antes no estaban en disco:

| OFB | BIAN oficial | Pares (v0) | Nivel |
|-----|--------------|------------|-------|
| credit-cards | CreditCard | 7/7 | Baja (0,46) |
| loans | Loan | 4/5 | Nula (0,27) |
| opendata-loans | Loan | 2/2 | Nula (0,28) |
| opendata-creditcards | CreditCard | 2/2 | Nula (0,30) |
| investments | InvestmentAccount | 2/5 | Nula (0,19) |

Sin par natural (solo inventario): `admin`, `common`, `resources`, `webhook`, `participants`, `capitalization-bonds`, `credit-fixed-incomes`.

## Regenerar

```
python3 descargar_bian.py
.venv/bin/python procesar_openapi.py --fuentes fuentes resultado
.venv/bin/python matching_v0.py
.venv/bin/python matching_s1.py
.venv/bin/python mapa_ofb_bian.py
```
