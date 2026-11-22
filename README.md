# Alineación OpenAPI bancario ↔ BIAN

**Grupo 10** · Alex Mancilla Antay · Dennis Jack Paitan Cano  
**Programa:** Maestría en Inteligencia Artificial · UNI

| | |
|--|--|
| **Tesis** | Alineación entre contratos **OpenAPI bancarios** y modelos de referencia **BIAN**, mediante análisis estructural y similitud semántica (S / E / C → AlignmentScore). |
| **Objeto** | Contrato OpenAPI **bancario** (no cambia). |
| **Referencia** | Service Domain BIAN. |
| **Piloto (ahora)** | Catálogo **Open Finance Brasil** × **258** SD BIAN v14 (I1–I6 = n = 7). |

Este directorio es el **hilo único** del proyecto: Curso I (diseño) → Curso II (ejecución). Empieza por aquí y luego por `ESTADO.md`.

**No van al git:** `00-archivo/clases-video/` (~10 GB) y `00-archivo/transcriptions/`. Quedan solo en local.

Tres repositorios. Este es el del curso. Los otros dos viven al lado y tienen su propio git; este repositorio no los versiona.

```
mia-proyecto-investigacion/   ← este repo: curso, plan, sesiones
├── README.md
├── ESTADO.md
├── 00-archivo/               ← clases y archivo (no es el producto)
├── 01-curso-I/               ← MIA 303 · Guía 1 · plan LaTeX
├── 02-curso-II/              ← MIA 403 · sesiones y plan v2
├── piloto-bank-api-bian/     ← repo propio, ya en GitHub
└── tesis-bank-api-bian/      ← repo propio: github.com/denniskano/tesis-bank-api-bian
```

## Dónde abrir cada cosa

| Qué necesitas | Ruta |
|---------------|------|
| **Plan vigente (Curso II)** | [`02-curso-II/plan-tesis-v2/PLAN_TESIS_V2.pdf`](02-curso-II/plan-tesis-v2/PLAN_TESIS_V2.pdf) |
| Matriz consistencia OFB | [`02-curso-II/plan-tesis-v2/Matriz_Consistencia_OFB_Grupo10.pdf`](02-curso-II/plan-tesis-v2/Matriz_Consistencia_OFB_Grupo10.pdf) |
| PDF / slides piloto | [Piloto OFB × BIAN](https://github.com/denniskano/piloto-bank-api-bian) |
| Revisión método (S6) | [`02-curso-II/sesion-06/Sesion06_Revision_Metodo.pdf`](02-curso-II/sesion-06/Sesion06_Revision_Metodo.pdf) |
| Revisión avances (S7) | [`02-curso-II/sesion-07/Sesion07_Revision_Avances.pdf`](02-curso-II/sesion-07/Sesion07_Revision_Avances.pdf) |
| Dataset piloto | [`piloto-bank-api-bian/`](piloto-bank-api-bian/) · [GitHub](https://github.com/denniskano/piloto-bank-api-bian) |
| Tesis | [`tesis-bank-api-bian/`](tesis-bank-api-bian/) · [GitHub](https://github.com/denniskano/tesis-bank-api-bian) |
| Plan Guía 1 (LaTeX) | [`01-curso-I/plan-tesis/latex/build/Plan_Tesis_Grupo10_final.pdf`](01-curso-I/plan-tesis/latex/build/Plan_Tesis_Grupo10_final.pdf) |
| Sílabo MIA 403 | [`02-curso-II/material-oficial/silabo/`](02-curso-II/material-oficial/silabo/) |

## Continuidad en una frase

Guía 1 **diseñó** S/E/C. MIA 403 **calcula** AlignmentScore sobre un piloto OFB, sin cambiar el objeto de la tesis.
