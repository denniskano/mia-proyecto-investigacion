#!/usr/bin/env python3
"""SemanticScore v1: embeddings sobre los pares estructurales ya congelados (OE2).

No reabre el matching de E. No busca pares semánticos sueltos.
Modelo oficial del protocolo: paraphrase-multilingual-MiniLM-L12-v2.

Uso:
  .venv/bin/python matching_s1.py
"""
from __future__ import annotations

import csv
import json
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESULTADO = ROOT / "resultado"
MATCH_V0 = RESULTADO / "matching"
MATCH_S1 = RESULTADO / "matching_s1"
MODEL_ID = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
PARSER_ID = "procesar_openapi.py"
THRESHOLDS = (0.45, 0.55, 0.65)
WEIGHTS_OFFICIAL = (1 / 3, 1 / 3, 1 / 3)
WEIGHTS_SENS = [(0.50, 0.30, 0.20), (0.20, 0.50, 0.30)]

INSTANCIAS = [
    "I1_accounts_x_SavingsAccount",
    "I2_accounts_x_CurrentAccount",
    "I3a_opendata-accounts_x_SavingsAccount",
    "I3b_opendata-accounts_x_CurrentAccount",
    "I4_payments_x_PaymentOrderInitiation",
    "I5_automatic-payments_x_PaymentOrderInitiation",
    "I6_enrollments_x_PaymentOrderInitiation",
]


def git_commit() -> str:
    try:
        return (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=ROOT, stderr=subprocess.DEVNULL
            )
            .decode()
            .strip()
        )
    except Exception:
        return "unknown"


def nivel(score: float) -> str:
    if score >= 0.80:
        return "Alta"
    if score >= 0.60:
        return "Media"
    if score >= 0.40:
        return "Baja"
    return "Nula"


def alignment(s: float, e: float, c: float, weights=WEIGHTS_OFFICIAL) -> float:
    a, b, g = weights
    return a * s + b * e + g * c


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter=";"))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter=";", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def load_corpus() -> dict[tuple[str, str], dict[str, str]]:
    """archivo, operation_id -> {raw, normalized}."""
    by: dict[tuple[str, str], dict[str, list[str]]] = defaultdict(
        lambda: {"raw": [], "normalized": []}
    )
    path = RESULTADO / "consolidado" / "corpus_semantico.csv"
    for row in read_csv(path):
        if row.get("element_type") != "operation":
            continue
        key = (row["archivo"], row["element_id"])
        raw = (row.get("raw_text") or "").strip()
        norm = (row.get("normalized_text") or "").strip()
        if raw and raw not in by[key]["raw"]:
            by[key]["raw"].append(raw)
        if norm and norm not in by[key]["normalized"]:
            by[key]["normalized"].append(norm)
    out = {}
    for key, parts in by.items():
        out[key] = {
            "raw": " ".join(parts["raw"]),
            "normalized": " ".join(parts["normalized"]),
        }
    return out


def text_for(archivo: str, op_id: str, corpus: dict) -> str:
    blob = corpus.get((archivo, op_id), {})
    raw = blob.get("raw") or ""
    if raw:
        return raw
    return blob.get("normalized") or op_id


def cosine_pairs(model, texts_a: list[str], texts_b: list[str]) -> list[float]:
    import numpy as np

    if not texts_a:
        return []
    ea = model.encode(texts_a, normalize_embeddings=True, show_progress_bar=False)
    eb = model.encode(texts_b, normalize_embeddings=True, show_progress_bar=False)
    return [float(np.dot(ea[i], eb[i])) for i in range(len(texts_a))]


