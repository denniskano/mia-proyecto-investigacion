# Libreto completo — Exposición Plan de Tesis Grupo 9.2

**Presentación oficial:** `Exposicion_Plan_Tesis_Grupo9.2-beamer.pdf` (**22 slides**)  
**Duración:** 15:00 (**19 slides orales**; **omitir slides 2, 3 y 4**)  
**Integrantes:** Alex Mancilla · Jack Paitan  
**Regla:** señalar la diapositiva al hablar. El público no conoce el plan: **explicar cada sigla la primera vez que aparezca**.

---

## Antes de empezar

- [ ] PDF **Casas et al. (2021)** y **Shvaiko & Euzenat (2005)** abiertos en pestañas
- [ ] PDF del plan con **Anexo C** (matriz) listo por si preguntan detalle
- [ ] Navegación: slide **1 → 5** (saltar **2** Fuentes, **3** Intro escrita, **4** Ontología)

---

## SLIDE 1 · 0:00–0:45 · **Jack**

**Diapositiva:** Título + IEEE/ACM

> Buenas [tardes/noches]. Somos el Grupo 9.2 — Alex Mancilla y Jack Paitan.  
>  
> Nuestro plan de tesis estudia qué tan bien **coinciden** dos descripciones del mismo negocio bancario: por un lado, el **contrato OpenAPI** — es decir, el archivo **YAML o JSON** con el que el banco **publica** su API REST (rutas, operaciones y esquemas de datos); por otro, el **Service Domain BIAN** — un bloque del modelo de referencia **BIAN** (*Banking Industry Architecture Network*), que estandariza capacidades bancarias como pagos o cuentas.  
>  
> Para medir esa coincidencia proponemos tres puntajes entre 0 y 1: **S** (*SemanticScore*, similitud de significado), **E** (*StructuralScore*, correspondencia estructural) y **C** (*CoverageScore*, cobertura de operaciones), integrados en un **AlignmentScore** ponderado.  
>  
> Es una **investigación tecnológica** en la línea de **design science** (*ciencia del diseño*): en esta **Guía 1** entregamos el **diseño** del procedimiento; la implementación y validación empírica quedan para **Tesis 2**.  
>  
> Clasificamos el tema en **IEEE: Knowledge Representation** y **ACM: Semantic networks**, porque comparamos dos **representaciones formales** — la técnica (OpenAPI) y la de negocio (BIAN).

**Acción:** señalar título y las dos líneas de clasificación IEEE/ACM.

---

## SLIDE 2 · ⛔ NO EXPONER

**Diapositiva:** Fuentes / Drive + Zotero (punto rojo)

> ⛔ **No exponer.** Solo cumplimiento de formato. Avanzar a slide 5.

**Acción:** pulsar siguiente sin hablar.

---

## SLIDE 3 · ⛔ NO EXPONER

**Diapositiva:** Introducción §1.1 (punto rojo)

> ⛔ **No exponer.** Texto de respaldo del Capítulo 1. Avanzar a slide 5.

**Acción:** pulsar siguiente sin hablar.

---

## SLIDE 4 · ⛔ NO EXPONER

**Diapositiva:** Ontología (figura informe · punto rojo)

> ⛔ **No exponer.** Figura de respaldo del informe. Avanzar a slide 5.

**Acción:** pulsar siguiente sin hablar.

---

## SLIDE 5 · 0:45–1:35 · **Jack**

**Diapositiva:** Problemática — situación real (figura)

> Entramos en la **problemática del sector** — Capítulo 1, sección 1.2: la **situación real** donde se observa el problema. Esto **no** es el problema tecnológico de nuestro artefacto ni la matriz del Anexo C; es el **contexto bancario** que motiva la investigación.  
>  
> **¿Dónde ocurre?** En el ecosistema de **banca digital**: el banco expone APIs, entran **fintechs** (empresas tecnológicas financieras) y, en muchos países, regímenes de **open banking** (*banca abierta*) — regulación que obliga o incentiva a compartir datos y servicios vía APIs estandarizadas. Un ejemplo citado en el plan es la investigación de la **CMA** (*Competition and Markets Authority*, la autoridad de competencia del **Reino Unido**) en **2016**, que impulsó el open banking británico al concluir que la competencia en servicios bancarios dependía de APIs más abiertas.  
>  
> **¿Quiénes intervienen?** Equipos de **arquitectura**, **integración**, **gobernanza de APIs** y **socios externos** que consumen o publican contratos.  
>  
> Los **síntomas concretos** — retrabajo, fragmentación — los veremos en la siguiente diapositiva. Aquí la idea es: hay **dolor observable** en el sector; eso **motiva** medir coherencia **antes** de integrar sistemas, aunque nuestro plan de Guía 1 solo **diseña** cómo medirla, no la resuelve en producción.

**Acción:** señalar en la figura el contexto sectorial y los actores al nombrarlos.

---

## SLIDE 6 · 1:35–2:25 · **Jack**

**Diapositiva:** Síntomas, dolor y estadísticas (2 figuras)

