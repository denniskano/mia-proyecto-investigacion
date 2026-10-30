# Retroalimentación docente — Grupo 9.2 (PI-11 + Clase 04)

**Fuentes:**
- Transcripción `transcriptions/MAE SE-A PI-11.txt` (sesión adquisición de datos · exposición Jack Paitan / Alex Mancilla)
- PDF `clases/class-04/class 04. adquisicion de datos.pdf` (Unidad 3 · medición, señales, experimento, población/muestra, protocolo)

**Complementa:** `fase-b-planteamiento/FEEDBACK_DOCENTE_PI10.md`  
**Integrantes:** Alex Mancilla · Jack Paitan  
**Última actualización:** 2026-07-02

> **Contexto docente:** El informe Guía 1 entregado **aún no fue revisado** en detalle, pero el docente anticipa que **habrá que reestructurar** el documento según los niveles de investigación y la separación problemática → diagnóstico → problema tecnológico. La guía institucional es **lo mínimo**; el curso exige más.

---

## 1. Mensajes centrales del docente

| # | Idea del docente | Implicación para Grupo 9.2 |
|---|------------------|----------------------------|
| M1 | **No hay un solo problema**; hay varios según el nivel (real → subyacente → tecnológico → artefacto → operación) | Separar claramente problemática, abstracción y problema tecnológico en Cap. 1 |
| M2 | El problema del **estado del arte (Cap. 3)** ≠ el problema de la **matriz de consistencia**; están vinculados pero **no son lo mismo** | Matriz = problema **tecnológico** (construir método de alineación); brecha V1–V5 ≠ fila experimental |
| M3 | En la maestría se resuelve el **problema tecnológico** (diseño + construcción + verificación del artefacto), **no** la realidad bancaria | Coherente con §1.6: plan = diseño; operación en producción = fuera de alcance |
| M4 | El problema se **resuelve en la necesidad del artefacto** (diseño/construcción/verificación), **no** en la operación en producción | Cap. 4 = diseño reproducible; Tesis 2 = construcción y evaluación |
| M5 | **Objetivo superior** = consecuencia en el mundo real **si** el artefacto existiera; **objetivo de investigación** = objetivo **técnico** | Añadir objetivo superior (impacto) distinto del OG tecnológico en Cap. 2 |
| M6 | **Problemática** = síntomas con **casos reales concretos** (noticias, costos, tiempos); no definir por **ausencia** («no siguen BIAN») | Reforzar §1.2 con casuística empírica y cifras donde sea posible |
| M7 | **Diagnóstico / situación subyacente** = abstracción ontológica del objeto; **ontología interna** (no se publica), texto sí en el orden de conceptos | Mantener mapa ontológico del equipo; redactar §1.1 y §1.4 en ese orden |
| M8 | **Variables independientes → factores**; **variables dependientes → ratios** | ✅ Anexo C/D/E · Cap. 2 · 2026-07-02 |
| M9 | **Parámetros** ≠ factores: organizan el muestreo pero no son manipulados como factores experimentales | Cap. 4: distinguir parámetros (p. ej. versión OpenAPI) de factores (p. ej. pesos α, β, γ) |
| M10 | Adquisición de datos, experimento y protocolo orientan **Tesis 2**; hay que anticiparlos aunque Guía 1 no lo pida todo | Cap. 4 + anexos: bosquejar protocolo y fuentes de contratos OpenAPI/BIAN |

---

## 2. Retroalimentación directa al Grupo 9.2 (PI-11 en clase)

### A. Problemática y niveles del problema

| ID | Comentario docente (Jack/Alex) | Estado actual | Acción |
|----|-------------------------------|---------------|--------|
| P1 | No definir el dolor como **ausencia** | ✅ §1.2 casos observables | — |
| P2 | **Números / estadísticas** en problemática | ✅ TSB, CMA, cifras | — |
| P3 | **Caso concreto** integración bancaria | ✅ §1.2 | — |
| P4 | **Problema abstracto** = dos estructuras jerárquicas | ✅ §1.3 subyacente | — |
| P5 | **Problema tecnológico** en matriz | ✅ Anexo C | — |
| P6 | **Tres niveles** conversan | ✅ §1.2 → §1.3 | — |

