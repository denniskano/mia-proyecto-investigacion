#!/usr/bin/env python3
"""Genera Figuras 1 y 2 para Fase B — Grupo 10."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "plan-tesis/fases/fase-b-planteamiento/figuras"

BLUE = "#2F5496"
BLUE_LIGHT = "#D6E4F0"
BLUE_MID = "#B4C7E7"
ORANGE = "#C55A11"
ORANGE_LIGHT = "#FCE4D6"
ORANGE_MID = "#F4B183"
GREEN = "#548235"
GREEN_LIGHT = "#E2EFDA"
PURPLE = "#7030A0"
PURPLE_LIGHT = "#E8D5F5"
GRAY = "#404040"
GRAY_LIGHT = "#767676"
LIGHT = "#F8F9FA"
WHITE = "#FFFFFF"
AMBER = "#FFF8E7"


def box(ax, x, y, w, h, text, fc, ec=BLUE, fontsize=9, bold=False):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        linewidth=1.5,
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
        linespacing=1.35,
    )


def header_band(ax, x, y, w, h, title, subtitle, fc, ec):
    """Caja con franja de título superior."""
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        linewidth=1.5,
        edgecolor=ec,
        facecolor=fc,
        zorder=2,
    )
    ax.add_patch(patch)
    header_h = min(0.38, h * 0.22)
    ax.add_patch(
        Rectangle(
            (x + 0.02, y + h - header_h - 0.02),
            w - 0.04,
            header_h,
            facecolor=ec,
            edgecolor=ec,
            alpha=0.15,
            zorder=3,
        )
    )
    ax.text(
        x + w / 2,
        y + h - header_h / 2 - 0.02,
        title,
        ha="center",
        va="center",
        fontsize=10,
        weight="bold",
        color=ec,
        zorder=4,
    )
    ax.text(
        x + w / 2,
        y + (h - header_h) / 2 + 0.02,
        subtitle,
        ha="center",
        va="center",
        fontsize=8.5,
        color=GRAY,
        zorder=4,
        linespacing=1.4,
    )


def arrow(ax, x1, y1, x2, y2, label=None, color=BLUE, style="-|>", rad=0.0, fontsize=8,
          label_offset=(0, 0.06)):
    arr = FancyArrowPatch(
        (x1, y1),
        (x2, y2),
        arrowstyle=style,
        mutation_scale=12,
        linewidth=1.4,
        color=color,
        connectionstyle=f"arc3,rad={rad}",
        zorder=1,
    )
    ax.add_patch(arr)
    if label:
        ax.text(
            (x1 + x2) / 2 + label_offset[0],
            (y1 + y2) / 2 + label_offset[1],
            label,
            ha="center",
            fontsize=fontsize,
            color=color,
            weight="bold",
            zorder=5,
        )


def pill(ax, x, y, text, fc, ec, fontsize=7.5):
    ax.text(
        x,
        y,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        color=GRAY,
        bbox=dict(boxstyle="round,pad=0.35", facecolor=fc, edgecolor=ec, linewidth=1.0),
        zorder=5,
    )


def save(fig, name):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for ext, dpi in [("png", 250), ("svg", None)]:
        path = OUT_DIR / f"{name}.{ext}"
        kw = {"bbox_inches": "tight", "facecolor": "white", "pad_inches": 0.08}
        if dpi:
            kw["dpi"] = dpi
        fig.savefig(path, **kw)
        print(f"Guardado: {path}")
    plt.close(fig)


def figura_01():
    """Contexto §1.1 — ecosistema API bancario, BIAN, OpenAPI y modelo S/E/C."""
    fig, ax = plt.subplots(figsize=(12.5, 8.5))
    ax.set_xlim(0, 12.5)
    ax.set_ylim(0, 8.5)
    ax.axis("off")

    # ── Capa 1: contexto sectorial ──────────────────────────────────────────
    ax.text(0.35, 8.15, "1", fontsize=9, weight="bold", color=GRAY_LIGHT, va="center")
    ax.text(0.55, 8.15, "Contexto sectorial", fontsize=9, weight="bold", color=GRAY, va="center")

    band = FancyBboxPatch(
        (0.35, 7.05),
        11.8,
        0.95,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        linewidth=1.2,
        edgecolor="#A6A6A6",
        facecolor=LIGHT,
        zorder=2,
    )
    ax.add_patch(band)
    ax.text(
        6.25,
        7.72,
        "Arquitectura API bancaria — integración entre sistemas, socios y canales",
        ha="center",
        fontsize=10,
        weight="bold",
        color=GRAY,
        zorder=3,
    )

    pills = [
        (1.55, "Canales\ndigitales"),
        (4.05, "Open Banking\n/ socios"),
        (6.55, "Core\nbancario"),
        (9.05, "API\nGateway"),
    ]
    for px, pt in pills:
        pill(ax, px, 7.28, pt, WHITE, "#A6A6A6", fontsize=7.5)

    for x1, x2 in [(2.35, 3.25), (4.85, 5.75), (7.35, 8.25)]:
        ax.plot([x1, x2], [7.28, 7.28], color="#BBBBBB", linewidth=1.2, zorder=3)

    ax.text(
        6.25,
        6.82,
        "OpenAPI como estándar de facto para describir APIs REST  ·  "
        "BIAN orienta coherencia arquitectónica a nivel de negocio",
        ha="center",
        fontsize=8,
        color=GRAY_LIGHT,
        style="italic",
        zorder=3,
    )

    # ── Capa 2: dos lenguajes ───────────────────────────────────────────────
    ax.text(0.35, 6.55, "2", fontsize=9, weight="bold", color=GRAY_LIGHT, va="center")
    ax.text(
        0.55,
        6.55,
        "Dos vocabularios que deben converger",
        fontsize=9,
        weight="bold",
        color=GRAY,
        va="center",
    )

    conv = FancyBboxPatch(
        (4.35, 5.72),
        3.8,
        0.72,
        boxstyle="round,pad=0.03,rounding_size=0.08",
        linewidth=2.0,
        edgecolor=GREEN,
        facecolor=GREEN_LIGHT,
        zorder=6,
    )
    ax.add_patch(conv)
    ax.text(6.25, 6.18, "Alineación", ha="center", fontsize=10.5, weight="bold", color=GREEN, zorder=7)
    ax.text(
        6.25,
        5.86,
        "Correspondencia estructural y semántica OpenAPI ↔ BIAN",
        ha="center",
        fontsize=8,
        color=GRAY,
        zorder=7,
    )

    header_band(
        ax,
        0.35,
        3.35,
        5.35,
        2.25,
        "BIAN — Banking Industry Architecture Network",
        "Modelo de referencia de negocio\n(no implementa la API)\n\n"
        "• Service Domains — capacidades bancarias\n"
        "• Behaviors — acciones de negocio\n"
        "• Business Objects — entidades de dominio",
        BLUE_LIGHT,
        BLUE,
    )
    ax.text(
        3.02,
        3.55,
        "Referencia de negocio",
        ha="center",
        fontsize=7.5,
        color=BLUE,
        weight="bold",
        style="italic",
    )

    header_band(
        ax,
        6.5,
        3.35,
        5.35,
        2.25,
        "Contrato OpenAPI 3.x",
        "Especificación técnica machine-readable\n(objeto de estudio — sector bancario)\n\n"
        "• paths · operations HTTP\n"
        "• schemas · parameters · constraints\n"
        "• YAML / JSON legible por herramientas",
        ORANGE_LIGHT,
        ORANGE,
    )
    ax.text(
        9.17,
        3.55,
        "Artefacto evaluado",
        ha="center",
        fontsize=7.5,
        color=ORANGE,
        weight="bold",
        style="italic",
    )

    arrow(ax, 3.02, 5.6, 4.35, 6.05, color=BLUE, rad=0.15)
    arrow(ax, 9.17, 5.6, 8.15, 6.05, color=ORANGE, rad=-0.15)

    # ── Capa 3: modelo propuesto ────────────────────────────────────────────
    ax.text(0.35, 2.95, "3", fontsize=9, weight="bold", color=GRAY_LIGHT, va="center")
    ax.text(
        0.55,
        2.95,
        "Modelo de alineación propuesto (producto del plan de tesis)",
        fontsize=9,
        weight="bold",
        color=GRAY,
        va="center",
    )

    arrow(ax, 6.25, 5.72, 6.25, 3.05, color=GREEN)

    metrics = [
        (0.55, "SemanticScore\n(S)", PURPLE_LIGHT, PURPLE, "Similitud de\nsignificado"),
        (3.35, "StructuralScore\n(E)", BLUE_LIGHT, BLUE, "Correspondencia\nde estructura"),
        (6.15, "CoverageScore\n(C)", ORANGE_LIGHT, ORANGE, "Cobertura de\nconceptos BIAN"),
        (8.95, "AlignmentScore", GREEN_LIGHT, GREEN, "Indicador global\nα·S + β·E + γ·C"),
    ]
    for i, (mx, label, fc, ec, sub) in enumerate(metrics):
        box(ax, mx, 1.65, 2.35, 1.05, label, fc, ec=ec, fontsize=9, bold=True)
        ax.text(mx + 1.175, 1.42, sub, ha="center", fontsize=7, color=GRAY_LIGHT, style="italic")
        if i < len(metrics) - 1:
            arrow(ax, mx + 2.35, 2.18, mx + 2.85, 2.18, color=GRAY)

    ax.text(
        6.25,
        1.25,
        "Clasificación: alta · media · baja alineación",
        ha="center",
        fontsize=8,
        color=GREEN,
        weight="bold",
    )

    # ── Capa 4: alcance investigación ───────────────────────────────────────
    ax.text(0.35, 0.88, "4", fontsize=9, weight="bold", color=GRAY_LIGHT, va="center")
    ax.text(
        0.55,
        0.88,
        "Alcance de este documento",
        fontsize=9,
        weight="bold",
        color=GRAY,
        va="center",
    )

    scope = FancyBboxPatch(
        (0.35, 0.08),
        11.8,
        0.62,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        linewidth=1.8,
        edgecolor=GREEN,
        facecolor=AMBER,
        zorder=2,
    )
    ax.add_patch(scope)
    ax.text(
        6.25,
        0.39,
        "Plan de tesis (Guía N°01): diseño del procedimiento de medición sobre artefactos documentales\n"
        "— sin construcción del artefacto software ni despliegue en producción —",
        ha="center",
        va="center",
        fontsize=8.5,
        color=GRAY,
        weight="bold",
        linespacing=1.35,
        zorder=3,
    )

    arrow(ax, 6.25, 1.65, 6.25, 0.7, color=GREEN, style="-|>")

    ax.text(
        6.25,
        -0.08,
        "Fuente: elaboración propia",
        ha="center",
        fontsize=8,
        color="#888888",
        style="italic",
    )

    save(fig, "Figura_01_Contexto")


def figura_02():
    """Objeto, unidad de análisis y ejemplo genérico §1.4 (sin caso piloto fijo)."""
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title(
        "Figura 2. Objeto de estudio, unidad de análisis y producto del modelo",
        fontsize=12,
        weight="bold",
        color=GRAY,
        pad=16,
    )

    box(
        ax,
        0.4,
        5.0,
        2.2,
        1.1,
        "Objeto de estudio\nContrato OpenAPI\nbancario (completo)",
        ORANGE_LIGHT,
        ec=ORANGE,
        fontsize=9,
        bold=True,
    )
    box(
        ax,
        2.95,
        5.0,
        2.4,
        1.1,
        "Unidad de análisis\nendpoint · schema\n↔ behavior · business object",
        BLUE_LIGHT,
        ec=BLUE,
        fontsize=8.5,
        bold=True,
    )
    box(
        ax,
        5.7,
        5.0,
        1.5,
        1.1,
        "Scores\nS · E · C",
        "#FFFFFF",
        ec=GREEN,
        fontsize=9,
        bold=True,
    )
    box(
        ax,
        7.55,
        5.0,
        2.05,
        1.1,
        "Producto\nAlignmentScore\n+ clasificación",
        GREEN_LIGHT,
        ec=GREEN,
        fontsize=9,
        bold=True,
    )

    arrow(ax, 2.6, 5.55, 2.95, 5.55, color=ORANGE)
    arrow(ax, 5.35, 5.55, 5.7, 5.55, color=BLUE)
    arrow(ax, 7.2, 5.55, 7.55, 5.55, color=GREEN)

    box(ax, 0.4, 1.0, 4.4, 3.6, "", ORANGE_LIGHT, ec=ORANGE)
    ax.text(
        2.6,
        4.35,
        "Ejemplo genérico — OpenAPI (ilustrativo)",
        ha="center",
        fontsize=10,
        weight="bold",
        color=ORANGE,
    )
    box(ax, 0.65, 3.15, 3.9, 0.85, "POST /payment-orders", "#FFFFFF", ec=ORANGE, fontsize=9)
    box(ax, 0.65, 2.15, 3.9, 0.85, "GET /payment-orders/{id}", "#FFFFFF", ec=ORANGE, fontsize=9)
    box(
        ax,
        0.65,
        1.15,
        3.9,
        0.85,
        "Schema PaymentOrder\n(amount · currency)",
        "#FFFFFF",
        ec=ORANGE,
        fontsize=9,
    )

    box(ax, 5.2, 1.0, 4.4, 3.6, "", BLUE_LIGHT)
    ax.text(
        7.4,
        4.35,
        "Referencia BIAN (dominio pagos — ilustrativo)",
        ha="center",
        fontsize=10,
        weight="bold",
        color=BLUE,
    )
    box(ax, 5.45, 3.15, 3.9, 0.85, "Behavior Initiate", "#FFFFFF", ec=BLUE, fontsize=9)
    box(ax, 5.45, 2.15, 3.9, 0.85, "Behavior Retrieve", "#FFFFFF", ec=BLUE, fontsize=9)
    box(
        ax,
        5.45,
        1.15,
        3.9,
        0.85,
        "Business Object Payment\n/ PaymentAmount",
        "#FFFFFF",
        ec=BLUE,
        fontsize=9,
    )

    for y in (3.57, 2.57, 1.57):
        arr = FancyArrowPatch(
            (4.55, y),
            (5.45, y),
            arrowstyle="<|-|>",
            mutation_scale=11,
            linewidth=1.3,
            color=GREEN,
        )
        ax.add_patch(arr)

    box(
        ax,
        0.4,
        0.25,
        9.2,
        0.55,
        "Sin caso piloto fijo: el procedimiento aplica a cualquier contrato OpenAPI bancario "
        "emparejado con un Service Domain BIAN",
        LIGHT,
        ec=GRAY,
        fontsize=8.5,
    )

    ax.text(
        5.0,
        -0.05,
        "Fuente: elaboración propia — coherente con Tabla 3 §1.4",
        ha="center",
        fontsize=8,
        color="#888888",
        style="italic",
    )
    save(fig, "Figura_02_Objeto_Unidad_Analisis")


def build():
    figura_01()
    figura_02()
    print("Figura 3 (AlignmentScore): usar plan-tesis/anexos/figuras_alineacion_openapi_bian.pdf")


if __name__ == "__main__":
    build()
