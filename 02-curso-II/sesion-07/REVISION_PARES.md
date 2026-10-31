# Revisión de pares — Sesión 7 (slides)

**Fecha:** 30 oct 2026  
**Documento:** `Sesion07_Revision_Avances_slides.pdf` (v1 Beamer)  
**Veredicto:** **no proyectable tal cual.** El contenido es el de la lámina; el diseño impide leerlo.

## Hallazgos

| # | Hallazgo | Gravedad |
|---|----------|----------|
| 1 | `\rowcolor` + Beamer: cabecera y filas quedan **blanco sobre navy**. La tabla de Trello no se distingue | Alta |
| 2 | Columnas sin ancho fijo: «Estado» flota; no hay reglas ni padding | Alta |
| 3 | Fórmulas de $E$/$S$/$C$ se rompen (`P epair`, `\mathrm` ilegible) | Alta |
| 4 | Filas largas parten mal (H1, métricas, criterios, OFB ≠ tesis) | Media |
| 5 | Portada y cierre son un bloque de texto; revistas sin marco | Media |
| 6 | Tablero Trello parte «Bloqueado» en la línea siguiente | Baja |
| 7 | `$S/E/C$` en tabla se ve como fórmula suelta, no como etiquetas | Baja |

## Lo que está bien (no tocar el fondo)

1. Encaje con la lámina: Trello, cuaderno, métricas, 2 revistas.
2. Objeto vs piloto (OpenAPI bancario / OFB).
3. Cifras 41 / 235 / EDA alineadas con `inventario.json`.
4. Criterios de éxito por hito (S7 → P4 → P7).
5. Revistas: *Journal of Web Semantics* y *Semantic Web Journal*.

## Correcciones aplicadas

- Tablas con cabecera navy **celda a celda** y cuerpo negro sobre blanco/gris.
- Fórmulas en prosa, no en `\mathrm`.
- Portada navy, KPIs y revistas en cajas.
- Recompilar: `pdflatex Sesion07_Revision_Avances_slides.tex`.
