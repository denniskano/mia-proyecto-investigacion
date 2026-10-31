# Alineación OpenAPI bancario ↔ BIAN

**Grupo 10** · Alex Mancilla Antay · Jack Paitan Cano  
**Programa:** Maestría en Inteligencia Artificial · UNI

| | |
|--|--|
| **Tesis** | Alineación entre contratos **OpenAPI bancarios** y modelos de referencia **BIAN**, mediante análisis estructural y similitud semántica (S / E / C → AlignmentScore). |
| **Objeto** | Contrato OpenAPI **bancario** (no cambia). |
| **Referencia** | Service Domain BIAN. |
| **Piloto (ahora)** | Catálogo **Open Finance Brasil** × 3 SD BIAN v14. |

Este directorio es el **hilo único** del proyecto: Curso I (diseño) → Curso II (ejecución). Empieza por aquí y luego por `ESTADO.md`.

**No van al git:** `00-archivo/clases-video/` (~10 GB) y `00-archivo/transcriptions/`. Quedan solo en local.

```
mia-proyecto-investigacion/
├── README.md                 ← estás aquí
├── ESTADO.md                 ← hecho / en curso / pendiente
├── 00-archivo/               ← clases, videos, transcripciones (no es el producto)
├── 01-curso-I/               ← MIA 303 · Guía 1 · plan LaTeX (diseño)
└── 02-curso-II/              ← MIA 403 · plan v2 + piloto OFB (ejecución)
    ├── material-oficial/     ← sílabo, guías, PDFs de sesión
    ├── plan-tesis-v2/        ← plan ejecutable vigente
    └── sesion-05/            ← operacionalización + EDA + dataset
```

## Dónde abrir cada cosa

| Qué necesitas | Ruta |
|---------------|------|
| **Plan vigente (Curso II)** | [`02-curso-II/plan-tesis-v2/PLAN_TESIS_V2.pdf`](02-curso-II/plan-tesis-v2/PLAN_TESIS_V2.pdf) |
| Matriz consistencia OFB | [`02-curso-II/plan-tesis-v2/Matriz_Consistencia_OFB_Grupo10.pdf`](02-curso-II/plan-tesis-v2/Matriz_Consistencia_OFB_Grupo10.pdf) |
| PPT / slides piloto | [`02-curso-II/sesion-05/Sesion05_Operacionalizacion_y_EDA_slides.pdf`](02-curso-II/sesion-05/Sesion05_Operacionalizacion_y_EDA_slides.pdf) |
| Revisión método (S6) | [`02-curso-II/sesion-06/Sesion06_Revision_Metodo.pdf`](02-curso-II/sesion-06/Sesion06_Revision_Metodo.pdf) |
| Revisión avances (S7) | [`02-curso-II/sesion-07/Sesion07_Revision_Avances.pdf`](02-curso-II/sesion-07/Sesion07_Revision_Avances.pdf) |
| Dataset piloto | [`02-curso-II/sesion-05/data/piloto_ofb_bian/`](02-curso-II/sesion-05/data/piloto_ofb_bian/) |
| Plan Guía 1 (LaTeX) | [`01-curso-I/plan-tesis/latex/build/Plan_Tesis_Grupo10.pdf`](01-curso-I/plan-tesis/latex/build/Plan_Tesis_Grupo10.pdf) |
| Sílabo MIA 403 | [`02-curso-II/material-oficial/silabo/`](02-curso-II/material-oficial/silabo/) |

## Continuidad en una frase

Guía 1 **diseñó** S/E/C. MIA 403 **calcula** AlignmentScore sobre un piloto OFB, sin cambiar el objeto de la tesis.
