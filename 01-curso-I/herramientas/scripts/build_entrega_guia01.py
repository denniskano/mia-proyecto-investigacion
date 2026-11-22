#!/usr/bin/env python3
"""Empaqueta la carpeta Informe Guía 1 para Google Drive — Grupo 10."""

from __future__ import annotations

import re
import shutil
import unicodedata
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / "plan-tesis"
V3 = ROOT
OUT = PLAN / "entrega" / "Informe_Guia1_Grupo10"
ZIP_PATH = PLAN / "entrega" / "Informe_Guia1_Grupo10.zip"

SKIP_DIR_NAMES = {".git", "build", "entrega", "__pycache__", ".venv-excel", "node_modules"}
SKIP_FILE_SUFFIXES = {".aux", ".log", ".fls", ".fdb_latexmk", ".out", ".toc", ".lof", ".lot"}

# Carpetas con nombres legibles (sin jerga de repo)
DIR_PAPERS = "01 Papers y resumenes"
DIR_DATOS = "02 Ejemplos objeto de estudio"
DIR_NORMAS = "03 Normas y estandares del tema"
DIR_FUENTES = "04 Fuentes LaTeX y PDF"
DIR_MATRIZ = "05 Matriz de consistencia"


def reset_out() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)


def safe_name(name: str, max_len: int = 180) -> str:
    text = re.sub(r'[<>:"/\\|?*]', "_", name).strip()
    text = re.sub(r"\s+", " ", text)
    if len(text) > max_len:
        text = text[: max_len - 3].rstrip() + "..."
    return text


def sin_tildes(text: str) -> str:
    """Estilo informal: sin acentos (solo en copias de entrega, no en fichas fuente)."""
    normalized = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in normalized if unicodedata.category(ch) != "Mn")


def pack_papers() -> None:
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from papers_estado_del_arte import PAPERS

    dst = OUT / DIR_PAPERS
    dst.mkdir(parents=True, exist_ok=True)
    papers_dir = V3 / "bibliografia" / "estado-del-arte"
    fichas_dir = PLAN / "fases" / "fase-0-bibliografia" / "fichas"

    for paper in PAPERS:
        pdf_src = papers_dir / paper["pdf"]
        if not pdf_src.exists():
            print(f"  [aviso] Falta PDF: {paper['pdf']}")
            continue

        base = safe_name(f'{paper["cite"]} - {paper["titulo"]}')
        shutil.copy2(pdf_src, dst / f"{base}.pdf")

        ficha_matches = list(fichas_dir.glob(f"{paper['id']}_*.md"))
        if ficha_matches:
            contenido = sin_tildes(ficha_matches[0].read_text(encoding="utf-8"))
            (dst / f"{base} - resumen.md").write_text(contenido, encoding="utf-8")

    extra = [
        (
            "He et al., 2022",
            "BERTMap: A BERT-based Ontology Alignment System",
            "He et al. - 2022 - BERTMap*.pdf",
        ),
        (
            "Hertling y Paulheim, 2023",
            "OLaLa: Ontology Matching with Large Language Models",
            "Hertling y Paulheim - 2023 - OLaLa*.pdf",
        ),
        (
            "Schneider et al., 2023",
            "NLFOA: Natural Language Focused Ontology Alignment",
            "Schneider et al. - 2023 - NLFOA*.pdf",
        ),
        (
            "Kotstein y Decker, 2024",
            "RESTBERTa: a Transformer-based question answering approach for semantic search in Web API documentation",
            "Kotstein y Decker - 2024 - RESTBERTa*.pdf",
        ),
        (
            "Lu et al., 2024",
            "Comparing the Similarity of OpenAPI-Based Microservices",
            "Lu et al. - 2024 - Comparing the Similarity*.pdf",
        ),
    ]
    aporte = V3 / "bibliografia" / "aporte"
    copiados = 0
    for cite, titulo, patron in extra:
        matches = sorted(aporte.glob(patron))
        if not matches:
            print(f"  [aviso] Falta PDF de aporte: {cite}")
            continue
        base = safe_name(f"{cite} - {titulo}")
        shutil.copy2(matches[0], dst / f"{base}.pdf")
        copiados += 1
    print("  [aviso] Sin PDF abierto: Oberle y Bauernhansl, 2024 (IEEE, acceso cerrado)")
    print(f"  Papers empaquetados: {len(PAPERS)} del Anexo B + {copiados} de 2022–2024")


