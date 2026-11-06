# Libreto — Piloto OFB × BIAN (15 láminas, 11–13 min)

**Grupo 10** · Alex = marco / objeto · Jack = números y pares  
**PDF:** `Piloto_OFB_BIAN_slides.pdf`

| # | Lámina | Quién | Qué decir (≈ 40–50 s) |
|---|--------|-------|------------------------|
| 1 | Portada | Alex | Objeto OpenAPI bancario. OFB es la muestra. Referencia: catálogo BIAN v14 completo. |
| 2 | Qué se cierra | Alex | 258 OpenAPI oficiales. OE1 296/296. I1–I6 no se tocan. Loans/cards ya tienen SD real. |
| 3 | Objeto vs piloto | Alex | No hay YAML de un banco emisor. No se inventa un SD: `Loan.yaml` y `CreditCard.yaml` son oficiales. |
| 4 | Dataset | Jack | 296 / 4 740 / 67 388 / 100 328. 38 OFB + 258 SD. No se puntúa 38 × 258. |
| 5 | n = 7 | Jack | I3 se parte en a/b. I1/I2 comparten accounts. El mapa extra no sustituye estas siete. |
| 6 | OE1 | Jack | Ratio 1,00 en ops y schemas. 296/296 firmados. Loan 24/24 y CreditCard 28/28. |
| 7 | Fórmula | Jack | E oficial incluye los 0. S solo sobre pares de E. Nivel = umbral, no ML. |
| 8 | Tabla 7 | Jack | Todas Nula. I2 es la más alta (0,33). I6 es 0. Eso se defiende. |
| 9 | I1 | Jack | 4/6 pares. Greedy manda accountId a Charge: C se infla. |
| 10 | I4 | Jack | Pix sí; consents no. C = 1/4. S = 0 porque PT vs EN. |
| 11 | Catálogo extra | Jack | credit-cards × CreditCard: 7/7, 0,46 Baja. loans × Loan: 4/5, 0,27 Nula. El hueco era de disco. |
| 12 | Lectura | Alex | Éxito = score interpretable + catálogo real. Baja en cards no reemplaza I1–I6. |
| 13 | IA | Alex | v0 = Jaccard + TF-IDF. MiniLM ya corre sobre los pares de E de I1–I6. Catálogo extra sigue léxico. |
| 14 | Prohibido | Alex | Leakage, BIAN↔BIAN, inventar SD, cartesiano 38×258, etiquetar a mano. |
| 15 | Cierre | Ambos | 258 SD. I1–I6 intactas. Siguiente: discusión P5, sin reabrir n = 7. |

Si preguntan por el 87 % de Turnitin: es el plan de Guía 1 ya enviado en agosto, no el piloto.
