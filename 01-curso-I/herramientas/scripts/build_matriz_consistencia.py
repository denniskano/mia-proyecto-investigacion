#!/usr/bin/env python3
"""Genera Matriz de Consistencia (Anexo C) — Grupo 10."""

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "plan-tesis/anexos/Matriz_Consistencia_Grupo10.xlsx"

HEADERS = [
    "Fase",
    "Problema",
    "Objetivo",
    "Producto verificable",
    "Factor",
    "Estados del factor",
    "Ratio (resultado)",
    "Hipótesis",
    "Indicadores / Métricas del ratio",
    "Parámetros de control",
]

ROWS = [
    {
        "fase": "Fase 1 — Diseño del modelo de alineación",
        "problema": (
            "Problema tecnológico (Fase 1): no existe un método reproducible que cuantifique "
            "en qué medida un contrato OpenAPI bancario se alinea con un Service Domain BIAN "
            "y bajo qué tipologías se desalinea (distinto de la problemática del sector, §1.2)."
        ),
        "objetivo": (
            "Diseñar el modelo de alineación OpenAPI ↔ BIAN, definiendo entradas, "
            "componentes de score (S, E, C), fórmula de agregación y criterios de clasificación."
        ),
        "producto": (
            "Modelo metodológico documentado: adquisición → normalización → "
            "SemanticScore (S) + StructuralScore (E) + CoverageScore (C) → AlignmentScore."
        ),
        "vi": "No aplica",
        "estados": "No aplica",
        "vd": "Adecuación del diseño del modelo",
        "hipotesis": (
            "Un modelo estructurado por componentes S, E y C permite calcular de forma "
            "reproducible un score de alineación interpretable entre OpenAPI y BIAN."
        ),
        "metricas": (
            "Cobertura del modelo (nº de etapas y scores definidos), trazabilidad "
            "entrada→salida, criterios de validez explícitos."
        ),
        "control": (
            "Ámbito: sector bancario; contratos OpenAPI 3.x evaluados contra Service Domains BIAN; "
            "alcance documental (sin despliegue en producción)."
        ),
    },
    {
        "fase": "Fase 2 — Adquisición y normalización de artefactos (OE1)",
        "problema": (
            "Los contratos OpenAPI bancarios y los Service Domains BIAN expresan el dominio "
            "en vistas conceptuales distintas (REST vs. negocio), lo que impide compararlos "
            "directamente (P1, P2)."
        ),
        "objetivo": (
            "Transformar contratos OpenAPI y artefactos BIAN en representaciones "
            "normalizadas y comparables sobre un modelo intermedio común."
        ),
        "producto": (
            "Conjunto de representaciones normalizadas versionadas (paths, operations, schemas, "
            "behaviors, business objects) listas para el cálculo de scores."
        ),
        "vi": "Esquema de representación intermedia",
        "estados": (
            "Modelo tabular (recurso–operación–esquema); modelo en grafo (nodos/aristas); "
            "modelo RDF/triples (opcional)."
        ),
        "vd": "Calidad y completitud de la extracción estructural",
        "hipotesis": (
            "La normalización de OpenAPI bancario y BIAN en un modelo intermedio común "
            "habilita el cálculo sistemático de los scores S, E y C."
        ),
        "metricas": (
            "Nº de elementos extraídos (endpoints, schemas, behaviors, business objects); "
            "% de cobertura respecto al artefacto fuente; integridad de metadatos."
        ),
        "control": (
            "Versión fija del contrato OpenAPI y del Service Domain BIAN emparejados; "
            "herramientas de parsing fijas; mismo ámbito sectorial."
        ),
    },
    {
        "fase": "Fase 3 — Cálculo del StructuralScore E (OE2 · P1)",
        "problema": (
            "No se conocen las correspondencias de jerarquía y organización entre endpoints, "
            "recursos y esquemas OpenAPI y los elementos del Service Domain BIAN."
        ),
        "objetivo": (
            "Calcular el StructuralScore (E): correspondencia estructural entre componentes "
            "OpenAPI y artefactos BIAN normalizados."
        ),
        "producto": (
            "Matriz de correspondencias estructurales y StructuralScore (E) normalizado [0, 1]."
        ),
        "vi": "Estrategia de matching estructural (schema matching)",
        "estados": (
            "Correspondencia por nombre exacto; similitud de ruta/recurso; "
            "correspondencia por profundidad y tipo de esquema; matching por operación HTTP."
        ),
        "vd": "StructuralScore (E) — alineación estructural OpenAPI ↔ BIAN",
        "hipotesis": (
            "Las técnicas de schema matching producen un StructuralScore que refleja "
            "la correspondencia entre la organización REST y el modelo BIAN."
        ),
        "metricas": (
            "StructuralScore E ∈ [0, 1]; tasa de correspondencia estructural (%); "
            "nº de pares alineados; desalineaciones estructurales detectadas."
        ),
        "control": (
            "Mismo conjunto normalizado de la Fase 2; umbral de correspondencia fijo; "
            "sin intervención manual en el matching."
        ),
    },
    {
        "fase": "Fase 4 — Cálculo del SemanticScore S (OE3 · P2)",
        "problema": (
            "Se desconoce el grado de equivalencia semántica entre términos de negocio BIAN "
            "y nombres/descripciones en contratos OpenAPI bancarios."
        ),
        "objetivo": (
            "Calcular el SemanticScore (S): similitud semántica entre conceptos de negocio BIAN "
            "y componentes del contrato OpenAPI."
        ),
        "producto": (
            "Matriz de similitud semántica y SemanticScore (S) normalizado [0, 1]."
        ),
        "vi": "Técnica de similitud semántica",
        "estados": (
            "Embeddings + similitud coseno; matching léxico/ontológico; "
            "enfoque híbrido (estructural + semántico)."
        ),
        "vd": "SemanticScore (S) — alineación semántica OpenAPI ↔ BIAN",
        "hipotesis": (
            "Las métricas de similitud semántica producen un SemanticScore que discrimina "
            "conceptos alineados de desalineaciones semánticas o de modelado."
        ),
        "metricas": (
            "SemanticScore S ∈ [0, 1]; similitud coseno promedio; "
            "nº de pares sobre umbral; distribución por tipología (semántica, modelado)."
        ),
        "control": (
            "Mismo corpus de términos; umbral de similitud fijo; "
            "misma técnica de embedding/modelo por corrida."
        ),
    },
    {
        "fase": "Fase 5 — CoverageScore, AlignmentScore y clasificación (OE4 · P3–P4)",
        "problema": (
            "No existe un indicador integrado que combine alineación semántica, estructural "
            "y cobertura de conceptos BIAN, ni una escala interpretable de alineación global."
        ),
        "objetivo": (
            "Calcular CoverageScore (C), obtener AlignmentScore = α·S + β·E + γ·C "
            "(α + β + γ = 1) y clasificar el nivel de alineación del contrato OpenAPI."
        ),
        "producto": (
            "CoverageScore (C); AlignmentScore; clasificación (Alta ≥0,80 · Media 0,60–0,79 · "
            "Baja 0,40–0,59 · Nula <0,40); informe de tipologías de desalineación."
        ),
        "vi": "Pesos de agregación (α, β, γ)",
        "estados": (
            "Pesos iguales (α=β=γ=1/3); ponderación experta; "
            "sensibilidad por tipología dominante."
        ),
        "vd": "AlignmentScore — alineación global OpenAPI ↔ BIAN",
        "hipotesis": (
            "La agregación ponderada de S, E y C produce un AlignmentScore interpretable "
            "y clasificable por niveles de alineación del contrato OpenAPI bancario."
        ),
        "metricas": (
            "CoverageScore C ∈ [0, 1]; AlignmentScore = α·S + β·E + γ·C; "
            "nivel de alineación (Alta/Media/Baja/Nula); frecuencia por tipología "
            "(estructural, semántica, modelado, REST/contrato)."
        ),
        "control": (
            "Pesos α + β + γ = 1 fijos por corrida; mismos S, E, C de Fases 3–4; "
            "misma taxonomía de desalineaciones (Tabla 2, Cap. 1); umbrales de clasificación fijos."
        ),
    },
]

