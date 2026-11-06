#!/usr/bin/env node
/**
 * PPT Sesión 5 — operacionalización + EDA. Grupo 10
 */

import path from "node:path";
import { fileURLToPath } from "node:url";
import pptxgen from "../../../01-curso-I/plan-tesis/exposicion/ppt/node_modules/pptxgenjs/dist/pptxgen.es.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(__dirname, "..", "Sesion05_Operacionalizacion_y_EDA.pptx");

const C = {
  navy: "1B365D",
  blue: "003DA5",
  accent: "E8A317",
  bg: "F7F9FC",
  text: "2D3436",
  muted: "636E72",
  white: "FFFFFF",
  danger: "C0392B",
  ok: "1E7F4F",
  warn: "C47B0A",
  tableHead: "1B365D",
  tableAlt: "EEF2F7",
  card: "EEF2F7",
};

const FONT = "Arial";
const FOOTER = "Grupo 10 · Sesión 5 · Piloto OFB × BIAN · objeto OpenAPI bancario · Oct 2026";

function footer(slide) {
  slide.addShape("rect", { x: 0, y: 7.05, w: 13.333, h: 0.02, fill: { color: C.muted } });
  slide.addText(FOOTER, {
    x: 0.45,
    y: 7.12,
    w: 11.4,
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
    h: 0.7,
    fontSize: 24,
    bold: true,
    color: C.navy,
    fontFace: FONT,
  });
}