### B. Objeto de estudio y unidad de análisis

| ID | Comentario docente | Estado actual | Acción |
|----|-------------------|---------------|--------|
| O1 | Objeto ≠ estándar OpenAPI genérico; objeto = **contratos OpenAPI bancarios** concretos | ✅ §1.4 | Mantener |
| O2 | Cada artefacto necesita **ID identificable** | ✅ §1.4 · §4.3 | Mantener convención ID |
| O3 | Unidad mínima al alinear: **contrato OpenAPI bancario** ↔ **Service Domain BIAN** | ✅ §1.4 Tabla 1.4 | Mantener |
| O4 | Describir el elemento con **ejemplos, casos, papers**; ahí entra la **ontología** | ✅ Anexo F · §3.3 glosario | Ontología interna del equipo: actualizar y no publicar |
| O5 | Objeto = lo que **pasa por el artefacto**; salida = **grado/porcentaje de alineamiento** (+ clasificación) | ✅ §1.4 · modelo S/E/C | Mantener en Cap. 2 y exposición |

### C. Unidad de análisis · población · muestra (Clase 04 + PI-11)

Definición del curso: **población** = conjunto completo de **mediciones** sobre UA; **muestra** = subconjunto observado.

| Concepto | En Grupo 9.2 |
|----------|--------------|
| **UA** | Par comparable **endpoint/operation/schema ↔ Behavior/BusinessObject** (instancia de medición dentro de un contrato × SD) |
| **Atributos medidos** | Correspondencia estructural (E), semántica (S), cobertura (C) |
| **Población (teórica)** | Todas las instancias de medición posibles sobre todos los pares **contrato OpenAPI bancario × Service Domain BIAN** del universo definido |
| **Muestra (empírica)** | Ilustración Anexo F; validación empírica **fuera de alcance Guía 1** (§1.6) |
| **Señal / dato** | Representación capturada del objeto: **archivo OpenAPI (YAML/JSON)** + **extracto del SD BIAN** (no sensores físicos; registros/documentos) |
| **Instrumento de medición** | Pipeline del artefacto (normalización + cálculo S/E/C), no encuesta ni sensor |

⏳ **Pendiente Cap. 4:** ~~tabla estilo Clase 04~~ ✅ `tab04-adquisicion-datos.tex` · §4.3 (2026-07-02).

---

## 3. Mapeo docente → secciones del plan de tesis

Según PI-11, la **guía mínima** se enriquece así:

| Nivel / concepto (curso) | Dónde redactarlo en el plan | Estado |
|--------------------------|----------------------------|--------|
| **Situación real / problemática** (síntomas, casos, cifras) | Cap. 1 §1.2 Problemática | ✅ TSB, CMA, Casas (2026-05-28) |
| **Situación subyacente** (objeto de estudio, ontología, caracterización) | Cap. 1 §1.1 + §1.4 + Cap. 3 §3.2 bases conceptuales | ✅ §1.4 marcado explícitamente (2026-07-02) |
| **Situación tecnológica** (datos, señales, registros) | Cap. 4 metodología · fuentes de datos | ✅ §4.3 adquisición (2026-07-02) |
| **Necesidad del artefacto** (diseño del modelo/procedimiento) | Cap. 2 objetivos · Cap. 4 · Anexo C matriz | ✅ |
| **Operación del artefacto** (verificación, no producción) | Fuera de Guía 1 (§1.6) | ✅ delimitado |
| **Factores** (antes «variables independientes») | Cap. 2 §2.4 · Anexo C/D · Anexo E factorial | ✅ 2026-07-02 |
| **Ratios / variables dependientes** (resultados del experimento) | Cap. 2 · Anexo D operacionalización | ✅ 2026-07-02 |
| **Diseño factorial / experimental** | Cap. 2 §2.5 · Anexo E | ✅ Anexo E: no aplica Guía 1; factores documentados |
| **Protocolo de experimentación** | Cap. 4 §4.2 | ✅ bosquejo delimitación (no ejecución) |
| **Estado del arte (brecha)** | Cap. 3 §3.5–§3.6 | ✅ · no confundir con problema tecnológico de matriz |
| **Objetivo superior** (impacto en mundo real) | Cap. 2 (nuevo párrafo o subsección) | ✅ 2026-05-28 |

