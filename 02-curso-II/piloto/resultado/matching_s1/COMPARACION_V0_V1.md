# SemanticScore v1 — MiniLM sobre pares OE2 congelados

Modelo: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
E y C no se recalcularon. No hay pares semánticos sueltos.

| ID | S v0 | S MiniLM | E | C | Score v0 | Score v1 | Nivel v0 → v1 |
|----|------|----------|---|---|----------|----------|---------------|
| I1 | 0.01 | **0.56** | 0.35 | 0.40 | 0.26 | **0.44** | Nula → Baja |
| I2 | 0.01 | **0.53** | 0.47 | 0.50 | 0.33 | **0.50** | Nula → Baja |
| I3a | 0.00 | **0.45** | 0.56 | 0.20 | 0.25 | **0.41** | Nula → Baja |
| I3b | 0.00 | **0.46** | 0.56 | 0.20 | 0.25 | **0.41** | Nula → Baja |
| I4 | 0.00 | **0.52** | 0.29 | 0.25 | 0.18 | **0.35** | Nula → Nula |
| I5 | 0.03 | **0.59** | 0.32 | 0.50 | 0.28 | **0.47** | Nula → Baja |
| I6 | 0.00 | **0.00** | 0.00 | 0.00 | 0.00 | **0.00** | Nula → Nula |

S oficial = promedio del coseno de los pares estructurales. El umbral 0,55 se reporta como sensibilidad, no recorta el S oficial.