> En la misma problemática, los **síntomas** que documentamos son tres.  
>  
> Primero, **fragmentación semántica**: distintos equipos nombran igual concepto de negocio de formas distintas en sus APIs. Segundo, **retrabajo** en adaptadores e integraciones cada vez que cambia el contrato. Tercero, **deriva** entre lo que el negocio entiende y lo que la capa REST expone en cada release.  
>  
> Un caso sectorial fuerte es el banco **TSB** (*Trustee Savings Bank*, Reino Unido): en **2018** sufrió una **caída masiva de servicios** tras una migración de sistemas; en el plan lo usamos como ejemplo de riesgo cuando la capa API **pierde trazabilidad** con el modelo de negocio. *(Señalar la figura del caso TSB.)*  
>  
> En el estado del arte, **Casas, Pinto y Silva (2021)** revisaron **47 artículos** sobre OpenAPI. El **68 %** propone herramientas y el **43 %** mejora documentación, pero **ningún artículo** enlaza OpenAPI con modelos **BIAN** de forma sistemática — ahí está el vacío que nuestro plan aborda. *(Señalar la cifra 68 % en la figura.)*  
>  
> Si el docente pide el paper: abrimos el PDF de Casas y señalamos el apartado del mapeo sistemático.

**Acción:** señalar **ambas** figuras; decir «sesenta y ocho por ciento» con claridad.

---

## SLIDE 7 · 2:25–3:15 · **Jack**

**Diapositiva:** Objeto de estudio — situación subyacente (figura)

> Subimos un nivel conceptual: la **situación subyacente** (§1.4). La **causa abstracta** de los síntomas es la **desalineación** entre dos jerarquías que deberían contar la misma historia:  
>  
> — el **contrato OpenAPI**: *paths* (rutas), *operations* (verbos HTTP) y *schemas* (estructuras de datos);  
> — el **Service Domain BIAN**: *behaviors* (comportamientos de negocio), *business objects* (objetos de negocio) y sus relaciones.  
>  
> Nuestro **objeto de estudio** es el **contrato OpenAPI bancario completo** — el archivo que el banco publica. **No** evaluamos código en ejecución ni tráfico en tiempo real.  
>  
> **BIAN** actúa como **modelo de referencia**: no es lo que medimos, sino el **patrón** con el que comparamos si la API expuesta refleja la misma capacidad de negocio.

**Acción:** señalar en la figura la capa técnica (OpenAPI) frente a la capa de negocio (BIAN).

---

## SLIDE 8 · 3:15–4:00 · **Jack**

**Diapositiva:** Objeto real — taxonomía y ciclo de vida

> El **objeto de estudio real** existe **independiente del investigador**: es el contrato que el banco **publica** en su repositorio de APIs.  
>  
> En el plan lo clasificamos así: contratos **OpenAPI 3.x**, en dominios como **pagos**, **cuentas** o **préstamos**, con **versiones** trazables (v1, v2…).  
>  
> También distinguimos el **ciclo de vida del contrato** — diseño, revisión, publicación, consumo por terceros — del ciclo de vida del **proceso bancario** completo. Nosotros medimos coherencia en el **documento** del contrato, típicamente **antes del despliegue**.  
>  
> Ejemplos concretos de contratos de referencia están en el **Anexo F** del informe escrito.

**Acción:** señalar taxonomía y ciclo de vida en la figura si están visibles.

---

## SLIDE 9 · 4:00–4:45 · **Alex**

**Diapositiva:** Instrumento y objeto modelado (figura)

> Para **obtener datos** del contrato usamos un **instrumento de investigación documental** — no encuestas ni sensores: un **procedimiento reproducible** sobre archivos.  
>  
> El flujo es: **(1)** un *parser* que lee OpenAPI 3.x y extrae la estructura; **(2)** un extracto del **Service Domain BIAN** emparejado; **(3)** **normalización** (objetivo **OE1**) para dejar ambos en representaciones comparables; **(4)** **schema matching** — técnica de emparejamiento entre esquemas, basada en **Shvaiko & Euzenat (2005)** — para el score **E**; **(5)** **similitud semántica** para el score **S**.  
>  
> El **objeto modelado** son matrices de correspondencia y puntajes en la escala **[0, 1]**.  
>  
> En la siguiente diapositiva mostramos **dos casos concretos** y la **escala de clasificación** del artefacto.

**Acción:** recorrer con el cursor el flujo de la figura de izquierda a derecha.

---

## SLIDE 10 · 4:45–5:30 · **Alex**

**Diapositiva:** Casos A/B + estados (figura)

> **Caso A — score semántico (S):** en OpenAPI aparece `POST /payments` con el schema `PaymentRequest`; en BIAN, los behaviors `InitiatePayment` y el objeto `PaymentOrder`. Representan el **mismo rol de negocio** con **nombres distintos** → el **SemanticScore S** sería **bajo**. *(Señalar columnas OpenAPI y BIAN.)*  
>  
> **Caso B — score de cobertura (C):** el contrato solo expone `GET /payments/{id}` (consultar un pago), pero BIAN define también iniciar, confirmar y cancelar pagos. Hay **operaciones de negocio sin equivalente** en la API → **C** bajo aunque la estructura (**E**) parezca correcta.  
>  
> El artefacto clasifica el contrato en **Alta, Media, Baja o Nula** según umbrales **provisionales** del diseño: **0,80 / 0,60 / 0,40** — convención para la Guía 1; la calibración con datos reales de bancos queda para **Tesis 2**.  
>  
> Cada medición se hace por **unidad de análisis**: un par comparable dentro del contrato frente a un Service Domain, identificado como `{fuente}_{service-domain}_{versión}`. El puntaje global se interpreta por **contrato × Service Domain**.

