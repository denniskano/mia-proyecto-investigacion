#!/usr/bin/env python3
"""Extrae dataset estructural y corpus textual de uno o más OpenAPI 3.x.

Uso:
  python procesar_openapi.py <archivo.yaml> <carpeta_salida>
  python procesar_openapi.py --fuentes <dir_fuentes> <carpeta_salida>
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

HTTP = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
DEFAULT_BIAN = (
    "https://raw.githubusercontent.com/bian-official/public/main/"
    "release14.0.0/semantic-apis/oas3%20/yamls"
)


def norm(s: str) -> str:
    s = re.sub(
        r"^(?:InCR|UpCR|CoCR|ReCR|InBQ|UpBQ|CoBQ|ReBQ|ExBQ)\s+",
        "",
        str(s or ""),
        flags=re.I,
    )
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", s)
    s = re.sub(r"[_/{}\-]+", " ", s)
    return " ".join(s.lower().split())


def refname(obj) -> str:
    if isinstance(obj, dict) and "$ref" in obj:
        return str(obj["$ref"]).rsplit("/", 1)[-1]
    return ""


def schema_from_media(obj) -> str:
    """Nombre de schema en requestBody/response, incluso anidado en content."""
    if not isinstance(obj, dict):
        return ""
    direct = refname(obj)
    if direct:
        return direct
    content = obj.get("content") or {}
    if not isinstance(content, dict):
        return ""
    for body in content.values():
        if not isinstance(body, dict):
            continue
        sch = body.get("schema") or {}
        name = refname(sch)
        if name:
            return name
        if isinstance(sch, dict):
            for key in ("allOf", "oneOf", "anyOf"):
                seq = sch.get(key) or []
                if isinstance(seq, list):
                    for item in seq:
                        name = refname(item)
                        if name:
                            return name
    return ""


def resolve_request_body(op: dict, components: dict) -> str:
    rb = op.get("requestBody")
    name = schema_from_media(rb) if isinstance(rb, dict) else ""
    if name and name in (components.get("requestBodies") or {}):
        nested = schema_from_media(components["requestBodies"][name])
        return nested or name
    return name


def resolve_response(op: dict, components: dict, code: str = "200") -> str:
    responses = op.get("responses") or {}
    resp = responses.get(code) or responses.get("201") or {}
    name = schema_from_media(resp) if isinstance(resp, dict) else ""
    if not name:
        name = refname(resp) if isinstance(resp, dict) else ""
    if name and name in (components.get("responses") or {}):
        nested = schema_from_media(components["responses"][name])
        return nested or name
    return name


def load_openapi(path: Path) -> dict:
    text = path.read_text(encoding="utf-8-sig")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    return yaml.safe_load(text)


def process_file(inp: Path, source_kind: str, source_url: str) -> dict:
    obj = load_openapi(inp)
    components = obj.get("components") or {}
    struct, semantic, props = [], [], []
    unresolved_refs = []

    for path, methods in (obj.get("paths") or {}).items():
        if not isinstance(methods, dict):
            continue
        for method, op in methods.items():
            if method.lower() not in HTTP or not isinstance(op, dict):
                continue
            rid = str(op.get("operationId") or f"{method}_{path}")
            description = str(op.get("description") or "")
            summary = str(op.get("summary") or "")
            params = [
                refname(p) or str(p.get("name", ""))
                for p in (op.get("parameters") or [])
                if isinstance(p, dict)
            ]
            req = resolve_request_body(op, components)
            resp = resolve_response(op, components)
            row = {
                "source": source_kind,
                "version": obj.get("info", {}).get("version", ""),
                "api": obj.get("info", {}).get("title", ""),
                "archivo": inp.name,
                "path": path,
                "method": method.upper(),
                "operation_id": rid,
                "tag": " | ".join(op.get("tags") or []),
                "parameters": " | ".join(params),
                "request_schema_ref": req,
                "response_200_ref": resp,
                "summary": summary,
                "description": description,
                "summary_normalized": norm(summary),
                "operation_id_normalized": norm(rid),
                "source_url": source_url,
            }
            struct.append(row)
            if summary:
                semantic.append(
                    {
                        "source": source_kind,
                        "archivo": inp.name,
                        "element_type": "operation",
                        "element_id": rid,
                        "field": "summary",
                        "raw_text": summary,
                        "normalized_text": norm(summary),
                        "path": path,
                        "source_url": source_url,
                    }
                )
            if description and description != summary:
                semantic.append(
                    {
                        "source": source_kind,
                        "archivo": inp.name,
                        "element_type": "operation",
                        "element_id": rid,
                        "field": "description",
                        "raw_text": description,
                        "normalized_text": norm(description),
                        "path": path,
                        "source_url": source_url,
                    }
                )

    for schema, sdef in (components.get("schemas") or {}).items():
        sdef = sdef or {}
        d = str(sdef.get("description") or "")
        if d:
            semantic.append(
                {
                    "source": source_kind,
                    "archivo": inp.name,
                    "element_type": "schema",
                    "element_id": schema,
                    "field": "description",
                    "raw_text": d,
                    "normalized_text": norm(d),
                    "path": f"#/components/schemas/{schema}",
                    "source_url": source_url,
                }
            )
        for key, p in (sdef.get("properties") or {}).items():
            p = p or {}
            pdesc = str(p.get("description") or "")
            pref = refname(p)
            props.append(
                {
                    "source": source_kind,
                    "archivo": inp.name,
                    "schema": schema,
                    "property": key,
                    "type": p.get("type", "") or "",
                    "format": p.get("format", "") or "",
                    "ref": pref,
                    "description": pdesc,
                    "property_normalized": norm(key),
                    "description_normalized": norm(pdesc),
                    "source_url": source_url,
                }
            )
            semantic.append(
                {
                    "source": source_kind,
                    "archivo": inp.name,
                    "element_type": "property",
                    "element_id": f"{schema}.{key}",
                    "field": "name",
                    "raw_text": key,
                    "normalized_text": norm(key),
                    "path": f"#/components/schemas/{schema}/properties/{key}",
                    "source_url": source_url,
                }
            )
            if pdesc:
                semantic.append(
                    {
                        "source": source_kind,
                        "archivo": inp.name,
                        "element_type": "property",
                        "element_id": f"{schema}.{key}",
                        "field": "description",
                        "raw_text": pdesc,
                        "normalized_text": norm(pdesc),
                        "path": f"#/components/schemas/{schema}/properties/{key}",
                        "source_url": source_url,
                    }
                )
            if pref and pref not in (components.get("schemas") or {}):
                unresolved_refs.append(f"schema:{schema}.{key}->{pref}")

    tags = Counter(r["tag"] or "(sin tag)" for r in struct)
    methods = Counter(r["method"] for r in struct)
    stats = {
        "archivo_entrada": inp.name,
        "source": source_kind,
        "contrato": obj.get("info", {}).get("title"),
        "version": obj.get("info", {}).get("version"),
        "openapi": obj.get("openapi"),
        "cantidad_operaciones": len(struct),
        "cantidad_schemas": len(components.get("schemas") or {}),
        "cantidad_propiedades": len(props),
        "fragmentos_corpus": len(semantic),
        "operaciones_con_summary": sum(bool(x["summary"]) for x in struct),
        "operaciones_con_description": sum(bool(x["description"]) for x in struct),
        "operaciones_summary_igual_description": sum(
            1 for x in struct if x["summary"] and x["summary"] == x["description"]
        ),
        "metodos": dict(methods),
        "tags": dict(tags),
        "refs_esquema_no_definidos_en_archivo": len(unresolved_refs),
        "source_url": source_url,
    }
    return {
        "stats": stats,
        "operaciones": struct,
        "propiedades": props,
        "corpus": semantic,
    }


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter=";")
        w.writeheader()
        w.writerows(rows)


def discover(fuentes: Path) -> list[tuple[Path, str, str]]:
    items = []
    for p in sorted(fuentes.rglob("*")):
        if p.suffix.lower() not in {".yaml", ".yml", ".json"}:
            continue
        if "archivo" in p.parts:
            continue
        rel = p.relative_to(fuentes)
        kind = rel.parts[0].upper() if len(rel.parts) > 1 else "OTRO"
        url = ""
        if kind == "BIAN":
            url = f"{DEFAULT_BIAN}/{p.name}"
        elif p.name.startswith("OFB_"):
            kind = "BANCO"
            m = re.match(r"OFB_(.+)_(\d.+)$", p.stem)
            if m:
                api, ver = m.group(1), m.group(2)
                url = (
                    "https://raw.githubusercontent.com/OpenBanking-Brasil/openapi/"
                    f"main/swagger-apis/{api}/{ver}{p.suffix}"
                )
        items.append((p, kind, url))
    return items


def run_batch(fuentes: Path, out: Path) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    all_ops, all_props, all_corpus, per_file = [], [], [], []
    for path, kind, url in discover(fuentes):
        print(f"Procesando {kind}: {path.name}")
        result = process_file(path, kind, url)
        per = out / "por_contrato" / path.stem
        write_csv(per / "operaciones_estructuradas.csv", result["operaciones"])
        write_csv(per / "propiedades_esquemas.csv", result["propiedades"])
        write_csv(per / "corpus_semantico.csv", result["corpus"])
        (per / "estadisticas.json").write_text(
            json.dumps(result["stats"], ensure_ascii=False, indent=2), encoding="utf-8"
        )
        all_ops.extend(result["operaciones"])
        all_props.extend(result["propiedades"])
        all_corpus.extend(result["corpus"])
        per_file.append(result["stats"])

    consolidado = out / "consolidado"
    write_csv(consolidado / "operaciones_estructuradas.csv", all_ops)
    write_csv(consolidado / "propiedades_esquemas.csv", all_props)
    write_csv(consolidado / "corpus_semantico.csv", all_corpus)

    inventario = {
        "alcance": (
            "PILOTO AMPLIADO: 3 Service Domains BIAN v14 completos "
            "(SavingsAccount, CurrentAccount, PaymentOrderInitiation) "
            "y el catálogo Open Finance Brasil (última versión estable de cada API "
            "publicada en swagger-apis: cuentas, pagos, créditos, tarjetas, "
            "consentimientos, open data, inversiones, etc.)."
        ),
        "advertencia": (
            "No se ha calculado AlignmentScore. El matching OFB–BIAN (OE2–OE4) sigue pendiente. "
            "Open Finance Brasil es el corpus del piloto (no el objeto de la tesis). "
            "Se tomó la última versión estable por API "
            "(si no hay estable, la pre-release más alta)."
        ),
        "preprocesamiento": (
            "parseo YAML, extracción, $ref anidado en requestBody/response, "
            "separación camelCase, minúsculas, normalización de prefijos BIAN. "
            "Sin embeddings ni AlignmentScore."
        ),
        "totales": {
            "contratos": len(per_file),
            "operaciones": len(all_ops),
            "schemas_propiedades": len(all_props),
            "fragmentos_corpus": len(all_corpus),
            "operaciones_bian": sum(1 for r in all_ops if r["source"] == "BIAN"),
            "operaciones_banco": sum(1 for r in all_ops if r["source"] == "BANCO"),
        },
        "por_contrato": per_file,
    }
    (out / "inventario.json").write_text(
        json.dumps(inventario, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(inventario["totales"], indent=2, ensure_ascii=False))
    return inventario


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("entrada", nargs="?")
    parser.add_argument("salida", nargs="?")
    parser.add_argument("--fuentes", type=Path)
    args = parser.parse_args()
    if args.fuentes:
        if not args.salida and not args.entrada:
            raise SystemExit("Uso: procesar_openapi.py --fuentes DIR SALIDA")
        out = Path(args.salida or args.entrada)
        run_batch(args.fuentes, out)
        return
    if not args.entrada or not args.salida:
        raise SystemExit(
            "Uso: procesar_openapi.py <archivo.yaml> <carpeta_salida>\n"
            "     procesar_openapi.py --fuentes <dir_fuentes> <carpeta_salida>"
        )
    inp, out = Path(args.entrada), Path(args.salida)
    kind = "BIAN" if "bian" in str(inp).lower() or "Savings" in inp.name else "OTRO"
    url = f"{DEFAULT_BIAN}/{inp.name}" if kind == "BIAN" else ""
    result = process_file(inp, kind, url)
    write_csv(out / "operaciones_estructuradas.csv", result["operaciones"])
    write_csv(out / "propiedades_esquemas.csv", result["propiedades"])
    write_csv(out / "corpus_semantico.csv", result["corpus"])
    (out / "estadisticas_procesamiento.json").write_text(
        json.dumps(result["stats"], ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(result["stats"], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
