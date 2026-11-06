# Libreto — Sesión 5 · Operacionalización y EDA

**Presentación:** `Sesion05_Operacionalizacion_y_EDA_slides.pdf` (**19 diapositivas**)  
**Duración:** 12–14 minutos (todas se exponen; la 9 es puente, 10 s)  
**Integrantes:** Alex Mancilla · Dennis Jack Paitan  
**Regla:** señalar la diapositiva al hablar. Explicar cada sigla la primera vez.

**Frase de ancla:** el objeto de la tesis no es OFB. OFB es la **muestra** con la que se ejecuta el procedimiento.  
**Frase oral:** parser al 100 % **no** implica AlignmentScore Alto.

---

## Antes de empezar

- [ ] PDF de las diapositivas abierto (19 páginas)
- [ ] Si preguntan catálogo: `data/piloto_ofb_bian/README.md`
- [ ] Si preguntan números: `data/piloto_ofb_bian/resultado/inventario.json`
- [ ] Reloj: Parte A (láminas 1–8) ~6 min; Parte B (9–19) ~7 min

| Quién | Láminas |
|-------|---------|
| Jack | 1, 3, 7, 8, 10, 11, 12, 13, 14, 15 |
| Alex | 2, 4, 5, 6, 9, 16, 17, 18, 19 |

---

## SLIDE 1 · 0:00–0:40 · **Jack**

**Diapositiva:** Portada navy — Operacionalización, instrumentos y EDA

> Buenas [tardes/noches]. Grupo 10, Alex Mancilla y Dennis Jack Paitan.  
>  
> Esta sesión cierra dos cosas **antes** del matching: la **operacionalización** de las variables y el **EDA** — análisis exploratorio de datos — del piloto.  
>  
> El **objeto de la tesis** es un contrato **OpenAPI bancario** frente a un Service Domain **BIAN** — *Banking Industry Architecture Network*.  
> El **piloto** es **Open Finance Brasil**, 38 APIs. OFB es un estándar de industria, no el YAML de un banco, y no redefine el objeto.

**Acción:** señalar objeto vs piloto.

---

## SLIDE 2 · 0:40–1:20 · **Alex**

**Diapositiva:** Agenda de la sesión

> Seis bloques. A1 a A3 son operacionalización: qué medimos, con qué instrumentos y cómo cada objetivo específico tiene indicador.  
> B1 a B5 son el EDA: inventario, distribuciones, faltantes, variable objetivo y riesgos de *leakage*.  
>  
> Hoy **no** entregamos AlignmentScore. Entregamos variables definidas y un corpus ya parseado.

**Acción:** señalar el corte A / B (navy vs azul).

---

## SLIDE 3 · 1:20–2:10 · **Jack**

**Diapositiva:** Dónde estamos en el plan de 12 semanas

> En el ciclo empírico: pares y parser ya corrieron. Esta sesión es limpieza, normalización y EDA. Matching y scores siguen pendientes.  
>  
> El piloto son **38 APIs OFB más 3 Service Domains BIAN versión 14**: 41 YAML.  
> Los pares que sí van a score son cuentas y pagos. Las otras APIs solo entran al inventario.  
> Todavía no hay AlignmentScore: faltan los objetivos específicos 2 a 4.

**Acción:** señalar la barra S5–S6 y el recuadro “Aún no hay AlignmentScore”.

---

## SLIDE 4 · 2:10–3:10 · **Alex**

**Diapositiva:** Qué se mide — variable dependiente del artefacto

> Lo que se mide no es un banco, ni OFB, ni “qué tan completo está el parser”.  
>  
> La **variable dependiente** del artefacto es el **AlignmentScore**: alfa por S, más beta por E, más gamma por C, con pesos que suman 1. La línea base es un tercio cada uno.  
>  
> La **base de medición** es una **instancia**: un contrato OpenAPI bancario por un Service Domain BIAN. Ejemplo en el piloto: *accounts* 2.4.2 contra *SavingsAccount* 14.  
>  
> **S**, *SemanticScore*: ¿significan lo mismo?  
> **E**, *StructuralScore*: ¿la jerarquía REST refleja el Service Domain?  
> **C**, *CoverageScore*: ¿cuánto del Service Domain cubre el contrato?  
>  
> Niveles: Alta desde 0,80; Media; Baja; Nula bajo 0,40. S, E, C y la completitud son **parciales**: no sustituyen la variable dependiente.

**Acción:** señalar la fórmula y las tres cajas S / E / C.

---

## SLIDE 5 · 3:10–4:00 · **Alex**

**Diapositiva:** A1 — Definición conceptual vs operacional

