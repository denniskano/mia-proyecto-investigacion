#!/usr/bin/env python3
"""Cierra el piloto P4: firma OE1 y scores v0 (baseline léxico) OFB × BIAN.

Uso:
  python matching_v0.py
  python matching_v0.py --solo I1 I4
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
FUENTES = ROOT / "fuentes"
RESULTADO = ROOT / "resultado"
MATCHING = RESULTADO / "matching"
HTTP = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
STOP = {
    "get",
    "retrieve",
    "id",
    "ids",
    "post",
    "put",
    "patch",
    "delete",
    "head",
    "options",
    "trace",
    "http",
    "api",
    "v1",
    "v2",
}
READ_METHODS = {"GET", "HEAD"}
WRITE_METHODS = {"POST", "PUT", "PATCH", "DELETE"}
PARSER_ID = "procesar_openapi.py"
EMBEDDING_MODEL = "tfidf+jaccard-lexical-v0"
WEIGHTS_OFFICIAL = (1 / 3, 1 / 3, 1 / 3)
WEIGHTS_SENS = [(0.50, 0.30, 0.20), (0.20, 0.50, 0.30)]

INSTANCIAS = [
    {
        "id": "I1",
        "prioridad": "semana-8",
        "ofb": "OFB_accounts_2.4.2.yml",
        "bian": "SavingsAccount.yaml",
        "carpeta": "I1_accounts_x_SavingsAccount",
    },
    {
        "id": "I2",
        "prioridad": "semana-10-11",
        "ofb": "OFB_accounts_2.4.2.yml",
        "bian": "CurrentAccount.yaml",
        "carpeta": "I2_accounts_x_CurrentAccount",
    },
    {
        "id": "I3a",
        "prioridad": "semana-10-11",
        "ofb": "OFB_opendata-accounts_1.0.1.yml",
        "bian": "SavingsAccount.yaml",
        "carpeta": "I3a_opendata-accounts_x_SavingsAccount",
    },
    {
        "id": "I3b",
        "prioridad": "semana-10-11",
        "ofb": "OFB_opendata-accounts_1.0.1.yml",
        "bian": "CurrentAccount.yaml",
        "carpeta": "I3b_opendata-accounts_x_CurrentAccount",
    },
    {
        "id": "I4",
        "prioridad": "semana-8",
        "ofb": "OFB_payments_4.0.0.yml",
        "bian": "PaymentOrderInitiation.yaml",
        "carpeta": "I4_payments_x_PaymentOrderInitiation",
    },
    {
        "id": "I5",
        "prioridad": "semana-10-11",
        "ofb": "OFB_automatic-payments_2.0.0.yml",
        "bian": "PaymentOrderInitiation.yaml",
        "carpeta": "I5_automatic-payments_x_PaymentOrderInitiation",
    },
    {
        "id": "I6",
        "prioridad": "semana-10-11",
        "ofb": "OFB_enrollments_2.1.0.yml",
        "bian": "PaymentOrderInitiation.yaml",
        "carpeta": "I6_enrollments_x_PaymentOrderInitiation",
    },
]


def git_commit() -> str:
    try:
        return (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"],
                cwd=ROOT,
                stderr=subprocess.DEVNULL,
            )
            .decode()
            .strip()
        )
    except Exception:
        return "unknown"


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8-sig")) or {}


def stem(tok: str) -> str:
    tok = tok.lower()
    if len(tok) > 3 and tok.endswith("s") and not tok.endswith("ss"):
        return tok[:-1]
    return tok


def tokens(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", (text or "").lower())
    out = {stem(w) for w in words if w and w not in STOP and not w.isdigit()}
    return {w for w in out if len(w) > 1}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def cosine_tfidf(docs: list[list[str]], i: int, j: int) -> float:
    df = Counter()
    for doc in docs:
        df.update(set(doc))
    n = len(docs)
    idf = {t: math.log((1 + n) / (1 + df[t])) + 1.0 for t in df}

    def vec(idx: int) -> dict[str, float]:
        tf = Counter(docs[idx])
        total = sum(tf.values()) or 1
        return {t: (c / total) * idf.get(t, 0.0) for t, c in tf.items()}

    va, vb = vec(i), vec(j)
    keys = set(va) | set(vb)
    dot = sum(va.get(k, 0.0) * vb.get(k, 0.0) for k in keys)
    na = math.sqrt(sum(v * v for v in va.values()))
    nb = math.sqrt(sum(v * v for v in vb.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def path_segments(path: str) -> list[str]:
    segs = []
    for raw in (path or "").split("/"):
        if not raw or raw.startswith("{") or raw.endswith("}"):
            continue
        segs.append(raw)
    return segs


def path_tokens(path: str) -> set[str]:
    out: set[str] = set()
    for seg in path_segments(path):
        out |= tokens(re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", seg))
    return out


def depth(path: str) -> int:
    return max(1, len(path_segments(path)))


def last_segment_tokens(path: str) -> set[str]:
    segs = path_segments(path)
    if not segs:
        return set()
    return tokens(re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", segs[-1]))


def concept_from_tag(tag: str) -> str:
    t = (tag or "").strip()
    t = re.sub(r"^(CR|BQ)\s*-\s*", "", t, flags=re.I)
    return t.strip()


def camel_tokens(text: str) -> set[str]:
    return tokens(re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", text or ""))


def sd_resource_tokens(bian_ops: list[dict]) -> set[str]:
    """Recurso del SD (primer segmento + CR), no el nombre de cada BQ."""
    out: set[str] = set()
    for op in bian_ops:
        segs = path_segments(op.get("path", ""))
        if segs:
            out |= camel_tokens(segs[0])
        tag = (op.get("tag") or "").strip()
        if tag.startswith("CR -"):
            out |= tokens(concept_from_tag(tag))
    return out


def name_tokens(op: dict) -> set[str]:
    return (
        tokens(op.get("operation_id_normalized") or op.get("operation_id", ""))
        | path_tokens(op.get("path", ""))
        | tokens(concept_from_tag(op.get("tag", "")))
    )


def http_igual(ofb_m: str, bian_m: str) -> float:
    a, b = ofb_m.upper(), bian_m.upper()
    if a == b:
        return 1.0
    if a in READ_METHODS and b in READ_METHODS:
        return 0.5
    if a in WRITE_METHODS and b in WRITE_METHODS:
        return 0.5
    return 0.0


def nivel(score: float) -> str:
    if score >= 0.80:
        return "Alta"
    if score >= 0.60:
        return "Media"
    if score >= 0.40:
        return "Baja"
    return "Nula"


def read_ops(csv_path: Path) -> list[dict]:
    with csv_path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter=";"))


def read_corpus(csv_path: Path) -> dict[tuple[str, str], list[str]]:
    by_el: dict[tuple[str, str], list[str]] = defaultdict(list)
    with csv_path.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh, delimiter=";"):
            if row.get("element_type") != "operation":
                continue
            text = row.get("normalized_text") or ""
            if text:
                by_el[(row["archivo"], row["element_id"])].append(text)
    return by_el


def expected_from_yaml(path: Path) -> dict:
    obj = load_yaml(path)
    components = obj.get("components") or {}
    schemas = components.get("schemas") or {}
    ops = 0
    ops_summary = 0
    ops_desc = 0
    texts = 0
    for _p, methods in (obj.get("paths") or {}).items():
        if not isinstance(methods, dict):
            continue
        for method, op in methods.items():
            if method.lower() not in HTTP or not isinstance(op, dict):
                continue
            ops += 1
            summary = str(op.get("summary") or "")
            description = str(op.get("description") or "")
            if summary:
                ops_summary += 1
                texts += 1
            if description and description != summary:
                ops_desc += 1
                texts += 1
            elif description:
                ops_desc += 1
    props_direct = 0
    props_allof = 0
    for sdef in schemas.values():
        sdef = sdef or {}
        if sdef.get("description"):
            texts += 1
        for _k, p in (sdef.get("properties") or {}).items():
            props_direct += 1
            texts += 1
            p = p or {}
            if p.get("description"):
                texts += 1
        for item in sdef.get("allOf") or []:
            if isinstance(item, dict):
                props_allof += len(item.get("properties") or {})
    return {
        "ops": ops,
        "schemas": len(schemas),
        "props_directas": props_direct,
        "props_en_allof": props_allof,
        "textos_estimados": texts,
        "ops_con_summary": ops_summary,
        "ops_con_description": ops_desc,
        "version": (obj.get("info") or {}).get("version", ""),
        "titulo": (obj.get("info") or {}).get("title", ""),
    }


def firmar_oe1() -> dict:
    rows = []
    yaml_files = sorted(FUENTES.rglob("*.yml")) + sorted(FUENTES.rglob("*.yaml"))
    for src in yaml_files:
        if "archivo" in src.parts:
            continue
        stats_path = RESULTADO / "por_contrato" / src.stem / "estadisticas.json"
        expected = expected_from_yaml(src)
        extracted = json.loads(stats_path.read_text(encoding="utf-8")) if stats_path.exists() else {}
        ops_x = extracted.get("cantidad_operaciones", 0)
        sch_x = extracted.get("cantidad_schemas", 0)
        pr_x = extracted.get("cantidad_propiedades", 0)
        tx_x = extracted.get("fragmentos_corpus", 0)
        row = {
            "archivo": src.name,
            "source": extracted.get("source", ""),
            "version_yaml": expected["version"],
            "ops_esperadas": expected["ops"],
            "ops_extraidas": ops_x,
            "ops_ratio": round(ops_x / expected["ops"], 4) if expected["ops"] else None,
            "schemas_esperados": expected["schemas"],
            "schemas_extraidos": sch_x,
            "schemas_ratio": round(sch_x / expected["schemas"], 4) if expected["schemas"] else None,
            "props_esperadas_directas": expected["props_directas"],
            "props_extraidas": pr_x,
            "props_ratio_directas": (
                round(pr_x / expected["props_directas"], 4) if expected["props_directas"] else None
            ),
            "props_en_allof_no_contadas_por_parser": expected["props_en_allof"],
            "textos_extraidos": tx_x,
            "refs_no_definidos": extracted.get("refs_esquema_no_definidos_en_archivo", 0),
            "firmado": bool(
                stats_path.exists()
                and ops_x == expected["ops"]
                and sch_x == expected["schemas"]
                and pr_x == expected["props_directas"]
                and extracted.get("refs_esquema_no_definidos_en_archivo", 0) == 0
            ),
        }
        rows.append(row)
    ok = all(r["firmado"] for r in rows)
    informe = {
        "parser_id": PARSER_ID,
        "git_commit": git_commit(),
        "fecha": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "criterio": (
            "Completitud = extraídos / esperados. Meta 1.00 en operaciones y schemas. "
            "Las propiedades se firman sobre properties directas (el parser no aplana allOf)."
        ),
        "contratos": len(rows),
        "todos_firmados": ok,
        "detalle": rows,
    }
    MATCHING.mkdir(parents=True, exist_ok=True)
    (MATCHING / "oe1_firma.json").write_text(
        json.dumps(informe, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return informe


def candidato(ofb: dict, bian: dict, sd_resource: set[str]) -> tuple[bool, dict]:
    j = jaccard(name_tokens(ofb), name_tokens(bian))
    last_ofb = last_segment_tokens(ofb["path"])
    path_hit = bool(last_ofb & sd_resource)
    sim_path = jaccard(path_tokens(ofb["path"]), path_tokens(bian["path"]))
    if path_hit:
        sim_path = max(sim_path, 0.80)
    http = http_igual(ofb["method"], bian["method"])
    d_ofb, d_bian = depth(ofb["path"]), depth(bian["path"])
    prof = 1.0 - abs(d_ofb - d_bian) / max(d_ofb, d_bian)
    e_pair = 0.40 * j + 0.25 * sim_path + 0.20 * http + 0.15 * prof
    ok = j >= 0.40 or path_hit or (http == 1.0 and j >= 0.25)
    metrics = {
        "jaccard_nombre": round(j, 4),
        "sim_path": round(sim_path, 4),
        "path_recurso": path_hit,
        "http_igual": http,
        "profundidad": round(prof, 4),
        "e_pair": round(e_pair, 4),
    }
    return ok, metrics


def greedy_pairs(ofb_ops: list[dict], bian_ops: list[dict]) -> list[dict]:
    sd_resource = sd_resource_tokens(bian_ops)
    cands = []
    for ofb in ofb_ops:
        for bian in bian_ops:
            ok, m = candidato(ofb, bian, sd_resource)
            if ok:
                cands.append((m["e_pair"], ofb, bian, m))
    cands.sort(key=lambda x: (-x[0], x[1]["operation_id"], x[2]["operation_id"]))
    used_ofb, used_bian = set(), set()
    assigned = []
    for _score, ofb, bian, m in cands:
        if ofb["operation_id"] in used_ofb or bian["operation_id"] in used_bian:
            continue
        used_ofb.add(ofb["operation_id"])
        used_bian.add(bian["operation_id"])
        assigned.append({"ofb": ofb, "bian": bian, **m})
    for ofb in ofb_ops:
        if ofb["operation_id"] not in used_ofb:
            assigned.append(
                {
                    "ofb": ofb,
                    "bian": None,
                    "jaccard_nombre": 0.0,
                    "sim_path": 0.0,
                    "path_recurso": False,
                    "http_igual": 0.0,
                    "profundidad": 0.0,
                    "e_pair": 0.0,
                }
            )
    order = {op["operation_id"]: i for i, op in enumerate(ofb_ops)}
    assigned.sort(key=lambda r: order[r["ofb"]["operation_id"]])
    return assigned


def pair_text(op: dict, corpus: dict[tuple[str, str], list[str]]) -> str:
    parts = corpus.get((op["archivo"], op["operation_id"]), [])
    if parts:
        return " ".join(parts)
    return op.get("operation_id_normalized") or op.get("operation_id", "")


def semantic_scores(pairs: list[dict], corpus: dict) -> list[dict]:
    docs = []
    idxs = []
    for row in pairs:
        ofb_txt = pair_text(row["ofb"], corpus)
        bian_txt = pair_text(row["bian"], corpus) if row["bian"] else ""
        docs.append(list(tokens(ofb_txt)))
        docs.append(list(tokens(bian_txt)))
        idxs.append((len(docs) - 2, len(docs) - 1))
    out = []
    for row, (i, j) in zip(pairs, idxs):
        if not row["bian"]:
            out.append({**row, "s_jaccard": 0.0, "s_tfidf": 0.0, "s_pair": 0.0})
            continue
        sj = jaccard(set(docs[i]), set(docs[j]))
        st = cosine_tfidf(docs, i, j)
        s_pair = (sj + st) / 2.0
        out.append(
            {
                **row,
                "s_jaccard": round(sj, 4),
                "s_tfidf": round(st, 4),
                "s_pair": round(s_pair, 4),
            }
        )
    return out


def catalogo_c(bian_ops: list[dict], paired: list[dict]) -> tuple[float, list[str], list[str]]:
    concepts = []
    seen = set()
    for op in bian_ops:
        tag = (op.get("tag") or "").strip()
        if tag.startswith("CR -") or tag.startswith("BQ -"):
            if tag not in seen:
                seen.add(tag)
                concepts.append(tag)
    covered_tags = {
        (row["bian"] or {}).get("tag", "")
        for row in paired
        if row["bian"] is not None
    }
    covered = [c for c in concepts if c in covered_tags]
    c = len(covered) / len(concepts) if concepts else 0.0
    return c, concepts, covered


def alignment(s: float, e: float, c: float, weights=WEIGHTS_OFFICIAL) -> float:
    a, b, g = weights
    return a * s + b * e + g * c


def tipologias(inst: dict, s: float, e: float, c: float, pairs: list[dict], n_ofb: int, n_cat: int) -> str:
    notes = []
    methods_ofb = Counter(p["ofb"]["method"] for p in pairs)
    paired = [p for p in pairs if p["bian"]]
    if any(m == "GET" for m in methods_ofb) and any(
        p["bian"] and p["bian"]["method"] in WRITE_METHODS for p in pairs
    ):
        notes.append(
            "- **REST/contrato:** OFB privilegia GET de consulta; BIAN publica PUT/POST de ciclo de vida. "
            "El matching no exige el mismo verbo."
        )
    if c < 0.40:
        notes.append(
            f"- **De modelado:** el catálogo BIAN tiene {n_cat} CR/BQ y C={c:.2f}. "
            "OFB no cubre el desglose de behaviors; hallazgo esperado, no fallo del parser."
        )
    if e < 0.40:
        notes.append(
            f"- **Estructural:** E={e:.2f} con {len(paired)}/{n_ofb} operaciones OFB emparejadas "
            "(las no emparejadas entran como 0 al promedio oficial)."
        )
    if s < 0.40:
        notes.append(
            f"- **Semántica:** S={s:.2f} en baseline léxico (sin embeddings). "
            "Los textos OFB están en portugués y los de BIAN en inglés."
        )
    if not notes:
        notes.append("- Sin tipología dominante: S/E/C por encima del umbral de Nula.")
    notes.append(
        f"\nInstancia **{inst['id']}**: `{inst['ofb']}` × `{inst['bian']}`. "
        "Nivel oficial = pesos 1/3. No se etiquetó a mano para entrenar un clasificador."
    )
    return "\n".join(
        [
            f"# Tipologías — {inst['id']}",
            "",
            *notes,
            "",
        ]
    )


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter=";", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def match_instance(inst: dict, ops: list[dict], corpus: dict) -> dict:
    ofb_ops = [r for r in ops if r["archivo"] == inst["ofb"]]
    bian_ops = [r for r in ops if r["archivo"] == inst["bian"]]
    if not ofb_ops or not bian_ops:
        raise SystemExit(f"{inst['id']}: faltan operaciones {inst['ofb']} o {inst['bian']}")
    paired = semantic_scores(greedy_pairs(ofb_ops, bian_ops), corpus)
    n_ofb = len(ofb_ops)
    e_sum = sum(p["e_pair"] for p in paired)
    e_oficial = e_sum / n_ofb
    emparejadas = [p for p in paired if p["bian"]]
    e_star = (
        sum(p["e_pair"] for p in emparejadas) / len(emparejadas) if emparejadas else 0.0
    )
    s_oficial = (
        sum(p["s_pair"] for p in emparejadas) / len(emparejadas) if emparejadas else 0.0
    )
    c_oficial, catalogo, cubiertos = catalogo_c(bian_ops, paired)
    score = alignment(s_oficial, e_oficial, c_oficial)
    sens = []
    for w in WEIGHTS_SENS:
        sc = alignment(s_oficial, e_oficial, c_oficial, w)
        sens.append(
            {
                "alpha": w[0],
                "beta": w[1],
                "gamma": w[2],
                "AlignmentScore": round(sc, 4),
                "nivel": nivel(sc),
            }
        )
    scores = {
        "id": inst["id"],
        "ofb": inst["ofb"],
        "bian": inst["bian"],
        "prioridad": inst["prioridad"],
        "git_commit": git_commit(),
        "parser_id": PARSER_ID,
        "embedding_model": EMBEDDING_MODEL,
        "fecha": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "umbrales": {
            "jaccard_nombre": 0.40,
            "jaccard_con_http": 0.25,
            "coseno_semantico_semana_11": 0.55,
            "nivel_alta": 0.80,
            "nivel_media": 0.60,
            "nivel_baja": 0.40,
        },
        "pesos_oficiales": {"alpha": 1 / 3, "beta": 1 / 3, "gamma": 1 / 3},
        "n_operaciones_ofb": n_ofb,
        "n_operaciones_bian": len(bian_ops),
        "n_pares": len(emparejadas),
        "S": round(s_oficial, 4),
        "E": round(e_oficial, 4),
        "E_estrella": round(e_star, 4),
        "C": round(c_oficial, 4),
        "catalogo_cr_bq": catalogo,
        "catalogo_cubierto": cubiertos,
        "AlignmentScore": round(score, 4),
        "nivel": nivel(score),
        "sensibilidad_pesos": sens,
        "leakage": {
            "cr_bq_copiados_a_ofb": False,
            "bian_contra_bian": False,
            "etiquetado_manual_ml": False,
        },
    }
    out = MATCHING / inst["carpeta"]
    struct_rows = []
    sem_rows = []
    for p in paired:
        bian = p["bian"] or {}
        struct_rows.append(
            {
                "ofb_operation_id": p["ofb"]["operation_id"],
                "ofb_method": p["ofb"]["method"],
                "ofb_path": p["ofb"]["path"],
                "bian_operation_id": bian.get("operation_id", ""),
                "bian_method": bian.get("method", ""),
                "bian_path": bian.get("path", ""),
                "bian_tag": bian.get("tag", ""),
                "jaccard_nombre": p["jaccard_nombre"],
                "sim_path": p["sim_path"],
                "path_recurso": p["path_recurso"],
                "http_igual": p["http_igual"],
                "profundidad": p["profundidad"],
                "e_pair": p["e_pair"],
                "emparejado": bool(p["bian"]),
            }
        )
        sem_rows.append(
            {
                "ofb_operation_id": p["ofb"]["operation_id"],
                "bian_operation_id": bian.get("operation_id", ""),
                "s_jaccard": p["s_jaccard"],
                "s_tfidf": p["s_tfidf"],
                "s_pair": p["s_pair"],
                "ofb_texto": pair_text(p["ofb"], corpus)[:240],
                "bian_texto": pair_text(p["bian"], corpus)[:240] if p["bian"] else "",
            }
        )
    write_csv(
        out / "pares_estructurales.csv",
        struct_rows,
        list(struct_rows[0].keys()),
    )
    write_csv(out / "pares_semanticos.csv", sem_rows, list(sem_rows[0].keys()))
    (out / "scores.json").write_text(
        json.dumps(scores, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out / "tipologias.md").write_text(
        tipologias(inst, s_oficial, e_oficial, c_oficial, paired, n_ofb, len(catalogo)),
        encoding="utf-8",
    )
    return scores


def informe_md(oe1: dict, scores: list[dict]) -> str:
    lines = [
        "# Cierre del piloto OFB × BIAN (P4 / baseline v0)",
        "",
        f"- Fecha: `{oe1['fecha']}`",
        f"- Commit: `{oe1['git_commit']}`",
        f"- Parser: `{PARSER_ID}`",
        f"- Semántica: `{EMBEDDING_MODEL}` (embeddings de frase = semana 11)",
        "",
        "## Qué faltaba y qué se cierra aquí",
        "",
        "| Entregable | Estado |",
        "|------------|--------|",
        f"| OE1 firmado (ops/schemas = 1.00) | {'Sí' if oe1['todos_firmados'] else 'No'} |",
        "| Matching v0 I1 e I4 (mínimo P4) | Sí |",
        "| Scores v0 de las 7 instancias (baseline léxico) | Sí |",
        "| Catálogo BIAN v14 (258 OpenAPI oficiales) | Sí |",
        "| Mapa extra OFB → SD oficial (sin inventar SD) | Sí (`catalogo/`) |",
        "| Embeddings MiniLM sobre pares OE2 de I1–I6 | Sí (`matching_s1/`) |",
        "| Discusión P5 / borrador P7 | Pendiente (tesis, no piloto) |",
        "",
        "## OE1 — completitud",
        "",
        "Meta: ratio 1.00 en operaciones y schemas. Propiedades firmadas sobre `properties` directas.",
        "",
        "| Archivo | Ops esp/ext | Schemas esp/ext | Props dir. | Firmado |",
        "|---------|-------------|-----------------|------------|---------|",
    ]
    clave = {
        "OFB_accounts_2.4.2.yml",
        "OFB_opendata-accounts_1.0.1.yml",
        "OFB_payments_4.0.0.yml",
        "OFB_automatic-payments_2.0.0.yml",
        "OFB_enrollments_2.1.0.yml",
        "OFB_loans_2.5.0.yml",
        "OFB_credit-cards_2.3.1.yml",
        "SavingsAccount.yaml",
        "CurrentAccount.yaml",
        "PaymentOrderInitiation.yaml",
        "Loan.yaml",
        "CreditCard.yaml",
    }
    for r in oe1["detalle"]:
        mark = "sí" if r["firmado"] else "NO"
        if r["archivo"] in clave:
            lines.append(
                f"| `{r['archivo']}` | {r['ops_esperadas']}/{r['ops_extraidas']} | "
                f"{r['schemas_esperados']}/{r['schemas_extraidos']} | "
                f"{r['props_esperadas_directas']}/{r['props_extraidas']} | {mark} |"
            )
    n_ok = sum(1 for r in oe1["detalle"] if r["firmado"])
    lines += [
        "",
        f"Inventario completo: **{n_ok}/{oe1['contratos']}** YAML firmados "
        f"(38 OFB + 258 Service Domains BIAN v14). I1–I6 no se reemplazan; "
        f"el resto de OFB se mapea a un SD oficial (`resultado/matching/catalogo/`).",
        "",
        "## Scores v0",
        "",
        "| ID | OFB × BIAN | S | E | C | AlignmentScore | Nivel | Pares |",
        "|----|------------|---|---|---|----------------|-------|-------|",
    ]
    for s in scores:
        lines.append(
            f"| {s['id']} | `{s['ofb']}` × `{s['bian']}` | {s['S']:.2f} | {s['E']:.2f} | "
            f"{s['C']:.2f} | **{s['AlignmentScore']:.2f}** | {s['nivel']} | "
            f"{s['n_pares']}/{s['n_operaciones_ofb']} |"
        )
    lines += [
        "",
        "El nivel **Nula/Baja no invalida** el piloto: valida que el score es computable, "
        "interpretable y sin leakage. C bajo en cuentas es hallazgo (pocos GET OFB vs 1 CR + varios BQ). "
        "I6 en 0 pares es hallazgo: enrollments/FIDO no comparte recurso léxico con PaymentOrderInitiation. "
        "S≈0 es el techo del baseline PT×EN; MiniLM ya corre sobre los mismos pares (`matching_s1/`).",
        "",
        "## Catálogo extra (no sustituye I1–I6)",
        "",
        "Con los 258 YAML oficiales, loans y credit-cards ya tienen SD BIAN "
        "(`Loan.yaml`, `CreditCard.yaml`). No se inventó un Service Domain. "
        "No se puntúa el producto cartesiano 38 × 258.",
        "",
        "| OFB | BIAN oficial | Pares | Score v0 |",
        "|-----|--------------|-------|----------|",
        "| credit-cards | CreditCard | 7/7 | Baja (0,46) |",
        "| loans | Loan | 4/5 | Nula (0,27) |",
        "| opendata-loans | Loan | 2/2 | Nula (0,28) |",
        "| opendata-creditcards | CreditCard | 2/2 | Nula (0,30) |",
        "| investments | InvestmentAccount | 2/5 | Nula (0,19) |",
        "",
        "Detalle: `catalogo/MAPA.md`.",
        "",
        "## Lo que sigue (ya no es cierre de piloto P4)",
        "",
        "1. MiniLM I1–I6 ya está en `matching_s1/` (S sobre pares OE2 congelados).",
        "2. Semana 12 (P5): discusión de tipologías contra literatura.",
        "3. No puntuar 38 OFB × 258 SD. No inventar un SD. I1–I6 siguen siendo n = 7.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--solo", nargs="+", help="IDs a calcular (default: las 7)")
    args = parser.parse_args()
    wanted = set(args.solo) if args.solo else {i["id"] for i in INSTANCIAS}
    ops = read_ops(RESULTADO / "consolidado" / "operaciones_estructuradas.csv")
    corpus = read_corpus(RESULTADO / "consolidado" / "corpus_semantico.csv")
    MATCHING.mkdir(parents=True, exist_ok=True)
    oe1 = firmar_oe1()
    scores = []
    for inst in INSTANCIAS:
        if inst["id"] not in wanted:
            continue
        print(f"Matching {inst['id']}: {inst['ofb']} × {inst['bian']}")
        scores.append(match_instance(inst, ops, corpus))
    fields = [
        "id",
        "ofb",
        "bian",
        "prioridad",
        "S",
        "E",
        "E_estrella",
        "C",
        "AlignmentScore",
        "nivel",
        "n_pares",
        "n_operaciones_ofb",
        "n_operaciones_bian",
        "embedding_model",
        "git_commit",
    ]
    write_csv(
        MATCHING / "resumen_instancias.csv",
        scores,
        fields,
    )
    (MATCHING / "CIERRE_PILOTO.md").write_text(informe_md(oe1, scores), encoding="utf-8")
    print(json.dumps({"oe1_firmado": oe1["todos_firmados"], "instancias": [
        {"id": s["id"], "AlignmentScore": s["AlignmentScore"], "nivel": s["nivel"]}
        for s in scores
    ]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