function tblOpts(rows, cols) {
  return {
    x: 0.45,
    y: 1.12,
    w: 12.43,
    colW: cols,
    border: [{ pt: 0.5, color: "D0D7DE" }],
    fontFace: FONT,
    fontSize: 12,
    color: C.text,
    align: "left",
    valign: "middle",
    rows,
  };
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

function kpi(slide, x, y, value, label, color = C.navy) {
  slide.addShape("roundRect", {
    x,
    y,
    w: 2.9,
    h: 1.35,
    fill: { color: C.card },
    rectRadius: 0.08,
  });
  slide.addText(String(value), {
    x,
    y: y + 0.12,
    w: 2.9,
    h: 0.7,
    fontSize: 28,
    bold: true,
    color,
    align: "center",
    fontFace: FONT,
  });
  slide.addText(label, {
    x: x + 0.08,
    y: y + 0.82,
    w: 2.74,
    h: 0.4,
    fontSize: 11,
    color: C.muted,
    align: "center",
    fontFace: FONT,
  });
}

async function main() {
  const pptx = new pptxgen();
  pptx.defineLayout({ name: "WIDE", width: 13.333, height: 7.5 });
  pptx.layout = "WIDE";
  pptx.author = "Grupo 10 — Alex Mancilla · Dennis Jack Paitan";
  pptx.title = "Sesión 5 — Operacionalización e instrumentos · EDA";
  pptx.subject = "Alineación OpenAPI bancario ↔ BIAN";

  // 1. Portada
  {
    const s = pptx.addSlide();
    s.addShape("rect", { x: 0, y: 0, w: 13.333, h: 7.5, fill: { color: C.navy } });
    s.addShape("rect", { x: 0, y: 0, w: 0.18, h: 7.5, fill: { color: C.accent } });
    s.addText("SESIÓN 5", {
      x: 0.7,
      y: 1.5,
      w: 11.5,
      h: 0.4,
      fontSize: 16,
      color: C.accent,
      fontFace: FONT,
      bold: true,
    });
    s.addText("Operacionalización, instrumentos\ny revisión inicial de datos (EDA)", {
      x: 0.7,
      y: 2.0,
      w: 12,
      h: 1.7,
      fontSize: 32,
      bold: true,
      color: C.white,
      fontFace: FONT,
    });
    s.addText(
      "Objeto: OpenAPI bancario ↔ BIAN  ·  Piloto: Open Finance Brasil (38 APIs)\nGrupo 10  ·  Alex Mancilla Antay  ·  Dennis Jack Paitan Cano  ·  MIA 403 · UNI",
      {
        x: 0.7,
        y: 4.1,
        w: 11.5,
        h: 1.1,
        fontSize: 16,
        color: "D6DEE8",
        fontFace: FONT,
      }
    );
    s.addNotes(
      "Documento de apoyo de la Sesión 5. No sustituye el plan LaTeX. Identidad vigente: Grupo 10."
    );
  }

  // 2. Agenda
  {
    const s = pptx.addSlide();
    titleBar(s, "Agenda de la sesión");
    footer(s);
    const items = [
      ["A1", "Definición conceptual y operacional de las variables"],
      ["A2", "Instrumentos, fuentes, métricas y procedimiento de medición"],
      ["A3", "Correspondencia OE ↔ indicadores"],
      ["B1", "Origen, estructura, calidad y disponibilidad del piloto"],
      ["B2", "Estadísticas descriptivas y distribuciones (gráficos)"],
      ["B3–B5", "Faltantes, variable objetivo, sesgos y data leakage"],
    ];
    items.forEach((it, i) => {
      const y = 1.2 + i * 0.85;
      s.addShape("roundRect", {
        x: 0.5,
        y,
        w: 1.4,
        h: 0.68,
        fill: { color: i < 3 ? C.navy : C.blue },
        rectRadius: 0.06,
      });
      s.addText(it[0], {
        x: 0.5,
        y,
        w: 1.4,
        h: 0.68,
        fontSize: 16,
        bold: true,
        color: C.white,
        align: "center",
        valign: "middle",
        fontFace: FONT,
      });
      s.addText(it[1], {
        x: 2.1,
        y,
        w: 10.5,
        h: 0.68,
        fontSize: 18,
        color: C.text,
        valign: "middle",
        fontFace: FONT,
      });
    });
  }

  // 3. Plan 12 semanas
  {
    const s = pptx.addSlide();
    titleBar(s, "Dónde estamos en el plan de 12 semanas");
    footer(s);
    s.addChart(pptx.ChartType.bar, [
      {
        name: "Avance (0=pendiente, 1=parcial, 2=en curso, 3=hecho)",
        labels: ["S1–2 Pares", "S3–4 Parser", "S5–6 Limpieza", "S7–8 Matching", "S9–10 Scores", "S11–12 Validación"],
        values: [2, 3, 2, 0, 0, 0],
      },
    ], {
      x: 0.4,
      y: 1.1,
      w: 7.4,
      h: 5.6,
      barGrouping: "clustered",
      showValue: true,
      showLegend: false,
      chartColors: [C.navy],
      chartArea: { fill: { color: C.white } },
      valAxisMaxValue: 3,
      valAxisMinValue: 0,
      catAxisLabelColor: C.text,
      valAxisLabelColor: C.muted,
      catAxisLabelFontSize: 11,
      valAxisHidden: true,
    });
    s.addShape("roundRect", { x: 8.0, y: 1.2, w: 4.85, h: 5.4, fill: { color: C.card }, rectRadius: 0.08 });
    s.addText("Lectura", {
      x: 8.2,
      y: 1.4,
      w: 4.45,
      h: 0.4,
      fontSize: 16,
      bold: true,
      color: C.navy,
      fontFace: FONT,
    });
    s.addText(
      [
        { text: "Piloto: 38 APIs Open Finance Brasil + 3 SD BIAN v14 (41 YAML).", options: { bullet: true, breakLine: true } },
        { text: "Objeto de la tesis sigue siendo OpenAPI bancario; OFB es la muestra.", options: { bullet: true, breakLine: true } },
        { text: "Pares de score: accounts / payments / enrollments × 3 SD.", options: { bullet: true, breakLine: true } },
        { text: "Aún no hay AlignmentScore: falta matching OE2–OE4.", options: { bullet: true } },
      ],
      { x: 8.2, y: 1.9, w: 4.45, h: 4.4, fontSize: 14, color: C.text, fontFace: FONT, valign: "top" }
    );
  }

  // 4. VD y fórmula
  {
    const s = pptx.addSlide();
    titleBar(s, "Qué se mide (variable dependiente del artefacto)");
    footer(s);
    s.addShape("roundRect", {
      x: 0.45,
      y: 1.15,
      w: 12.4,
      h: 1.55,
      fill: { color: C.navy },
      rectRadius: 0.08,
    });
    s.addText("AlignmentScore  =  α·S  +  β·E  +  γ·C     con  α+β+γ = 1", {
      x: 0.6,
      y: 1.28,
      w: 12.1,
      h: 0.7,
      fontSize: 26,
      bold: true,
      color: C.white,
      align: "center",
      fontFace: FONT,
    });
    s.addText("Base de medición: instancia  contrato OpenAPI bancario  ×  Service Domain BIAN", {
      x: 0.6,
      y: 2.0,
      w: 12.1,
      h: 0.45,
      fontSize: 14,
      color: "D6DEE8",
      align: "center",
      fontFace: FONT,
    });
    const boxes = [
      ["S  SemanticScore", "Similitud de significado OpenAPI ↔ BIAN"],
      ["E  StructuralScore", "Correspondencia de jerarquía REST ↔ SD"],
      ["C  CoverageScore", "Conceptos BIAN cubiertos por el contrato"],
    ];
    boxes.forEach((b, i) => {
      const x = 0.45 + i * 4.2;
      s.addShape("roundRect", { x, y: 2.95, w: 4.0, h: 1.7, fill: { color: C.card }, rectRadius: 0.08 });
      s.addText(b[0], { x: x + 0.15, y: 3.1, w: 3.7, h: 0.55, fontSize: 16, bold: true, color: C.navy, fontFace: FONT });
      s.addText(b[1], { x: x + 0.15, y: 3.65, w: 3.7, h: 0.8, fontSize: 14, color: C.text, fontFace: FONT });
    });
    s.addText(
      "Clasificación (umbrales provisionales §1.4):  Alta ≥ 0,80   ·   Media 0,60–0,79   ·   Baja 0,40–0,59   ·   Nula < 0,40\nS, E, C y la completitud de extracción son productos parciales de OE1–OE4; no sustituyen la VD.",
      { x: 0.45, y: 4.9, w: 12.4, h: 1.7, fontSize: 15, color: C.text, fontFace: FONT }
    );
  }

  // 5. Conceptual vs operacional
  {
    const s = pptx.addSlide();
    titleBar(s, "A1. Definición conceptual vs. operacional");
    footer(s);
    s.addTable(
      [
        headerRow(["Constructo", "Definición conceptual", "Definición operacional", "Escala"]),
        row(["SemanticScore (S)", "¿Los conceptos significan lo mismo?", "Similitud coseno / ontológica sobre corpus OE1", "[0, 1]"], false),
        row(["StructuralScore (E)", "¿La jerarquía REST refleja el SD?", "Matriz de pares + promedio de alineados", "[0, 1]"], true),
        row(["CoverageScore (C)", "¿Cuánto del SD cubre el contrato?", "Conceptos BIAN mapeados / total del SD", "[0, 1]"], false),
        row(["AlignmentScore", "Alineación global del contrato", "α·S + β·E + γ·C  (VD del artefacto)", "[0, 1]"], true),
        row(["Clasificación", "Nivel interpretable", "Umbrales fijos Alta / Media / Baja / Nula", "Nominal 4"], false),
        row(["Completitud (OE1)", "¿El parser recuperó el artefacto?", "Extraídos / esperados (ops, schemas, textos)", "Ratio"], true),
      ],
      { ...tblOpts(7, [2.4, 3.6, 4.5, 1.93]), y: 1.15, fontSize: 12 }
    );
    s.addText("Factores de diseño (no son la VD): esquema intermedio · estrategia de matching · técnica semántica · pesos α, β, γ.", {
      x: 0.45,
      y: 6.45,
      w: 12.4,
      h: 0.45,
      fontSize: 13,
      color: C.muted,
      fontFace: FONT,
    });
  }

  // 6. OE indicadores
  {
    const s = pptx.addSlide();
    titleBar(s, "A3. Correspondencia OE ↔ indicador");
    footer(s);
    s.addTable(
      [
        headerRow(["OE", "Pregunta", "Indicador", "Estado piloto"]),
        row(["Fase 1", "¿Qué se mide y cómo se combina?", "Definición S/E/C, fórmula, umbrales", "Cumplido (plan)"], false),
        row(["OE1", "¿Se pueden comparar REST y BIAN?", "Completitud + representaciones normalizadas", "41 contratos parseados"], true),
        row(["OE2 · P1", "¿La estructura refleja el SD?", "StructuralScore (E)", "Pendiente"], false),
        row(["OE3 · P2", "¿Los conceptos coinciden?", "SemanticScore (S)", "Pendiente"], true),
        row(["OE4 · P3–P4", "¿Alineación global y tipologías?", "C + AlignmentScore + nivel", "Pendiente"], false),
      ],
      { ...tblOpts(6, [1.8, 4.3, 3.9, 2.43]), y: 1.15 }
    );
    s.addShape("roundRect", { x: 0.45, y: 5.55, w: 12.4, h: 1.25, fill: { color: "FDEBD0" }, rectRadius: 0.08 });
    s.addText(
      "Criterio oral: un parser al 100 % no implica AlignmentScore Alto. La completitud de OE1 no sustituye la VD del artefacto.\nNo hay aprendizaje supervisado: los scores salen de reglas y métricas (schema matching + similitud semántica).",
      { x: 0.65, y: 5.7, w: 12.0, h: 1.0, fontSize: 14, color: C.text, fontFace: FONT }
    );
  }

  // 7. Fuentes e instrumentos
  {
    const s = pptx.addSlide();
    titleBar(s, "A2. Fuentes de datos e instrumentos");
    footer(s);
    s.addTable(
      [
        headerRow(["Elemento", "Diseño del plan", "Piloto actual"]),
        row(["Objeto de estudio", "Contrato OpenAPI bancario", "No cambia (OFB no sustituye el objeto)"], false),
        row(["Muestra / piloto", "Contratos bancarios parseables", "38 APIs Open Finance Brasil (160 ops)"], true),
        row(["Referencia", "Service Domain BIAN", "Savings + Current + PaymentOrderInitiation v14"], false),
        row(["Unidad de análisis", "endpoint/schema ↔ Behavior/BO", "235 ops; matching pendiente"], true),
        row(["Instancia", "{fuente}_{api}_{versión} × {sd}", "p. ej. OFB_accounts_2.4.2 × SavingsAccount_14"], false),
        row(["Instrumento OE1", "Parser OpenAPI 3.x", "procesar_openapi.py → consolidado + por_contrato"], true),
      ],
      { ...tblOpts(7, [2.6, 4.9, 4.93]), y: 1.12 }
    );
    s.addText(
      "Adquirir (versionar YAML) va antes de normalizar. Criterios de inclusión: OpenAPI 3.x parseable, ≥1 operación y esquema, BIAN legible, sin PII (Ley 29733).",
      { x: 0.45, y: 6.35, w: 12.4, h: 0.55, fontSize: 13, color: C.muted, fontFace: FONT }
    );
  }

  // 8. Procedimiento
  {
    const s = pptx.addSlide();
    titleBar(s, "Procedimiento de medición (cinco fases)");
    footer(s);
    const fases = [
      ["1", "Diseñar", "Entradas, S/E/C,\nfórmula y umbrales", C.ok],
      ["2", "Adquirir +\nnormalizar", "YAML versionado →\nrepresentación OE1", C.warn],
      ["3", "Emparejar\nestructuras", "Matriz + E", C.muted],
      ["4", "Similitud\nsemántica", "Corpus + S", C.muted],
      ["5", "Integrar y\nclasificar", "C + AlignmentScore\n+ tipologías", C.muted],
    ];
    fases.forEach((f, i) => {
      const x = 0.4 + i * 2.55;
      s.addShape("roundRect", { x, y: 1.4, w: 2.4, h: 3.6, fill: { color: C.card }, rectRadius: 0.1 });
      s.addShape("ellipse", { x: x + 0.8, y: 1.6, w: 0.8, h: 0.8, fill: { color: f[3] } });
      s.addText(f[0], {
        x: x + 0.8,
        y: 1.6,
        w: 0.8,
        h: 0.8,
        align: "center",
        valign: "middle",
        color: C.white,
        bold: true,
        fontSize: 20,
        fontFace: FONT,
      });
      s.addText(f[1], {
        x: x + 0.1,
        y: 2.55,
        w: 2.2,
        h: 1.0,
        align: "center",
        fontSize: 15,
        bold: true,
        color: C.navy,
        fontFace: FONT,
      });
      s.addText(f[2], {
        x: x + 0.1,
        y: 3.55,
        w: 2.2,
        h: 1.2,
        align: "center",
        fontSize: 13,
        color: C.text,
        fontFace: FONT,
      });
      if (i < 4) {
        s.addShape("rightArrow", {
          x: x + 2.32,
          y: 2.95,
          w: 0.28,
          h: 0.22,
          fill: { color: C.accent },
        });
      }
    });
    s.addText("Fase 2 cubierta: 38 APIs OFB + 3 SD BIAN. Fases 3–5: matching sobre los pares I1–I6 (n = 7 instancias).", {
      x: 0.45,
      y: 5.3,
      w: 12.4,
      h: 1.4,
      fontSize: 16,
      color: C.text,
      fontFace: FONT,
    });
  }

  // 9. Section EDA
  {
    const s = pptx.addSlide();
    s.addShape("rect", { x: 0, y: 0, w: 13.333, h: 7.5, fill: { color: C.navy } });
    s.addShape("rect", { x: 0, y: 0, w: 0.18, h: 7.5, fill: { color: C.accent } });
    s.addText("PARTE B", {
      x: 0.7,
      y: 2.3,
      w: 11,
      h: 0.4,
      fontSize: 16,
      color: C.accent,
      bold: true,
      fontFace: FONT,
    });
    s.addText("Revisión inicial de datos\ny análisis exploratorio (EDA)", {
      x: 0.7,
      y: 2.8,
      w: 12,
      h: 1.6,
      fontSize: 32,
      bold: true,
      color: C.white,
      fontFace: FONT,
    });
    s.addText("Dataset: 02-curso-II/piloto/\n41 contratos · 235 operaciones · 3 SD BIAN v14 + 38 APIs Open Finance Brasil", {
      x: 0.7,
      y: 4.55,
      w: 11.5,
      h: 0.85,
      fontSize: 16,
      color: "D6DEE8",
      fontFace: FONT,
    });
  }

  // 10. KPIs
  {
    const s = pptx.addSlide();
    titleBar(s, "B1. Inventario del piloto OFB × BIAN");
    footer(s);
    kpi(s, 0.45, 1.2, "41", "contratos");
    kpi(s, 3.55, 1.2, "235", "operaciones");
    kpi(s, 6.65, 1.2, "6746", "propiedades");
    kpi(s, 9.75, 1.2, "10906", "textos (corpus)");
    s.addTable(
      [
        headerRow(["Atributo", "Valor"]),
        row(["Carpeta", "02-curso-II/piloto/  (fuentes/ofb + fuentes/bian)"], false),
        row(["BIAN v14", "SavingsAccount 34 · CurrentAccount 34 · PaymentOrderInitiation 7 (75 ops)"], true),
        row(["Open Finance Brasil", "38 APIs (última estable) · 160 ops · cuentas, pagos, créditos, tarjetas, open data…"], false),
        row(["Criterio OFB", "Última versión estable por carpeta swagger-apis (1 beta: payroll-credit-portability)"], true),
        row(["PII", "Material público BIAN + OFB; sin datos personales"], false),
        row(["Pendiente", "Matching OFB × BIAN y AlignmentScore (OE2–OE4)"], true),
      ],
      { x: 0.45, y: 2.7, w: 12.43, colW: [2.6, 9.83], border: [{ pt: 0.5, color: "D0D7DE" }], fontFace: FONT, color: C.text, valign: "middle", fontSize: 12 }
    );
  }

  // 11. Chart métodos HTTP
  {
    const s = pptx.addSlide();
    titleBar(s, "B2. Distribución de operaciones por método HTTP");
    footer(s);
    s.addChart(pptx.ChartType.bar, [
      {
        name: "Operaciones",
        labels: ["GET", "POST", "PUT", "PATCH", "DELETE"],
        values: [152, 39, 36, 7, 1],
      },
    ], {
      x: 0.3,
      y: 1.05,
      w: 7.2,
      h: 5.7,
      barGrouping: "clustered",
      showValue: true,
      showLegend: false,
      chartColors: [C.navy],
      catAxisLabelColor: C.text,
      valAxisHidden: true,
      valAxisMaxValue: 160,
    });
    s.addShape("roundRect", { x: 7.7, y: 1.2, w: 5.15, h: 5.4, fill: { color: C.card }, rectRadius: 0.08 });
    s.addText("Lectura", { x: 7.9, y: 1.4, w: 4.8, h: 0.4, fontSize: 16, bold: true, color: C.navy, fontFace: FONT });
    s.addText(
      [
        { text: "GET 152 · POST 39 · PUT 36 · PATCH 7 · DELETE 1.", options: { bullet: true, breakLine: true } },
        { text: "OFB es mayormente GET (130/160): consulta de datos del cliente.", options: { bullet: true, breakLine: true } },
        { text: "BIAN concentra los PUT (Update/Control/Execute del SD).", options: { bullet: true, breakLine: true } },
        { text: "Aparece 1 DELETE (lado OFB); BIAN v14 de este piloto no borra.", options: { bullet: true, breakLine: true } },
        { text: "E debe tolerar REST de consulta (OFB) vs. REST de facility (BIAN).", options: { bullet: true } },
      ],
      { x: 7.9, y: 1.95, w: 4.8, h: 4.3, fontSize: 15, color: C.text, fontFace: FONT }
    );
  }

  // 12. Chart tags CR/BQ
  {
    const s = pptx.addSlide();
    titleBar(s, "B2. Operaciones por tag BIAN (CR vs. BQ)");
    footer(s);
    s.addChart(pptx.ChartType.doughnut, [
      {
        name: "Tags",
        labels: ["Open Finance Brasil", "BQ BIAN", "CR BIAN"],
        values: [160, 64, 11],
      },
    ], {
      x: 0.2,
      y: 1.1,
      w: 7.0,
      h: 5.6,
      showPercent: true,
      showLegend: true,
      legendPos: "b",
      chartColors: [C.navy, C.blue, C.accent, C.danger],
    });
    s.addShape("roundRect", { x: 7.4, y: 1.2, w: 5.45, h: 5.4, fill: { color: C.card }, rectRadius: 0.08 });
    s.addText("Desbalance", { x: 7.6, y: 1.4, w: 5.1, h: 0.4, fontSize: 16, bold: true, color: C.navy, fontFace: FONT });
    s.addText(
      [
        { text: "160 ops OFB vs 75 BIAN: la muestra del piloto es más ancha que la referencia (3 SD).", options: { bullet: true, breakLine: true } },
        { text: "BIAN: 64 BQ + 11 CR (Charge, Sweep, Interest, Payment, Deposit…).", options: { bullet: true, breakLine: true } },
        { text: "OFB no usa tags CR/BQ: no imputarlos (leakage).", options: { bullet: true, breakLine: true } },
        { text: "Para préstamos/tarjetas OFB faltan SD BIAN (Loan, CreditCard) en este zip.", options: { bullet: true } },
      ],
      { x: 7.6, y: 1.95, w: 5.1, h: 4.3, fontSize: 15, color: C.text, fontFace: FONT }
    );
  }

  // 13. Schemas + corpus
  {
    const s = pptx.addSlide();
    titleBar(s, "B2. Operaciones por contrato (piloto OFB)");
    footer(s);
    s.addChart(pptx.ChartType.bar, [
      {
        name: "Operaciones",
        labels: ["OFB (38 APIs)", "CurrentAccount", "SavingsAccount", "PaymentOrderInit."],
        values: [160, 34, 34, 7],
      },
    ], {
      x: 0.25,
      y: 1.05,
      w: 7.3,
      h: 5.7,
      barGrouping: "clustered",
      showValue: true,
      showLegend: false,
      chartColors: [C.navy],
      valAxisHidden: true,
      valAxisMaxValue: 170,
    });
    s.addShape("roundRect", { x: 7.7, y: 1.2, w: 5.15, h: 5.4, fill: { color: C.card }, rectRadius: 0.08 });
    s.addText("Scope enriquecido", { x: 7.9, y: 1.4, w: 4.8, h: 0.4, fontSize: 16, bold: true, color: C.navy, fontFace: FONT });
    s.addText(
      "38 APIs OFB: cuentas, pagos, créditos, tarjetas, consentimientos, open data, inversiones, seguros, pensiones…\n\nPares listos con BIAN actual: accounts↔Savings/Current y payments↔PaymentOrderInitiation.\n\nHueco: loans, credit-cards, financings no tienen SD BIAN en este piloto.\n\nCatálogo en 02-curso-II/piloto/README.md.",
      { x: 7.9, y: 1.95, w: 4.8, h: 4.3, fontSize: 14, color: C.text, fontFace: FONT }
    );
  }

  // 14. Corpus mix
  {
    const s = pptx.addSlide();
    titleBar(s, "B2. Composición del corpus semántico (10 906 fragmentos)");
    footer(s);
    s.addChart(pptx.ChartType.bar, [
      {
        name: "Fragmentos",
        labels: ["property", "schema", "operation"],
        values: [9314, 1253, 339],
      },
    ], {
      x: 0.3,
      y: 1.1,
      w: 6.8,
      h: 5.6,
      barGrouping: "clustered",
      showValue: true,
      showLegend: false,
      chartColors: [C.blue],
      valAxisHidden: true,
      valAxisMaxValue: 10000,
    });
    s.addTable(
      [
        headerRow(["Campo", "n", "Nota"]),
        row(["property.name", "6746", "Una fila por atributo"], false),
        row(["property + desc", "9314", "Incluye nombres y glosas"], true),
        row(["operation.summary", "235", "100 % de las operaciones"], false),
        row(["operation (textos)", "339", "OFB aporta description extra"], true),
        row(["schema.description", "1253", "Schemas con glosa"], false),
      ],
      { x: 7.3, y: 1.2, w: 5.55, colW: [2.2, 0.7, 2.65], border: [{ pt: 0.5, color: "D0D7DE" }], fontFace: FONT, color: C.text, valign: "middle", fontSize: 12 }
    );
    s.addText("Corpus: 10 906 fragmentos. Prefijos InCR/ReBQ limpios. BIAN: summary = description en 75/75 ops.", {
      x: 7.3,
      y: 5.7,
      w: 5.55,
      h: 1.0,
      fontSize: 13,
      color: C.muted,
      fontFace: FONT,
    });
  }

  // 15. Faltantes
  {
    const s = pptx.addSlide();
    titleBar(s, "B3. Faltantes, duplicados e inconsistencias");
    footer(s);
    s.addChart(pptx.ChartType.bar, [
      {
        name: "% del campo",
        labels: ["BIAN summary=desc", "prop. sin desc.", "props BIAN vacías", "props OFB vacías", "DELETE"],
        values: [100, 62, 90, 38, 0],
      },
    ], {
      x: 0.25,
      y: 1.05,
      w: 7.4,
      h: 5.7,
      barGrouping: "clustered",
      showValue: true,
      showLegend: false,
      chartColors: [C.danger],
      valAxisMaxValue: 100,
      valAxisHidden: true,
      catAxisLabelFontSize: 10,
    });
    s.addShape("roundRect", { x: 7.8, y: 1.2, w: 5.05, h: 5.4, fill: { color: C.card }, rectRadius: 0.08 });
    s.addText("Calidad", { x: 8.0, y: 1.4, w: 4.7, h: 0.35, fontSize: 16, bold: true, color: C.navy, fontFace: FONT });
    s.addText(
      [
        { text: "BIAN: summary = description en 75/75 operaciones.", options: { bullet: true, breakLine: true } },
        { text: "OFB: descriptions distintas (12 ops con texto extra).", options: { bullet: true, breakLine: true } },
        { text: "61,9 % props sin description (BIAN 90,4 %; OFB 38,1 %).", options: { bullet: true, breakLine: true } },
        { text: "Parser ahora resuelve $ref anidados de request/response.", options: { bullet: true, breakLine: true } },
        { text: "CSV UTF-8 con BOM: abrir con utf-8-sig.", options: { bullet: true } },
      ],
      { x: 8.0, y: 1.9, w: 4.7, h: 4.4, fontSize: 14, color: C.text, fontFace: FONT }
    );
  }

  // 16. Variable objetivo / clases
  {
    const s = pptx.addSlide();
    titleBar(s, "B4. Variable objetivo y distribución de clases");
    footer(s);
    s.addShape("roundRect", { x: 0.45, y: 1.15, w: 12.4, h: 1.5, fill: { color: C.navy }, rectRadius: 0.08 });
    s.addText("VD = AlignmentScore + clasificación {Alta, Media, Baja, Nula}", {
      x: 0.65,
      y: 1.28,
      w: 12.0,
      h: 0.55,
      fontSize: 22,
      bold: true,
      color: C.white,
      align: "center",
      fontFace: FONT,
    });
    s.addText("Hay pares de artefactos, pero aún no S/E/C. No hay distribución de clases empírica.", {
      x: 0.65,
      y: 1.85,
      w: 12.0,
      h: 0.55,
      fontSize: 15,
      color: "D6DEE8",
      align: "center",
      fontFace: FONT,
    });
    s.addChart(pptx.ChartType.bar, [
      {
        name: "Proxy (NO es la VD)",
        labels: ["OFB (piloto)", "BQ BIAN", "CR BIAN"],
        values: [160, 64, 11],
      },
    ], {
      x: 0.3,
      y: 2.8,
      w: 7.3,
      h: 3.9,
      showValue: true,
      showLegend: false,
      chartColors: [C.blue],
      valAxisHidden: true,
      valAxisMaxValue: 170,
    });
    s.addText(
      "Proxy estructural (tags), no la VD.\n\nOFB 160 ops vs BIAN 75: el catálogo open banking es más ancho que la referencia BIAN de este zip.\n\nAlta/Media/Baja/Nula se reportará tras AlignmentScore en pares accounts↔Savings/Current y payments↔PaymentOrderInitiation.",
      { x: 7.8, y: 3.0, w: 5.0, h: 3.5, fontSize: 15, color: C.text, fontFace: FONT }
    );
  }

  // 17. Leakage
  {
    const s = pptx.addSlide();
    titleBar(s, "B5. Sesgos y riesgos de fuga de información");
    footer(s);
    s.addTable(
      [
        headerRow(["Riesgo", "Qué ocurriría", "Mitigación"]),
        row(["Identidad de artefacto", "Evaluar BIAN contra sí mismo → scores trivialmente altos", "Usar OFB × BIAN; no reportar autoalineación BIAN↔BIAN"], false),
        row(["Tags CR/BQ en el banco", "Contaminar E con estructura de la referencia", "No imputar tags BIAN al contrato bancario"], true),
        row(["Nombre del $ref", "SavingsAccountFacility es un nombre BIAN, no del banco", "No usarlo como evidencia semántica del lado banco"], false),
        row(["Calibrar umbrales in-sample", "Pesos α,β,γ ajustados en los mismos pares del reporte", "Separar calibración vs. reporte (Tesis 2)"], true),
        row(["Prefijos InCR / ReBQ", "Reintroducir la etiqueta BIAN como feature", "Limpiarlos en S; no usarlos como predictor"], false),
        row(["Confundir OFB con el objeto", "Estrechar la tesis a un estándar brasileño", "OFB = piloto; objeto = OpenAPI bancario"], true),
      ],
      { ...tblOpts(7, [2.6, 5.3, 4.53]), y: 1.12, fontSize: 11 }
    );
  }

  // 18. Próximos pasos
  {
    const s = pptx.addSlide();
    titleBar(s, "Implicaciones · qué sigue");
    footer(s);
    const pasos = [
      ["P0", C.ok, "Hecho: catálogo OFB (38 APIs, última estable) + 3 SD BIAN v14 en el zip."],
      ["P1", C.warn, "Definir pares de matching: Accounts↔Savings/Current y Payments↔PaymentOrderInitiation."],
      ["P1", C.warn, "Cerrar OE1: completitud extraídos/esperados por contrato (inventario.json)."],
      ["P2", C.navy, "OE2–OE3: matrices estructurales y semánticas (S7–S8)."],
      ["P2", C.navy, "OE4: C + AlignmentScore; no usar autoalineación BIAN↔BIAN como resultado."],
    ];
    pasos.forEach((p, i) => {
      const y = 1.2 + i * 1.05;
      s.addShape("roundRect", { x: 0.5, y, w: 1.2, h: 0.85, fill: { color: p[1] }, rectRadius: 0.06 });
      s.addText(p[0], {
        x: 0.5,
        y,
        w: 1.2,
        h: 0.85,
        align: "center",
        valign: "middle",
        color: C.white,
        bold: true,
        fontSize: 18,
        fontFace: FONT,
      });
      s.addText(p[2], {
        x: 1.95,
        y,
        w: 10.8,
        h: 0.85,
        valign: "middle",
        fontSize: 16,
        color: C.text,
        fontFace: FONT,
      });
    });
  }

  // 19. Cierre
  {
    const s = pptx.addSlide();
    s.addShape("rect", { x: 0, y: 0, w: 13.333, h: 7.5, fill: { color: C.navy } });
    s.addShape("rect", { x: 0, y: 0, w: 0.18, h: 7.5, fill: { color: C.accent } });
    s.addText("En una frase", {
      x: 0.7,
      y: 1.8,
      w: 12,
      h: 0.4,
      fontSize: 16,
      color: C.accent,
      bold: true,
      fontFace: FONT,
    });
    s.addText(
      "La tesis mide OpenAPI bancario ↔ BIAN. El piloto de esta sesión es Open Finance Brasil (38 APIs, 160 ops) frente a tres SD v14. AlignmentScore aún no calculado.",
      {
        x: 0.7,
        y: 2.4,
        w: 11.8,
        h: 2.2,
        fontSize: 24,
        bold: true,
        color: C.white,
        fontFace: FONT,
      }
    );
    s.addText("Grupo 10  ·  Alex Mancilla  ·  Dennis Jack Paitan  ·  fuente escrita: Sesion05_Operacionalizacion_y_EDA.md", {
      x: 0.7,
      y: 5.3,
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