> Cada constructo tiene pregunta, operación y escala de 0 a 1.  
>  
> S se opera como similitud sobre el corpus emparejado.  
> E como matriz de pares; las operaciones sin par aportan cero.  
> C como conceptos BIAN — tags de *Control Record* y *Behavior Qualifier* — con al menos un par, sin contar el CR dos veces.  
> AlignmentScore es la combinación. La clasificación son umbrales fijos, no un modelo.  
> Completitud del objetivo 1 es otra cosa: extraídos sobre esperados.  
>  
> Los pesos, la técnica semántica y la estrategia de matching son **factores de diseño**, no la variable dependiente.

**Acción:** señalar la fila AlignmentScore y la nota de factores.

---

## SLIDE 6 · 4:00–4:55 · **Alex**

**Diapositiva:** A3 — Correspondencia OE ↔ indicador

> Fase 1, definir S, E, C, fórmula y umbrales: **cumplida** en el plan.  
> Objetivo específico 1: ¿se pueden comparar REST y BIAN? **41 contratos parseados**. Falta firmar completitud por YAML.  
> Objetivos 2, 3 y 4 — E, S, C y AlignmentScore — **pendientes**.  
>  
> Criterio oral: un parser al 100 % **no** implica AlignmentScore Alto. No hay aprendizaje supervisado.

**Acción:** señalar el recuadro naranja del criterio oral.

---

## SLIDE 7 · 4:55–5:50 · **Jack**

**Diapositiva:** A2 — Fuentes de datos e instrumentos

> El objeto **no cambia**. OFB no lo sustituye.  
>  
> Muestra del piloto: 38 APIs Open Finance Brasil, 160 operaciones.  
> Referencia: tres Service Domains BIAN v14 — *SavingsAccount*, *CurrentAccount*, *PaymentOrderInitiation*.  
> Unidad: endpoint o schema frente a *Behavior*, *Business Object* o *Behavior Qualifier*. Matching aún no calculado.  
> Instrumento del objetivo 1: `procesar_openapi.py`.  
>  
> Criterios: OpenAPI 3.x parseable, al menos una operación y un esquema, BIAN legible, sin datos personales — Ley 29733 no aplica porque el material es público.

**Acción:** señalar “Objeto de estudio / No cambia”.

---

## SLIDE 8 · 5:50–6:35 · **Jack**

**Diapositiva:** Procedimiento de medición — cinco fases

> Cinco fases. Una, diseñar: hecha. Dos, adquirir y normalizar: **cubierta**, 38 más 3 YAML. Tres a cinco — emparejar, similitud e integrar — pendientes, y solo sobre los pares I1 a I6, **siete instancias**.  
>  
> Las otras 33 APIs OFB no entran al AlignmentScore.

**Acción:** señalar fases 1–2 en color y 3–5 en gris.

---

## SLIDE 9 · 6:35–6:45 · **Alex**

**Diapositiva:** Parte B — EDA (puente navy)

> Pasamos a datos. 41 contratos, 235 operaciones, carpeta `piloto_ofb_bian`.

**Acción:** no detenerse.

---

## SLIDE 10 · 6:45–7:35 · **Jack**

**Diapositiva:** B1 — Inventario del piloto

> Cuatro números que hay que recordar: **41** contratos, **235** operaciones, **6 746** propiedades, **10 906** fragmentos de corpus.  
>  
> BIAN: 34, 34 y 7 operaciones — 75 en total. OFB: 38 APIs, última estable; solo *payroll-credit-portability* es beta.  
> Material público, sin PII. Pendiente: matching y AlignmentScore.

**Acción:** señalar los cuatro KPI y “Pendiente”.

---

## SLIDE 11 · 7:35–8:25 · **Jack**

**Diapositiva:** B2 — Métodos HTTP

> En el consolidado: 152 GET, 39 POST, 36 PUT, 7 PATCH, 1 DELETE.  
>  
> OFB es consulta: **130 GET de 160**. BIAN concentra los PUT: Update, Control, Execute.  
> Por eso **E no puede exigir el mismo verbo HTTP**. Tiene que tolerar REST de consulta frente a REST de *facility*.

**Acción:** señalar GET vs PUT en la lectura.

---

## SLIDE 12 · 8:25–9:10 · **Jack**

**Diapositiva:** B2 — Tags BIAN (CR vs BQ)

> 160 operaciones OFB frente a 75 BIAN: la muestra es más ancha que la referencia de tres Service Domains.  
>  
> En BIAN hay **64 Behavior Qualifiers** y **11 Control Records**. OFB **no trae** esas etiquetas. Imputarlas sería *leakage*: contaminaríamos E con la estructura de la referencia.  
> Loans, cards y financings de OFB no tienen Service Domain en este zip: *gap* de referencia, no de objeto.