def pack_datos() -> None:
    dst = OUT / DIR_DATOS
    dst.mkdir(parents=True, exist_ok=True)
    src = PLAN / "datos-objeto-estudio"

    yaml_src = src / "ejemplo_openapi_payment_initiation.yaml"
    if yaml_src.exists():
        shutil.copy2(yaml_src, dst / "Ejemplo contrato OpenAPI - iniciacion de pagos.yaml")

    bian_src = src / "referencia_bian_payment_initiation.md"
    if bian_src.exists():
        (dst / "Referencia BIAN - Payment Initiation.md").write_text(
            sin_tildes(bian_src.read_text(encoding="utf-8")), encoding="utf-8"
        )


def pack_normas() -> None:
    dst = OUT / DIR_NORMAS
    dst.mkdir(parents=True, exist_ok=True)
    contexto = V3 / "bibliografia" / "contexto-openapi-bian"
    if not contexto.exists():
        print(f"  [aviso] Falta: {contexto}")
        return
    pdfs = sorted(contexto.glob("*.pdf"))
    for pdf in pdfs:
        shutil.copy2(pdf, dst / safe_name(pdf.name))
    print(f"  PDFs normas/estandares tema: {len(pdfs)}")


def should_skip_path(path: Path) -> bool:
    if set(path.parts) & SKIP_DIR_NAMES:
        return True
    if path.suffix.lower() in SKIP_FILE_SUFFIXES:
        return True
    if path.name.startswith("README"):
        return True
    return False


def pack_fuentes() -> None:
    dst = OUT / DIR_FUENTES
    dst.mkdir(parents=True, exist_ok=True)

    candidatos = [
        PLAN / "latex" / "build" / "Plan_Tesis_Grupo10_v2.pdf",
        PLAN / "latex" / "build" / "Plan_Tesis_Grupo10.pdf",
    ]
    pdf = next((path for path in candidatos if path.exists()), None)
    if pdf is not None:
        shutil.copy2(pdf, dst / "Plan de tesis Grupo 10.pdf")
        print(f"  PDF del plan: {pdf.name}")
    else:
        print(f"  [aviso] Compilar antes: {candidatos[0]}")

    zip_path = dst / "Fuentes LaTeX.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(PLAN.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(PLAN)
            if should_skip_path(rel):
                continue
            zf.write(path, rel.as_posix())
    print(f"  Zip LaTeX: {zip_path.name} ({zip_path.stat().st_size // 1024} KB)")


def pack_matriz() -> None:
    dst = OUT / DIR_MATRIZ
    dst.mkdir(parents=True, exist_ok=True)
    xlsx = PLAN / "anexos" / "Matriz_Consistencia_Grupo10.xlsx"
    if xlsx.exists():
        shutil.copy2(xlsx, dst / "Matriz de consistencia Grupo 10.xlsx")
    else:
        print(f"  [aviso] Falta: {xlsx}")


def zip_entrega() -> None:
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(OUT.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(OUT.parent).as_posix())
    print(f"Zip listo: {ZIP_PATH} ({ZIP_PATH.stat().st_size // 1024} KB)")


def main() -> None:
    print("Empaquetando entrega Guía 1…")
    reset_out()
    print(DIR_PAPERS)
    pack_papers()
    print(DIR_DATOS)
    pack_datos()
    print(DIR_NORMAS)
    pack_normas()
    print(DIR_FUENTES)
    pack_fuentes()
    print(DIR_MATRIZ)
    pack_matriz()
    zip_entrega()
    print(f"\nListo → {OUT}")


if __name__ == "__main__":
    main()