**Nota docente:** La situación subyacente **no es copiar** el marco teórico; es **abstraer** y enfocar al caso. Los conceptos definidos ahí **sí** pasan después al marco teórico (§3.2–§3.4).

---

## 4. Contenido Clase 04 (PDF) aplicado al proyecto

### 4.1 Medición

| Componente (PDF) | Aplicación OpenAPI–BIAN |
|------------------|-------------------------|
| Variable a medir | Grado de alineación (S, E, C, AlignmentScore) |
| Instrumento | Procedimiento + implementación del modelo (artefacto) |
| Unidad de medida | Score normalizado [0, 1]; clasificación ordinal |
| Escala | Razón (0–1) + nominal ordinal (Alta/Media/Baja/Nula) |
| Frecuencia | Por instancia evaluada (contrato × SD × par UA) |
| Error | Amenazas a validez (Cap. 4): parsing, ambigüedad léxica, cobertura parcial |

### 4.2 Señales y adquisición

- En este proyecto la «señal» no es una foto ni una serie temporal: es la **representación digital del contrato y del SD BIAN** (YAML/JSON + modelo de referencia).
- Cada registro debe tener **ID** (docente PI-11) + contenido (señal) + metadatos (fuente, versión, dominio).
- Fuentes posibles: catálogos públicos OpenAPI bancarios, artefactos BIAN, repositorios de referencia, contratos sintéticos documentados (Anexo F).

### 4.3 Experimento (Tesis 2)

El docente pide anticipar en el plan:

1. **Factores** a manipular (p. ej. pesos α, β, γ; umbral de clasificación; técnica de matching semántico).
2. **Ratios / variables dependientes** (p. ej. AlignmentScore medio, precisión vs. juicio experto, correlación S vs. E).
3. **Parámetros controlados** (versión OpenAPI 3.x, dominio SD, idioma de descripciones).
4. **Parámetros no controlados** (calidad redaccional del contrato, madurez BIAN del banco).
5. **Tamaño de muestra** de contratos/pares UA (criterio de representatividad; fórmula Clase 04 si aplica encuesta experta).
6. **Etiquetado:** juicio experto o ground truth documentado para pares OpenAPI↔BIAN (ex ante o ex post).
7. **Protocolo** (7 pasos PDF): instrumento DAQ → infraestructura → condiciones captura → tamaño muestra → etiquetado → ética/legal (sin datos personales en contratos) → evaluación desempeño.

### 4.4 Ética

- Contratos bancarios pueden contener datos sensibles: usar **ejemplos anonimizados/sintéticos** o públicos (Anexo F).
- Ley N° 29733: no exponer identificadores de clientes en APIs reales.

---

## 5. Coherencia con PI-10 (sin contradicción)

| Tema | PI-10 | PI-11 | Resolución |
|------|-------|-------|------------|
| Alcance Guía 1 | Diseño procedimiento; sin experimentación en plan | Anticipar experimento para Tesis 2 | Cap. 4 describe diseño + **plan** de validación futura |
| Matriz 5 fases | Transformadores S/E/C | Problema matriz = tecnológico | ✅ mantener |
| Objeto / UA | Contrato vs. par endpoint↔BIAN | ID por instancia; ontología | ✅ refinar IDs y ontología interna |
| Fase 6 / piloto | Eliminado | — | ✅ sin cambio |

---

## 6. Citas textuales de referencia

**PI-11 (sesión):**
- «El problema del estado del arte **no es el mismo** que… la matriz de consistencia.»
- «**Dime números, dime estadísticas.**»
- «Busquen un **caso, una situación real, concreta**… una noticia.»
- «El problema principal [matriz] es un **problema tecnológico**… **no existe un método** que haga ese alineamiento.»
- «**Contrato OpenAPI bancario** y **Service Domain de BIAN**… ese va a ser tu elemento.»
- «La ontología **nunca la muestras**, solamente es para ustedes.»
- «Ustedes **no van a resolver ningún problema en la realidad**… van a entregar un **modelo**.»
- «**Objetivo superior**… si yo logro construir el artefacto, ¿qué va a pasar en el mundo?»
- «Variables independientes → **factores**… variables dependientes → **ratios**.»
- «Hay que armar un **protocolo**.»

