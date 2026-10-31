#!/usr/bin/env python3
"""Genera Anexo B — Matriz de fichas de papers (estado del arte)."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

from papers_estado_del_arte import EJES, PAPERS

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "plan-tesis/anexos/Matriz_Papers_EstadoDelArte_Grupo10.xlsx"
FICHAS_DIR = ROOT / "plan-tesis/fases/fase-0-bibliografia/fichas"

HEADERS = [
    "ID",
    "Eje",
    "Cita",
    "Tipo",
    "Título",
    "Objetivo del estudio",
    "Dominio y fuente de datos",
    "Técnicas usadas",
    "Métricas de evaluación",
    "Limitaciones",
    "Vacío/oportunidad OpenAPI–BIAN",
    "Estado ficha",
    "PDF",
]

SECTION_KEYS = [
    (2, "objetivo"),
    (3, "dominio"),
    (4, "tecnicas"),
    (5, "metricas"),
    (6, "limitaciones"),
    (7, "vacio"),
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


def style_body(cell, fill=None):
    cell.font = Font(size=10)
    cell.alignment = Alignment(vertical="top", wrap_text=True)
    if fill:
        cell.fill = PatternFill("solid", fgColor=fill)
    cell.border = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin"),
    )


def ficha_stub(paper: dict) -> str:
    return f"""# {paper['cite']} — {paper['titulo'][:60]}

| Campo | Contenido |
|-------|-----------|
| **ID** | {paper['id']} |
| **Eje** | {paper['eje']} — {EJES[paper['eje']]} |
| **Tipo** | {paper['tipo']} |
| **PDF** | `bibliografia/estado-del-arte/{paper['pdf']}` |
| **Estado ficha** | pendiente |

## 1. Referencia

- **Autores:** {paper['cite']}
- **Año:**
- **Título:** {paper['titulo']}
- **Venue / DOI:**

## 2. Objetivo del estudio

[Por completar]

## 3. Dominio y fuente de datos

[Por completar]

## 4. Técnicas usadas

[Por completar]

## 5. Métricas de evaluación

[Por completar]

## 6. Limitaciones (según autores)

[Por completar]

## 7. Vacío u oportunidad para OpenAPI–BIAN

[Por completar]

## 8. Cita para el plan de tesis

- **Usar en:** §3.5 / §3.6
- **Frase clave (1 línea):** [Por completar]
"""


def find_ficha_path(paper_id: str) -> Path | None:
    matches = sorted(FICHAS_DIR.glob(f"{paper_id}_*.md"))
    return matches[0] if matches else None


def extract_section(text: str, section_num: int) -> str:
    pattern = rf"## {section_num}\.[^\n]*\n\n(.*?)(?=\n## |\Z)"
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return ""
    body = match.group(1).strip()
    if body.startswith("[Por completar]"):
        return ""
    lines = []
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        line = re.sub(r"^\*\*Usar en:\*\*.*", "", line).strip()
        line = re.sub(r"^\*\*Frase clave.*", "", line).strip()
        if line.startswith("- "):
            line = line[2:]
        lines.append(line)
    return " ".join(lines)


def parse_ficha(paper_id: str) -> dict:
    path = find_ficha_path(paper_id)
    if not path:
        return {"estado": "pendiente"}

    text = path.read_text(encoding="utf-8")
    estado_match = re.search(r"\*\*Estado ficha\*\* \| (\S+)", text)
    estado = estado_match.group(1) if estado_match else "pendiente"

    data = {"estado": estado}
    for num, key in SECTION_KEYS:
        data[key] = extract_section(text, num)
    return data


def write_fichas():
    FICHAS_DIR.mkdir(parents=True, exist_ok=True)
    for paper in PAPERS:
        fname = f"{paper['id']}_{paper['cite'].replace(', ', '_').replace(' ', '_')}.md"
        path = FICHAS_DIR / fname
        if not path.exists():
            path.write_text(ficha_stub(paper), encoding="utf-8")


def build():
    write_fichas()

    wb = Workbook()
    ws = wb.active
    ws.title = "Estado del arte"

    ws.merge_cells("A1:M1")
    ws["A1"] = "ANEXO B — MATRIZ DE PAPERS (ESTADO DEL ARTE)"
    ws["A1"].font = Font(bold=True, size=14)
    ws["A1"].alignment = Alignment(horizontal="center")

    ws.merge_cells("A2:M2")
    ws["A2"] = (
        "Grupo 10 — Fase 0 · Columnas 6–11 sincronizadas desde fichas Markdown"
    )
    ws["A2"].alignment = Alignment(horizontal="center")
    ws["A2"].font = Font(italic=True, size=10)

    start = 4
    for col, h in enumerate(HEADERS, 1):
        cell = ws.cell(row=start, column=col, value=h)
        style_header(cell)

    status_colors = {"pendiente": "FFF2CC", "en revisión": "DDEBF7", "completada": "E2EFDA", "revisada": "E2EFDA"}

    for r, p in enumerate(PAPERS, start + 1):
        fic = parse_ficha(p["id"])
        row = [
            p["id"],
            f"{p['eje']} — {EJES[p['eje']]}",
            p["cite"],
            p["tipo"],
            p["titulo"],
            fic.get("objetivo", ""),
            fic.get("dominio", ""),
            fic.get("tecnicas", ""),
            fic.get("metricas", ""),
            fic.get("limitaciones", ""),
            fic.get("vacio", ""),
            fic.get("estado", "pendiente"),
            p["pdf"],
        ]
        for c, val in enumerate(row, 1):
            cell = ws.cell(row=r, column=c, value=val)
            fill = status_colors.get(val, None) if c == 12 else None
            style_body(cell, fill=fill)

    widths = [8, 22, 18, 14, 32, 28, 22, 22, 20, 20, 28, 12, 36]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for row in range(start, start + len(PAPERS) + 1):
        ws.row_dimensions[row].height = 45 if row > start else 30
    ws.freeze_panes = f"A{start + 1}"

    ws2 = wb.create_sheet("Por eje")
    ws2.cell(row=1, column=1, value="Eje").font = Font(bold=True)
    ws2.cell(row=1, column=2, value="Papers").font = Font(bold=True)
    for i, (code, name) in enumerate(EJES.items(), 2):
        papers = [p["cite"] for p in PAPERS if p["eje"] == code]
        ws2.cell(row=i, column=1, value=f"{code} — {name}")
        ws2.cell(row=i, column=2, value="\n".join(papers))
        ws2.cell(row=i, column=2).alignment = Alignment(wrap_text=True)
    ws2.column_dimensions["A"].width = 30
    ws2.column_dimensions["B"].width = 50

    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print(f"Guardado: {OUT}")
    print(f"Fichas: {FICHAS_DIR} ({len(PAPERS)} archivos)")


if __name__ == "__main__":
    build()
