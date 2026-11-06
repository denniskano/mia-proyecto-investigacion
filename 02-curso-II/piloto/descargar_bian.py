#!/usr/bin/env python3
"""Descarga todos los OpenAPI BIAN v14 publicados (bian-official/public).

No inventa Service Domains. Solo copia YAML oficiales a fuentes/bian/.
"""
from __future__ import annotations

import json
import urllib.request
from pathlib import Path

API = (
    "https://api.github.com/repos/bian-official/public/contents/"
    "release14.0.0/semantic-apis/oas3%20/yamls"
)
RAW = (
    "https://raw.githubusercontent.com/bian-official/public/main/"
    "release14.0.0/semantic-apis/oas3%20/yamls"
)
OUT = Path(__file__).resolve().parent / "fuentes" / "bian"


def list_yamls() -> list[str]:
    req = urllib.request.Request(API, headers={"User-Agent": "grupo10-piloto-bian"})
    with urllib.request.urlopen(req, timeout=60) as fh:
        data = json.loads(fh.read().decode())
    return sorted(
        x["name"]
        for x in data
        if x.get("type") == "file" and str(x.get("name", "")).endswith((".yaml", ".yml"))
    )


def download(name: str) -> Path:
    dest = OUT / name
    url = f"{RAW}/{name}"
    req = urllib.request.Request(url, headers={"User-Agent": "grupo10-piloto-bian"})
    with urllib.request.urlopen(req, timeout=90) as fh:
        dest.write_bytes(fh.read())
    return dest


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    names = list_yamls()
    print(f"{len(names)} YAML BIAN v14")
    ok, fail = 0, []
    for i, name in enumerate(names, 1):
        try:
            p = download(name)
            print(f"[{i}/{len(names)}] {name} ({p.stat().st_size} bytes)")
            ok += 1
        except Exception as exc:
            print(f"[{i}/{len(names)}] FALLÓ {name}: {exc}")
            fail.append(name)
    (OUT / "_descarga.json").write_text(
        json.dumps(
            {"release": "14.0.0", "esperados": len(names), "ok": ok, "fallidos": fail},
            indent=2,
        ),
        encoding="utf-8",
    )
    print(json.dumps({"ok": ok, "fallidos": fail}, indent=2))


if __name__ == "__main__":
    main()