**Acción:** señalar casos A y B y la escala Alta–Nula.

---

## SLIDE 11 · 5:30–6:20 · **Alex**

**Diapositiva:** Problema tecnológico + P1–P4 (§1.3)

> Hasta aquí Jack nos mostró el **dolor del sector** — la problemática real — y yo mostré **cómo mediríamos** casos concretos con S, E y C. Ahora cambiamos de registro: esta diapositiva es el **problema tecnológico** del plan, sección **1.3**. Es el problema que aparece en la **matriz de consistencia** del Anexo C — no confundirlo con la slide 5 ni con la brecha de la slide 19.  
>  
> Señalo primero el recuadro dorado de **recordatorio**: **«Problemática del sector ≠ problema tecnológico del artefacto»**. En palabras simples: que exista fragmentación en los bancos **motiva** la investigación, pero **no es** el problema que nuestro procedimiento resuelve directamente. Nuestro problema tecnológico es otro: **cómo diseñar un método reproducible** para cuantificar la alineación entre un contrato OpenAPI y un Service Domain BIAN.

**El problema tecnológico en una frase**

> Formulamos que los enfoques actuales son **insuficientes o no adaptados** a este par específico OpenAPI↔BIAN. Quiero que quede claro: **no** decimos «no existe ningún método». Sí existen revisión manual entre equipos, herramientas genéricas de *schema matching* — del tipo que revisa **Shvaiko y Euzenat en 2005** — y trabajos sobre OpenAPI como el mapeo de **Casas et al. en 2021**. Lo que **falta** es un procedimiento **documentado, reproducible y orientado** a contratos bancarios OpenAPI frente a dominios BIAN, que entregue los scores S, E y C de forma sistemática.

**Las cuatro preguntas P1–P4**

> Para no dejar el problema en abstracto, lo descomponemos en **cuatro preguntas de diseño**, P1 a P4, que ven en el panel. Las señalo una por una:  
>  
> **P1 — Matching estructural:** ¿cómo emparejar de forma sistemática paths, operaciones y schemas del contrato con behaviors y objetos de negocio del Service Domain? Esa pregunta alimenta el **StructuralScore E** — la dimensión «¿encajan las piezas?».  
>  
> **P2 — Similitud semántica:** aunque la estructura coincida, ¿los nombres y conceptos significan lo mismo? Recuerden el **Caso A** de la slide anterior: mismos roles de negocio, nombres distintos. Esa pregunta alimenta el **SemanticScore S**.  
>  
> **P3 — Cobertura:** ¿qué proporción del Service Domain BIAN queda reflejada en el contrato? Si faltan operaciones — como en el **Caso B** — el contrato puede ser estructuralmente correcto pero **incompleto**. Esa pregunta alimenta el **CoverageScore C**.  
>  
> **P4 — Score integrado:** ¿cómo combinar S, E y C en un **AlignmentScore** único, interpretable, y cómo clasificar el contrato en **Alta, Media, Baja o Nula** en la escala [0, 1]? Aquí entran los pesos **α, β, γ** que verán en las slides de variables.

**El artefacto que respondemos diseñar**

> El **artefacto** que el plan se compromete a **diseñar** — no a implementar en producción en Guía 1 — es la **unión de dos piezas**: un **procedimiento** paso a paso (normalizar → emparejar → calcular similitud → integrar) y el **modelo S/E/C** con su **AlignmentScore** y reglas de clasificación. El producto es **documentación verificable**; el software ejecutable queda para **Tesis 2**.  
>  
> Cierro la idea señalando la última viñeta: el artefacto termina en una **clasificación en [0, 1]** — no en una opinión subjetiva del arquitecto, sino en un ratio reproducible que el banco podría usar **antes del despliegue** para decidir si el contrato cuenta la misma historia de negocio que el modelo BIAN de referencia.

**Acción:** leer en voz alta y con énfasis «**insuficiente o no adaptado**» — es un matiz que el docente valora (PI-12). Señalar el **recuadro dorado**, luego **P1 → P2 → P3 → P4** en orden. Si preguntan por las citas: Shvaiko sustenta P1/E; Casas contextualiza por qué OpenAPI está maduro pero BIAN no está integrado en la literatura.

---

## SLIDE 12 · 6:20–6:55 · **Alex**

**Diapositiva:** Objetivo general + variable dependiente

