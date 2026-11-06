# Diagnóstico Guía 1 → Guía 2

Documento de la **semana 1** (P1). Detalle operativo: `PLAN_TESIS_V2.md` §2 y `cronograma-sprints.md`.

## Herencia

| Activo Guía 1 | Uso en Guía 2 |
|---------------|---------------|
| Problema tecnológico, P1–P4, OG, OE1–OE4 | Se mantienen; el **piloto** los instancia en OFB |
| Modelo S/E/C y umbrales | Sin cambio de fórmula |
| Estado del arte (14 papers) | Se reargumenta; se añade contexto OFB |
| Anexos C, D, F | Protocolo y operacionalización |
| Matriz consistencia v2 (8 cols) | Nueva matriz OFB en esta carpeta |
| Parser + EDA Sesión 5 | Base empírica OE1 |

## Decisión que abre el segundo curso

El **objeto de la tesis** sigue siendo el contrato OpenAPI **bancario**. BIAN sigue siendo la **referencia**.  
Lo que se fija en MIA 403 es la **muestra del piloto:** Open Finance Brasil.  
No se añaden en este curso YAML de un banco emisor ni Open Banking UK; eso no reescribe el objeto.

## Brechas que el plan v2 cierra (papel) vs. las que se cierran ejecutando

| Brecha | ¿Este plan la cierra? | ¿Cuándo se ejecuta? |
|--------|------------------------|---------------------|
| ¿Con qué contrato se mide ahora? | Sí — piloto = OFB (objeto intacto) | Semana 1 |
| Falta contrato “banco” en Sesión 5 (texto viejo) | Sí — 38 APIs OFB ya parseadas | Hecho |
| Matching E / S | No (solo protocolo) | Semanas 7–11 |
| AlignmentScore (7 instancias) | No | Semanas 8 (I1, I4) y 11 (resto) |
| SD BIAN para loans/cards | Sí — `Loan.yaml` / `CreditCard.yaml` oficiales (mapa extra; no sustituye I1–I6) | Hecho |
| Borrador integral | No | Semana 16 |

## Riesgos que el diagnóstico no puede eliminar

1. 160 ops OFB vs. 4 580 BIAN (258 SD): C global o el producto 38 × 258 sería un error de unidad.
2. El piloto OFB no es un banco peruano ni agota OpenAPI bancario: validez externa acotada.
3. BIAN summary = description: riesgo de inflar S.
4. Sin etiquetas expertas: no hay *ground truth* supervisado.

## Criterio de salida de la semana 1

Grupo 10 puede decir en una frase: *la tesis mide alineación de contratos OpenAPI bancarios frente a BIAN; en este curso el piloto es Open Finance Brasil × catálogo BIAN v14 (258 SD), con score oficial en los pares I1–I6*.