**Clase 04 (PDF):**
- «Población = conjunto completo de **medidas**… de **unidades de análisis**.»
- «Un experimento… **observar, medir y comprobar una hipótesis**.»
- «Protocolo: instrumento → infraestructura → condiciones → muestra → etiquetado → ética → desempeño.»

---

## 7. Seguimiento de pendientes (priorizado)

### P0 — Reestructuración Cap. 1 (feedback PI-11)

| ID | Tarea | Archivo LaTeX | Estado |
|----|-------|---------------|--------|
| P0.1 | §1.2: caso real + cifras/tiempos/costos integración | `02-problematica.tex` | ✅ 2026-05-28 |
| P0.2 | §1.3: etiquetar explícitamente real / abstracto / tecnológico | `03-planteamiento.tex` | ✅ 2026-05-28 |
| P0.3 | Cap. 2: **objetivo superior** (impacto) vs. OG técnico | `cap02-objetivos/` | ✅ 2026-05-28 |
| P0.4 | Verificar Anexo C: problema filas = tecnológico | `anexo-c.tex` + Excel | ✅ 2026-05-28 |

### P1 — Cap. 4 metodología (Fase F + PI-11)

| ID | Tarea | Estado |
|----|-------|--------|
| P1.1 | Tabla adquisición datos (objeto, UA, señal, instrumento, muestra) | ✅ 2026-07-02 |
| P1.2 | Distinción factores / parámetros / ratios | ✅ Cap. 2, §4.3, Anexo D |
| P1.3 | Bosquejo protocolo experimentación (Tesis 2) | ✅ §4.2 |
| P1.4 | Fuentes de contratos OpenAPI + criterios inclusión muestra | ✅ §4.3 |
| P1.5 | Amenazas a validez vinculadas a medición | ✅ §4.7–§4.8 |

### P2 — Terminología y anexos

| ID | Tarea | Estado |
|----|-------|--------|
| P2.1 | Renombrar VI → **factores**, VD → **ratios** en Anexo C/D/E | ✅ 2026-07-02 |
| P2.2 | Convención ID instancias (contrato × SD × par) | ✅ §1.4 · §4.3 |
| P2.3 | Ontología interna del equipo (repo privado / notas; no en PDF) | ⏳ notas internas |

### P3 — Ya alineado (mantener)

- Objeto = contrato OpenAPI bancario; BIAN = referencia ✅  
- UA = par endpoint/schema ↔ behavior/business object ✅  
- Matriz 5 fases transformadoras ✅  
- Experimentación/construcción fuera de alcance Guía 1 ✅  
- Anexo F ejemplos concretos ✅  

---

## 8. Respuestas rápidas para el curso (Grupo 9.2)

**¿En qué nivel se resuelve el problema?**  
En la **necesidad del artefacto** (diseño, construcción y verificación del método de alineación), no en la operación en producción bancaria.

**¿Cuál es la UA?**  
Cada **par comparable** OpenAPI ↔ BIAN dentro de la evaluación de un contrato contra un Service Domain.

**¿Cuál es la población?**  
Todas las **mediciones** de alineación posibles sobre esas UA en el universo de contratos bancarios emparejados con SD BIAN.

**¿Cuál es la muestra?**  
Los contratos/pares que se usarán en la validación empírica (Tesis 2); ilustración actual: Anexo F.

**¿Cuál es la señal/dato?**  
Archivos **OpenAPI + extracto BIAN** (representación documental, no sensor físico).

**¿Objetivo superior (ejemplo)?**  
Si el artefacto existiera, los equipos de arquitectura/API podrían **cuantificar y gobernar** la coherencia OpenAPI–BIAN antes del despliegue, reduciendo retrabajo en integraciones.

---

*Documento interno Grupo 9.2 — acta PI-11 + Clase 04. Complementa `FEEDBACK_DOCENTE_PI10.md`, checklists por fase y `planificacion/PLAN_ELABORACION_PLAN_TESIS.md`.*