> **Insumo del procedimiento:** un contrato OpenAPI bancario emparejado con un **Service Domain BIAN** del mismo dominio (por ejemplo, pagos con pagos).  
>  
> **Objetivo general (técnico):** **diseñar** el modelo S/E/C y el procedimiento reproducible que produce el **AlignmentScore**.  
>  
> **Variable dependiente del artefacto:** el **AlignmentScore** en **[0, 1]** más la **clasificación** por niveles.  
>  
> El **objetivo superior** — lo que ocurriría en el mundo real **si** el artefacto existiera y se usara — es que equipos de arquitectura **cuantifiquen la coherencia negocio–API antes del despliegue**. En Guía 1 **no implementamos** ese cambio; solo entregamos el **diseño** validable en Tesis 2.

**Acción:** distinguir en voz «objetivo general técnico» vs «objetivo superior (consecuencia)».

---

## SLIDE 13 · 6:55–7:45 · **Alex**

**Diapositiva:** Objetivos específicos OE1–OE4 (figura cadena)

> Los **objetivos específicos** son **hitos con producto verificable** — no formulaciones vagas como «programar en Python» o «hacer experimentos».  
>  
> **OE1 — Normalizar:** transformar contrato y extracto BIAN en **representaciones intermedias comparables**. Producto: esquemas normalizados versionados.  
> **OE2 — Emparejar:** aplicar *schema matching* → producto: **StructuralScore E** ∈ [0, 1].  
> **OE3 — Similitud semántica:** calcular correspondencia de significado → producto: **SemanticScore S** ∈ [0, 1].  
> **OE4 — Integrar:** agregar S, E y C con pesos **α, β, γ** (que suman 1) → producto: **CoverageScore C**, **AlignmentScore** y **tipologías** de desalineación.  
>  
> La figura muestra la **cadena**: cada OE recibe la salida del anterior, como una línea de transformación documental.

**Acción:** recorrer la cadena OE1→OE4 con el cursor en la figura.

---

## SLIDE 14 · 7:45–8:25 · **Alex**

**Diapositiva:** Variables independientes (Tabla 5)

> Las **variables independientes (VI)** son **decisiones de diseño** que el investigador fija al construir el procedimiento — **no** hiperparámetros de *machine learning* como *epochs* o *learning rate*.  
>  
> **OE1:** esquema de **representación intermedia** (cómo aplanar paths/schemas frente a behaviors/objetos BIAN).  
> **OE2:** estrategia de **schema matching** (Shvaiko & Euzenat, 2005 — revisión clásica de técnicas de emparejamiento entre esquemas).  
> **OE3:** técnica de **similitud semántica** — por ejemplo embeddings vectoriales, alineación ontológica o enfoque híbrido.  
> **OE4:** pesos **α, β, γ** de la fórmula **AlignmentScore = α·S + β·E + γ·C**, con **α + β + γ = 1**.  
>  
> Cada factor tiene **alternativas** definidas en el plan para una validación futura en Tesis 2.

**Acción:** señalar cada fila OE1–OE4 en la tabla.

---

## SLIDE 15 · 8:25–9:05 · **Alex**

**Diapositiva:** Variables dependientes (Tabla 5 · Anexo D)

> En la slide anterior vimos las **variables independientes (VI)** — las **decisiones de diseño** que **nosotros fijamos** al construir el procedimiento. Esta diapositiva muestra las **variables dependientes (VD)**. La palabra «dependiente» suele generar duda, así que la aclaro primero.  
>  
> **¿Dependientes de qué?** Dependen de **dos cosas**:  
> **(1)** de las **VI** de la slide 14 — si cambiamos el esquema de normalización, la estrategia de matching, la técnica semántica o los pesos **α, β, γ**, cambia el puntaje que obtiene el mismo contrato;  
> **(2)** del **insumo concreto** que entra al procedimiento — un **contrato OpenAPI** emparejado con un **Service Domain BIAN** determinado. No son decisiones que el investigador elige a mano en cada ejecución: son **salidas medidas** que el artefacto **produce** al procesar ese par.

**Por qué «dependiente» y no «independiente»**

> En el plan usamos el lenguaje clásico de investigación: la **VI** es lo que **controlamos** en el diseño (*¿con qué algoritmo emparejo?*, *¿con qué pesos agrego?*); la **VD** es lo que **observamos** como resultado (*¿qué tan completa fue la normalización?*, *¿cuánto vale E, S, C?*).  
>  
> En **Guía 1** no ejecutamos el procedimiento a escala; por eso las VD están **definidas y documentadas** — sabemos **qué** mediremos y **en qué escala** [0, 1] —, pero los valores numéricos concretos se obtendrán en **Tesis 2** cuando corramos el software sobre contratos reales del **Anexo F**.

**Cada fila de la tabla — qué medimos y de qué VI depende**