**Acción:** señalar “no imputarlos”.

---

## SLIDE 13 · 9:10–9:50 · **Jack**

**Diapositiva:** B2 — Operaciones por contrato

> Visual del desbalance: 160 operaciones OFB contra 34, 34 y 7 de BIAN.  
>  
> Pares listos: *accounts* con *Savings* y *Current*; pagos con *PaymentOrderInitiation*.  
> El hueco — préstamos, tarjetas, financiamientos — **no** se resuelve inventando un Service Domain.

**Acción:** señalar el hueco, no el catálogo entero.

---

## SLIDE 14 · 9:50–10:30 · **Jack**

**Diapositiva:** B2 — Corpus semántico (10 906)

> El corpus de S son 10 906 fragmentos: sobre todo nombres de propiedad, luego schemas, luego operaciones.  
>  
> Prefijos *InCR* y *ReBQ* ya están limpios. En BIAN, *summary* es igual a *description* en las **75 de 75** operaciones: una sola copia, no se cuenta dos veces.

**Acción:** señalar property 9 314 y la nota BIAN.

---

## SLIDE 15 · 10:30–11:15 · **Jack**

**Diapositiva:** B3 — Faltantes e inconsistencias

> Calidad, no score.  
>  
> El 61,9 % de las propiedades no tiene *description*: BIAN 90,4 %, OFB 38,1 %. Por eso S de atributos BIAN cae sobre el **nombre**.  
> El parser ya resuelve `$ref` anidados. Los CSV van con BOM: abrir con `utf-8-sig`.  
> No hay *path* ni *operationId* duplicados en el consolidado.

**Acción:** señalar 61,9 % y 90,4 %.

---

## SLIDE 16 · 11:15–12:00 · **Alex**

**Diapositiva:** B4 — Variable objetivo y clases

> La variable dependiente es AlignmentScore más {Alta, Media, Baja, Nula}.  
>  
> Hay pares de artefactos, **pero no hay S, E ni C**. Por eso **no hay distribución de clases**.  
> La barra OFB / BQ / CR es un **proxy estructural**, no la variable.  
> Los niveles se asignan **después** de los umbrales, no como etiqueta para entrenar.

**Acción:** señalar “NO es la VD”.

---

## SLIDE 17 · 12:00–12:55 · **Alex**

**Diapositiva:** B5 — Sesgos y leakage

> Seis riesgos que ya están declarados.  
>  
> No evaluar BIAN contra BIAN. No copiar tags CR o BQ a OFB. No usar el nombre de un `$ref` BIAN como evidencia del banco. No calibrar los pesos en los mismos pares del reporte. No reintroducir *InCR* o *ReBQ* como *feature*. Y no tratar OFB como si fuera el objeto de la tesis.  
>  
> C se calcula **por instancia** I1 a I6, no como un C global de las 38 APIs.

**Acción:** señalar las dos filas de autoalineación y de confundir OFB con el objeto.

---

## SLIDE 18 · 12:55–13:35 · **Alex**

**Diapositiva:** Implicaciones · qué sigue

> Hecho: catálogo OFB más tres Service Domains parseados.  
> Siguiente: firmar completitud del objetivo 1 por contrato, y matching de I1 e I4 en la semana 8. El resto de instancias, semanas 10 y 11.  
> No presentar AlignmentScore de autoalineación BIAN–BIAN.

**Acción:** señalar P0 hecho y P2 pendiente.

---

## SLIDE 19 · 13:35–14:10 · **Alex**

**Diapositiva:** En una frase

> Cierre: la tesis mide OpenAPI bancario frente a BIAN. El piloto de esta sesión es Open Finance Brasil — 38 APIs, 160 operaciones — frente a tres Service Domains v14. El AlignmentScore **aún no está calculado**.  
>  
> Preguntas.

**Acción:** dejar la frase en pantalla.

---

## Si preguntan

| Pregunta | Respuesta corta |
|----------|-----------------|
| ¿OFB es un banco? | No. Estándar de industria. El objeto sigue siendo OpenAPI bancario. |
| ¿Ya tienen AlignmentScore? | No. Hoy es operacionalización + EDA. I1 e I4 en semana 8. |
| ¿Por qué 38 APIs y solo 7 instancias? | Solo accounts, opendata-accounts, payments, automatic-payments y enrollments tienen par natural BIAN. |
| ¿Por qué no inventar un SD para loans? | Gap de referencia. El objeto de la tesis no se recorta; este piloto sí. |
| ¿Parser al 100 % = Alta? | No. Completitud OE1 ≠ AlignmentScore. |
| ¿Se pueden copiar tags CR/BQ a OFB? | No. Eso es leakage. |
