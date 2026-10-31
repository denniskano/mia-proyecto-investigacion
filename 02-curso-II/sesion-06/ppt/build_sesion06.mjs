#!/usr/bin/env node
/**
 * PPT Sesión 6 — revisión del método. Grupo 10
 */

import path from "node:path";
import { fileURLToPath } from "node:url";
import pptxgen from "../../../01-curso-I/plan-tesis/exposicion/ppt/node_modules/pptxgenjs/dist/pptxgen.es.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(__dirname, "..", "Sesion06_Revision_Metodo.pptx");

const C = {
  navy: "1B365D",
  accent: "E8A317",
  text: "2D3436",
  muted: "636E72",
  white: "FFFFFF",
  ok: "1E7F4F",
  warn: "C47B0A",
  tableHead: "1B365D",
  tableAlt: "EEF2F7",
  card: "EEF2F7",
};

const FONT = "Arial";
const FOOTER = "Grupo 10 · Sesión 6 · Revisión del método · objeto OpenAPI bancario · Oct 2026";

function footer(slide) {
  slide.addShape("rect", { x: 0, y: 7.05, w: 13.333, h: 0.02, fill: { color: C.muted } });
  slide.addText(FOOTER, {
    x: 0.45,
    y: 7.12,
    w: 12.4,
    h: 0.28,
    fontSize: 10,
    color: C.muted,
    fontFace: FONT,
  });
}

function titleBar(slide, title) {
  slide.addShape("rect", { x: 0, y: 0, w: 13.333, h: 0.12, fill: { color: C.navy } });
  slide.addText(title, {
    x: 0.45,
    y: 0.28,
    w: 12.4,
    h: 0.55,
    fontSize: 22,
    bold: true,
    color: C.navy,
    fontFace: FONT,
  });
}

function headerRow(cells) {
  return cells.map((t) => ({
    text: t,
    options: { fill: { color: C.tableHead }, color: C.white, bold: true, fontSize: 11 },
  }));
}

function row(cells, alt = false) {
  return cells.map((t) => ({
    text: t,
    options: { fill: { color: alt ? C.tableAlt : C.white }, fontSize: 11 },
  }));
}