> Recorro la tabla señalando cada fila y enlazándola con la slide 14:  
>  
> **OE1 — Completitud de la normalización.**  
> **VD:** ratio **elementos extraídos / elementos esperados** al pasar el contrato y BIAN al esquema intermedio.  
> **Depende de la VI «esquema de representación intermedia»:** si el esquema es pobre, la completitud será baja aunque el contrato sea bueno. Es el indicador de que **OE1 cumplió su producto** antes de calcular scores.  
>  
> **OE2 — StructuralScore (E).**  
> **VD:** puntaje **E ∈ [0, 1]** — qué tan bien emparejan estructuras REST y BIAN.  
> **Depende de la VI «estrategia de schema matching»** (base teórica: Shvaiko & Euzenat, 2005): distinta estrategia → distinta matriz de correspondencia → distinto **E** para el mismo contrato.  
>  
> **OE3 — SemanticScore (S).**  
> **VD:** puntaje **S ∈ [0, 1]** — similitud de **significado**, no solo de forma.  
> **Depende de la VI «técnica de similitud semántica»** (embeddings, ontología o híbrido). Recuerden el **Caso A** de la slide 10: mismos roles de negocio, nombres distintos → **S** bajo.  
>  
> **OE4 — CoverageScore (C), AlignmentScore y clasificación.**  
> **VD:** tres salidas ligadas: **C** (cobertura del Service Domain), el **AlignmentScore** agregado y el **nivel** Alta / Media / Baja / Nula.  
> **Dependen de la VI «pesos α, β, γ»** y, indirectamente, de todo lo anterior — porque **C** usa el emparejamiento previo, y el **AlignmentScore** combina S, E y C. La fórmula que debe quedar en la cabeza del auditor es:  
>  
> **AlignmentScore = α·S + β·E + γ·C**, con **α + β + γ = 1**.  
>  
> Si subo el peso **β**, doy más importancia a la estructura; si subo **α**, a la semántica. Por eso el score final **depende** de las decisiones de diseño **y** de los S, E, C que salieron de ese contrato concreto.

**Cierre y enlaces**

> En resumen: las **VD no son entradas** — son **productos medibles** del artefacto. La slide 14 dice **cómo lo construimos**; esta slide dice **qué nos devuelve** al evaluar un contrato frente a BIAN.  
>  
> El **Anexo D** del informe detalla **cómo calcular** cada ratio; el **Anexo C** enlaza cada VD con su **hipótesis** (H1–H4) para la validación futura. Si el docente pide profundidad, abrimos el Anexo D en la fila que pregunte.

**Acción:** antes de recorrer filas, decir en voz alta: «**Dependen de las VI de la slide anterior y del contrato que evaluamos**». Señalar **OE1→OE4** en orden; escribir o trazar en el aire la fórmula **α·S + β·E + γ·C**. Enlace oral explícito: «la fila OE2 de VI era matching; la fila OE2 de VD es **E**».

---

## SLIDE 16 · 9:05–9:45 · **Alex**

**Diapositiva:** Metodología — 5 fases (§4.2 · §4.2.1)

> Hasta ahora definimos **objetivos**, **variables independientes** y **dependientes**. Esta diapositiva responde la pregunta operativa: **¿en qué orden se hace el trabajo?** Es la **metodología** del Capítulo 4 — sección **4.2** y tabla **4.2.1** del informe.  
>  
> Si el docente dice «**empiecen por metodología**» — criterio **PI-14** — esta es la diapositiva por la que **conviene arrancar** la parte técnica: muestra el **procedimiento como una secuencia de verbos**, no como una lista suelta de conceptos.

**Qué muestra la tabla**

> La tabla tiene **cuatro columnas** que conviene nombrar antes de bajar fila por fila: **Fase** (el número de paso), **Verbo** (la acción en infinitivo — diseñar, normalizar, emparejar…), **Transformación** (qué entra y qué operación se aplica) y **Producto** (qué queda **verificable** al terminar esa fase). Esa lógica **Problema → objetivo → producto** es la misma que verán formalizada en la **matriz del Anexo C** en la slide 18.

**Fase 1 — Diseñar**

> **Verbo: Diseñar.**  
> Aquí estamos **hoy**, en **Guía 1**: fijamos **entradas** (contrato OpenAPI + Service Domain BIAN), **definición de los scores** S, E y C, **umbrales** de clasificación (0,80 / 0,60 / 0,40) y la **fórmula** de agregación.  
> **Transformación:** no procesamos aún un banco real a escala; **documentamos** el modelo.  
> **Producto:** el **modelo S/E/C documentado** — el entregable central del plan. Sin esta fase, las demás no tendrían reglas claras.

**Fase 2 — Normalizar (OE1)**

> **Verbo: Normalizar.**  
> **Transformación:** tomamos el **contrato** y el **extracto BIAN** — en Tesis 2, con parser y extracto real — y los llevamos a **representaciones comparables** en un esquema intermedio.  
> **Producto:** representaciones **versionadas** listas para matching.  
> Enlazo con la slide 15: la **VD** de esta fase es la **completitud de la normalización**; si falla aquí, no tiene sentido calcular E, S ni C.

**Fase 3 — Emparejar (OE2)**

> **Verbo: Emparejar.**  
> **Transformación:** sobre las representaciones normalizadas, aplicamos **schema matching** — emparejamiento estructural entre capa REST y modelo BIAN.  
> **Producto:** matriz de correspondencia + **StructuralScore E** ∈ [0, 1].  
> Responde a la **P1** de la slide 11: «¿cómo emparejar estructuras?». Base teórica: **Shvaiko & Euzenat (2005)**.

