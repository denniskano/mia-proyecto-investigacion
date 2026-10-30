# Figuras — Fase B (Capítulo 1)

Generadas con `build_figuras_fase_b.py`. Copias canónicas en `../../figuras/cap01/` (symlinks).

| Figura | Sección | Archivo local | LaTeX |
|--------|---------|---------------|-------|
| **1** | §1.1 | `Figura_01_Contexto.png` | ✅ |
| **2** | §1.4 | `Figura_02_Objeto_Unidad_Analisis.png` | ✅ |
| **3** | §1.4.1 | `../../figuras/modelo-alineacion/Figura_03_AlignmentScore.pdf` | ✅ |

Pies de figura definidos en `latex/chapters/cap01-planteamiento/*.tex`.

Modelo S/E/C (pág. 2–4 del PDF fuente): ver `../../figuras/modelo-alineacion/README.md`.

## Regenerar Fig. 1 y 2

```bash
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_figuras_fase_b.py
```

## Notas

- Fig. 1 sin problemática (§1.2).
- Fig. 2 sustituye el antiguo piloto Payment Execution.
- Fig. 3 proviene del PDF anexo (pág. 1 separada en `figuras/modelo-alineacion/`).
