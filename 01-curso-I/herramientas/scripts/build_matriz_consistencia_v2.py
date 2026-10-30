#!/usr/bin/env python3
"""Matriz de consistencia v2 — columnas institucionales (8 cols). Grupo 9.2."""

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "plan-tesis/anexos/Matriz_Consistencia_Grupo9.2_v2.xlsx"

HEADERS = [
    "Problema de Estudio",
    "Objetivo General",
    "Objetivos Específicos",
    "Hipótesis",
    "Variables",
    "Metodología",
    "Técnicas e Instrumentos",
    "Resultados Esperados",
]

META = {
    "titulo": "MATRIZ DE CONSISTENCIA (v2)",
    "subtitulo": (
        "Alineación entre contratos OpenAPI bancarios y modelos de referencia BIAN "
        "mediante análisis estructural y similitud semántica"
    ),
    "grupo": "Grupo 9.2 — Alex Mancilla · Jack Paitan",
    "objetivo_general": (
        "Diseñar un modelo de alineación (SemanticScore S, StructuralScore E, CoverageScore C) "
        "y un procedimiento reproducible que, sobre cada instancia "
        "contrato OpenAPI bancario × Service Domain BIAN, calcule el AlignmentScore ∈ [0, 1] "
        "y la clasificación por niveles (Alta / Media / Baja / Nula), documentado en la Guía 1 "
        "(Cap. 2 §2.3). Base de medición: par contrato + extracto BIAN; VD del artefacto: "
        "AlignmentScore + clasificación."
    ),
}

ROWS = [
    {
        "problema": (
            "Problema tecnológico (Fase 1): no existe un procedimiento documentado y reproducible "
            "que cuantifique en qué medida un contrato OpenAPI bancario se alinea con un "
            "Service Domain BIAN y bajo qué tipologías se desalinea (distinto de la problemática "
            "del sector, §1.2)."
        ),
        "og": META["objetivo_general"],
        "oe": (
            "Marco del plan: definir entradas, componentes S/E/C, fórmula AlignmentScore = "
            "α·S + β·E + γ·C, umbrales y criterios de verificación (Fase 1 — diseño del modelo)."
        ),
        "hipotesis": (
            "Un modelo estructurado por componentes S, E y C permite calcular de forma "
            "reproducible un score de alineación interpretable entre OpenAPI y BIAN."
        ),
        "variables": (
            "VI: esquema S/E/C; pesos α, β, γ. VD (artefacto): definición documentada de scores "
            "y trazabilidad. Control: ámbito bancario; OpenAPI 3.x; alcance Guía 1 (diseño)."
        ),
        "metodologia": (
            "Investigación tecnológica · Design Science. Fase 1 — Diseñar el modelo de alineación "
            "y el procedimiento (Anexo C)."
        ),
        "tecnicas": (
            "Revisión documental; modelado conceptual; matriz de consistencia; redacción del "
            "procedimiento §4.2 (sin implementación en producción)."
        ),
        "resultados": (
            "Modelo metodológico documentado: adquisición → normalización → S + E + C → "
            "AlignmentScore."
        ),
    },
    {
        "problema": (
            "Los contratos OpenAPI bancarios y los Service Domains BIAN expresan el dominio en "
            "vistas distintas (REST vs. negocio), lo que impide compararlos directamente (P1, P2). "
            "Falta adquisición versionada de artefactos antes del análisis."
        ),
        "og": "Contribuye al OG: habilitar mediciones sobre representaciones comparables (OE1).",
        "oe": (
            "OE1 — Adquirir y normalizar: transformar contrato OpenAPI y extracto BIAN en "
            "representaciones normalizadas sobre un modelo intermedio común."
        ),
        "hipotesis": (
            "La normalización de OpenAPI bancario y BIAN en un modelo intermedio común habilita "
            "el cálculo sistemático de los scores S, E y C."
        ),
        "variables": (
            "VI: esquema de representación intermedia (tabular / grafo / RDF). "
            "VD (ratio OE1): completitud de extracción (extraídos / esperados). "
            "Control: versión fija contrato + SD; herramientas de parsing fijas."
        ),
        "metodologia": (
            "Fase 2 — Adquirir artefactos (§4.3) y normalizar (OE1): parsing OpenAPI 3.x; "
            "extracción paths, operations, schemas, behaviors, business objects."
        ),
        "tecnicas": (
            "Adquisición de datos (YAML/JSON versionado); parsing OpenAPI 3.x; extracción "
            "estructural; metadatos por instancia {fuente}_{service-domain}_{version}."
        ),
        "resultados": (
            "Representaciones normalizadas versionadas listas para matching y cálculo de scores."
        ),
    },
    {
        "problema": (
            "No se conocen las correspondencias de jerarquía entre endpoints, recursos y esquemas "
            "OpenAPI y los elementos del Service Domain BIAN (P1)."
        ),
        "og": "Contribuye al OG: cuantificar dimensión estructural (StructuralScore E).",
        "oe": (
            "OE2 — Emparejar estructuras: calcular correspondencias y StructuralScore (E) ∈ [0, 1]."
        ),
        "hipotesis": (
            "Las técnicas de schema matching producen un StructuralScore que refleja la "
            "correspondencia entre la organización REST y el modelo BIAN."
        ),
        "variables": (
            "VI: estrategia de schema matching (nombre, ruta, profundidad, operación HTTP). "
            "VD (ratio OE2): StructuralScore (E). "
            "Control: mismo conjunto normalizado OE1; umbral de correspondencia fijo."
        ),
        "metodologia": (
            "Fase 3 — Emparejar estructuras (OE2): matriz de correspondencias endpoint/schema ↔ "
            "Behavior/BusinessObject."
        ),
        "tecnicas": (
            "Schema matching (Shvaiko & Euzenat, 2005): correspondencia por nombre, ruta, "
            "profundidad de esquema y operación HTTP; no aprendizaje supervisado."
        ),
        "resultados": (
            "Matriz de correspondencias estructurales y StructuralScore (E) normalizado [0, 1]."
        ),
    },
    {
        "problema": (
            "Se desconoce el grado de equivalencia semántica entre términos BIAN y "
            "nombres/descripciones en contratos OpenAPI bancarios (P2)."
        ),
        "og": "Contribuye al OG: cuantificar dimensión semántica (SemanticScore S).",
        "oe": (
            "OE3 — Calcular similitud semántica: SemanticScore (S) ∈ [0, 1] entre conceptos "
            "OpenAPI y BIAN."
        ),
        "hipotesis": (
            "Las métricas de similitud semántica producen un SemanticScore que discrimina "
            "conceptos alineados de desalineaciones semánticas o de modelado."
        ),
        "variables": (
            "VI: técnica de similitud semántica (embeddings / ontología / híbrido). "
            "VD (ratio OE3): SemanticScore (S). "
            "Control: mismo corpus de términos; umbral de similitud fijo."
        ),
        "metodologia": (
            "Fase 4 — Calcular similitud semántica (OE3) sobre representaciones de OE1."
        ),
        "tecnicas": (
            "Similitud semántica (El Bayadh et al., 2015; Chandrasekaran & Mago, 2022): "
            "embeddings + coseno, matching léxico/ontológico u híbrido."
        ),
        "resultados": "Matriz de similitud semántica y SemanticScore (S) normalizado [0, 1].",
    },
    {
        "problema": (
            "No existe un indicador integrado que combine S, E y C ni una escala interpretable "
            "de alineación global por instancia contrato × SD (P3, P4)."
        ),
        "og": (
            "Contribuye al OG: entregar AlignmentScore y clasificación — VD global del artefacto."
        ),
        "oe": (
            "OE4 — Integrar: CoverageScore (C), AlignmentScore = α·S + β·E + γ·C y clasificación "
            "por tipologías de desalineación."
        ),
        "hipotesis": (
            "La agregación ponderada de S, E y C produce un AlignmentScore interpretable y "
            "clasificable por niveles de alineación del contrato OpenAPI bancario."
        ),
        "variables": (
            "VI: pesos α, β, γ (α+β+γ=1). "
            "VD (artefacto): AlignmentScore + clasificación Alta/Media/Baja/Nula. "
            "VD (ratio OE4): CoverageScore (C). "
            "Control: pesos fijos; taxonomía §1.4; umbrales 0,80 / 0,60 / 0,40."
        ),
        "metodologia": (
            "Fase 5 — Integrar y clasificar (OE4): agregación ponderada e informe de tipologías."
        ),
        "tecnicas": (
            "Agregación lineal α·S + β·E + γ·C; reglas de clasificación; tipologías Tabla 2 Cap. 1. "
            "Validación empírica del prototipo: Tesis 2 (ground truth especialistas)."
        ),
        "resultados": (
            "CoverageScore (C); AlignmentScore; clasificación (Alta ≥0,80 · Media · Baja · Nula); "
            "informe de tipologías de desalineación."
        ),
    },
]


