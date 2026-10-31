# Libreto — Sesión 7 · Revisión de avances

**Presentación:** `Sesion07_Revision_Avances_slides.pdf` (**10 diapositivas**)  
**Duración:** 8–10 minutos (todas se exponen)  
**Integrantes:** Alex Mancilla · Jack Paitan  
**Regla:** señalar la diapositiva al hablar. Explicar cada sigla la primera vez.

**Frase de ancla:** la tesis mide OpenAPI bancario ↔ BIAN; OFB es el piloto.  
**Frase oral:** parser al 100 % **no** implica AlignmentScore Alto.

---

## Antes de empezar

- [ ] PDF de las diapositivas (versión con tablas legibles, no el informe)
- [ ] Si preguntan Trello: `../plan-tesis-v2/cronograma-sprints.md`
- [ ] Si preguntan números: `cuaderno-pruebas.md` + `inventario.json`
- [ ] Reloj: ~45–55 s; las láminas 3, 5 y 7 pueden ir a 70 s

| Quién | Láminas |
|-------|---------|
| Jack | 1, 3, 4, 5, 7 |
| Alex | 2, 6, 8, 9, 10 |

---

## SLIDE 1 · 0:00–0:40 · **Jack**

**Diapositiva:** Portada navy — Revisión de avances

> Buenas [tardes/noches]. Grupo 10, Alex Mancilla y Jack Paitan.  
>  
> Esta sala revisa **avances**, no el matching final. Cuatro bloques: el Trello de 12 semanas, el cuaderno de primeras pruebas, las métricas y dos revistas.  
>  
> El **objeto** sigue siendo contrato **OpenAPI bancario** frente a un Service Domain **BIAN** — *Banking Industry Architecture Network*. El **piloto** es **Open Finance Brasil**, OFB. OFB no es un banco y no es toda la tesis.

**Acción:** señalar objeto vs piloto.

---

## SLIDE 2 · 0:40–1:15 · **Alex**

**Diapositiva:** Agenda de la sala

> Cuatro puntos, los mismos de la lámina del aula.  
>  
> Uno: el plan de trabajo del ciclo empírico, 12 semanas, en Trello.  
> Dos: primeros resultados en el cuaderno — objetivo específico 1 y EDA, análisis exploratorio.  
> Tres: qué métricas usamos, cómo se calculan y cuál es el criterio de éxito.  
> Cuatro: dos revistas candidatas para el artículo.  
>  
> Producto del sílabo que se abre con esto: **P4**, semanas 8 y 9. Hoy no entregamos P4.

**Acción:** no leer la agenda como lista seca; decir “hoy no es P4”.

---

## SLIDE 3 · 1:15–2:20 · **Jack**

**Diapositiva:** Trello — ciclo empírico de 12 semanas

> El ciclo de 12 semanas **se superpone** a las semanas 5 a 16 del sílabo. S1 a S4 ya ocurrieron en la Sesión 5: pares y parser.  
>  
> S1 a S4: pares I1 a I6 y parser. **Hecho.**  
> S5 y S6: EDA y revisión del método. **Hecho.**  
> **S7, hoy:** protocolo y cuaderno.  
> S8, semana 8, producto P4: scores v0 de **I1 e I4**.  
> S9: defensa intermedia.  
> S10 y S11: las **siete** instancias con S, E y C.  
> S12 cubre P5 a P7: discusión y borrador.  
>  
> Lo verde ya está. Lo gris es lo que la sala debe exigirnos a partir de la semana 8.

**Acción:** señalar la fila S7 “Hoy” y la fila S8.

---

## SLIDE 4 · 2:20–3:10 · **Jack**

**Diapositiva:** Tablero y tarjetas que no se borran

> El tablero es lineal: Backlog, Semana, En curso con WIP 2 — máximo dos tarjetas a la vez —, Revisión de pareja, Hecho y Bloqueado.  
>  
> Cuatro tarjetas **permanentes**, no se archivan.  
>  
> **LEAKAGE:** no copiamos etiquetas CR o BQ — *Control Record* y *Behavior Qualifier* — al CSV de OFB, y no puntuamos BIAN contra sí mismo.  
> **VERSIONES:** *accounts* 2.4.2, *payments* 4.0.0, BIAN 14.0.0.  
> **PARES:** solo I1 a I6 reciben AlignmentScore; el resto es inventario.  
> **SIN-ML:** no etiquetamos Alta, Media o Baja a mano para entrenar un clasificador.

**Acción:** señalar LEAKAGE primero; es la pregunta más probable.

---

## SLIDE 5 · 3:10–4:20 · **Jack**

**Diapositiva:** Cuaderno — primeras pruebas (aún no hay score)

> El cuaderno ya tiene números. **41** contratos, **235** operaciones, **6 746** propiedades, **10 906** fragmentos de corpus. Eso prueba que el parser corre. **No** es el AlignmentScore.  
>  
> OFB es REST de consulta: 130 GET de 160. BIAN es control: 36 PUT de 75. Por eso E, el score estructural, **no** exige el mismo verbo.  
> El 61,9 % de las propiedades no tiene *description* — en BIAN, 90,4 % —. El score semántico S cae sobre el **nombre**.  
> La hipótesis 1, que se puede extraer y normalizar, está **soportada**. H2 a H4 esperan I1 e I4.

**Acción:** señalar el bloque 41 / 235 y la fila “aún no hay score” del título.

---

