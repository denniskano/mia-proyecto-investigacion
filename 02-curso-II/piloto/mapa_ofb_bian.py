#!/usr/bin/env python3
"""Mapa OFB → Service Domain BIAN oficial (catálogo v14 completo).

No inventa SD. No puntúa BIAN contra BIAN. I1–I6 del protocolo no se pisan.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

import matching_v0 as m0

ROOT = Path(__file__).resolve().parent
OUT = m0.RESULTADO / "matching" / "catalogo"

# Emparejamientos naturales con YAML BIAN oficiales (no inventados).
CURADO = {
    "accounts": ["SavingsAccount.yaml", "CurrentAccount.yaml"],
    "opendata-accounts": ["SavingsAccount.yaml", "CurrentAccount.yaml"],
    "payments": ["PaymentOrderInitiation.yaml"],
    "automatic-payments": ["PaymentOrderInitiation.yaml"],
    "enrollments": ["PartyAuthentication.yaml", "CustomerAccessEntitlement.yaml"],
    "loans": ["Loan.yaml", "ConsumerLoan.yaml"],
    "opendata-loans": ["Loan.yaml"],
    "credit-cards": ["CreditCard.yaml"],
    "opendata-creditcards": ["CreditCard.yaml"],
    "financings": ["CreditFacility.yaml"],
    "opendata-financings": ["CreditFacility.yaml"],
    "invoice-financings": ["Factoring.yaml"],
    "opendata-invoicefinancings": ["Factoring.yaml"],
    "unarranged-accounts-overdraft": ["CurrentAccount.yaml", "CreditFacility.yaml"],
    "opendata-unarranged": ["CurrentAccount.yaml"],
    "customers": ["PartyReferenceDataDirectory.yaml"],
    "consents": ["CustomerAccessEntitlement.yaml"],
    "investments": ["InvestmentAccount.yaml"],
    "funds": ["MutualFundAdministration.yaml"],
    "exchange": ["CurrencyExchange.yaml"],
    "exchanges": ["CurrencyExchange.yaml"],
    "acquiring-services": ["MerchantAcquiringFacility.yaml"],
    "channels": ["eBranchOperations.yaml"],
    "bank-fixed-incomes": ["TermDeposit.yaml"],
    "credit-portability": ["CreditFacility.yaml"],
    "payroll-credit-portability": ["CorporatePayrollServices.yaml"],
    "products-services": ["ProductDirectory.yaml"],
    "variable-incomes": ["InvestmentAccount.yaml"],
    "treasure-titles": ["CustodyAdministration.yaml"],
    "insurances": ["Underwriting.yaml"],
    "pension": ["TrustServices.yaml"],
}

OFICIALES = {inst["id"] for inst in m0.INSTANCIAS}
STOP = {"ofb", "api", "opendata", "services", "service", "and"}


def tokens(name: str) -> set[str]:
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", name)
    s = re.sub(r"[_\-/]+", " ", s)
    words = re.findall(r"[a-z0-9]+", s.lower())
    out = set()
    for w in words:
        if w in STOP or w.isdigit() or len(w) < 3:
            continue
        if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
            w = w[:-1]
        out.add(w)
    return out


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def ofb_slug(filename: str) -> str:
    stem = Path(filename).stem
    m = re.match(r"OFB_(.+)_(\d.+)$", stem)
    return m.group(1) if m else stem


def main() -> None:
    ops = m0.read_ops(m0.RESULTADO / "consolidado" / "operaciones_estructuradas.csv")
    corpus = m0.read_corpus(m0.RESULTADO / "consolidado" / "corpus_semantico.csv")
    ofb_files = sorted({r["archivo"] for r in ops if r["source"] == "BANCO"})
    bian_files = sorted({r["archivo"] for r in ops if r["source"] == "BIAN"})
    bian_tok = {f: tokens(Path(f).stem) for f in bian_files}

    ranking = []
    for ofb in ofb_files:
        slug = ofb_slug(ofb)
        ot = tokens(slug)
        cands = sorted(
            ((jaccard(ot, bt), bf) for bf, bt in bian_tok.items()),
            reverse=True,
        )[:5]
        ranking.append(
            {
                "ofb": ofb,
                "slug": slug,
                "auto_top": [
                    {"bian": bf, "jaccard_nombre": round(j, 4)} for j, bf in cands if j > 0
                ],
                "curado": CURADO.get(slug, []),
            }
        )

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "mapa_ofb_sd.json").write_text(
        json.dumps(
            {
                "bian_yaml": len(bian_files),
                "ofb_yaml": len(ofb_files),
                "regla": (
                    "Cada API OFB se contrasta con SD oficiales. "
                    "I1–I6 siguen siendo las instancias del protocolo. "
                    "El catálogo extra no sustituye n=7."
                ),
                "ranking": ranking,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    extra = []
    seen = set()
    for row in ranking:
        slug = row["slug"]
        chosen = list(row["curado"])
        if not chosen and row["auto_top"] and row["auto_top"][0]["jaccard_nombre"] >= 0.40:
            chosen = [row["auto_top"][0]["bian"]]
        for bian in chosen:
            key = (row["ofb"], bian)
            if key in seen:
                continue
            seen.add(key)
            extra.append({"ofb": row["ofb"], "bian": bian, "slug": slug})

    scores = []
    for i, pair in enumerate(extra, 1):
        inst = {
            "id": f"C{i:02d}",
            "prioridad": "catalogo-v14",
            "ofb": pair["ofb"],
            "bian": pair["bian"],
            "carpeta": f"C{i:02d}_{pair['slug']}_x_{Path(pair['bian']).stem}",
        }
        print(f"Matching {inst['id']}: {inst['ofb']} × {inst['bian']}")
        prev = m0.MATCHING
        m0.MATCHING = OUT
        try:
            sc = m0.match_instance(inst, ops, corpus)
        finally:
            m0.MATCHING = prev
        sc["slug"] = pair["slug"]
        scores.append(sc)

    fields = [
        "id",
        "ofb",
        "bian",
        "S",
        "E",
        "C",
        "AlignmentScore",
        "nivel",
        "n_pares",
        "n_operaciones_ofb",
        "n_operaciones_bian",
    ]
    m0.write_csv(OUT / "resumen_catalogo.csv", scores, fields)

    lines = [
        "# Mapa OFB × catálogo BIAN v14 (258 SD oficiales)",
        "",
        "No se inventó ningún Service Domain. I1–I6 del protocolo no se reemplazan.",
        "",
        "| ID | OFB | BIAN | S | E | C | Score | Nivel | Pares |",
        "|----|-----|------|---|---|---|-------|-------|-------|",
    ]
    for s in scores:
        lines.append(
            f"| {s['id']} | `{s['ofb']}` | `{s['bian']}` | {s['S']:.2f} | {s['E']:.2f} | "
            f"{s['C']:.2f} | **{s['AlignmentScore']:.2f}** | {s['nivel']} | "
            f"{s['n_pares']}/{s['n_operaciones_ofb']} |"
        )
    sin_par = [r["slug"] for r in ranking if r["slug"] not in CURADO and not (
        r["auto_top"] and r["auto_top"][0]["jaccard_nombre"] >= 0.40
    )]
    lines += [
        "",
        "## OFB sin par natural (inventario OE1)",
        "",
        ", ".join(f"`{x}`" for x in sin_par) or "(ninguna)",
        "",
    ]
    (OUT / "MAPA.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"pares_catalogo": len(scores), "sin_par": sin_par}, indent=2))


if __name__ == "__main__":
    main()
