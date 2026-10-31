#!/usr/bin/env python3
"""Matriz de consistencia Plan v2 — objeto OpenAPI bancario; piloto OFB. Grupo 10."""

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

OUT = Path(__file__).resolve().parent / "Matriz_Consistencia_OFB_Grupo10.xlsx"

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

OG = (
    "Calcular, sobre cada instancia contrato OpenAPI bancario × Service Domain BIAN, "
    "el AlignmentScore ∈ [0, 1] y la clasificación (Alta / Media / Baja / Nula), "
    "mediante S, E y C. Verificación empírica de este curso: corpus piloto "
    "(38 APIs Open Finance Brasil + 3 SD BIAN v14)."
)

META = {
    "titulo": "MATRIZ DE CONSISTENCIA — Plan de tesis v2 (MIA 403)",
    "subtitulo": (
        "Alineación entre contratos OpenAPI bancarios y modelos de referencia BIAN "
        "mediante análisis estructural y similitud semántica (piloto: Open Finance Brasil)"
    ),
    "grupo": "Grupo 10 — Alex Mancilla Antay · Jack Paitan Cano · objeto = OpenAPI bancario · referencia = BIAN · piloto = OFB",
}

ROWS = [
    {
        "problema": (
            "No hay un procedimiento ejecutado que cuantifique en qué medida un "
            "contrato OpenAPI bancario se alinea con un Service Domain BIAN "
            "ni bajo qué tipologías se desalinea. La Guía 1 diseñó S/E/C; "
            "la Guía 2 lo mide primero en el piloto Open Finance Brasil."
        ),
        "og": OG,
        "oe": (
            "Marco del plan v2: objeto OpenAPI bancario, piloto OFB, pares I1–I6, fórmula "
            "AlignmentScore = α·S + β·E + γ·C, umbrales y criterios de verificación."
        ),
        "hipotesis": (
            "Un modelo S, E y C permite calcular de forma reproducible un score "
            "interpretable entre contratos OpenAPI bancarios y Service Domains BIAN."
        ),
        "variables": (
            "VI: esquema S/E/C; pesos α, β, γ. VD (artefacto): AlignmentScore + "
            "clasificación. Control: OpenAPI 3.x; BIAN v14; muestra del curso = OFB."
        ),
        "metodologia": (
            "Investigación tecnológica · Design Science. Fase 1 (diseño) heredada "
            "de Guía 1; Fases 2–5 se ejecutan en MIA 403."
        ),
        "tecnicas": (
            "Revisión documental; matriz institucional de 8 columnas; "
            "PLAN_TESIS_V2.md; inventario OFB de la Sesión 5."
        ),
        "resultados": (
            "Plan v2 + pares declarados I1–I6 + protocolo empírico "
            "(aún sin scores globales)."
        ),
    },
    {
        "problema": (
            "REST OFB (mayoría GET) y la vista de negocio BIAN (CR/BQ, mayoría PUT) "
            "no son comparables en crudo. Falta firmar la completitud del parser "
            "sobre el catálogo OFB ya adquirido."
        ),
        "og": "Contribuye al OG: habilitar mediciones sobre representaciones comparables (OE1).",
        "oe": (
            "OE1 — Adquirir y normalizar YAML OFB y BIAN versionados "
            "(parser OpenAPI 3.x → CSV)."
        ),
        "hipotesis": (
            "H1: la normalización OFB y BIAN a un esquema intermedio común "
            "habilita el cálculo sistemático de S, E y C."
        ),
        "variables": (
            "VI: esquema intermedio tabular. VD (ratio OE1): completitud "
            "(extraídos / esperados). Control: versiones congeladas."
        ),
        "metodologia": (
            "Fase 2. Universo: 38 APIs OFB + 3 SD BIAN. La muestra de scores "
            "son siete instancias (I1–I6, I3 desdoblada); el resto es inventario."
        ),
        "tecnicas": (
            "procesar_openapi.py; resolución de $ref anidados; metadatos "
            "{OFB|BIAN}_{api}_{versión}."
        ),
        "resultados": (
            "41 contratos, 235 operaciones, 6 746 propiedades, 10 906 textos; "
            "informe de completitud por contrato."
        ),
    },
    {
        "problema": (
            "Se desconocen las correspondencias path / operation / schema OFB ↔ "
            "Behavior / Business Object / BQ (P1)."
        ),
        "og": "Contribuye al OG: cuantificar la dimensión estructural (StructuralScore E).",
        "oe": "OE2 — Matriz de pares y StructuralScore E ∈ [0, 1] en las instancias I1–I6.",
        "hipotesis": (
            "H2: el schema matching distingue correspondencia REST ↔ CR/BQ "
            "sin exigir el mismo verbo HTTP."
        ),
        "variables": (
            "VI: estrategia (nombre, ruta, HTTP relajado, profundidad). "
            "VD (ratio OE2): E. Control: umbral Jaccard fijo; mismo OE1."
        ),
        "metodologia": (
            "Fase 3. Emparejamiento greedy 1–1 (operación OFB → Behavior BIAN) "
            "solo en pares declarados."
        ),
        "tecnicas": (
            "Schema matching (Shvaiko y Euzenat, 2005). No ML supervisado. "
            "Baseline léxico en la semana 8."
        ),
        "resultados": "pares_estructurales.csv y StructuralScore E por instancia.",
    },
    {
        "problema": (
            "Se desconoce la equivalencia semántica entre términos OFB y conceptos "
            "BIAN (P2). BIAN duplica summary=description; 61,9 % de propiedades "
            "del consolidado sin description (BIAN 90,4 %; OFB 38,1 %)."
        ),
        "og": "Contribuye al OG: cuantificar la dimensión semántica (SemanticScore S).",
        "oe": "OE3 — SemanticScore S ∈ [0, 1] calculado sobre los pares oficiales de OE2.",
        "hipotesis": (
            "H3: la similitud semántica discrimina alineación de desalineación "
            "de modelado (p. ej. account vs. SavingsAccountFacility)."
        ),
        "variables": (
            "VI: TF-IDF (v0) / embeddings (v1). VD (ratio OE3): S. "
            "Control: un texto BIAN si summary=description; umbral 0,55."
        ),
        "metodologia": (
            "Fase 4. S no se busca en el catálogo libre: se calcula sobre pares OE2."
        ),
        "tecnicas": (
            "Jaccard / TF-IDF (semana 8); embeddings + coseno "
            "(Chandrasekaran y Mago, 2022) en semana 11."
        ),
        "resultados": "pares_semanticos.csv y SemanticScore S por instancia.",
    },
    {
        "problema": (
            "Falta el indicador integrado y la escala interpretable por instancia "
            "(P3, P4). Loans, credit-cards y financings OFB no tienen SD BIAN en el piloto."
        ),
        "og": "Contribuye al OG: entregar AlignmentScore y clasificación — VD del artefacto.",
        "oe": (
            "OE4 — CoverageScore C, AlignmentScore = α·S + β·E + γ·C, "
            "clasificación y tipologías de desalineación."
        ),
        "hipotesis": (
            "H4: la agregación con pesos 1/3 produce un AlignmentScore clasificable "
            "por los umbrales §1.4. La sensibilidad de pesos se reporta como análisis."
        ),
        "variables": (
            "VI: α, β, γ (α+β+γ=1). VD (artefacto): AlignmentScore + "
            "Alta/Media/Baja/Nula. VD (ratio OE4): C. "
            "Control: umbrales 0,80 / 0,60 / 0,40; catálogo CR+BQ+BO del SD."
        ),
        "metodologia": (
            "Fase 5. C se calcula por instancia I1–I6, no sobre las 38 APIs "
            "como un solo contrato."
        ),
        "tecnicas": (
            "Agregación lineal; reglas de umbral; tipologías (Tabla 2 Guía 1); "
            "análisis de sensibilidad de pesos."
        ),
        "resultados": (
            "Tabla I1–I6; informe de gaps (loans/cards); amenazas a la validez "
            "(OFB no es un banco peruano; 3 SD)."
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
    ws.title = "Matriz OFB v2"

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
        ws.row_dimensions[row].height = 105 if row > start_row else 40

    ws.freeze_panes = f"A{start_row + 1}"

    ws2 = wb.create_sheet("Resumen OG-OE")
    ws2["A1"] = "Elemento"
    ws2["B1"] = "Descripción"
    ws2["C1"] = "Vinculación"
    for col in range(1, 4):
        style_header(ws2.cell(row=1, column=col))
    resumen = [
        ("OG", OG, "VD artefacto = AlignmentScore + clasificación"),
        ("OE1", "Adquirir y normalizar OFB + BIAN", "H1 · completitud · 41 contratos"),
        ("OE2", "Emparejar estructuras → E", "H2 · instancias I1–I6"),
        ("OE3", "Similitud semántica → S", "H3 · pares de OE2"),
        ("OE4", "C + AlignmentScore + nivel", "H4 · tipologías · sensibilidad"),
        ("Objeto", "Contrato OpenAPI bancario", "Se mantiene desde Guía 1"),
        ("Piloto", "Open Finance Brasil (38 APIs)", "Muestra MIA 403; no es un banco emisor"),
        ("Referencia", "BIAN v14 (3 Service Domains)", "No se puntúa BIAN contra sí mismo"),
    ]
    for i, (a, b, c) in enumerate(resumen, 2):
        ws2.cell(row=i, column=1, value=a)
        ws2.cell(row=i, column=2, value=b)
        ws2.cell(row=i, column=3, value=c)
        for col in range(1, 4):
            style_body(ws2.cell(row=i, column=col))
    ws2.column_dimensions["A"].width = 16
    ws2.column_dimensions["B"].width = 70
    ws2.column_dimensions["C"].width = 42

    wb.save(OUT)
    print(f"Guardado: {OUT}")


if __name__ == "__main__":
    build()