**Fases 4 y 5 — Calcular similitud e integrar (OE3 y OE4)**

> En la diapositiva, **Fase 4–5** aparecen en **una fila** por espacio, pero oralmente son **dos pasos**:  
>  
> **Fase 4 — Calcular (OE3):** medir **similitud semántica** → producto **SemanticScore S**. Responde a **P2** y al **Caso A** (nombres distintos, mismo negocio).  
>  
> **Fase 5 — Integrar (OE4):** medir **cobertura C**, agregar **AlignmentScore = α·S + β·E + γ·C** y asignar la **clasificación** Alta / Media / Baja / Nula, más las **tipologías** de desalineación. Responde a **P3** y **P4** y al **Caso B** (operaciones faltantes).  
>  
> El **producto final** del procedimiento es el **AlignmentScore** con su etiqueta interpretable para arquitectura — no un número suelto.

**Cierre — Guía 1 vs ejecución**

> Repito el matiz del plan: en **Guía 1** **diseñamos y documentamos** estas cinco fases; en **Tesis 2** **ejecutamos** el software sobre contratos del **Anexo F** y **validamos** las hipótesis H1–H4. La metodología ya está **cerrada en papel**; falta la evidencia empírica.  
>  
> La **slide 17** muestra el **mismo artefacto** en figura — S, E, C y la fórmula — para quien prefiera visualizarlo.

**Acción:** señalar el **encabezado de columnas** antes de bajar. Recorrer **Fase 1 → 5** con el dedo en la columna **Verbo**. En **Fase 4–5**, separar oralmente «primero S, luego C y score». Si preguntan detalle de actividades, abrir PDF **§4.2.1**. Cierre en voz: «**Cinco verbos, cinco productos, un solo procedimiento reproducible**».

---

## SLIDE 17 · 9:45–10:30 · **Alex**

**Diapositiva:** Artefacto S / E / C (figura)

> El **artefacto** descompone la evaluación en tres dimensiones complementarias:  
>  
> **E (StructuralScore):** grado en que la organización REST (recursos, métodos, anidamiento) corresponde a la estructura del Service Domain BIAN. Base teórica: emparejamiento de esquemas (**Shvaiko & Euzenat, 2005**).  
> **S (SemanticScore):** similitud de **significado** entre nombres y conceptos — no solo la forma.  
> **C (CoverageScore):** qué **proporción** de behaviors/objetos definidos en BIAN tiene equivalente en el contrato.  
>  
> Se combinan en **AlignmentScore = α·S + β·E + γ·C**, que alimenta la clasificación **Alta / Media / Baja / Nula**.  
>  
> **S, E y C se calculan por unidad de análisis** (cada par comparable dentro del contrato); el resultado global resume el **contrato completo frente a un Service Domain**.

**Acción:** señalar S, E, C y la fórmula en la figura. Tener PDF Shvaiko listo.

---

## SLIDE 18 · 10:30–11:30 · **Alex**

**Diapositiva:** Matriz de consistencia — Anexo C (2 tablas)

> Llegamos a una pieza que el docente suele revisar con lupa: la **matriz de consistencia** del **Anexo C** del informe escrito.  
>  
> **¿Para qué sirve?** Para demostrar que el plan **no está desarmado**: cada fase del procedimiento tiene un **problema tecnológico concreto**, un **objetivo** que lo responde y un **producto verificable** — algo que se puede revisar en un documento o, en Tesis 2, en una ejecución.  
>  
> **Antes de entrar en la tabla**, una distinción importante — la repetiremos en la slide 19: esta matriz **no** es la **brecha** del estado del arte. La matriz habla del **artefacto que diseñamos**; la brecha habla de lo que **aún no hace la literatura**. Son complementarias, no intercambiables.

**Primera tabla — «Problema tecnológico → objetivo → producto»**

> Señalo el título de la primera tabla y las **cuatro columnas**: **F** es la **fase** del procedimiento; luego **problema tecnológico**, **objetivo** y **producto verificable**.  
>  
> **Fase 1 — Diseño del modelo.**  
> El **problema** es que hoy no existe un **método reproducible** para cuantificar la alineación entre OpenAPI y BIAN — hay prácticas aisladas, pero no un procedimiento documentado para este par.  
> El **objetivo** de la fase es **diseñar** el modelo **S/E/C** y su agregación.  
> El **producto** es el **modelo metodológico documentado** — lo que estamos entregando en esta Guía 1, visible en el propio Anexo C.  
>  
> **Fase 2 — Normalización (OE1).**  
> El **problema**: contrato OpenAPI y extracto BIAN vienen en **representaciones distintas** — no se pueden comparar directamente.  
> El **objetivo**: **OE1**, normalizar ambos a un **esquema intermedio** comparable.  
> El **producto**: **representaciones versionadas** — archivos o estructuras normalizadas que quedan trazadas por versión del contrato.  
>  
> **Fase 3 — Emparejamiento estructural (OE2).**  
> El **problema**: aún no tenemos un **StructuralScore E** sistemático que diga qué tan bien encajan paths, operaciones y schemas con behaviors y objetos BIAN.  
> El **objetivo**: **OE2**, emparejar estructuras con *schema matching*.  
> El **producto**: una **matriz de correspondencia** más el puntaje **E ∈ [0, 1]** por unidad de análisis.  
>  
> **Fase 4 — Similitud semántica (OE3).**  
> El **problema**: la estructura puede coincidir pero los **nombres y significados** no — recuerden el Caso A de la slide 10.  
> El **objetivo**: **OE3**, calcular similitud semántica.  
> El **producto**: matriz ampliada con **S ∈ [0, 1]**.  
>  
> **Fase 5 — Integración (OE4).**  
> El **problema**: faltan **cobertura**, **score integrado** y **clasificación** interpretable para arquitectos.  
> El **objetivo**: **OE4**, integrar S, E y C con pesos **α, β, γ**.  
> El **producto**: **CoverageScore C**, **AlignmentScore** y la **clasificación** Alta / Media / Baja / Nula.  
>  
> Si leen la tabla de izquierda a derecha, cada fila responde: «**qué falla hoy → qué hacemos → qué entregamos**».