def style_header(cell):
    cell.font = Font(bold=True, color="FFFFFF", size=10)
    cell.fill = PatternFill("solid", fgColor="2F5496")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin"),
    )


def style_body(cell):
    cell.font = Font(size=10)
    cell.alignment = Alignment(vertical="top", wrap_text=True)
    cell.border = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin"),
    )


def build():
    wb = Workbook()
    ws = wb.active
    ws.title = "Matriz v2"

    ncols = len(HEADERS)
    last_col = get_column_letter(ncols)

    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = META["titulo"]
    ws["A1"].font = Font(bold=True, size=14)
    ws["A1"].alignment = Alignment(horizontal="center")

    ws.merge_cells(f"A2:{last_col}2")
    ws["A2"] = META["subtitulo"]
    ws["A2"].font = Font(size=10, italic=True)
    ws["A2"].alignment = Alignment(horizontal="center", wrap_text=True)

    ws.merge_cells(f"A3:{last_col}3")
    ws["A3"] = META["grupo"]
    ws["A3"].alignment = Alignment(horizontal="center")

    start_row = 5
    for col, header in enumerate(HEADERS, 1):
        cell = ws.cell(row=start_row, column=col, value=header)
        style_header(cell)

    keys = [
        "problema",
        "og",
        "oe",
        "hipotesis",
        "variables",
        "metodologia",
        "tecnicas",
        "resultados",
    ]
    for r_idx, row in enumerate(ROWS, start_row + 1):
        for c_idx, key in enumerate(keys, 1):
            cell = ws.cell(row=r_idx, column=c_idx, value=row[key])
            style_body(cell)

    widths = [26, 28, 26, 24, 28, 24, 26, 26]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

    for row in range(start_row, start_row + len(ROWS) + 1):
        ws.row_dimensions[row].height = 95 if row > start_row else 40

    ws.freeze_panes = f"A{start_row + 1}"

    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print(f"Guardado: {OUT}")


if __name__ == "__main__":
    build()
