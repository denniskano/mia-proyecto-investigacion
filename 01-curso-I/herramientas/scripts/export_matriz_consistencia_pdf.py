#!/usr/bin/env python3
"""Exporta matriz de consistencia (.xlsx) a PDF (LaTeX)."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_XLSX = ROOT / "plan-tesis/anexos/Matriz_Consistencia_Grupo9.2.xlsx"
DEFAULT_PDF = ROOT / "plan-tesis/anexos/Matriz_Consistencia_Grupo9.2.pdf"


def latex_escape(text: str) -> str:
    if text is None:
        return ""
    s = str(text)
    repl = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for a, b in repl.items():
        s = s.replace(a, b)
    for src, dst in (
        ("↔", r"$\leftrightarrow$"),
        ("≥", r"$\geq$"),
        ("α", r"$\alpha$"),
        ("β", r"$\beta$"),
        ("γ", r"$\gamma$"),
        ("∈", r"$\in$"),
        ("≠", r"$\neq$"),
        ("×", r"$\times$"),
        ("·", r"\textbullet{}"),
    ):
        s = s.replace(src, dst)
    return s


def cell_value(ws, row: int, col: int) -> str:
    v = ws.cell(row=row, column=col).value
    return latex_escape(v) if v is not None else ""


def preamble() -> str:
    return r"""\documentclass[10pt,landscape]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish,es-tabla]{babel}
\usepackage[a3paper,margin=10mm]{geometry}
\usepackage{array,booktabs,longtable,ragged2e,colortbl,xcolor}
\renewcommand{\arraystretch}{1.15}
\setlength{\tabcolsep}{3.5pt}
\definecolor{tablehead}{RGB}{47,84,150}
\definecolor{tablealt}{RGB}{238,242,247}
\newcolumntype{L}[1]{>{\RaggedRight\arraybackslash}p{#1}}
\newcolumntype{P}[1]{>{\RaggedRight\arraybackslash}p{#1}}
\begin{document}
\pagestyle{empty}
"""


def sheet_intro(ws, max_intro_row: int = 5) -> str:
    lines: list[str] = []
    for row in range(1, max_intro_row + 1):
        parts = []
        for col in range(1, ws.max_column + 1):
            val = ws.cell(row=row, column=col).value
            if val:
                parts.append(str(val).strip())
        if parts:
            text = " ".join(parts)
            if row == 1:
                lines.append(r"\begin{center}{\LARGE\bfseries " + latex_escape(text) + r"}\end{center}")
            else:
                lines.append(r"\noindent{\small " + latex_escape(text) + r"}\par\vspace{0.4em}")
    return "\n".join(lines)


def sheet_table(ws, header_row: int) -> str:
    headers = [cell_value(ws, header_row, c) for c in range(1, ws.max_column + 1)]
    ncols = len(headers)
    base = 0.94 / ncols
    w = f"{base:.3f}\\textwidth"
    cols = " ".join(f"P{{{w}}}" for _ in headers)

    out = [
        r"\vspace{0.5em}",
        r"\scriptsize",
        r"\begin{longtable}{@{} " + cols + r" @{}}",
        r"\toprule",
    ]
    out.append(" & ".join(r"\textbf{\color{white}\cellcolor{tablehead}" + h + "}" for h in headers) + r" \\")
    out.append(r"\midrule")
    out.append(r"\endhead")
    out.append(r"\midrule")
    out.append(r"\multicolumn{" + str(ncols) + r"}{r}{\textit{(continúa)}} \\")
    out.append(r"\midrule")
    out.append(r"\endfoot")
    out.append(r"\bottomrule")
    out.append(r"\endlastfoot")

    alt = False
    for row in range(header_row + 1, ws.max_row + 1):
        if all(ws.cell(row=row, column=c).value is None for c in range(1, ncols + 1)):
            continue
        cells = [cell_value(ws, row, c) for c in range(1, ncols + 1)]
        prefix = r"\rowcolor{tablealt} " if alt else ""
        out.append(prefix + " & ".join(cells) + r" \\")
        alt = not alt

    out.append(r"\end{longtable}")
    out.append(r"\normalsize")
    return "\n".join(out)


def sheet_resumen(ws) -> str:
    parts = [
        r"\newpage",
        r"\begin{center}{\Large\bfseries Resumen OG--OE}\end{center}",
        r"\vspace{0.5em}",
        r"\small",
        r"\begin{longtable}{@{}L{0.22\textwidth}L{0.52\textwidth}L{0.22\textwidth}@{}}",
        r"\toprule",
        r"\textbf{\color{white}\cellcolor{tablehead}Elemento} & "
        r"\textbf{\color{white}\cellcolor{tablehead}Descripción} & "
        r"\textbf{\color{white}\cellcolor{tablehead}Vinculación} \\",
        r"\midrule",
        r"\endhead",
        r"\bottomrule",
        r"\endfoot",
        r"\endlastfoot",
    ]
    alt = False
    for row in range(2, ws.max_row + 1):
        a, b, c = (cell_value(ws, row, i) for i in range(1, 4))
        if not (a or b or c):
            continue
        prefix = r"\rowcolor{tablealt} " if alt else ""
        parts.append(prefix + f"{a} & {b} & {c} \\\\")
        alt = not alt
    parts.append(r"\end{longtable}")
    return "\n".join(parts)


def export_pdf(
    xlsx: Path,
    out_pdf: Path,
    *,
    header_row: int = 6,
    intro_rows: int = 5,
    include_resumen: bool = True,
) -> None:
    if not xlsx.exists():
        raise SystemExit(f"No existe: {xlsx}")

    build_dir = out_pdf.parent / f"_build_{out_pdf.stem}"
    tex_path = build_dir / f"{out_pdf.stem}.tex"

    wb = load_workbook(xlsx, data_only=True)
    ws = wb[wb.sheetnames[0]]
    ws2 = wb[wb.sheetnames[1]] if include_resumen and len(wb.sheetnames) > 1 else None

    body = [preamble(), sheet_intro(ws, max_intro_row=intro_rows), sheet_table(ws, header_row=header_row)]
    if ws2:
        body.append(sheet_resumen(ws2))
    body.append(r"\end{document}")

    build_dir.mkdir(parents=True, exist_ok=True)
    tex_path.write_text("\n".join(body), encoding="utf-8")

    cmd = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-output-directory",
        str(build_dir),
        str(tex_path),
    ]
    for _ in range(2):
        subprocess.run(cmd, check=False, cwd=build_dir)

    built = build_dir / f"{out_pdf.stem}.pdf"
    if not built.exists():
        raise SystemExit(f"Error al compilar PDF; ver log en {build_dir}/")
    out_pdf.write_bytes(built.read_bytes())
    print(f"PDF: {out_pdf}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Exportar matriz xlsx → PDF")
    parser.add_argument("--xlsx", type=Path, default=DEFAULT_XLSX)
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--header-row", type=int, default=6)
    parser.add_argument("--intro-rows", type=int, default=5)
    parser.add_argument("--no-resumen", action="store_true")
    args = parser.parse_args()

    export_pdf(
        args.xlsx,
        args.pdf,
        header_row=args.header_row,
        intro_rows=args.intro_rows,
        include_resumen=not args.no_resumen,
    )


if __name__ == "__main__":
    main()
