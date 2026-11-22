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
            "SemanticScore (S) + StructuralScore (E) + CoverageScore (C) → AlignmentScore. "
            "El prototipo implementa este modelo."
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
            "Ámbito: sector bancario; OpenAPI 3.x contra Service Domains BIAN. "
            "El prototipo ejecuta el procedimiento. Fuera: despliegue en producción y la corrida "
            "38×258. Umbrales 0,80 / 0,60 / 0,40: convención de diseño hasta el subconjunto etiquetado."
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
            "Elegido: tabla (operación, ruta, verbo, esquema, texto). Descartados: grafo y RDF."
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
            "Adquisición: 38 YAML de Open Finance Brasil y 258 Service Domains BIAN v14.0.0; "
            "el parser firma 296/296. Muestra de score, no el producto 38×258: "
            "I1 accounts 2.4.2 × Savings Account; I2 el mismo YAML × Current Account; "
            "I3a y I3b opendata-accounts 1.0.1 × Savings Account y Current Account; "
            "I4 payments 4.0.0 × Payment Order Initiation; "
            "I5 automatic-payments 2.0.0 × Payment Order Initiation; "
            "I6 enrollments 2.1.0 × Payment Order Initiation (control negativo). "
            "I1 con I2, e I3a con I3b, comparten YAML."
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
            "Elegido: greedy uno a uno. Candidato si el Jaccard del nombre ≥ 0,40, "
            "o la ruta toca el recurso del Service Domain, o el verbo coincide y el Jaccard "
            "del nombre ≥ 0,25. e_pair = 0,40 nombre + 0,25 ruta + 0,20 verbo HTTP + 0,15 "
            "profundidad. Sin par, la operación vale 0. GET y PUT pueden emparejarse."
        ),
        "vd": "StructuralScore (E) — alineación estructural OpenAPI ↔ BIAN",
        "hipotesis": (
            "Las técnicas de schema matching producen un StructuralScore que refleja "
            "la correspondencia entre la organización REST y el modelo BIAN."
        ),
        "metricas": (
            "StructuralScore E ∈ [0, 1]: media de e_pair sobre las operaciones del contrato. "
            "La operación sin par entra como 0. Nº de pares del greedy."
        ),
        "control": (
            "Mismo conjunto normalizado de la Fase 2. Los pares de E quedan congelados "
            "para el SemanticScore. I6 (enrollments × Payment Order Initiation) es control "
            "negativo de diseño: no comparte recurso."
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
            "Elegido, sobre los pares que congeló E: v0 = (Jaccard + coseno TF-IDF) / 2; "
            "v1 = coseno de paraphrase-multilingual-MiniLM-L12-v2, ya entrenado, sin fine-tuning. "
            "No se usa un modelo generativo para armar el par. E y C no se recalculan."
        ),
        "vd": "SemanticScore (S) — alineación semántica OpenAPI ↔ BIAN",
        "hipotesis": (
            "Las métricas de similitud semántica producen un SemanticScore que discrimina "
            "conceptos alineados de desalineaciones semánticas o de modelado."
        ),
        "metricas": (
            "SemanticScore S ∈ [0, 1], por separado en v0 (léxico) y v1 (MiniLM). "
            "Los cortes de coseno 0,45 / 0,55 / 0,65 no recortan el S oficial."
        ),
        "control": (
            "Mismos pares congelados de la Fase 3. OFB en portugués y BIAN en inglés. "
            "Modelo preentrenado, sin ajuste y sin GPU obligatoria."
        ),
    },
    {
        "fase": "Fase 5 — CoverageScore, AlignmentScore y clasificación (OE4 · P3–P4)",
        "problema": (
            "No existe un indicador integrado que combine alineación semántica, estructural "
            "y cobertura de conceptos BIAN, ni una escala interpretable de alineación global."
        ),
        "objetivo": (
            "Calcular CoverageScore (C), obtener AlignmentScore = (S + E + C) / 3 "
            "y clasificar el nivel de alineación del contrato OpenAPI. Reportar la sensibilidad "
            "de los pesos y, cuando haya etiquetas, precision, recall y F1."
        ),
        "producto": (
            "CoverageScore (C); AlignmentScore; clasificación (Alta ≥ 0,80 · Media 0,60–0,79 · "
            "Baja 0,40–0,59 · Nula < 0,40); scores por instancia. Precision, recall, F1 y kappa "
            "de Cohen cuando el subconjunto etiquetado esté cerrado."
        ),
        "vi": "Pesos de agregación (α, β, γ)",
        "estados": (
            "Oficial: α = β = γ = 1/3. Sensibilidad: (0,50, 0,30, 0,20) y (0,20, 0,50, 0,30)."
        ),
        "vd": "AlignmentScore — alineación global OpenAPI ↔ BIAN",
        "hipotesis": (
            "La agregación ponderada de S, E y C produce un AlignmentScore interpretable "
            "y clasificable por niveles de alineación del contrato OpenAPI bancario."
        ),
        "metricas": (
            "C = (CR y BQ con al menos un par) / (CR y BQ del Service Domain). "
            "AlignmentScore = (S + E + C) / 3. Nivel por instancia y por dominio (cuentas, pagos). "
            "Contra la etiqueta: precision, recall y F1. Un verdadero positivo es un par del greedy "
            "que el lector confirma; un falso positivo, un par que rechaza; un falso negativo, "
            "un par del lector que el greedy no armó. Kappa de Cohen del doble etiquetado."
        ),
        "control": (
            "Pesos oficiales iguales en el score que se reporta. Umbrales fijos como convención. "
            "Alex y Jack etiquetan match o no-match por recurso de negocio, no por el verbo HTTP. "
            "El asesor adjudica el desacuerdo cuando el programa lo designe. "
            "I6 no sustituye la etiqueta."
        ),
    },
]

