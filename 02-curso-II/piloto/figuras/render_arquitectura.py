#!/usr/bin/env python3
"""Renderiza arquitectura-piloto.png (16:9) para la lámina Beamer."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).with_name("arquitectura-piloto.png")
W, H = 3200, 1800
NAVY = (27, 54, 93)
GOLD = (232, 163, 35)
GREEN = (30, 127, 79)
ALT = (238, 242, 247)
MUTED = (99, 110, 114)
WHITE = (255, 255, 255)
BLACK = (20, 28, 40)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        ("/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf"),
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def rounded(draw: ImageDraw.ImageDraw, xy, r, fill, outline=None, width=3):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def center_text(draw, box, lines, fonts, fills):
    x0, y0, x1, y1 = box
    heights = []
    widths = []
    for line, fnt in zip(lines, fonts):
        b = draw.textbbox((0, 0), line, font=fnt)
        widths.append(b[2] - b[0])
        heights.append(b[3] - b[1])
    gap = 8
    total = sum(heights) + gap * (len(lines) - 1)
    y = y0 + (y1 - y0 - total) / 2
    cx = (x0 + x1) / 2
    for line, fnt, fill, tw, th in zip(lines, fonts, fills, widths, heights):
        draw.text((cx - tw / 2, y), line, font=fnt, fill=fill)
        y += th + gap


def chevron(draw, x, y, h=36, w=22):
    draw.polygon([(x, y), (x + w, y + h / 2), (x, y + h)], fill=NAVY)


def main() -> None:
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)
    title = font(54, True)
    sub = font(26)
    colh = font(32, True)
    body_b = font(28, True)
    body = font(24)
    small = font(22)
    tiny = font(20)

    d.text((W / 2, 36), "Arquitectura del piloto  ·  OFB × BIAN v14", font=title, fill=NAVY, anchor="ma")
    d.text(
        (W / 2, 100),
        "Objeto: contrato OpenAPI bancario   ·   Muestra: Open Finance Brasil   ·   Referencia: catálogo BIAN 14.0.0",
        font=sub,
        fill=MUTED,
        anchor="ma",
    )

    cols = [
        (56, "1. Fuentes oficiales"),
        (836, "2. Parser OE1"),
        (1616, "3. Matching"),
        (2396, "4. Scores"),
    ]
    col_w, col_top, col_h = 748, 150, 1188
    for x, label in cols:
        rounded(d, (x, col_top, x + col_w, col_top + col_h), 18, ALT, NAVY, 3)
        d.rectangle((x, col_top, x + col_w, col_top + 78), fill=NAVY)
        d.text((x + col_w / 2, col_top + 39), label, font=colh, fill=WHITE, anchor="mm")

    boxes = [
        (80, 260, 780, 480, WHITE, NAVY, ["Open Finance Brasil", "38 YAML  ·  160 operaciones", "accounts, payments, loans, cards…"], False),
        (80, 510, 780, 760, WHITE, NAVY, ["BIAN v14", "258 Service Domains  ·  4 580 ops", "descargar_bian.py  ·  release 14.0.0"], False),
        (80, 790, 780, 1260, WHITE, GOLD, ["Reglas de adquisición", "Sin banco emisor  ·  sin recorte de 12 ops", "No se inventa un Service Domain"], False),
        (860, 260, 1560, 480, WHITE, NAVY, ["procesar_openapi.py", "OpenAPI 3.x  ·  $ref anidados", "ops, schemas, propiedades, corpus"], False),
        (860, 510, 1560, 720, WHITE, NAVY, ["Representación intermedia", "CSV por contrato + consolidado", "inventario.json"], False),
        (860, 750, 1560, 1260, GREEN, GREEN, ["OE1 firmado  ·  296 / 296 YAML", "ops y schemas = 1,00", "Parser 100 % ≠ AlignmentScore Alto"], True),
        (1640, 260, 2340, 480, WHITE, NAVY, ["matching_v0.py", "I1–I6 oficiales (n = 7)", "S léxico  ·  E greedy  ·  C CR/BQ"], False),
        (1640, 510, 2340, 720, WHITE, GOLD, ["matching_s1.py  ·  MiniLM", "S sobre pares OE2 congelados", "E y C no se recalculan"], False),
        (1640, 750, 2340, 1260, WHITE, NAVY, ["mapa_ofb_bian.py", "Catálogo extra (no sustituye n = 7)", "loans × Loan  ·  cards × CreditCard"], False),
        (2420, 260, 3120, 460, GOLD, GOLD, ["AlignmentScore = (S + E + C) / 3", "Alta ≥ 0,80   Media   Baja", "Nula < 0,40"], False),
        (2420, 490, 3120, 680, WHITE, NAVY, ["resultado/matching/", "I1–I6  ·  oe1_firma.json", "CIERRE_PILOTO.md"], False),
        (2420, 710, 3120, 880, WHITE, NAVY, ["resultado/matching_s1/", "S MiniLM de I1–I6"], False),
        (2420, 910, 3120, 1260, WHITE, NAVY, ["resultado/matching/catalogo/", "MAPA.md  ·  cards Baja 0,46"], False),
    ]
    for x0, y0, x1, y1, fill, outline, lines, on_green in boxes:
        rounded(d, (x0, y0, x1, y1), 16, fill, outline, 4)
        fonts = [body_b, body, small][: len(lines)]
        if on_green:
            fills = [WHITE] * len(lines)
        elif fill == GOLD:
            fills = [NAVY] * len(lines)
        else:
            fills = [NAVY, BLACK, MUTED][: len(lines)]
        center_text(d, (x0 + 16, y0 + 10, x1 - 16, y1 - 10), lines, fonts, fills)

    for y in (360, 620):
        chevron(d, 798, y)
        chevron(d, 1578, y)
        chevron(d, 2358, y)
    chevron(d, 1578, 980)
    chevron(d, 2358, 980)

    rounded(d, (56, 1370, 3144, 1490), 16, NAVY, NAVY, 2)
    d.text(
        (W / 2, 1406),
        "Prohibido: copiar CR/BQ a OFB   ·   BIAN ↔ BIAN como banco   ·   inventar un SD   ·   etiquetar Alta/Media/Baja a mano",
        font=small,
        fill=WHITE,
        anchor="ma",
    )
    d.text(
        (W / 2, 1454),
        "I1–I6 no se reemplazan   ·   no se puntúa 38 OFB × 258 SD",
        font=small,
        fill=GOLD,
        anchor="ma",
    )
    d.text(
        (W / 2, 1568),
        "Dorado = experimento IA (MiniLM)    ·    Verde = OE1 cerrado    ·    Blanco = artefactos del piloto",
        font=tiny,
        fill=MUTED,
        anchor="ma",
    )

    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} {img.size}")


if __name__ == "__main__":
    main()