**Segunda tabla — «VI · VD · Hipótesis»**

> Bajo el segundo título aparecen tres columnas más técnicas, pero la lógica es la misma.  
> **VI** = **variable independiente**: la **decisión de diseño** que el investigador fija.  
> **VD** = **variable dependiente**: el **puntaje o ratio** que el procedimiento **mide**.  
> **Hipótesis** = lo que **esperamos comprobar** cuando ejecutemos el artefacto en Tesis 2 — aquí solo las **declaramos**, no las probamos aún.  
>  
> **Fase 1.**  
> **VI:** definición del esquema S/E/C y de los pesos **α, β, γ**.  
> **VD:** que los scores queden **definidos** de forma reproducible.  
> **H0:** el **modelo metodológico es reproducible** — es decir, dos investigadores con el mismo contrato y el mismo Service Domain deberían obtener el mismo procedimiento documentado.  
>  
> **Fase 2 / OE1.**  
> **VI:** diseño del **esquema intermedio** de normalización.  
> **VD:** **completitud** de la normalización — cuántos elementos se extrajeron vs cuántos se esperaban.  
> **H1:** si normalizamos bien, **habilitamos** el cálculo sistemático de S, E y C en las fases siguientes.  
>  
> **Fase 3 / OE2.**  
> **VI:** estrategia de **schema matching** (Shvaiko & Euzenat).  
> **VD:** **StructuralScore E**.  
> **H2:** el matching produce un **E coherente** con la organización REST frente a BIAN.  
>  
> **Fase 4 / OE3.**  
> **VI:** técnica de **similitud semántica** (embeddings, ontología o híbrido).  
> **VD:** **SemanticScore S**.  
> **H3:** la similitud produce un **S** que **discrimina** desalineaciones reales — no todos los contratos salen iguales.  
>  
> **Fase 5 / OE4.**  
> **VI:** pesos **α, β, γ** de agregación.  
> **VD:** **C**, **AlignmentScore** y nivel de clasificación.  
> **H4:** la agregación ponderada produce un **AlignmentScore interpretable** para decisiones de arquitectura.  
>  
> **Cierre de la slide:** la matriz cierra el circuito **problema → objetivo → producto → variable → hipótesis**. El detalle celda por celda, con redacción completa, está en el **Anexo C** del PDF del plan — lo tenemos listo si el docente pide profundizar en una fila.

**Acción:** recorrer **primero** la tabla superior fila por fila señalando las columnas; **pausa breve**; luego la tabla inferior. No leer cada celda palabra por palabra — **narrar la lógica** señalando la fila activa. Tener **Anexo C** abierto en otra pestaña. Cerrar en voz: «**Matriz = diseño del artefacto; brecha = literatura — slide siguiente**».

---

## SLIDE 19 · 11:30–12:10 · **Jack + Alex**

**Diapositiva:** Brecha V1–V5 (figura Cap. 3)

**Jack (V1–V2):**

> La **brecha de investigación** resume **vacíos del estado del arte** (Capítulo 3, §3.6) — **distinta** de la matriz.  
> **V1:** no existe un marco **sistemático** para alinear OpenAPI con BIAN.  
> **V2:** falta una forma **reproducible** de **cuantificar** la desalineación — hoy predomina revisión manual.

**Alex (V3–V5):**

> **V3:** falta integrar **S, E y C** en un **único score** interpretable para arquitectos.  
> **V4:** falta un procedimiento aplicable **antes del despliegue**, sobre el contrato publicado.  
> **V5:** confundir **calidad en runtime** (latencia, errores HTTP) con **coherencia documental** negocio–API; nuestro plan mide lo segundo.  
>  
> La figura muestra cómo los trabajos previos (**E1–E6** en la revisión) dejan estos vacíos (**V1–V5**) y dónde se ubica nuestra propuesta.

**Acción:** señalar vacíos en la figura; cerrar: «**Brecha ≠ matriz**». Leer el caption navy (PI-11) si hace falta reforzar.

---

## SLIDE 20 · 12:10–12:40 · **Jack**

