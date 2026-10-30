#!/usr/bin/env python3
"""Genera tablas LaTeX para Anexos B, C y D — Fase G."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_matriz_consistencia import ROWS
from papers_estado_del_arte import EJES, PAPERS

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "plan-tesis/latex/tables"


def esc(text: str) -> str:
    repl = {
        "&": r"\&",
        "%": r"\%",
        "#": r"\#",
        "_": r"\_",
        "α": r"$\alpha$",
        "β": r"$\beta$",
        "γ": r"$\gamma$",
        "≥": r"$\geq$",
        "∈": r"$\in$",
        "↔": r"$\leftrightarrow$",
        "·": r"--",
    }
    for k, v in repl.items():
        text = text.replace(k, v)
    return text


def write_anexo_b():
    lines = [
        r"\begin{longtable}{@{}p{0.07\textwidth}p{0.08\textwidth}p{0.18\textwidth}p{0.10\textwidth}p{0.47\textwidth}@{}}",
        r"\caption{Resumen de papers del estado del arte (Anexo B)} \label{tab:anexo-b} \\",
        r"\toprule",
        r"\textbf{ID} & \textbf{Eje} & \textbf{Cita} & \textbf{Tipo} & \textbf{Título} \\",
        r"\midrule",
        r"\endfirsthead",
        r"\multicolumn{5}{l}{\textit{(continúa)}} \\",
        r"\midrule",
        r"\textbf{ID} & \textbf{Eje} & \textbf{Cita} & \textbf{Tipo} & \textbf{Título} \\",
        r"\midrule",
        r"\endhead",
        r"\midrule",
        r"\multicolumn{5}{r}{\textit{(continúa en la siguiente página)}} \\",
        r"\endfoot",
        r"\bottomrule",
        r"\endlastfoot",
    ]
    for p in PAPERS:
        titulo = esc(p["titulo"])
        if len(titulo) > 120:
            titulo = titulo[:117] + r"\ldots"
        lines.append(
            f"{p['id']} & {p['eje']} & {esc(p['cite'])} & {esc(p['tipo'])} & {titulo} \\\\"
        )
    lines.append(r"\end{longtable}")
    path = OUT / "tab-anexo-b-resumen.tex"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Guardado: {path}")


def write_anexo_c():
    lines = [
        r"\begin{longtable}{@{}p{0.14\textwidth}p{0.26\textwidth}p{0.26\textwidth}p{0.28\textwidth}@{}}",
        r"\caption{Matriz de consistencia — resumen por fase (Anexo C)} \label{tab:anexo-c} \\",
        r"\toprule",
        r"\textbf{Fase} & \textbf{Objetivo} & \textbf{Producto verificable} & \textbf{Hipótesis (síntesis)} \\",
        r"\midrule",
        r"\endfirsthead",
        r"\multicolumn{4}{l}{\textit{(continúa)}} \\",
        r"\midrule",
        r"\textbf{Fase} & \textbf{Objetivo} & \textbf{Producto verificable} & \textbf{Hipótesis (síntesis)} \\",
        r"\midrule",
        r"\endhead",
        r"\midrule",
        r"\multicolumn{4}{r}{\textit{(continúa en la siguiente página)}} \\",
        r"\endfoot",
        r"\bottomrule",
        r"\endlastfoot",
    ]
    for row in ROWS:
        fase = esc(row["fase"].split("—")[0].strip())
        obj = esc(row["objetivo"])
        prod = esc(row["producto"])
        hip = esc(row["hipotesis"])
        for label, val in [("obj", obj), ("prod", prod), ("hip", hip)]:
            if len(val) > 200:
                val = val[:197] + r"\ldots"
            if label == "obj":
                obj = val
            elif label == "prod":
                prod = val
            else:
                hip = val
        lines.append(f"{fase} & {obj} & {prod} & {hip} \\\\")
    lines.append(r"\end{longtable}")
    path = OUT / "tab-anexo-c-resumen.tex"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Guardado: {path}")


def write_anexo_d():
    rows = [
        (
            "StructuralScore (E)",
            "Fase 3 / OE2",
            "Correspondencia estructural OpenAPI $\\leftrightarrow$ BIAN",
            "[0, 1] continua",
            "Matriz de correspondencias + promedio ponderado de pares alineados",
            "Umbral de matching fijo; mismo insumo normalizado (OE1)",
        ),
        (
            "SemanticScore (S)",
            "Fase 4 / OE3",
            "Similitud semántica entre términos OpenAPI y conceptos BIAN",
            "[0, 1] continua",
            "Similitud coseno (embeddings) o medida ontológica acordada",
            "Corpus de términos fijo; modelo de embedding fijo por corrida",
        ),
        (
            "CoverageScore (C)",
            "Fase 5 / OE4",
            "Proporción de conceptos BIAN cubiertos por el contrato",
            "[0, 1] continua",
            "Ratio conceptos BIAN mapeados / total de conceptos del SD",
            "Mismos S y E; taxonomía BIAN del SD emparejado",
        ),
        (
            "AlignmentScore",
            "Fase 5 / OE4",
            "Indicador global de alineación del contrato",
            "[0, 1] continua",
            "$\\alpha \\cdot S + \\beta \\cdot E + \\gamma \\cdot C$",
            "$\\alpha+\\beta+\\gamma=1$; umbrales Alta/Media/Baja/Nula fijos",
        ),
        (
            "Clasificación de alineación",
            "Fase 5 / OE4",
            "Nivel interpretativo del contrato evaluado",
            "Nominal (4 niveles)",
            "Alta $\\geq$0,80; Media 0,60--0,79; Baja 0,40--0,59; Nula $<$0,40",
            "Mismo AlignmentScore; reglas Tabla tipologías Cap.~1",
        ),
        (
            "Calidad de extracción (OE1)",
            "Fase 2 / OE1",
            "Completitud de la normalización documental",
            "Ratio + conteos",
            "\\% elementos extraídos vs.\\ artefacto fuente",
            "Versión fija OpenAPI + BIAN; parser fijo",
        ),
    ]
    lines = [
        r"\begin{longtable}{@{}p{0.16\textwidth}p{0.10\textwidth}p{0.20\textwidth}p{0.12\textwidth}p{0.22\textwidth}p{0.14\textwidth}@{}}",
        r"\caption{Operación de variables de investigación (Anexo D)} \label{tab:anexo-d} \\",
        r"\toprule",
        r"\textbf{Variable} & \textbf{Fase} & \textbf{Def. operativa} & \textbf{Escala} & \textbf{Instrumento / cálculo} & \textbf{Control} \\",
        r"\midrule",
        r"\endfirsthead",
        r"\multicolumn{6}{l}{\textit{(continúa)}} \\",
        r"\midrule",
        r"\textbf{Variable} & \textbf{Fase} & \textbf{Def. operativa} & \textbf{Escala} & \textbf{Instrumento / cálculo} & \textbf{Control} \\",
        r"\midrule",
        r"\endhead",
        r"\midrule",
        r"\multicolumn{6}{r}{\textit{(continúa en la siguiente página)}} \\",
        r"\endfoot",
        r"\bottomrule",
        r"\endlastfoot",
    ]
    for r in rows:
        lines.append(" & ".join(r) + r" \\")
    lines.append(r"\end{longtable}")
    path = OUT / "tab-anexo-d-operacion.tex"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Guardado: {path}")


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    write_anexo_b()
    write_anexo_c()
    write_anexo_d()


if __name__ == "__main__":
    build()
