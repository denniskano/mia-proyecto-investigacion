#!/usr/bin/env node
/**
 * Genera Exposicion_Plan_Tesis_Grupo9.2-v2.pptx con PptxGenJS.
 * Estrategia: master slide + zonas (título / cuerpo / pie) + layouts split (texto + figura).
 * No modifica PPT existentes.
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import pptxgen from "pptxgenjs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ASSETS = path.join(__dirname, "assets");
const OUTPUT = path.join(__dirname, "Exposicion_Plan_Tesis_Grupo9.2-v2.pptx");

const C = {
  navy: "1B365D",
  blue: "003DA5",
  accent: "E8A317",
  bg: "F7F9FC",
  text: "2D3436",
  muted: "636E72",
  white: "FFFFFF",
  danger: "C0392B",
  tableHead: "1B365D",
  tableAlt: "EEF2F7",
};

const FONT = "Arial";
const FOOTER = "Grupo 9.2 · Plan de Tesis · UNI · Jul 2026";

let slideNum = 0;

function asset(name) {
  const p = path.join(ASSETS, name);
  return fs.existsSync(p) ? p : null;
}

function defineMasters(pptx) {
  const footerLine = {
    x: 0.5,
    y: 7.05,
    w: 12.33,
    h: 0.02,
    line: { color: C.muted, width: 0.5 },
  };

  pptx.defineSlideMaster({
    title: "MASTER_CONTENT",
    background: { color: C.white },
    objects: [
      footerLine,
      {
        placeholder: {
          options: { name: "title", type: "title", x: 0.5, y: 0.28, w: 12.33, h: 0.95, fontSize: 24, bold: true, color: C.navy, fontFace: FONT },
        },
      },
      {
        placeholder: {
          options: { name: "body", type: "body", x: 0.5, y: 1.35, w: 12.33, h: 5.55, fontSize: 20, color: C.text, fontFace: FONT },
        },
      },
      {
        text: {
          options: {
            x: 0.5,
            y: 7.12,
            w: 10.5,
            h: 0.28,
            fontSize: 9,
            color: C.muted,
            fontFace: FONT,
          },
          text: FOOTER,
        },
      },
    ],
    slideNumber: { x: 12.55, y: 7.1, color: C.muted, fontFace: FONT, fontSize: 10 },
  });

  pptx.defineSlideMaster({
    title: "MASTER_SPLIT",
    background: { color: C.white },
    objects: [
      footerLine,
      {
        placeholder: {
          options: { name: "title", type: "title", x: 0.5, y: 0.28, w: 12.33, h: 0.95, fontSize: 22, bold: true, color: C.navy, fontFace: FONT },
        },
      },
      {
        placeholder: {
          options: { name: "body", type: "body", x: 0.5, y: 1.35, w: 5.75, h: 5.55, fontSize: 18, color: C.text, fontFace: FONT },
        },
      },
      {
        placeholder: {
          options: { name: "img", type: "pic", x: 6.45, y: 1.35, w: 6.38, h: 5.55 },
        },
      },
      {
        text: {
          options: { x: 0.5, y: 7.12, w: 10.5, h: 0.28, fontSize: 9, color: C.muted, fontFace: FONT },
          text: FOOTER,
        },
      },
    ],
    slideNumber: { x: 12.55, y: 7.1, color: C.muted, fontFace: FONT, fontSize: 10 },
  });

  pptx.defineSlideMaster({
    title: "MASTER_FIGURE",
    background: { color: C.white },
    objects: [
      footerLine,
      {
        placeholder: {
          options: { name: "title", type: "title", x: 0.5, y: 0.28, w: 12.33, h: 0.85, fontSize: 22, bold: true, color: C.navy, fontFace: FONT },
        },
      },
      {
        placeholder: {
          options: { name: "img", type: "pic", x: 0.65, y: 1.25, w: 12.03, h: 5.35 },
        },
      },
      {
        text: {
          options: { x: 0.5, y: 7.12, w: 10.5, h: 0.28, fontSize: 9, color: C.muted, fontFace: FONT },
          text: FOOTER,
        },
      },
    ],
    slideNumber: { x: 12.55, y: 7.1, color: C.muted, fontFace: FONT, fontSize: 10 },
  });

  pptx.defineSlideMaster({
    title: "MASTER_SECTION",
    background: { color: C.navy },
    objects: [
      {
        rect: { x: 0, y: 0, w: "100%", h: "100%", fill: { color: C.navy } },
      },
      {
        placeholder: {
          options: {
            name: "title",
            type: "title",
            x: 0.8,
            y: 2.6,
            w: 11.73,
            h: 1.5,
            fontSize: 36,
            bold: true,
            color: C.white,
            align: "left",
            fontFace: FONT,
          },
        },
      },
      {
        text: {
          options: { x: 0.8, y: 4.2, w: 11, h: 0.5, fontSize: 16, color: C.accent, fontFace: FONT },
          text: FOOTER,
        },
      },
    ],
  });
}

function bulletsToText(items) {
  return items.map((t) => ({ text: t, options: { bullet: true, breakLine: true, paraSpaceAfter: 6 } }));
}

function addBullets(slide, items, opts = {}) {
  slide.addText(bulletsToText(items), {
    placeholder: "body",
    valign: "top",
    fontSize: opts.size ?? 20,
    color: C.text,
    fontFace: FONT,
  });
}

function addNotes(slide, text) {
  if (text) slide.addNotes(text);
}

function addImage(slide, file, box = { x: 6.45, y: 1.35, w: 6.38, h: 5.55 }) {
  const p = asset(file);
  if (!p) return;
  slide.addImage({
    path: p,
    x: box.x,
    y: box.y,
    w: box.w,
    h: box.h,
    sizing: { type: "contain", w: box.w, h: box.h },
  });
}

function addCaption(slide, text) {
  slide.addText(text, {
    x: 0.65,
    y: 6.62,
    w: 12.03,
    h: 0.38,
    fontSize: 18,
    color: C.muted,
    align: "center",
    fontFace: FONT,
  });
}

function addTableSlide(pptx, title, headers, rows, notes, colW) {
  slideNum += 1;
  const slide = pptx.addSlide({ masterName: "MASTER_CONTENT" });
  slide.addText(title, { placeholder: "title" });

  const tableRows = [
    headers.map((h) => ({
      text: h,
      options: { bold: true, color: C.white, fill: { color: C.tableHead }, fontSize: 11, fontFace: FONT },
    })),
    ...rows.map((row, ri) =>
      row.map((cell) => ({
        text: cell,
        options: {
          fontSize: 11,
          fontFace: FONT,
          color: C.text,
          fill: { color: ri % 2 ? C.tableAlt : C.white },
        },
      }))
    ),
  ];

  slide.addTable(tableRows, {
    x: 0.45,
    y: 1.35,
    w: 12.43,
    h: 5.5,
    colW,
    border: { pt: 0.5, color: "BDC3C7" },
    autoPage: false,
  });
  addNotes(slide, notes);
  return slide;
}

function build() {
  const pptx = new pptxgen();
  pptx.layout = "LAYOUT_WIDE";
  pptx.author = "Grupo 9.2 — Alex Mancilla · Jack Paitan";
  pptx.company = "Universidad Nacional de Ingeniería";
  pptx.subject = "Plan de Tesis — Alineación OpenAPI ↔ BIAN";
  pptx.title = "Exposición Plan de Tesis Grupo 9.2 (v2)";

  defineMasters(pptx);

  // --- 1 Title ---
  slideNum += 1;
  {
    const slide = pptx.addSlide();
    slide.background = { color: C.navy };
    slide.addText("Alineación contratos OpenAPI bancarios\n↔ Service Domains BIAN", {
      x: 0.8,
      y: 1.6,
      w: 11.5,
      h: 1.8,
      fontSize: 34,
      bold: true,
      color: C.white,
      fontFace: FONT,
    });
    slide.addText(
      [
        { text: "Investigación tecnológica · Design Science", options: { breakLine: true } },
        { text: "IEEE: Knowledge Representation · ACM: Semantic networks", options: { breakLine: true } },
        { text: "Grupo 9.2 — Alex Mancilla · Jack Paitan", options: { breakLine: true } },
        { text: "Universidad Nacional de Ingeniería · Julio 2026", options: { breakLine: true } },
      ],
      { x: 0.8, y: 3.6, w: 11, h: 2.2, fontSize: 20, color: C.accent, fontFace: FONT }
    );
    slide.addShape(pptx.shapes.RECTANGLE, {
      x: 0.8,
      y: 6.5,
      w: 2.2,
      h: 0.06,
      fill: { color: C.accent },
      line: { color: C.accent },
    });
    addNotes(slide, "[0:00–0:45] Jack. Título + tipo investigación + clasificación ACM/IEEE.");
  }

  // --- 2 Fuentes (NO EXPONER) ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_CONTENT" });
    slide.addShape(pptx.shapes.RECTANGLE, {
      x: 0,
      y: 0,
      w: "100%",
      h: 0.55,
      fill: { color: C.danger },
      line: { color: C.danger },
    });
    slide.addText("⛔ NO EXPONER EN CLASE — solo entrega (ppt-rules §3)", {
      x: 0.5,
      y: 0.1,
      w: 12,
      h: 0.4,
      fontSize: 16,
      bold: true,
      color: C.white,
      fontFace: FONT,
    });
    slide.addText("Fuentes bibliográficas y gestión documental", { placeholder: "title" });
    addBullets(
      slide,
      [
        "Formato: una sola fuente · texto ≥ 20 pt · figuras con caption",
        "Gestión: Zotero + carpeta Drive del grupo (entrega Guía 1)",
        "Esta slide documenta cumplimiento de formato — no forma parte del guion oral",
        "En exposición: avanzar de slide 1 directamente a slide 3",
      ],
      { size: 20 }
    );
    addNotes(slide, "NO EXPONER. Saltar en clase.");
  }

  // --- 3 Intro ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_CONTENT" });
    slide.addText("OpenAPI y BIAN definen el problema de alineación documental", { placeholder: "title" });
    addBullets(slide, [
      "OpenAPI: contrato YAML/JSON machine-readable (Casas et al., 2021)",
      "BIAN: Service Domains como referencia de negocio (Farzi, 2021)",
      "Alineación = correspondencia estructural + semántica contrato ↔ SD",
      "Producto del plan: S, E, C → AlignmentScore (procedimiento reproducible)",
      "Guía 1: diseño documentado; validación empírica → Tesis 2 (§1.6)",
    ]);
    addNotes(slide, "[0:45–1:35] Alex. Conceptos antes del problema (PI-12).");
  }

  // --- 4 Ontología ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_SPLIT" });
    slide.addText("La ontología separa objeto, UA, producto y referencia BIAN", { placeholder: "title" });
    addBullets(slide, [
      "Objeto real: contrato OpenAPI bancario completo",
      "UA: instancia {fuente}_{SD}_{versión}",
      "Producto: scores S, E, C + AlignmentScore",
      "BIAN = referencia de contraste, no objeto",
    ], { size: 18 });
    addImage(slide, "Figura_02_Objeto_Unidad_Analisis.png");
    addNotes(slide, "[1:35–2:20] Jack. Señalar cajas; ID {fuente}_{SD}_{versión}.");
  }

  // --- 5 Problemática situación ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_SPLIT" });
    slide.addText("La problemática ocurre en el ecosistema bancario digital (§1.2)", { placeholder: "title" });
    addBullets(slide, [
      "Dónde: APIs propias, fintechs, open banking (CMA, 2016)",
      "Ambiente: contratos OpenAPI antes del despliegue",
      "Actores: arquitectura, integración, gobernanza, socios",
      "La problemática no se resuelve solo con el artefacto del plan",
    ], { size: 18 });
    addImage(slide, "Figura_01_Contexto.png");
    addNotes(slide, "[2:20–3:10] Jack. Situación real ≠ objeto ≠ problema tecnológico.");
  }

  // --- 6 Síntomas ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_CONTENT" });
    slide.addText("Síntomas y evidencia sectorial motivan medir coherencia antes de integrar", { placeholder: "title" });
    addBullets(slide, [
      "Síntomas: fragmentación semántica, costos de integración, deriva negocio–REST",
      "Dolor: retrabajo en adaptadores, ensayo–error, riesgo en releases (TSB, 2018)",
      "Casas et al. (2021): 68 % papers proponen herramientas; 43 % documentación",
      "Actores más afectados: equipos de integración y gobernanza de APIs",
      "Motiva medir coherencia documental antes de exponer servicios",
    ]);
    addNotes(slide, "[3:10–4:05] Jack. Tener PDF Casas listo (PI-13). Señalar cifra 68 %.");
  }

  // --- 7 Objeto subyacente ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_SPLIT" });
    slide.addText("El objeto es el contrato OpenAPI; BIAN es referencia (§1.4)", { placeholder: "title" });
    addBullets(slide, [
      "Causa: desalineación entre capa REST y modelo BIAN",
      "Objeto: contrato OpenAPI (paths, operations, schemas)",
      "Dos jerarquías comparables: OpenAPI ↔ Service Domain",
      "Usar ontología (slide 4) al exponer el problema subyacente",
    ], { size: 18 });
    addImage(slide, "Figura_02_Objeto_Unidad_Analisis.png");
    addNotes(slide, "[4:05–4:50] Jack. BIAN = referencia, no objeto.");
  }

  // --- 8 Objeto real ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_CONTENT" });
    slide.addText("El contrato publicado es la entidad real observable del estudio", { placeholder: "title" });
    addBullets(slide, [
      "Entidad real: contrato OpenAPI publicado por un banco",
      "Taxonomía: OpenAPI 3.x · pagos / cuentas / préstamos · versiones",
      "Ciclo de vida: diseño → revisión → publicación → consumo (no tráfico runtime)",
      "Registro: archivo versionado en repositorio / portal de desarrolladores",
      "Ejemplos Anexo F: pares contrato ↔ Payment Initiation SD",
    ]);
    addNotes(slide, "[4:50–5:30] Jack. Ciclo de vida del contrato.");
  }

  // --- 9 Instrumento ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_SPLIT" });
    slide.addText("El instrumento captura y normaliza contrato y Service Domain", { placeholder: "title" });
    addBullets(slide, [
      "Parser OpenAPI 3.x + extracto BIAN",
      "Procedimiento de normalización (OE1)",
      "Schema matching + similitud semántica",
      "Salida: representaciones + matrices + scores S/E/C",
    ], { size: 18 });
    addImage(slide, "Figura_05_Bases_Conceptuales.png");
    addNotes(slide, "[5:30–6:15] Alex. Instrumento = procedimiento, no encuesta.");
  }

  // --- 10 Casos A/B ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_CONTENT" });
    slide.addText("Instancias modeladas ilustran cómo S, E y C responden al diseño", { placeholder: "title" });
    addBullets(slide, [
      "Caso A: POST /payments vs InitiatePayment → afecta S",
      "Caso B: GET /payments/{id} vs 3 behaviors → afecta C",
      "Estados de clasificación del artefacto:",
      "Alta ≥0,80 · Media 0,60–0,79 · Baja 0,40–0,59 · Nula <0,40",
    ]);
    addNotes(slide, "[6:15–7:00] Alex. Ejemplos Anexo F.");
  }

  // --- 11 Problema tecnológico ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_CONTENT" });
    slide.addText("El artefacto responde P1–P4 con métodos insuficientes hoy (§1.3)", { placeholder: "title" });
    addBullets(slide, [
      "Artefacto: procedimiento + modelo S/E/C → AlignmentScore",
      "Tipo: clasificación + regresión acotada [0,1] por score",
      "Problema: métodos no adaptados a OpenAPI↔BIAN (Shvaiko, 2005; Casas, 2021)",
      "P1 matching estructural · P2 similitud semántica · P3 cobertura · P4 score integrado",
      "Solo relacionado al artefacto — no a la problemática del sector",
    ]);
    addNotes(slide, "[7:00–7:50] Alex. «Insuficiente», no «no existe» (PI-12).");
  }

  // --- 12 OG ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_CONTENT" });
    slide.addText("El objetivo general diseña el procedimiento reproducible S/E/C", { placeholder: "title" });
    addBullets(slide, [
      "Insumo: contrato OpenAPI + Service Domain BIAN emparejado",
      "OG: diseñar modelo S/E/C y procedimiento reproducible de alineación",
      "VD del artefacto: AlignmentScore ∈ [0,1] + clasificación",
      "Objetivo superior: cuantificar coherencia antes del despliegue",
      "Medida: S, E, C y score integrado por contrato × SD",
    ]);
    addNotes(slide, "[7:50–8:25] Alex. Separar OG técnico vs objetivo superior.");
  }

  // --- 13 OE ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_FIGURE" });
    slide.addText("OE1–OE4 encadenan normalización, E, S y C con productos verificables", { placeholder: "title" });
    addImage(slide, "Figura_04_Cadena_Objetivos.png", { x: 0.65, y: 1.25, w: 12.03, h: 5.0 });
    addCaption(slide, "Cada OE es hito con producto medible — no «programar» ni «experimentar»");
    addNotes(slide, "[8:25–9:15] Alex. OE1 normaliza · OE2→E · OE3→S · OE4→C + AlignmentScore.");
  }

  // --- 14 VI ---
  addTableSlide(
    pptx,
    "Variables independientes — factores de diseño del investigador (Tabla 5)",
    ["OE", "Factor (VI)", "Estados / alternativas"],
    [
      ["OE1", "Esquema de representación intermedia", "Paths/schemas vs behaviors/BO normalizados"],
      ["OE2", "Estrategia de schema matching", "Correspondencia estructural + umbral fijo"],
      ["OE3", "Técnica de similitud semántica", "Embeddings / ontología / híbrido"],
      ["OE4", "Pesos α, β, γ de agregación", "α+β+γ=1; taxonomía de tipologías"],
    ],
    "[9:15–9:55] Alex. VI = factores de diseño.",
    [0.9, 3.2, 8.3]
  );

  // --- 15 VD ---
  addTableSlide(
    pptx,
    "Variables dependientes — ratios por OE (Tabla 5 · Anexo D)",
    ["OE", "Ratio (VD)", "Rango / fórmula"],
    [
      ["OE1", "Completitud de normalización", "Elementos extraídos / esperados"],
      ["OE2", "StructuralScore (E)", "E ∈ [0, 1] — schema matching"],
      ["OE3", "SemanticScore (S)", "S ∈ [0, 1] — similitud semántica"],
      ["OE4", "CoverageScore (C); AlignmentScore", "C ∈ [0,1]; Score = αS+βE+γC"],
    ],
    "[9:55–10:35] Alex. VD = AlignmentScore + clasificación.",
    [0.8, 3.5, 8.2]
  );

  // --- 16 Metodología ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_CONTENT" });
    slide.addText("Cinco fases con verbos de diseño guían el procedimiento (§4.2)", { placeholder: "title" });
    addBullets(slide, [
      "Fase 1 · Diseñar entradas, scores y umbrales → modelo S/E/C documentado",
      "Fase 2 · Normalizar contrato + SD → representaciones comparables (OE1)",
      "Fase 3 · Emparejar estructuras → StructuralScore E (OE2)",
      "Fase 4 · Calcular similitud → SemanticScore S (OE3)",
      "Fase 5 · Integrar S,E,C → CoverageScore + AlignmentScore + tipologías (OE4)",
    ]);
    addNotes(slide, "[10:35–11:15] Alex. Partir por metodología (PI-14).");
  }

  // --- 17 Modelo S/E/C ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_FIGURE" });
    slide.addText("AlignmentScore integra S, E y C con pesos α, β, γ", { placeholder: "title" });
    addImage(slide, "Figura_03_AlignmentScore.png", { x: 0.65, y: 1.25, w: 12.03, h: 5.0 });
    addCaption(slide, "AlignmentScore = α·S + β·E + γ·C  →  Alta / Media / Baja / Nula");
    addNotes(slide, "[11:15–12:00] Alex. Shvaiko (2005) sustenta E.");
  }

  // --- 18 Matriz I ---
  addTableSlide(
    pptx,
    "Matriz de consistencia (I) — problema tecnológico y productos (Anexo C)",
    ["Fase", "Problema tecnológico", "Objetivo", "Producto verificable"],
    [
      [
        "Fase 1",
        "Método insuficiente para cuantificar alineación OpenAPI↔BIAN",
        "Diseñar modelo S/E/C y procedimiento",
        "Modelo metodológico documentado (Anexo C)",
      ],
      [
        "Fase 2",
        "Representaciones no comparables entre contrato y SD",
        "OE1 · Normalizar artefactos",
        "Representaciones normalizadas versionadas",
      ],
      [
        "Fase 3",
        "Sin StructuralScore sistemático",
        "OE2 · Emparejar estructuras",
        "Matriz correspondencias + E ∈ [0,1]",
      ],
    ],
    "[12:00–12:40] Alex. Matriz ≠ brecha Cap. 3.",
    [0.9, 3.5, 2.8, 5.3]
  );

  // --- 19 Matriz II ---
  addTableSlide(
    pptx,
    "Matriz de consistencia (II) — VI · VD · Hipótesis",
    ["Fase", "Variable independiente", "Variable dependiente", "Hipótesis (síntesis)"],
    [
      ["Fase 1", "Esquema S/E/C; pesos α,β,γ", "Definición scores", "H0: modelo S/E/C reproducible"],
      ["Fase 2", "Esquema intermedio", "Completitud normalización", "H1 (OE1)"],
      ["Fase 3", "Schema matching", "StructuralScore E", "H2 (OE2)"],
      ["Fase 4", "Similitud semántica", "SemanticScore S", "H3 (OE3)"],
      ["Fase 5", "Pesos α,β,γ", "C; AlignmentScore; clasif.", "H4 (OE4)"],
    ],
    "[12:40–13:20] Alex. Matriz completa en PDF Anexo C.",
    [0.9, 3.0, 3.2, 5.4]
  );

  // --- 20 Brecha ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_FIGURE" });
    slide.addText("La brecha V1–V5 (§3.6) no debe confundirse con la matriz", { placeholder: "title" });
    addImage(slide, "Figura_06_Brecha.png", { x: 0.65, y: 1.25, w: 12.03, h: 5.0 });
    addCaption(slide, "Brecha = estado del arte · Matriz = problema tecnológico del diseño");
    addNotes(slide, "[13:20–14:00] Jack: V1–V2 · Alex: V3–V5.");
  }

  // --- 21 Conclusiones ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_CONTENT" });
    slide.addText("El plan entrega diseño reproducible; Tesis 2 validará el artefacto", { placeholder: "title" });
    addBullets(slide, [
      "OpenAPI maduro técnicamente; falta procedimiento OpenAPI↔BIAN reproducible",
      "Objeto (contrato) + referencia (BIAN) + UA → scores S/E/C integrados",
      "OE1–OE4 encadenan transformaciones con productos verificables",
      "Matriz Anexo C alinea problema tecnológico, objetivos, VI/VD e hipótesis",
      "Guía 1 entrega diseño; Tesis 2: artefacto software y validación empírica",
    ]);
    addNotes(slide, "[14:00–14:30] Jack. Concluir con relaciones, no opinión.");
  }

  // --- 22 Recomendaciones ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_CONTENT" });
    slide.addText("Recomendaciones hacia Tesis 2 y gobernanza de APIs", { placeholder: "title" });
    addBullets(
      slide,
      [
        "Implementar artefacto software según procedimiento §4.2 (Tesis 2)",
        "Calibrar umbrales 0,80/0,60/0,40 con muestra bancaria representativa",
        "Validar hipótesis H1–H4 con contratos OpenAPI 3.x públicos (Anexo F)",
        "Integrar score en pipeline de gobernanza de APIs antes del despliegue",
      ],
      { size: 20 }
    );
    addNotes(slide, "[14:30–14:45] Alex. Breve; continuidad post-Guía 1.");
  }

  // --- 23 Referencias ---
  slideNum += 1;
  {
    const slide = pptx.addSlide({ masterName: "MASTER_CONTENT" });
    slide.addText("Referencias citadas en esta exposición", { placeholder: "title" });
    addBullets(
      slide,
      [
        "Casas, L., Pinto, S. & Silva, J. (2021). OpenAPI specification survey. J. Syst. Softw.",
        "Shvaiko, P. & Euzenat, J. (2005). A survey of schema-based matching approaches. J. Data Semant.",
        "Farzi, H. et al. (2021). BIAN service landscape. BIAN documentation.",
        "CMA (2016). Retail banking market investigation. UK Competition and Markets Authority.",
        "UK Treasury / TSB (2018). Independent review of TSB IT failure.",
      ],
      { size: 20 }
    );
    addNotes(slide, "[14:45–15:00] Jack. PDFs Casas y Shvaiko abiertos. ¿Preguntas?");
  }

  return pptx.writeFile({ fileName: OUTPUT });
}

build()
  .then(() => {
    const stat = fs.statSync(OUTPUT);
    console.log(`Generado: ${OUTPUT}`);
    console.log(`Tamaño: ${(stat.size / 1024).toFixed(0)} KB`);
  })
  .catch((err) => {
    console.error(err);
    process.exit(1);
  });
