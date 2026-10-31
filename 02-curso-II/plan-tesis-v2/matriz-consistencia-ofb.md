# Matriz de consistencia — Plan v2 (piloto OFB)

**Grupo 10** · Alex Mancilla Antay · Jack Paitan Cano  
**Formato:** 8 columnas institucionales (Sesión 2 / matriz v2).  
**Objeto (tesis, se mantiene):** contratos OpenAPI **bancarios** frente a Service Domains BIAN.  
**Muestra (piloto MIA 403):** catálogo **Open Finance Brasil**.

**Título del estudio:** Alineación entre contratos OpenAPI bancarios y modelos de referencia BIAN, mediante análisis estructural y similitud semántica.

**Objetivo general (se copia en la Fase 1; las demás filas indican cómo contribuyen):**  
Calcular, sobre cada instancia `contrato OpenAPI bancario × Service Domain BIAN`, el AlignmentScore ∈ [0, 1] y la clasificación (Alta / Media / Baja / Nula), mediante S, E y C. En este curso la verificación se hace sobre el corpus piloto (38 APIs OFB + 3 SD BIAN v14).

---

## Fase 1 — Marco del plan (diseño heredado + reencuadre OFB)

| Columna | Contenido |
|---------|-----------|
| **1. Problema de estudio** | No hay un procedimiento *ejecutado* que cuantifique en qué medida un contrato **OpenAPI bancario** se alinea con un SD BIAN ni bajo qué tipologías se desalinea. Guía 1 diseñó el modelo; Guía 2 lo mide primero en el piloto OFB. |
| **2. Objetivo general** | Calcular AlignmentScore y clasificación por instancia `contrato bancario × SD BIAN` (fórmula αS+βE+γC; umbrales 0,80 / 0,60 / 0,40). |
| **3. Objetivos específicos** | Cerrar el marco: entradas contrato+BIAN, componentes S/E/C, pares declarados del piloto I1–I6, criterios de verificación. |
| **4. Hipótesis** | Un modelo S/E/C permite un score reproducible e interpretable entre OpenAPI bancario y BIAN. |
| **5. Variables** | VI: esquema S/E/C y pesos. VD (artefacto): AlignmentScore + nivel. Control: OpenAPI 3.x; BIAN v14; **muestra del curso = OFB**. |
| **6. Metodología** | Investigación tecnológica / design science. Fase 1 = diseño (hecho). Fases 2–5 = ejecución (este curso). |
| **7. Técnicas e instrumentos** | Revisión documental; matriz 8 cols; `PLAN_TESIS_V2.md`; inventario OFB. |
| **8. Resultados esperados** | Plan v2 + pares I1–I6 + protocolo; no aún los scores globales. |

## Fase 2 — OE1 Adquirir y normalizar

| Columna | Contenido |
|---------|-----------|
| **1. Problema** | REST OFB (mayoría GET) y vista de negocio BIAN (CR/BQ, mayoría PUT) no son comparables en crudo. |
| **2. OG** | Contribuye: habilitar mediciones sobre representaciones comparables. |
| **3. OE** | **OE1** — Adquirir YAML OFB y BIAN versionados y normalizarlos (parser → CSV). |
| **4. Hipótesis** | **H1:** la normalización habilita el cálculo sistemático de S, E y C. *(piloto: soportada a nivel de extracción)* |
| **5. Variables** | VI: esquema intermedio tabular. **VD ratio OE1:** completitud (extraídos/esperados). Control: versiones congeladas. |
| **6. Metodología** | Fase 2. Universo: 38 APIs OFB + 3 SD. Muestra: 7 instancias (I1–I6, I3 desdoblada). |
| **7. Técnicas** | `procesar_openapi.py`; OpenAPI 3.x; `$ref` anidados; metadatos `{OFB\|BIAN}_{api}_{versión}`. |
| **8. Resultados** | 41 contratos, 235 ops, 6 746 props, 10 906 textos; informe de completitud por contrato. |