def process_instance(carpeta: str, corpus: dict, model) -> dict:
    v0 = json.loads((MATCH_V0 / carpeta / "scores.json").read_text(encoding="utf-8"))
    pares = read_csv(MATCH_V0 / carpeta / "pares_estructurales.csv")
    ofb_file = v0["ofb"]
    bian_file = v0["bian"]

    ofb_texts, bian_texts, flags = [], [], []
    for row in pares:
        emparejado = str(row.get("emparejado", "")).lower() in {"true", "1", "yes"}
        ofb_id = row["ofb_operation_id"]
        bian_id = row.get("bian_operation_id") or ""
        if not emparejado or not bian_id:
            flags.append(False)
            ofb_texts.append(text_for(ofb_file, ofb_id, corpus))
            bian_texts.append("")
            continue
        flags.append(True)
        ofb_texts.append(text_for(ofb_file, ofb_id, corpus))
        bian_texts.append(text_for(bian_file, bian_id, corpus))

    paired_idx = [i for i, ok in enumerate(flags) if ok]
    if paired_idx:
        cosines_paired = cosine_pairs(
            model,
            [ofb_texts[i] for i in paired_idx],
            [bian_texts[i] for i in paired_idx],
        )
        by_pair = dict(zip(paired_idx, cosines_paired))
    else:
        by_pair = {}

    sem_rows = []
    s_vals = []
    for i, row in enumerate(pares):
        cos = round(by_pair.get(i, 0.0), 4) if flags[i] else 0.0
        if flags[i]:
            s_vals.append(by_pair[i])
        sem_rows.append(
            {
                "ofb_operation_id": row["ofb_operation_id"],
                "bian_operation_id": row.get("bian_operation_id", ""),
                "s_coseno": cos,
                "s_ge_045": flags[i] and by_pair.get(i, 0) >= 0.45,
                "s_ge_055": flags[i] and by_pair.get(i, 0) >= 0.55,
                "s_ge_065": flags[i] and by_pair.get(i, 0) >= 0.65,
                "ofb_texto": ofb_texts[i][:240],
                "bian_texto": bian_texts[i][:240] if flags[i] else "",
            }
        )

    s_oficial = sum(s_vals) / len(s_vals) if s_vals else 0.0
    e_oficial = v0["E"]
    c_oficial = v0["C"]
    score = alignment(s_oficial, e_oficial, c_oficial)
    n_par = len(s_vals)
    sens_umbral = []
    for t in THRESHOLDS:
        n_ok = sum(1 for x in s_vals if x >= t)
        s_clip = (sum(x if x >= t else 0.0 for x in s_vals) / n_par) if n_par else 0.0
        sens_umbral.append(
            {
                "umbral": t,
                "pares_sobre_umbral": n_ok,
                "fraccion": round(n_ok / n_par, 4) if n_par else 0.0,
                "S_si_bajo_umbral_es_cero": round(s_clip, 4),
                "AlignmentScore_con_S_clip": round(
                    alignment(s_clip, e_oficial, c_oficial), 4
                ),
            }
        )
    sens_pesos = []
    for w in WEIGHTS_SENS:
        sc = alignment(s_oficial, e_oficial, c_oficial, w)
        sens_pesos.append(
            {
                "alpha": w[0],
                "beta": w[1],
                "gamma": w[2],
                "AlignmentScore": round(sc, 4),
                "nivel": nivel(sc),
            }
        )

    scores = {
        "id": v0["id"],
        "ofb": ofb_file,
        "bian": bian_file,
        "prioridad": v0.get("prioridad", ""),
        "git_commit": git_commit(),
        "parser_id": PARSER_ID,
        "embedding_model": MODEL_ID,
        "text_field": "raw_text (fallback: normalized_text / operation_id)",
        "pares_estructurales": "congelados de matching v0 (OE2)",
        "fecha": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "S_v0_lexico": v0["S"],
        "S": round(s_oficial, 4),
        "E": e_oficial,
        "E_estrella": v0.get("E_estrella"),
        "C": c_oficial,
        "AlignmentScore_v0": v0["AlignmentScore"],
        "AlignmentScore": round(score, 4),
        "nivel_v0": v0["nivel"],
        "nivel": nivel(score),
        "n_pares": n_par,
        "n_operaciones_ofb": v0["n_operaciones_ofb"],
        "catalogo_cr_bq": v0.get("catalogo_cr_bq", []),
        "catalogo_cubierto": v0.get("catalogo_cubierto", []),
        "umbrales": {
            "coseno_semantico": 0.55,
            "sensibilidad_coseno": list(THRESHOLDS),
            "nivel_alta": 0.80,
            "nivel_media": 0.60,
            "nivel_baja": 0.40,
        },
        "pesos_oficiales": {"alpha": 1 / 3, "beta": 1 / 3, "gamma": 1 / 3},
        "sensibilidad_umbral_S": sens_umbral,
        "sensibilidad_pesos": sens_pesos,
        "leakage": {
            "cr_bq_copiados_a_ofb": False,
            "bian_contra_bian": False,
            "etiquetado_manual_ml": False,
            "pares_semanticos_sueltos": False,
        },
    }

    out = MATCH_S1 / carpeta
    write_csv(out / "pares_semanticos.csv", sem_rows, list(sem_rows[0].keys()) if sem_rows else [
        "ofb_operation_id", "bian_operation_id", "s_coseno"
    ])
    (out / "scores.json").write_text(
        json.dumps(scores, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out / "tipologias.md").write_text(
        (
            f"# Tipologías — {v0['id']} (S v1 embeddings)\n\n"
            f"- **S léxico v0** = {v0['S']:.2f}. **S MiniLM** = {s_oficial:.2f}. "
            f"E y C se congelaron ({e_oficial:.2f} / {c_oficial:.2f}).\n"
            f"- AlignmentScore {v0['AlignmentScore']:.2f} ({v0['nivel']}) → "
            f"**{score:.2f} ({nivel(score)})**.\n"
            f"- Pares OE2: {n_par}/{v0['n_operaciones_ofb']}. "
            f"No se buscaron pares semánticos que contradigan E.\n"
            f"- Modelo: `{MODEL_ID}`.\n"
        ),
        encoding="utf-8",
    )
    return scores


def main() -> None:
    from sentence_transformers import SentenceTransformer

    print(f"Cargando {MODEL_ID}")
    model = SentenceTransformer(MODEL_ID)
    corpus = load_corpus()
    MATCH_S1.mkdir(parents=True, exist_ok=True)
    scores = []
    for carpeta in INSTANCIAS:
        print(f"S v1 {carpeta}")
        scores.append(process_instance(carpeta, corpus, model))
    fields = [
        "id",
        "ofb",
        "bian",
        "S_v0_lexico",
        "S",
        "E",
        "C",
        "AlignmentScore_v0",
        "AlignmentScore",
        "nivel_v0",
        "nivel",
        "n_pares",
        "embedding_model",
    ]
    write_csv(MATCH_S1 / "resumen_instancias.csv", scores, fields)
    lines = [
        "# SemanticScore v1 — MiniLM sobre pares OE2 congelados",
        "",
        f"Modelo: `{MODEL_ID}`",
        "E y C no se recalcularon. No hay pares semánticos sueltos.",
        "",
        "| ID | S v0 | S MiniLM | E | C | Score v0 | Score v1 | Nivel v0 → v1 |",
        "|----|------|----------|---|---|----------|----------|---------------|",
    ]
    for s in scores:
        lines.append(
            f"| {s['id']} | {s['S_v0_lexico']:.2f} | **{s['S']:.2f}** | {s['E']:.2f} | "
            f"{s['C']:.2f} | {s['AlignmentScore_v0']:.2f} | **{s['AlignmentScore']:.2f}** | "
            f"{s['nivel_v0']} → {s['nivel']} |"
        )
    lines += [
        "",
        "S oficial = promedio del coseno de los pares estructurales. "
        "El umbral 0,55 se reporta como sensibilidad, no recorta el S oficial.",
        "",
    ]
    (MATCH_S1 / "COMPARACION_V0_V1.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(
        [
            {
                "id": s["id"],
                "S_v0": s["S_v0_lexico"],
                "S_v1": s["S"],
                "score_v0": s["AlignmentScore_v0"],
                "score_v1": s["AlignmentScore"],
                "nivel_v1": s["nivel"],
            }
            for s in scores
        ],
        indent=2,
        ensure_ascii=False,
    ))


if __name__ == "__main__":
    main()