META = {
    "titulo": "MATRIZ DE CONSISTENCIA",
    "subtitulo": (
        "Alineación entre contratos OpenAPI bancarios y modelos de referencia BIAN "
        "mediante análisis estructural y similitud semántica"
    ),
    "grupo": "Grupo 10 — Alex Mancilla · Dennis Jack Paitan",
    "problema_tecnologico": (
        "No existe un método reproducible que cuantifique en qué medida un contrato OpenAPI "
        "bancario se alinea con un Service Domain BIAN y bajo qué tipologías se desalinea."
    ),
    "objetivo_superior": (
        "Si el artefacto existiera: equipos de arquitectura/API podrían cuantificar la coherencia "
        "OpenAPI–BIAN antes del despliegue, reduciendo retrabajo en integraciones."
    ),
    "objetivo_general": (
        "Diseñar un modelo de alineación que defina cómo calcular SemanticScore (S), "
        "StructuralScore (E), CoverageScore (C) y un AlignmentScore integrado para evaluar "
        "contratos OpenAPI frente a Service Domains BIAN. Esta tesis entrega el modelo, "
        "el prototipo que lo calcula y el piloto de siete instancias."
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
        ws.row_dimensions[row].height = 120
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
            "(S + E + C) / 3; sensibilidad (0,50, 0,30, 0,20) y (0,20, 0,50, 0,30); "
            "clasificación Alta/Media/Baja/Nula",
            "Fase 5 · Cap. 4 §4.4",
        ),
        (
            "Prototipo",
            "Parser OpenAPI, matching greedy (v0) y MiniLM (v1) sobre las siete instancias",
            "Cap. 4 §4.2–§4.6",
        ),
        (
            "Muestra de score",
            "I1–I6: siete instancias OFB × BIAN v14. Fuera: 38×258 y el YAML de un banco emisor",
            "Cap. 4 §4.3 · §1.6",
        ),
        (
            "Referencia experta",
            "Doble etiquetado, kappa de Cohen, precision, recall y F1. Sin números hasta cerrar el subconjunto",
            "Cap. 4 §4.2 y §4.5",
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
