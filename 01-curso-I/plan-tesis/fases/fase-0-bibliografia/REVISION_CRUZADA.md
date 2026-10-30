# Revisión cruzada — Fichas estado del arte (Grupo 9.2)

**Fecha simulada:** 2026-05-28  
**Revisores:** Alex Mancilla → fichas de Jack · Jack Paitan → fichas de Alex  
**Criterios:** `PLANTILLA_FICHA.md`, `EJES_ESTADO_DEL_ARTE.md`, Cap. 1 LaTeX (`latex/chapters/cap01-planteamiento/`)

---

## Resumen ejecutivo

| Revisor | Fichas revisadas | Aprobadas | Con observaciones | Requiere corrección |
|---------|------------------|-----------|-------------------|-------------------|
| Alex → Jack | 7 | 2 | 4 | 1 (E5-03) |
| Jack → Alex | 7 | 4 | 3 | 0 |

**Veredicto global:** lote **aprobado para Fase C** tras correcciones menores aplicadas (ver commit en fichas). Pendiente: validación humana Alex/Jack en 15 min.

---

## Alex revisa fichas de Jack

| ID | Veredicto | Observación clave |
|----|-----------|-------------------|
| E1-02 Mainas 2023 | Aprobada con obs. | Distinguir enriquecimiento semántico vs. cálculo de S |
| E2-01 Shvaiko 2005 | Aprobada | — |
| E3-02 Chandrasekaran 2022 | Aprobada con obs. | Criterio de citación 2022 (catálogo) |
| E4-01 Schmidt 2020 | Aprobada con obs. | Tipo → SLR |
| E5-01 Ehsan 2022 | Aprobada | Tipo → SLR |
| E5-03 Otieno 2026 | **Corregida** | Vol. 5(1), año 2026 (no Vol. 6 / 2025) |
| E5-05 Vitorino 2025 | Aprobada con obs. | Periferia OpenAPI; peso menor en síntesis E5 |

**Riesgos transversales (Jack):** metadatos bibliográficos; no confundir técnica del paper con score del modelo; E5 heterogéneo — priorizar Ehsan/Otieno en §3.5.

---

## Jack revisa fichas de Alex

| ID | Veredicto | Observación clave |
|----|-----------|-------------------|
| E1-01 Casas 2021 | Aprobada | — |
| E1-03 Santos y Casas 2025 | Aprobada con obs. | E1 periférico (gateway runtime) |
| E3-01 El Bayadh 2015 | Aprobada con obs. | §9: S y C, **no E** del modelo tesis |
| E3-03 Santos Sousa 2026 | Aprobada | Matiz E = grafo ontológico |
| E5-02 Golmohammadi 2024 | Aprobada | — |
| E5-04 Tanveer 2025 | Aprobada | — |
| E6-01 Mahanra Rao 2025 | Aprobada con obs. | S = selección, no validación BIAN |

**Riesgos transversales (Alex):** deriva del significado de **E** (StructuralScore); vacío §7 repetitivo — graduar en Fase C; lote Alex = más **borde** (E5/E6) que núcleo técnico.

---

## Acuerdos de equipo (post-revisión)

1. **StructuralScore (E)** solo cuando el aporte sea correspondencia REST (paths/operations/schemas) ↔ BIAN; no confundir con estructura ontológica genérica.
2. **SemanticScore (S)** vía embeddings/ontología/similitud léxica; Mainas aporta **representación**, no score predefinido.
3. **Papers E5/E6** en §3.5: rol de **delimitación** explícita, no como solución parcial.
4. **Citas:** usar año del catálogo Grupo 9.2; nota al pie si publicación difiere (Chandrasekaran 2022; Golmohammadi 2024).

---

## Correcciones aplicadas en fichas

- E5-03: metadatos Vol. 5(1), año 2026
- E3-01: §9 S/C sin E del modelo
- E1-02, E1-03, E4-01, E5-01, E5-05, E6-01: matices §7/§9 según observaciones
- E3-03: §9 matiz E = grafo ontológico ≠ StructuralScore REST↔BIAN
- Excel Anexo B regenerado

---

*Simulación asistida por revisión especializada; sustituir por firma Alex/Jack en entrega formal.*