META = {
    "titulo": "MATRIZ DE CONSISTENCIA",
    "subtitulo": (
        "Alineación entre contratos OpenAPI bancarios y modelos de referencia BIAN "
        "mediante análisis estructural y similitud semántica"
    ),
    "grupo": "Grupo 10 — Alex Mancilla · Jack Paitan",
    "problema_tecnologico": (
        "No existe un método reproducible que cuantifique en qué medida un contrato OpenAPI "
        "bancario se alinea con un Service Domain BIAN y bajo qué tipologías se desalinea."
    ),
    "objetivo_superior": (
        "Si el artefacto existiera: equipos de arquitectura/API podrían cuantificar la coherencia "
        "OpenAPI–BIAN antes del despliegue, reduciendo retrabajo en integraciones."
    ),
    "objetivo_general": (
        "Diseñar un modelo de alineación y el procedimiento que calculen SemanticScore (S), "
        "StructuralScore (E), CoverageScore (C) y AlignmentScore integrado para evaluar "
        "contratos OpenAPI frente a Service Domains BIAN (Guía 1)."
    ),
}


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
    ws.title = "Matriz de consistencia"

    ws.merge_cells("A1:J1")
    ws["A1"] = META["titulo"]
    ws["A1"].font = Font(bold=True, size=14)
    ws["A1"].alignment = Alignment(horizontal="center")

    ws.merge_cells("A2:J2")
    ws["A2"] = META["subtitulo"]
    ws["A2"].font = Font(size=10, italic=True)
    ws["A2"].alignment = Alignment(horizontal="center", wrap_text=True)

    ws.merge_cells("A3:J3")
    ws["A3"] = META["grupo"]
    ws["A3"].alignment = Alignment(horizontal="center")

    ws.merge_cells("A4:E4")
    ws["A4"] = f"Problema tecnológico: {META['problema_tecnologico']}"
    ws["A4"].alignment = Alignment(wrap_text=True)

    ws.merge_cells("F4:J4")
    ws["F4"] = f"Objetivo general (técnico): {META['objetivo_general']}"
    ws["F4"].alignment = Alignment(wrap_text=True)

    ws.merge_cells("A5:J5")
    ws["A5"] = f"Objetivo superior: {META['objetivo_superior']}"
    ws["A5"].alignment = Alignment(wrap_text=True)

    start_row = 7
    for col, header in enumerate(HEADERS, 1):
        cell = ws.cell(row=start_row, column=col, value=header)
        style_header(cell)

    for r_idx, row in enumerate(ROWS, start_row + 1):
        values = [
            row["fase"],
            row["problema"],
            row["objetivo"],
            row["producto"],
            row["vi"],
            row["estados"],
            row["vd"],
            row["hipotesis"],
            row["metricas"],
            row["control"],
        ]
        for c_idx, value in enumerate(values, 1):
            cell = ws.cell(row=r_idx, column=c_idx, value=value)
            style_body(cell)

    widths = [22, 28, 28, 26, 22, 26, 22, 28, 28, 26]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

    for row in range(start_row, start_row + len(ROWS) + 1):
        ws.row_dimensions[row].height = 80
    ws.row_dimensions[start_row].height = 36

    ws.freeze_panes = f"A{start_row + 1}"

    ws2 = wb.create_sheet("Resumen OG-OE")
    resumen_headers = ["Elemento", "Descripción", "Vinculación"]
    for col, h in enumerate(resumen_headers, 1):
        cell = ws2.cell(row=1, column=col, value=h)
        style_header(cell)

    resumen = [
        ("Problemática (situación real)", "Síntomas sector bancario — §1.2", "Cap. 1 §1.2"),
        ("Problema abstracto", "Correspondencia OpenAPI ↔ BIAN — §1.3", "Cap. 1 §1.3"),
        ("Problema tecnológico", META["problema_tecnologico"], "Cap. 1 §1.3 · Anexo C"),
        ("Objetivo superior", META["objetivo_superior"], "Cap. 2 §2.2"),
        ("Objetivo general (técnico)", META["objetivo_general"], "Cap. 2 §2.3"),
        ("OE1", ROWS[1]["objetivo"], "Fase 2 — Normalización"),
        ("OE2", ROWS[2]["objetivo"], "Fase 3 — StructuralScore (E)"),
        ("OE3", ROWS[3]["objetivo"], "Fase 4 — SemanticScore (S)"),
        ("OE4", ROWS[4]["objetivo"], "Fase 5 — CoverageScore + AlignmentScore"),
        ("P1", "Correspondencia estructural → E", "Fase 3"),
        ("P2", "Similitud semántica → S", "Fase 4"),
        ("P3–P4", "Cobertura + score global → C + AlignmentScore", "Fase 5"),
        ("SemanticScore (S)", "Similitud de significado OpenAPI ↔ BIAN", "Fase 4"),
        ("StructuralScore (E)", "Correspondencia de jerarquía y organización", "Fase 3"),
        ("CoverageScore (C)", "Conceptos BIAN cubiertos por el contrato", "Fase 5"),
        (
            "AlignmentScore",
            "α·S + β·E + γ·C (α+β+γ=1); clasificación Alta/Media/Baja/Nula",
            "Fase 5 · Anexo figuras_alineacion_openapi_bian.pdf",
        ),
    ]
    for r, (a, b, c) in enumerate(resumen, 2):
        for col, val in enumerate((a, b, c), 1):
            cell = ws2.cell(row=r, column=col, value=val)
            style_body(cell)
    ws2.column_dimensions["A"].width = 20
    ws2.column_dimensions["B"].width = 55
    ws2.column_dimensions["C"].width = 32

    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print(f"Guardado: {OUT}")


if __name__ == "__main__":
    build()