**Diapositiva:** Conclusiones

> Cerramos con **relaciones entre conceptos**, no con opinión personal:  
>  
> **OpenAPI** es maduro como formato de contrato técnico; falta un procedimiento **OpenAPI↔BIAN** reproducible.  
> El **objeto** es el contrato; **BIAN** es **referencia**; la **unidad de análisis** es cada par comparable dentro del contrato → de ahí salen **S, E, C** integrados.  
> **OE1 a OE4** encadenan transformaciones con **productos verificables** en cada paso.  
> La **matriz del Anexo C** cierra la trazabilidad: problema tecnológico → objetivos → variables → hipótesis.  
> **Guía 1** entrega el **diseño**; **Tesis 2** prevé software y validación empírica con contratos reales.

---

## SLIDE 21 · 12:40–12:55 · **Alex**

**Diapositiva:** Recomendaciones

> Como **recomendaciones** de continuidad: **(1)** implementar el artefacto según el procedimiento del §4.2; **(2)** calibrar los umbrales 0,80 / 0,60 / 0,40 con una muestra representativa de contratos bancarios; **(3)** validar las hipótesis **H1–H4** con contratos OpenAPI 3.x públicos del **Anexo F**; **(4)** integrar el score en la **gobernanza de APIs** del banco **antes** del despliegue a producción.

---

## SLIDE 22 · 12:55–15:00 · **Jack**

**Diapositiva:** Referencias + cierre

> En esta exposición citamos principalmente a:  
> — **Casas et al. (2021)** — revisión sistemática de investigación sobre OpenAPI;  
> — **Shvaiko & Euzenat (2005)** — taxonomía de *schema matching*;  
> — **Farzi et al. (2021)** — documentación del panorama de servicios **BIAN**;  
> — **CMA (2016)** — informe británico que impulsó **open banking**;  
> — **TSB (2018)** — caso de falla tras migración IT.  
>  
> Tenemos abiertos los PDFs de **Casas** y **Shvaiko** para mostrar el pasaje citado si lo solicitan.  
>  
> **¿Preguntas?**  
>  
> *(Cierre fijo, ~15 s:)* «El plan entrega el **diseño** del procedimiento S/E/C; la **validación empírica** con datos bancarios queda para **Tesis 2**, según el §1.6 del informe.»

---

## Anexo — Respuestas rápidas (preguntas del docente)

| Pregunta | Respuesta narrativa (quien responde) |
|----------|--------------------------------------|
| ¿Qué es OpenAPI? | Estándar de facto para describir APIs REST en YAML/JSON: rutas, operaciones y esquemas. Es nuestro **objeto de estudio**. (**Jack**) |
| ¿Qué es BIAN? | *Banking Industry Architecture Network*: red de la industria que publica un modelo de referencia de capacidades bancarias en **Service Domains**. Lo usamos como **contraste**, no como objeto. (**Jack**) |
| ¿Cuál es la UA? | **Unidad de análisis**: cada par comparable *endpoint/schema ↔ behavior/objeto de negocio* dentro de un contrato evaluado frente a un Service Domain, identificado como `{fuente}_{SD}_{versión}`. (**Jack**) |
| ¿Objeto vs UA? | **Objeto** = contrato OpenAPI completo. **UA** = instancia de medición dentro de ese contrato. El score global resume **contrato × Service Domain**. (**Alex**) |
| ¿Qué es la CMA? | *Competition and Markets Authority* del Reino Unido; su informe de **2016** sobre competencia bancaria impulsó el **open banking** británico. (**Jack**) |
| ¿Tres niveles de problema? | **Real** (§1.2): síntomas en el sector. **Subyacente** (§1.4): dos jerarquías desalineadas. **Tecnológico** (§1.3): falta método reproducible — es el de la **matriz**. (**Alex**) |
| ¿Brecha vs matriz? | **Brecha** = vacíos V1–V5 del **estado del arte** (Cap. 3). **Matriz** = trazabilidad del **problema tecnológico** del diseño (Anexo C). (**Alex**) |
| ¿Por qué no experimentan? | **Guía 1** = solo **diseño** del procedimiento (§1.6); la ejecución y prueba con bancos reales es **Tesis 2**. (**Alex**) |
| ¿Leíste Casas/Shvaiko? | Sí → abrir PDF y señalar el párrafo (68 % dominio concreto en Casas; taxonomía de matching en Shvaiko). (**quien citó**) |

---

## Errores a evitar

- Mencionar siglas (**CMA**, **BIAN**, **OE1**, **UA**…) **sin una frase que las explique**
- Hablar sin señalar la diapositiva
- Decir «no existe ningún método» (usar **insuficiente / no adaptado**)
- Confundir problemática del sector ↔ problema tecnológico ↔ brecha ↔ matriz
- Exponer slides **2**, **3** o **4**
- Leer párrafos enteros del slide en lugar de narrar

---

*Libreto Grupo 9.2 — sincronizado con `Exposicion_Plan_Tesis_Grupo9.2-beamer.pdf` y `ppt/GUION_15MIN_AMPLIADO.md`.*
