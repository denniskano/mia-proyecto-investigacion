# Plan de Tesis — LaTeX (Grupo 9.2)

Documento colaborativo Alex Mancilla · Jack Paitan.

## Compilar

Desde la raíz del repo (`plan-tesis/`):

```bash
cd latex
make pdf
# Salida: build/Plan_Tesis_Grupo9.2.pdf
```

Figuras en `../figuras/` (ver `../figuras/README.md`). No commitear `build/` — ver `../.gitignore`.

## Estructura y estado

| Ruta | Contenido | Estado |
|------|-----------|--------|
| `main.tex` | Ensamblado | ✅ |
| `config/` | Paquetes, metadatos, macros S/E/C | ✅ |
| `frontmatter/` | Portada, datos generales, resumen, abstract | ✅ Anexo III |
| `chapters/cap01-planteamiento/` | Cap. 1 | ✅ Fase B |
| `chapters/cap02-objetivos/` | Cap. 2 | ✅ Fase D |
| `chapters/cap03-marco/` | Cap. 3 §3.1–§3.6 | ✅ Fases C + E |
| `chapters/cap05-administracion/` | Cap. 5 | ✅ Fase G |
| `chapters/cap04-metodologia/` | Cap. 4 | ✅ Fase F |
| `anexos/` | Anexos A–F | ✅ Fase G |
| `frontmatter/referencias.tex` | Bibliografía APA | ✅ |
| `referencias.bib` | Export Zotero / plataforma | ✅ |

## Figuras

Índice: `../figuras/README.md`

| Carpeta | Figuras |
|---------|---------|
| `../figuras/cap01/` | 1, 2 |
| `../figuras/cap02/` | 4 |
| `../figuras/cap03/` | 5, 6 |
| `../figuras/modelo-alineacion/` | 3, 7 + apoyos S/C |

```bash
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_figuras_fase_b.py
herramientas/.venv-excel/bin/python3 herramientas/scripts/build_figuras_fase_cd.py
```

## Colaboración Git

- Un PR por sección (`.tex` individual).
- Macros en `config/commands.tex`: `\SemanticScore`, `\AlignmentScore`, etc.

## Anexo III (Guía N°01)

- Fuente: Helvetica 11 pt (sustituto de Arial), márgenes 3/2,5 cm, interlineado 1,5 / 1,0 en índices, anexos y referencias.
- Escudo UNI: `frontmatter/escudo-uni.png` (carátula Anexo III).

## Pendiente (no es redacción LaTeX)

- [x] Cap. 4 completo (Fase F) — 2026-07-02
- [x] Escudo UNI en `frontmatter/escudo-uni.png`
- [ ] Actualizar `\asesorPlan` en `config/metadata.tex` cuando se asigne asesor
- [ ] Verificar DOI en Zotero vs. `referencias.bib`
- [ ] Segundo Turnitin · subir aula virtual (PI-03)
