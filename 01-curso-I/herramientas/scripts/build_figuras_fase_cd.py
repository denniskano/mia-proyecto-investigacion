#!/usr/bin/env python3
"""Genera Figuras 4 (Cap. 2) y 6 (Cap. 3) — Grupo 10."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[2]
OUT_CAP02 = ROOT / "plan-tesis/figuras/cap02"
OUT_CAP03 = ROOT / "plan-tesis/figuras/cap03"

BLUE = "#2F5496"
BLUE_LIGHT = "#D6E4F0"
ORANGE = "#C55A11"
ORANGE_LIGHT = "#FCE4D6"
GREEN = "#548235"
GREEN_LIGHT = "#E2EFDA"
PURPLE = "#7030A0"
PURPLE_LIGHT = "#E8D5F5"
GRAY = "#404040"


def box(ax, x, y, w, h, text, fc, ec=BLUE, fontsize=8.5, bold=False):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        linewidth=1.4,
        edgecolor=ec,
        facecolor=fc,
    )
    ax.add_patch(patch)
    weight = "bold" if bold else "normal"
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        color=GRAY,
        weight=weight,
    )


def arrow(ax, x1, y1, x2, y2, color=BLUE):
    arr = FancyArrowPatch(
        (x1, y1),
        (x2, y2),
        arrowstyle="-|>",
        mutation_scale=11,
        linewidth=1.3,
        color=color,
        connectionstyle="arc3,rad=0.0",
    )
    ax.add_patch(arr)


def save(fig, out_dir, name):
    out_dir.mkdir(parents=True, exist_ok=True)
    for ext, dpi in [("png", 200), ("svg", None)]:
        path = out_dir / f"{name}.{ext}"
        kw = {"bbox_inches": "tight", "facecolor": "white"}
        if dpi:
            kw["dpi"] = dpi
        fig.savefig(path, **kw)
        print(f"Guardado: {path}")
    plt.close(fig)


def figura_04_cadena_objetivos():
    fig, ax = plt.subplots(figsize=(11, 4.2))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 4.2)
    ax.axis("off")

    box(ax, 0.2, 1.5, 1.5, 1.2, "Contrato\nOpenAPI\nbancario", BLUE_LIGHT, bold=True)
    box(ax, 0.2, 0.1, 1.5, 1.0, "Service\nDomain\nBIAN", ORANGE_LIGHT, ec=ORANGE, bold=True)

    arrow(ax, 1.75, 2.1, 2.3, 2.1)
    arrow(ax, 1.75, 0.6, 2.3, 2.0, color=ORANGE)

    box(
        ax,
        2.3,
        1.4,
        1.8,
        1.4,
        "OE1\nNormalización\n(representaciones\ncomparables)",
        GREEN_LIGHT,
        ec=GREEN,
        bold=True,
    )
    arrow(ax, 4.15, 2.1, 4.65, 2.8)
    arrow(ax, 4.15, 2.1, 4.65, 1.4)

    box(ax, 4.65, 2.3, 1.6, 1.0, "OE2\nStructuralScore (E)", BLUE_LIGHT, fontsize=8)
    box(ax, 4.65, 0.9, 1.6, 1.0, "OE3\nSemanticScore (S)", PURPLE_LIGHT, ec=PURPLE, fontsize=8)

    arrow(ax, 6.3, 2.8, 6.8, 2.1)
    arrow(ax, 6.3, 1.4, 6.8, 2.1)

    box(
        ax,
        6.8,
        1.4,
        1.9,
        1.4,
        "OE4\nCoverageScore (C)\n+ AlignmentScore\n+ clasificación",
        ORANGE_LIGHT,
        ec=ORANGE,
        bold=True,
        fontsize=8,
    )
    arrow(ax, 8.75, 2.1, 9.25, 2.1)

    box(
        ax,
        9.25,
        1.5,
        1.5,
        1.2,
        "Producto:\nAlignmentScore\n+ tipologías",
        GREEN_LIGHT,
        ec=GREEN,
        bold=True,
        fontsize=8,
    )

    ax.text(
        5.5,
        3.85,
        "Figura 4 — Cadena de objetivos: transformaciones entrada $\\rightarrow$ salida",
        ha="center",
        fontsize=10,
        weight="bold",
        color=GRAY,
    )
    save(fig, OUT_CAP02, "Figura_04_Cadena_Objetivos")


def figura_06_brecha():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")

    ax.text(1.5, 4.5, "Estado del arte\n(E1--E6)", ha="center", fontsize=9, weight="bold", color=GRAY)
    for i, (label, fc, ec) in enumerate(
        [
            ("E1 OpenAPI", BLUE_LIGHT, BLUE),
            ("E2 Estructural", BLUE_LIGHT, BLUE),
            ("E3 Semántico", PURPLE_LIGHT, PURPLE),
            ("E4 Dominio", GREEN_LIGHT, GREEN),
            ("E5 Testing*", ORANGE_LIGHT, ORANGE),
            ("E6 Selección*", ORANGE_LIGHT, ORANGE),
        ]
    ):
        y = 3.6 - i * 0.55
        box(ax, 0.3, y, 2.4, 0.42, label, fc, ec=ec, fontsize=7.5)

    ax.text(5.0, 4.5, "Vacíos (V1--V5)", ha="center", fontsize=9, weight="bold", color=GRAY)
    vacios = [
        "V1: sin OpenAPI $\\cap$ BIAN banca",
        "V2: sin métrica integrada S+E+C",
        "V3: sin cobertura BO BIAN",
        "V4: sin procedimiento + score",
        "V5: sin gobernanza documental",
    ]
    for i, v in enumerate(vacios):
        box(ax, 3.5, 3.6 - i * 0.55, 3.0, 0.42, v, "#FFF2CC", ec="#BF9000", fontsize=7.5)

    arrow(ax, 6.55, 2.5, 7.05, 2.5, color=GREEN)
    box(
        ax,
        7.05,
        1.6,
        2.5,
        1.8,
        "Oportunidad\nModelo S + E + C\n$\\rightarrow$ AlignmentScore\n(plan de tesis)",
        GREEN_LIGHT,
        ec=GREEN,
        bold=True,
        fontsize=8,
    )

    ax.text(5.0, 0.35, "* E5/E6 delimitan el foco (testing/runtime fuera de alcance)", ha="center", fontsize=7, color=GRAY)
    ax.text(
        5.0,
        4.85,
        "Figura 6 — De la literatura revisada a la brecha de investigación",
        ha="center",
        fontsize=10,
        weight="bold",
        color=GRAY,
    )
    save(fig, OUT_CAP03, "Figura_06_Brecha")


def figura_05_bases_conceptuales():
    fig, ax = plt.subplots(figsize=(9, 3.8))
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 3.8)
    ax.axis("off")

    box(
        ax,
        0.4,
        1.0,
        2.2,
        1.8,
        "Capa técnica\nContrato OpenAPI\n(paths, operations,\nschemas)",
        BLUE_LIGHT,
        bold=True,
        fontsize=8,
    )
    box(
        ax,
        3.2,
        0.8,
        2.6,
        2.2,
        "Modelo de alineación\nS + E + C\n→ AlignmentScore",
        GREEN_LIGHT,
        ec=GREEN,
        bold=True,
        fontsize=8,
    )
    box(
        ax,
        6.4,
        1.0,
        2.2,
        1.8,
        "Capa de negocio\nService Domain BIAN\n(behaviors, business\nobjects)",
        ORANGE_LIGHT,
        ec=ORANGE,
        bold=True,
        fontsize=8,
    )

    arrow(ax, 2.65, 1.9, 3.15, 1.9)
    arrow(ax, 5.85, 1.9, 6.35, 1.9)

    ax.text(
        4.5,
        3.45,
        "Figura 5 — Bases conceptuales: contrato OpenAPI, modelo S/E/C y referencia BIAN",
        ha="center",
        fontsize=10,
        weight="bold",
        color=GRAY,
    )
    save(fig, OUT_CAP03, "Figura_05_Bases_Conceptuales")


if __name__ == "__main__":
    figura_04_cadena_objetivos()
    figura_05_bases_conceptuales()
    figura_06_brecha()
