# Figuras del plan de tesis — Grupo 9.2

**Carpeta canónica** para incluir imágenes en LaTeX (`\graphicspath` apunta aquí).

```
plan-tesis/figuras/
├── README.md                 ← este archivo (índice maestro)
├── cap01/                      Capítulo 1 — planteamiento
│   ├── Figura_01_Contexto.png
│   └── Figura_02_Objeto_Unidad_Analisis.png
├── cap02/                      Capítulo 2 — objetivos
│   └── Figura_04_Cadena_Objetivos.png
├── cap03/                      Capítulo 3 — marco teórico
│   ├── Figura_05_Bases_Conceptuales.png
│   └── Figura_06_Brecha.png
├── modelo-alineacion/          Modelo S/E/C (extraídas del PDF fuente)
│   ├── Figura_03_AlignmentScore.pdf
│   ├── Figura_07_StructuralScore.pdf
│   ├── Apoyo_SemanticScore.pdf
│   └── Apoyo_CoverageScore.pdf
└── _fuente/                    Respaldo del PDF multipágina original
    └── figuras_alineacion_openapi_bian_completo.pdf
```

## Dónde va cada figura en el documento

| Archivo | Figura plan | Sección | Capítulo |
|---------|-------------|---------|----------|
| `cap01/Figura_01_Contexto.png` | **Figura 1** | §1.1 Introducción | 1 |
| `cap01/Figura_02_Objeto_Unidad_Analisis.png` | **Figura 2** | §1.4 Objeto de estudio | 1 |

> **Git:** `cap01/` guarda copias PNG (no symlinks). Tras regenerar con `build_figuras_fase_b.py`, copiar de nuevo desde `fases/fase-b-planteamiento/figuras/`.
| `modelo-alineacion/Figura_03_AlignmentScore.pdf` | **Figura 3** | §1.4.1 Modelo integrado S/E/C | 1 |
| `cap02/Figura_04_Cadena_Objetivos.png` | **Figura 4** | §2.6 Cadena de objetivos | 2 |
| `cap03/Figura_05_Bases_Conceptuales.png` | **Figura 5** | §3.2 Bases conceptuales | 3 |
| `cap03/Figura_06_Brecha.png` | **Figura 6** | §3.6 Brecha V1–V5 | 3 |
| `modelo-alineacion/Figura_07_StructuralScore.pdf` | **Figura 7** | §4.2 Procedimiento (E) | 4 |
| `modelo-alineacion/Apoyo_SemanticScore.pdf` | Apoyo §4.4 | §4.4 Técnicas (S) | 4 |
| `modelo-alineacion/Apoyo_CoverageScore.pdf` | Apoyo §4.5 | §4.5 Métricas (C) | 4 |

Figura **8** del plan maestro no aplica (experimentación fuera de alcance del plan).

## Origen y regeneración

| Origen | Cómo se produce |
|--------|-----------------|
| Fig. 1 y 2 | `herramientas/scripts/build_figuras_fase_b.py` → `fase-b-planteamiento/figuras/` (symlinks en `cap01/`) |
| Fig. 4 y 5–6 | `herramientas/scripts/build_figuras_fase_cd.py` → `cap02/`, `cap03/` |
| Modelo alineación | PDF original en `anexos/figuras_alineacion_openapi_bian.pdf`; páginas separadas con `pdfseparate` |

Para re-extraer tras editar el PDF fuente:

```bash
SRC=plan-tesis/anexos/figuras_alineacion_openapi_bian.pdf
DST=plan-tesis/figuras/modelo-alineacion
pdfseparate "$SRC" "$DST/_page-%d.pdf"
mv "$DST/_page-1.pdf" "$DST/Figura_03_AlignmentScore.pdf"
mv "$DST/_page-2.pdf" "$DST/Figura_07_StructuralScore.pdf"
mv "$DST/_page-3.pdf" "$DST/Apoyo_SemanticScore.pdf"
mv "$DST/_page-4.pdf" "$DST/Apoyo_CoverageScore.pdf"
rm -f "$DST/_page-"*.pdf
cp "$SRC" plan-tesis/figuras/_fuente/figuras_alineacion_openapi_bian_completo.pdf
```

## LaTeX

```latex
\includegraphics{Figura_01_Contexto}              % cap01/
\includegraphics{Figura_03_AlignmentScore}        % modelo-alineacion/
```

Ver `../latex/config/preamble.tex` (`\graphicspath`).

## Nota SchemaConformance (δ)

`Apoyo_CoverageScore.pdf` proviene de la pág. 4 del PDF fuente, que incluye **δ** en el diagrama
original. El modelo del plan usa solo **S, E, C** — ver `../anexos/README.md`.
