# Libreto — Piloto OFB × BIAN (16 láminas, 12–14 min)

**Grupo 10** · Alex = marco / objeto / conclusiones · Jack = fuentes, modelos, números  
**PDF:** `Piloto_OFB_BIAN_slides.pdf`  
**Figuras:** `figuras/arquitectura-piloto.drawio` + PNG de arquitectura y 5 gráficos.

| # | Lámina | Quién | Qué decir |
|---|--------|-------|-----------|
| 1 | Portada | Alex | Ya no es un diseño: el piloto **mide**. Objeto OpenAPI bancario; OFB es la muestra; BIAN v14 el catálogo. |
| 2 | Lo que entrega | Alex | 296 YAML firmados, 258 SD, n = 7, MiniLM pasa a Baja en 5. Parser 100 % no es score Alto. |
| 3 | Objeto vs piloto | Alex | No hay banco emisor. No se inventa SD. No se puntúa 38 × 258. OFB no redefine la tesis. |
| 4 | Arquitectura | Jack | Fuentes → parser → tres matching (v0, MiniLM, mapa extra) → scores. Dorado = único experimento de embeddings. |
| 5 | Fuentes | Jack | OFB GET vs BIAN PUT. Por eso E no exige el mismo verbo. 160 ops contra 4 580: asimetría, no error. |
| 6 | OE1 | Jack | Descargar, parsear, firmar 1,00. Loan y CreditCard ya están en disco. Parser habilita; no clasifica. |
| 7 | Fórmula | Jack | E incluye los 0. S solo sobre pares de E. C = CR+BQ. Nivel = umbral, no ML. |
| 8 | Modelos | Jack | v0 léxico = techo PT×EN. MiniLM-L12 multilingual porque OFB es PT y BIAN EN. E/C son reglas. No hay clasificador. |
| 9 | n = 7 | Jack | I3 se parte. I1/I2 no son independientes. El mapa extra no sustituye estas siete. |
| 10 | AlignmentScore | Jack | Todas Nula en v0. MiniLM cruza 0,40 en cinco. I4 se queda Nula (0,35). I6 es 0. |
| 11 | S léxico vs MiniLM | Jack | Jaccard no cruza idiomas. `conta` ≠ `SavingsAccountFacility`. MiniLM no reabre E. |
| 12 | S/E/C | Jack | Había estructura; S tumba el promedio. Open data cubre poco del SD (C = 0,20). |
| 13 | I1, I4, I6 | Jack | Greedy manda accountId a Charge. Pix sí, consents no. I6 = 0 es rechazo válido (FIDO ≠ POI). |
| 14 | Catálogo extra | Jack | El hueco de loans/cards era de disco. credit-cards × CreditCard = 0,46 Baja. No 38×258. |
| 15 | Conclusiones | Alex | Corre, es interpretable, rechaza pares falsos, y el SD de cards existía. Nula no tumba el piloto. |
| 16 | Líneas | Alex | Leakage, BIAN↔BIAN, inventar SD, etiquetar a mano. Medimos; no entrenamos un clasificador. |

Si preguntan por el 87 % de Turnitin: es el plan de Guía 1 de agosto, no este piloto.  
Si preguntan por Alta: nadie llega a 0,80; el piloto no finge un éxito de cobertura.
