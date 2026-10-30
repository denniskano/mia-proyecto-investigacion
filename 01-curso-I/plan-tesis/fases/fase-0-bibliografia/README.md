# Fase 0 — Bibliografía y fichas de estado del arte

**Propósito:** Leer, clasificar y sistematizar los papers **antes** de redactar el marco teórico (Cap. 3).  
Alimenta **Anexo B**, **Tabla 5** (§3.5) y la **brecha** (§3.6).

**Objeto de estudio del proyecto:** contratos OpenAPI bancarios evaluados frente a Service Domains BIAN (referencia). Al leer cada paper, anotar si aporta técnicas para S, E o C del modelo de alineación.

> Esta fase corresponde a la tarea que el plan original llamaba «Fase C — matriz de papers».  
> Se ubica como **Fase 0** porque es prerequisito de A–G: sin fichas no hay estado del arte defendible.

## Entregables

| Archivo | Descripción |
|---------|-------------|
| `fichas/*.md` | Una ficha por paper (formato §3.5.2) |
| `../../anexos/Matriz_Papers_EstadoDelArte_Grupo9.2.xlsx` | Matriz consolidada (Anexo B) |
| `EJES_ESTADO_DEL_ARTE.md` | Mapa paper → eje temático |
| `CHECKLIST.md` | Progreso por paper |

## Flujo de trabajo

```
PDF en bibliografia/estado-del-arte/
    → leer paper
    → completar fichas/<id>.md
    → actualizar Excel (regenerar o editar)
    → marcar en CHECKLIST
```

## Ritmo sugerido

~3 papers/día → 14 papers en ≈ 5 días (2 integrantes: 7 cada uno).

## Regenerar Excel

```bash
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_matriz_papers.py
```

## Siguiente fase

Cap. 3 §3.5–§3.6 ✅ (Fase C) · §3.1–§3.4 ✅ (Fase E) · **Fase F** — Cap. 4 metodología.
