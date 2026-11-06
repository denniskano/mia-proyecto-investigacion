#!/usr/bin/env python3
"""Gráficos del piloto para Beamer (colores UNI)."""
from __future__ import annotations

from collections import Counter
from pathlib import Path

import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

ROOT = Path(__file__).resolve().parent
NAVY = "#1B365D"
GOLD = "#E8A323"
GREEN = "#1E7F4F"
MUTED = "#636E72"
ALT = "#EEF2F7"
WHITE = "#FFFFFF"
NULA = 0.40
BAJA = 0.60

IDS = ["I1", "I2", "I3a", "I3b", "I4", "I5", "I6"]
S_V0 = [0.0131, 0.0099, 0.00, 0.00, 0.00, 0.0269, 0.00]
S_V1 = [0.5557, 0.5306, 0.4527, 0.4561, 0.5248, 0.5930, 0.00]
E = [0.3528, 0.4736, 0.5625, 0.5625, 0.2885, 0.3235, 0.00]
C = [0.40, 0.50, 0.20, 0.20, 0.25, 0.50, 0.00]
ALIGN_V0 = [0.2553, 0.3278, 0.2542, 0.2542, 0.1795, 0.2834, 0.00]
ALIGN_V1 = [0.4362, 0.5014, 0.4051, 0.4062, 0.3544, 0.4722, 0.00]

CAT_LABELS = [
    "credit-cards\n× CreditCard",
    "opendata-cards\n× CreditCard",
    "opendata-loans\n× Loan",
    "loans\n× Loan",
    "investments\n× Inv.Account",
]
CAT_SCORES = [0.4582, 0.3042, 0.2819, 0.2744, 0.1854]


def style():
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
            "axes.edgecolor": NAVY,
            "axes.labelcolor": NAVY,
            "xtick.color": NAVY,
            "ytick.color": NAVY,
            "text.color": NAVY,
            "figure.facecolor": WHITE,
            "axes.facecolor": WHITE,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.linewidth": 0.8,
            "font.size": 11,
        }
    )


def save(fig, name: str):
    path = ROOT / name
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor=WHITE, pad_inches=0.15)
    plt.close(fig)
    print("wrote", path.name)


def fig_alignment():
    x = np.arange(len(IDS))
    w = 0.36
    fig, ax = plt.subplots(figsize=(10.2, 4.4))
    ax.bar(x - w / 2, ALIGN_V0, w, color=NAVY, label="v0 léxico")
    ax.bar(x + w / 2, ALIGN_V1, w, color=GOLD, label="v1 MiniLM")
    ax.axhline(NULA, color=MUTED, ls="--", lw=1, label="umbral Baja (0,40)")
    ax.set_xticks(x, IDS)
    ax.set_ylim(0, 0.85)
    ax.set_ylabel("AlignmentScore")
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.2f"))
    ax.legend(frameon=False, loc="upper right")
    ax.set_title("AlignmentScore: baseline léxico vs MiniLM (mismos pares E)", loc="left", fontsize=13, pad=10)
    save(fig, "grafico-alignment.png")


def fig_semantic():
    x = np.arange(len(IDS))
    w = 0.36
    fig, ax = plt.subplots(figsize=(10.2, 4.4))
    ax.bar(x - w / 2, S_V0, w, color=NAVY, label="S v0  Jaccard + TF-IDF")
    ax.bar(x + w / 2, S_V1, w, color=GOLD, label="S v1  MiniLM multilingual")
    ax.set_xticks(x, IDS)
    ax.set_ylim(0, 0.75)
    ax.set_ylabel("SemanticScore")
    ax.legend(frameon=False, loc="upper right")
    ax.set_title("S ≈ 0 en léxico PT×EN; MiniLM recupera significado sin reabrir E", loc="left", fontsize=13, pad=10)
    save(fig, "grafico-semantico.png")


def fig_sec():
    x = np.arange(len(IDS))
    w = 0.24
    fig, ax = plt.subplots(figsize=(10.2, 4.4))
    ax.bar(x - w, S_V0, w, color=GOLD, label="S léxico")
    ax.bar(x, E, w, color=NAVY, label="E estructural")
    ax.bar(x + w, C, w, color=GREEN, label="C cobertura")
    ax.axhline(NULA, color=MUTED, ls="--", lw=1)
    ax.set_xticks(x, IDS)
    ax.set_ylim(0, 0.75)
    ax.set_ylabel("Componente")
    ax.legend(frameon=False, ncol=3, loc="upper right")
    ax.set_title("Descomposición v0: hay estructura; el léxico PT×EN tumba el promedio", loc="left", fontsize=13, pad=10)
    save(fig, "grafico-sec.png")


def fig_catalogo():
    fig, ax = plt.subplots(figsize=(10.2, 4.4))
    colors = [GOLD if s >= NULA else NAVY for s in CAT_SCORES]
    ax.barh(CAT_LABELS[::-1], CAT_SCORES[::-1], color=colors[::-1], height=0.62)
    ax.axvline(NULA, color=MUTED, ls="--", lw=1)
    ax.set_xlim(0, 0.7)
    ax.set_xlabel("AlignmentScore v0")
    ax.set_title("Catálogo extra: SD oficiales (no inventados). credit-cards es el primer Baja", loc="left", fontsize=13, pad=10)
    for y, s in enumerate(CAT_SCORES[::-1]):
        ax.text(s + 0.015, y, f"{s:.2f}", va="center", fontsize=10, color=NAVY)
    save(fig, "grafico-catalogo.png")


def fig_fuentes():
    ops_csv = ROOT.parent / "resultado" / "consolidado" / "operaciones_estructuradas.csv"
    counts = Counter()
    methods = Counter()
    with ops_csv.open(encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh, delimiter=";"):
            src = (row.get("source") or row.get("fuente") or "").upper()
            met = (row.get("method") or row.get("metodo") or "").upper()
            if src in {"BIAN", "BANCO", "OFB"}:
                key = "BIAN" if src == "BIAN" else "OFB"
                counts[key] += 1
                methods[(key, met)] += 1
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.3), gridspec_kw={"width_ratios": [1.05, 1.35]})

    ax = axes[0]
    labels = ["OFB\n38 YAML", "BIAN v14\n258 YAML"]
    vals = [counts.get("OFB", 160), counts.get("BIAN", 4580)]
    ax.bar(labels, vals, color=[GOLD, NAVY], width=0.55)
    ax.set_ylabel("Operaciones")
    ax.set_title("Inventario parseado", loc="left", fontsize=12)
    for i, v in enumerate(vals):
        ax.text(i, v + 80, f"{v:,}".replace(",", " "), ha="center", fontsize=11, color=NAVY)

    ax = axes[1]
    verbs = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    ofb = [methods.get(("OFB", v), 0) for v in verbs]
    bian = [methods.get(("BIAN", v), 0) for v in verbs]
    x = np.arange(len(verbs))
    w = 0.36
    ax.bar(x - w / 2, ofb, w, color=GOLD, label="OFB")
    ax.bar(x + w / 2, bian, w, color=NAVY, label="BIAN")
    ax.set_xticks(x, verbs)
    ax.set_ylabel("Operaciones")
    ax.set_title("Sesgo REST: OFB consulta · BIAN control", loc="left", fontsize=12)
    ax.legend(frameon=False)
    fig.tight_layout()
    save(fig, "grafico-fuentes.png")


if __name__ == "__main__":
    style()
    fig_alignment()
    fig_semantic()
    fig_sec()
    fig_catalogo()
    fig_fuentes()