## SLIDE 6 · 4:20–5:15 · **Alex**

**Diapositiva:** Métricas adecuadas a la tarea

> Las métricas son las del **artefacto**, no *accuracy* de un clasificador.  
>  
> Completitud del objetivo 1: ¿el parser recuperó el YAML? Es reproducibilidad.  
> **E**, *StructuralScore*: ¿la jerarquía REST refleja el Service Domain? Pregunta 1, hipótesis 2.  
> **S**, *SemanticScore*: ¿los conceptos significan lo mismo? Pregunta 2, hipótesis 3.  
> **C**, *CoverageScore*: ¿cuánto del Service Domain cubre el contrato?  
> **AlignmentScore** más el nivel: ¿cuánto se alinea la instancia? Esa es la **variable dependiente**, pregunta 4, hipótesis 4.  
>  
> No usamos F1 supervisado, encuestas, latencia ni “mismos PUT que BIAN”.

**Acción:** señalar la fila AlignmentScore y la nota de lo que no entra.

---

## SLIDE 7 · 5:15–6:25 · **Jack**

**Diapositiva:** Cómo se calculan e interpretan

> La unidad de medición es una **instancia**: un contrato OFB por un Service Domain BIAN. Ejemplo: I1 es *accounts* 2.4.2 contra *SavingsAccount* 14.  
>  
> **E** es la suma de los puntajes de cada par, y **cero** si esa operación OFB no tiene par, dividido entre todas las operaciones OFB.  
> **S** es el promedio de similitud **solo** de los pares oficiales de E.  
> **C** es cuántos Control Record y Behavior Qualifiers tienen al menos un par, sobre el total de CR más BQ del Service Domain. El CR no se cuenta dos veces.  
> El AlignmentScore oficial es el promedio de S, E y C.  
>  
> Lectura: 0,80 o más, Alta. 0,60 a 0,79, Media: hay que declarar tipología. 0,40 a 0,59, Baja. Menos de 0,40, Nula.  
> El EDA ya adelanta que C de I1 tiende a Baja o Nula: 6 GET frente a 10 conceptos BIAN. Hallazgo, no error.

**Acción:** señalar umbral Alta y la fila Nula.

---

## SLIDE 8 · 6:25–7:20 · **Alex**

**Diapositiva:** Criterios verificables de éxito

> Criterios de sí o no, con evidencia.  
>  
> **Hoy, S7:** 41 YAML, cuaderno y protocolo en git. Evidencia: `inventario.json`.  
> **Semana 8, P4:** objetivo 1 firmado **y** I1 más I4 con score v0. Evidencia: `scores.json`.  
> Semana 9: defensa de 8 a 10 minutos con EDA y esas dos instancias.  
> Semana 11: las siete instancias y sensibilidad de pesos.  
> Semana 16, P7: borrador v2; OFB **no** se vende como toda la tesis.  
>  
> Falla el criterio si reportamos BIAN contra BIAN, si inventamos un Service Domain para *loans*, o si no hay commit de la corrida.

**Acción:** señalar “Hoy · S7” como cumplido y “Sem. 8 · P4” como el siguiente sí/no.

---

## SLIDE 9 · 7:20–8:15 · **Alex**

**Diapositiva:** Dos revistas para el artículo

> Dos candidatas, ya fijadas en el Plan v2. Se envía **después** de P5, con scores. No esta semana.  
>  
> Una: *Journal of Web Semantics*, Elsevier. Encaja porque publica schema matching y servicios semánticos. Mandaríamos AlignmentScore y tipologías de desalineación.  
> Dos: *Semantic Web Journal*, IOS Press, acceso abierto. Encaja por web semántica aplicada y reproducibilidad. Mandaríamos el piloto OFB público y el procedimiento S, E, C.  
>  
> No son candidatas de primer envío las revistas de *fuzzing* o solo de regulación de open banking: el objeto no es vulnerabilidades ni OFB.

**Acción:** señalar “Se envía después de P5”.

---

## SLIDE 10 · 8:15–9:10 · **Alex**

**Diapositiva:** Pedido a la sala (cierre navy)

> Pedido concreto a la sala.  
>  
> Uno: el ciclo de 12 semanas en Trello es coherente con el sílabo.  
> Dos: el cuaderno de 41 contratos cuenta como **primer resultado**, no como score final.  
> Tres: las métricas adecuadas son S, E, C y AlignmentScore; no un clasificador.  
> Cuatro: las revistas quedan nominadas; el envío espera a P5.  
>  
> El score v0 de I1 e I4 es la **semana 8**.  
>  
> Preguntas.

**Acción:** dejar el cierre en pantalla.

---

## Si preguntan

| Pregunta | Respuesta corta |
|----------|-----------------|
| ¿Ya tienen el score? | No. Hoy es OE1 + EDA. I1 e I4 en semana 8. |
| ¿Por qué solo I1 e I4 en P4? | Un par de cuentas y un par de pagos; el resto llega en semanas 10–11. |
| ¿Por qué n = 7? | Solo esos YAML tienen par natural BIAN. Las otras 33 APIs son inventario. |
| ¿C de I1 baja es fracaso? | No. 6 GET vs 1 CR + 9 BQ es hallazgo de cobertura. |
| ¿Por qué esas revistas? | Matching semántico y reproducibilidad. No fuzzing ni solo regulación OFB. |
| ¿OFB = la tesis? | No. OFB es el piloto. El objeto es OpenAPI bancario × BIAN. |