## Fase 3 — OE2 Emparejar estructuras

| Columna | Contenido |
|---------|-----------|
| **1. Problema** | Se desconocen las correspondencias path/operation/schema OFB ↔ Behavior/BO/BQ (P1). |
| **2. OG** | Contribuye: cuantificar **E**. |
| **3. OE** | **OE2** — Matriz de pares y StructuralScore E ∈ [0, 1] en I1–I6. |
| **4. Hipótesis** | **H2:** el schema matching distingue correspondencia REST ↔ CR/BQ (sin exigir el mismo verbo HTTP). |
| **5. Variables** | VI: estrategia (nombre, ruta, HTTP relajado, profundidad). **VD ratio:** E. Control: umbral Jaccard fijo; mismo OE1. |
| **6. Metodología** | Fase 3. Greedy 1–1 operación OFB → Behavior BIAN. |
| **7. Técnicas** | Schema matching (Shvaiko y Euzenat, 2005). **No** ML supervisado. Baseline token en semana 8. |
| **8. Resultados** | `pares_estructurales.csv` + E por instancia. |

## Fase 4 — OE3 Similitud semántica

| Columna | Contenido |
|---------|-----------|
| **1. Problema** | Equivalencia de significado entre términos OFB y conceptos BIAN (P2). BIAN duplica summary=description; 61,9 % de propiedades del consolidado sin description (BIAN 90,4 %; OFB 38,1 %). |
| **2. OG** | Contribuye: cuantificar **S**. |
| **3. OE** | **OE3** — SemanticScore S ∈ [0, 1] sobre los pares de OE2. |
| **4. Hipótesis** | **H3:** la similitud discrimina alineación vs. desalineación de modelado (p. ej. *account* vs. *SavingsAccountFacility*). |
| **5. Variables** | VI: TF-IDF (v0) / embeddings (v1). **VD ratio:** S. Control: un texto BIAN si summary=description; umbral 0,55. |
| **6. Metodología** | Fase 4. S se calcula **sobre pares OE2**, no en búsqueda libre. |
| **7. Técnicas** | Jaccard/TF-IDF; luego embeddings + coseno (Chandrasekaran y Mago, 2022). |
| **8. Resultados** | `pares_semanticos.csv` + S por instancia. |

## Fase 5 — OE4 Integrar y clasificar

| Columna | Contenido |
|---------|-----------|
| **1. Problema** | Falta el indicador integrado y la escala interpretable por instancia (P3, P4). El catálogo OFB (loans, cards) no tiene SD en el piloto. |
| **2. OG** | Contribuye: entregar la **VD del artefacto**. |
| **3. OE** | **OE4** — C + AlignmentScore + nivel + tipologías. |
| **4. Hipótesis** | **H4:** αS+βE+γC (1/3) produce un AlignmentScore clasificable por los umbrales §1.4. La sensibilidad de pesos se reporta como análisis, no como hipótesis adicional. |
| **5. Variables** | VI: α, β, γ. **VD artefacto:** AlignmentScore + Alta/Media/Baja/Nula. **VD ratio:** C. Control: umbrales fijos; catálogo CR+BQ+BO del SD. |
| **6. Metodología** | Fase 5. C no se calcula sobre las 38 APIs como un solo contrato. |
| **7. Técnicas** | Agregación lineal; reglas de umbral; Tabla 2 (tipologías); análisis de sensibilidad. |
| **8. Resultados** | Tabla I1–I6; informe de gaps (loans/cards); amenazas a la validez. |

---

## Lectura oral (defensa semana 9)

Orden por fila: Problema → OE → Resultado esperado → Hipótesis y variables → Técnicas.

Frase de ancla: *parser al 100 % no implica AlignmentScore Alto*.  
Frase de objeto: *la tesis es OpenAPI bancario ↔ BIAN; OFB es el piloto, no el objeto*.