async function main() {
  const pptx = new pptxgen();
  pptx.defineLayout({ name: "WIDE", width: 13.333, height: 7.5 });
  pptx.layout = "WIDE";
  pptx.author = "Grupo 10 — Alex Mancilla · Jack Paitan";
  pptx.title = "Sesión 6 — Revisión del método";

  {
    const s = pptx.addSlide();
    s.addShape("rect", { x: 0, y: 0, w: 13.333, h: 7.5, fill: { color: C.navy } });
    s.addShape("rect", { x: 0, y: 0, w: 0.18, h: 7.5, fill: { color: C.accent } });
    s.addText("SESIÓN 6", {
      x: 0.7,
      y: 1.6,
      w: 11.5,
      h: 0.4,
      fontSize: 16,
      color: C.accent,
      fontFace: FONT,
      bold: true,
    });
    s.addText("Revisión del método\n(Capítulo III)", {
      x: 0.7,
      y: 2.15,
      w: 12,
      h: 1.7,
      fontSize: 34,
      bold: true,
      color: C.white,
      fontFace: FONT,
    });
    s.addText(
      "Población · instrumentos · procedimiento · análisis · viabilidad\nGrupo 10  ·  Alex Mancilla Antay  ·  Jack Paitan Cano  ·  MIA 403 · UNI",
      {
        x: 0.7,
        y: 4.2,
        w: 11.5,
        h: 1.1,
        fontSize: 16,
        color: "D6DEE8",
        fontFace: FONT,
      }
    );
  }

  {
    const s = pptx.addSlide();
    titleBar(s, "Cinco puntos de la lámina");
    footer(s);
    const items = [
      ["1", "Población, muestra o fuentes de datos y criterios de selección"],
      ["2", "Técnicas e instrumentos de recolección de datos"],
      ["3", "Procedimiento de investigación claro y reproducible"],
      ["4", "Técnicas de análisis y correspondencia con objetivos e hipótesis"],
      ["5", "Evidencia de viabilidad: EDA, baseline o prueba piloto"],
    ];
    items.forEach((p, i) => {
      const y = 1.05 + i * 1.1;
      s.addShape("roundRect", {
        x: 0.45,
        y,
        w: 12.4,
        h: 0.95,
        fill: { color: C.card },
        rectRadius: 0.08,
      });
      s.addText(p[0], {
        x: 0.6,
        y,
        w: 0.7,
        h: 0.95,
        fontSize: 22,
        bold: true,
        color: C.navy,
        valign: "middle",
        fontFace: FONT,
      });
      s.addText(p[1], {
        x: 1.4,
        y,
        w: 11.2,
        h: 0.95,
        fontSize: 16,
        color: C.text,
        valign: "middle",
        fontFace: FONT,
      });
    });
  }

  {
    const s = pptx.addSlide();
    titleBar(s, "1. Tres capas: no confundir objeto y piloto");
    footer(s);
    s.addTable(
      [
        headerRow(["Capa", "Qué es", "Qué no es"]),
        row(["Población (tesis)", "OpenAPI bancario × SD BIAN", "Un estándar de un país"], false),
        row(["Universo del piloto", "38 APIs OFB + 3 SD BIAN v14", "Todo el catálogo BIAN"], true),
        row(["Muestra de scores", "7 instancias I1–I6", "Las otras 33 APIs OFB"], false),
      ],
      { x: 0.45, y: 1.1, w: 12.4, colW: [3.1, 5.2, 4.1], border: [{ pt: 0.5, color: "D0D7DE" }], fontFace: FONT, valign: "middle" }
    );
    s.addText(
      "OFB es estándar de industria, no el YAML de un banco. El objeto de la tesis no cambia.",
      { x: 0.45, y: 4.3, w: 12.4, h: 0.7, fontSize: 16, color: C.navy, bold: true, fontFace: FONT }
    );
    s.addText(
      "Incluye: OpenAPI 3.x público, par natural accounts/payments ↔ Savings/Current/POI.\nExcluye de este piloto: banco emisor, Open Banking UK, inventar SD para loans/cards, recorte de 12 ops.",
      { x: 0.45, y: 5.1, w: 12.4, h: 1.5, fontSize: 14, color: C.text, fontFace: FONT }
    );
  }

  {
    const s = pptx.addSlide();
    titleBar(s, "1. Muestra empírica (n = 7)");
    footer(s);
    const kpis = [
      ["41", "contratos"],
      ["235", "operaciones"],
      ["7", "instancias"],
      ["33", "APIs solo OE1"],
    ];
    kpis.forEach((k, i) => {
      const x = 0.45 + i * 3.2;
      s.addShape("roundRect", { x, y: 1.1, w: 3.0, h: 1.25, fill: { color: C.card }, rectRadius: 0.08 });
      s.addText(k[0], { x, y: 1.18, w: 3.0, h: 0.7, fontSize: 28, bold: true, color: C.navy, align: "center", fontFace: FONT });
      s.addText(k[1], { x, y: 1.85, w: 3.0, h: 0.35, fontSize: 12, color: C.muted, align: "center", fontFace: FONT });
    });
    s.addTable(
      [
        headerRow(["ID", "OFB", "BIAN"]),
        row(["I1 / I2", "accounts 2.4.2", "SavingsAccount / CurrentAccount"], false),
        row(["I3a / I3b", "opendata-accounts 1.0.1", "SavingsAccount / CurrentAccount"], true),
        row(["I4 / I5 / I6", "payments / automatic-payments / enrollments", "PaymentOrderInitiation"], false),
      ],
      { x: 0.45, y: 2.6, w: 12.4, colW: [2.2, 5.5, 4.7], border: [{ pt: 0.5, color: "D0D7DE" }], fontFace: FONT, valign: "middle" }
    );
    s.addText("I1/I2 e I3a/I3b no son independientes: mismo YAML OFB, dos referencias.", {
      x: 0.45,
      y: 5.5,
      w: 12.4,
      h: 0.5,
      fontSize: 14,
      color: C.warn,
      fontFace: FONT,
    });
  }

  {
    const s = pptx.addSlide();
    titleBar(s, "2. Recolección: artefactos, no encuestas");
    footer(s);
    s.addTable(
      [
        headerRow(["Técnica", "Instrumento", "Salida"]),
        row(["Adquisición versionada", "YAML oficiales + git", "38 OFB + 3 BIAN congelados"], false),
        row(["Parsing OpenAPI 3.x", "procesar_openapi.py", "ops, schemas, $ref anidados"], true),
        row(["Normalización", "mismo parser", "CSV listos para matching"], false),
        row(["Inventario", "inventario.json", "41 / 235 / 6 746 / 10 906"], true),
      ],
      { x: 0.45, y: 1.1, w: 12.4, colW: [3.6, 4.0, 4.8], border: [{ pt: 0.5, color: "D0D7DE" }], fontFace: FONT, valign: "middle" }
    );
    s.addText(
      "Ética: YAML públicos. Sin PII. Ley 29733 no aplica. Citar OFB y BIAN.\nAún no existen pares_estructurales.csv ni scores.json — eso es semana 7–8.",
      { x: 0.45, y: 5.15, w: 12.4, h: 1.4, fontSize: 15, color: C.text, fontFace: FONT }
    );
  }

  {
    const s = pptx.addSlide();
    titleBar(s, "3. Procedimiento reproducible");
    footer(s);
    const steps = [
      ["OE1", "Parsear y firmar completitud"],
      ["OE2", "Emparejar estructura → E"],
      ["OE3", "Similitud semántica → S"],
      ["OE4", "C + AlignmentScore + nivel"],
    ];
    steps.forEach((st, i) => {
      const x = 0.45 + i * 3.2;
      s.addShape("roundRect", { x, y: 1.15, w: 3.0, h: 1.55, fill: { color: C.navy }, rectRadius: 0.08 });
      s.addText(st[0], { x, y: 1.25, w: 3.0, h: 0.5, fontSize: 18, bold: true, color: C.accent, align: "center", fontFace: FONT });
      s.addText(st[1], { x: x + 0.12, y: 1.8, w: 2.76, h: 0.7, fontSize: 13, color: C.white, align: "center", fontFace: FONT });
    });
    s.addText(
      "Design science · cuantitativo sobre documentos · sin ML supervisado.\nBaseline semana 8: E por Jaccard/path/HTTP; S léxico. Embeddings en semana 11.\nAlignmentScore = (S+E+C)/3. Ops OFB sin par aportan 0 a E. C = CR+BQ cubiertos / catálogo del SD.",
      { x: 0.45, y: 3.0, w: 12.4, h: 1.8, fontSize: 15, color: C.text, fontFace: FONT }
    );
    s.addText(
      "Prohibido: BIAN↔BIAN como resultado · copiar CR/BQ a OFB · etiquetar niveles a mano.",
      { x: 0.45, y: 5.15, w: 12.4, h: 1.2, fontSize: 16, bold: true, color: C.warn, fontFace: FONT }
    );
  }

  {
    const s = pptx.addSlide();
    titleBar(s, "4. Análisis ↔ preguntas, OE e hipótesis");
    footer(s);
    s.addTable(
      [
        headerRow(["Pregunta", "OE", "Técnica", "H", "Ahora"]),
        row(["P1 estructura", "OE2", "Schema matching → E", "H2", "Pendiente"], false),
        row(["P2 semántica", "OE3", "Léxico / embeddings → S", "H3", "Pendiente"], true),
        row(["P3 tipologías", "OE4", "Lectura de pares + Tabla 2", "—", "Condicionada por EDA"], false),
        row(["P4 score", "OE4", "αS+βE+γC, umbrales", "H4", "Pendiente"], true),
        row(["¿Se puede medir?", "OE1", "Parser + completitud", "H1", "Soportada (41 YAML)"], false),
      ],
      { x: 0.45, y: 1.1, w: 12.4, colW: [2.5, 1.4, 4.0, 1.1, 3.4], border: [{ pt: 0.5, color: "D0D7DE" }], fontFace: FONT, valign: "middle" }
    );
    s.addText(
      "VD = AlignmentScore + {Alta ≥ 0,80 · Media · Baja · Nula < 0,40}. Los ratios OE1–OE3 no sustituyen la VD.",
      { x: 0.45, y: 5.55, w: 12.4, h: 0.9, fontSize: 15, color: C.navy, fontFace: FONT }
    );
  }

  {
    const s = pptx.addSlide();
    titleBar(s, "5. Viabilidad: EDA ya corrido (Sesión 5)");
    footer(s);
    s.addTable(
      [
        headerRow(["Hallazgo", "Dato", "Implicación"]),
        row(["OFB es consulta", "GET 130/160", "E no exige el mismo verbo"], false),
        row(["BIAN es control", "PUT 36/75", "Asimetría REST vs CR/BQ"], true),
        row(["Texto BIAN pobre", "90,4 % props sin description", "S cae sobre el nombre"], false),
        row(["Summary = description", "75/75 ops BIAN", "No contar el texto dos veces"], true),
        row(["Gap de referencia", "loans / cards / financings", "No inventar SD; no puntuar"], false),
      ],
      { x: 0.45, y: 1.1, w: 12.4, colW: [3.3, 4.3, 4.8], border: [{ pt: 0.5, color: "D0D7DE" }], fontFace: FONT, valign: "middle" }
    );
    s.addText("C de I1 será baja (6 GET vs 1 CR + 9 BQ). Eso es hallazgo, no fallo del parser.", {
      x: 0.45,
      y: 5.6,
      w: 12.4,
      h: 0.8,
      fontSize: 16,
      bold: true,
      color: C.navy,
      fontFace: FONT,
    });
  }

  {
    const s = pptx.addSlide();
    titleBar(s, "Checklist de revisión (lámina)");
    footer(s);
    s.addTable(
      [
        headerRow(["Punto", "¿Cubierto?", "Dónde"]),
        row(["Población y criterios", "Sí", "Plan v2 §3–4 · esta §1"], false),
        row(["Instrumentos de recolección", "Sí", "Parser + CSV · esta §2"], true),
        row(["Procedimiento reproducible", "Sí", "protocolo-empirico.md"], false),
        row(["Análisis ↔ OE / H", "Sí", "Esta §4"], true),
        row(["Viabilidad EDA / piloto", "Sí, sin scores", "Sesión 5"], false),
      ],
      { x: 0.45, y: 1.1, w: 12.4, colW: [4.2, 2.8, 5.4], border: [{ pt: 0.5, color: "D0D7DE" }], fontFace: FONT, valign: "middle" }
    );
  }

  {
    const s = pptx.addSlide();
    titleBar(s, "Qué falta (no es de esta lámina)");
    footer(s);
    const next = [
      ["Sem. 7", "Firmar OE1 por YAML · matching estructural v0"],
      ["Sem. 8 · P4", "Scores v0 de I1 (accounts × Savings) e I4 (payments × POI)"],
      ["Sem. 9", "Defensa intermedia (8 slides del cronograma)"],
      ["Sem. 10–11", "Las 7 instancias con S, E, C y AlignmentScore"],
    ];
    next.forEach((n, i) => {
      const y = 1.15 + i * 1.25;
      s.addShape("roundRect", { x: 0.45, y, w: 12.4, h: 1.1, fill: { color: C.card }, rectRadius: 0.08 });
      s.addText(n[0], { x: 0.65, y, w: 3.1, h: 1.1, fontSize: 16, bold: true, color: C.navy, valign: "middle", fontFace: FONT });
      s.addText(n[1], { x: 3.9, y, w: 8.7, h: 1.1, fontSize: 16, color: C.text, valign: "middle", fontFace: FONT });
    });
  }

  {
    const s = pptx.addSlide();
    s.addShape("rect", { x: 0, y: 0, w: 13.333, h: 7.5, fill: { color: C.navy } });
    s.addShape("rect", { x: 0, y: 0, w: 0.18, h: 7.5, fill: { color: C.accent } });
    s.addText("En una frase", {
      x: 0.7,
      y: 1.7,
      w: 12,
      h: 0.4,
      fontSize: 16,
      color: C.accent,
      bold: true,
      fontFace: FONT,
    });
    s.addText(
      "El método está revisado y es ejecutable: población = OpenAPI bancario × BIAN; muestra = 7 instancias OFB; evidencia de viabilidad = EDA de 41 contratos. AlignmentScore se calcula a partir de la semana 8.",
      {
        x: 0.7,
        y: 2.3,
        w: 11.8,
        h: 2.6,
        fontSize: 22,
        bold: true,
        color: C.white,
        fontFace: FONT,
      }
    );
    s.addText("Grupo 10  ·  Alex Mancilla  ·  Jack Paitan  ·  fuente: Sesion06_Revision_Metodo.md", {
      x: 0.7,
      y: 5.5,
      w: 11.5,
      h: 0.5,
      fontSize: 14,
      color: "D6DEE8",
      fontFace: FONT,
    });
  }

  await pptx.writeFile({ fileName: OUT });
  console.log("PPTX:", OUT);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
