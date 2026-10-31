# Libreto — Sesión 6 · Revisión del método

**Presentación:** `Sesion06_Revision_Metodo_slides.pdf` (**11 diapositivas**)  
**Duración:** 8–10 minutos (todas se exponen)  
**Integrantes:** Alex Mancilla · Jack Paitan  
**Regla:** señalar la diapositiva al hablar. Explicar cada sigla la primera vez.

**Frase de ancla:** el objeto de la tesis es *OpenAPI bancario × BIAN*; Open Finance Brasil es solo el piloto.  
**Frase oral:** parser al 100 % **no** implica AlignmentScore Alto.

---

## Antes de empezar

- [ ] PDF de las diapositivas abierto (no el informe)
- [ ] Si preguntan detalle: `protocolo-empirico.md` y `PLAN_TESIS_V2.pdf` §7
- [ ] Reloj: ~45–55 s por lámina; la 3, 4 y 7 pueden ir a 70 s

| Quién | Láminas |
|-------|---------|
| Jack | 1, 3, 4, 5, 6, 8, 10 |
| Alex | 2, 7, 9, 11 |

---

## SLIDE 1 · 0:00–0:40 · **Jack**

**Diapositiva:** Portada — Revisión del método (Capítulo III)

> Buenas [tardes/noches]. Somos el Grupo 10, Alex Mancilla y Jack Paitan.  
>  
> Esta lámina revisa el **Capítulo III**: población, instrumentos, procedimiento, análisis y viabilidad.  
>  
> El **objeto de la tesis** no cambia: medimos qué tan bien coincide un **contrato OpenAPI bancario** — el YAML o JSON con el que un banco publica su API REST — con un **Service Domain BIAN**. BIAN es *Banking Industry Architecture Network*, el modelo de referencia de capacidades bancarias.  
>  
> El **piloto** de este curso es **Open Finance Brasil** — OFB — frente a tres Service Domains BIAN. OFB es un estándar de industria, no el YAML de un banco emisor y no redefine el objeto.

**Acción:** señalar objeto vs piloto en la línea inferior.

---

## SLIDE 2 · 0:40–1:20 · **Alex**

**Diapositiva:** Cinco puntos de la lámina

> El aula pide cinco puntos. Los cubrimos en este orden.  
>  
> Uno: **población, muestra y criterios**. Dos: **técnicas e instrumentos** — artefactos, no encuestas. Tres: un **procedimiento reproducible**. Cuatro: que el análisis corresponda a preguntas, objetivos e hipótesis. Cinco: **evidencia de viabilidad**: ya corrimos el EDA — análisis exploratorio — sobre 41 contratos.  
>  
> Lo que **no** hay todavía es el AlignmentScore. Eso empieza en la semana 8.

**Acción:** señalar los cinco ítems sin leerlos en voz de lista larga.

---

## SLIDE 3 · 1:20–2:25 · **Jack**

**Diapositiva:** Tres capas — no confundir objeto y piloto

> Aquí está el error que queremos evitar. Hay **tres capas**.  
>  
> La **población de la tesis** son los pares posibles *contrato OpenAPI bancario × Service Domain BIAN*. No es “el estándar de un país”.  
>  
> El **universo del piloto** son 38 APIs de Open Finance Brasil más tres Service Domains BIAN versión 14. No es todo el catálogo BIAN.  
>  
> La **muestra de scores** son **siete instancias**, I1 a I6. Las otras 33 APIs de OFB **no** reciben AlignmentScore: solo entran al inventario del objetivo específico 1, la extracción.  
>  
> Incluimos OpenAPI 3.x público y pares naturales de cuentas y pagos. De este piloto **excluimos** YAML de un banco emisor, Open Banking UK e inventar un Service Domain para préstamos.

**Acción:** señalar la fila “Población” y luego “Muestra de scores”.

---

## SLIDE 4 · 2:25–3:20 · **Jack**

**Diapositiva:** Muestra empírica (n = 7)

> Números del corpus: **41** contratos, **235** operaciones, **7** instancias de medición, **33** APIs solo inventario.  
>  
> I1 e I2 usan el mismo YAML de *accounts* 2.4.2: una vez contra *SavingsAccount* y otra contra *CurrentAccount*.  
> I3a e I3b hacen lo mismo con *opendata-accounts*.  
> I4, I5 e I6 cruzan pagos, pagos automáticos y enrolamientos contra *PaymentOrderInitiation*.  
>  
> Importante: I1 con I2, e I3a con I3b, **no son independientes**. Mismo contrato OFB, dos referencias BIAN. Eso se declara en amenazas a la validez.

**Acción:** señalar I1/I2 y la nota de no independencia.

---

## SLIDE 5 · 3:20–4:10 · **Jack**

**Diapositiva:** Recolección — artefactos, no encuestas

> No hay encuestas, ni runtime, ni usuarios. Recolectamos **documentos públicos**.  
>  
> Técnica: adquisición versionada de YAML oficiales en git. Instrumento: el parser `procesar_openapi.py`, que lee OpenAPI 3.x, operaciones, esquemas y referencias anidadas. La salida ya está: el inventario con 41 contratos, 235 operaciones, 6 746 propiedades y 10 906 fragmentos de corpus.  
>  
> Ética: YAML públicos, sin datos personales, citando OFB y BIAN.  
>  
> Aún **no** existen `pares_estructurales.csv` ni `scores.json`. Eso es matching, no recolección.

**Acción:** señalar “Aún no existen” para cortar la pregunta “¿ya tienen el score?”.

---

## SLIDE 6 · 4:10–5:10 · **Jack**

**Diapositiva:** Procedimiento reproducible

> El pipeline es lineal: objetivo específico 1, parsear; 2, score estructural **E**; 3, score semántico **S**; 4, cobertura **C** y el **AlignmentScore**.  
>  
> Es *design science*, cuantitativo sobre documentos. **No** hay aprendizaje supervisado.  
>  
> Baseline de la semana 8: E por Jaccard, path y verbo HTTP; S léxico. Embeddings en la semana 11. El AlignmentScore oficial es el promedio de S, E y C. Una operación OFB **sin par** aporta **cero** a E: no se descarta del denominador.  
>  
> Tres prohibiciones: no puntuar BIAN contra BIAN y llamarlo resultado de banco; no copiar etiquetas CR o BQ — *Control Record* y *Behavior Qualifier* — al CSV de OFB; no etiquetar Alta, Media o Baja a mano para entrenar un clasificador.

**Acción:** señalar la línea “Prohibido”.

---

## SLIDE 7 · 5:10–6:15 · **Alex**

**Diapositiva:** Análisis ↔ preguntas, OE e hipótesis

> Cada pregunta del plan tiene técnica, objetivo e hipótesis.  
>  
> P1, estructura, es el objetivo 2 y la hipótesis 2: schema matching hacia E. Pendiente.  
> P2, semántica, objetivo 3 e hipótesis 3: léxico o embeddings hacia S. Pendiente.  
> P3, tipologías, usa pares más la Tabla 2; hoy solo tenemos EDA.  
> P4, el score, es el objetivo 4 y la hipótesis 4. Pendiente.  
> La pregunta previa — ¿se puede medir? — es el objetivo 1 y la hipótesis 1: **ya está soportada** a nivel de extracción, 41 YAML.  
>  
> La **variable dependiente** del artefacto es AlignmentScore más el nivel: Alta desde 0,80, Media, Baja, y Nula por debajo de 0,40. Los ratios de los objetivos 1 a 3 son parciales: no sustituyen esa variable.

**Acción:** señalar la fila “¿Se puede medir?” y la VD al pie.

---

## SLIDE 8 · 6:15–7:20 · **Jack**

**Diapositiva:** Viabilidad — EDA ya corrido

> La viabilidad de **esta** semana no es un score: es que el procedimiento corre sobre un corpus real.  
>  
> OFB es de consulta: 130 GET de 160 operaciones. BIAN es de control: 36 PUT de 75. Por eso E **no** puede exigir el mismo verbo HTTP.  
> El texto de BIAN es pobre: 90,4 % de propiedades sin *description*. S cae sobre el **nombre**. Además, en las 75 operaciones BIAN el *summary* es igual a la *description*: una sola copia en el corpus.  
> Loans, cards y financings son un *gap* de **referencia**, no de objeto: no inventamos un Service Domain.  
>  
> La cobertura C de I1 será baja: 6 GET frente a 1 Control Record y 9 Behavior Qualifiers. Eso es **hallazgo**, no fallo del parser.

**Acción:** señalar “Gap de referencia” y la nota de C de I1.

---

## SLIDE 9 · 7:20–8:00 · **Alex**

**Diapositiva:** Checklist de la lámina

> Contra los cinco puntos del aula: población y criterios, cubiertos en el Plan v2. Instrumentos, parser y CSV. Procedimiento, el protocolo empírico. Análisis alineado a objetivos e hipótesis, esta lámina 4. Viabilidad, el EDA de la Sesión 5, **sin scores**.  
>  
> El Capítulo III está revisado y es ejecutable. No está “terminada la medición”.

**Acción:** señalar la columna “¿Cubierto?”.

---

## SLIDE 10 · 8:00–8:40 · **Jack**

**Diapositiva:** Qué falta (no es de esta lámina)

> Lo que queda **no** es de esta revisión de método.  
>  
> Semana 7: firmar completitud del objetivo 1 por cada YAML y el matching estructural v0.  
> Semana 8, producto P4: scores v0 de I1 e I4.  
> Semana 9: defensa intermedia.  
> Semanas 10 y 11: las siete instancias con S, E y C.

**Acción:** no detenerse; es puente a Sesión 7 y P4.

---

## SLIDE 11 · 8:40–9:20 · **Alex**

**Diapositiva:** En una frase

> Cierre: el método está revisado y es ejecutable. Población: OpenAPI bancario por BIAN. Muestra: siete instancias OFB. Evidencia de viabilidad: EDA de 41 contratos.  
>  
> El AlignmentScore se calcula a partir de la semana 8.  
>  
> Preguntas.

**Acción:** dejar la frase en pantalla; no pasar a otra lámina.

---

## Si preguntan

| Pregunta | Respuesta corta |
|----------|-----------------|
| ¿OFB es un banco? | No. Estándar de industria. El objeto sigue siendo OpenAPI bancario. |
| ¿Por qué n = 7 y no 41? | Solo I1–I6 tienen par natural. El resto es inventario OE1. |
| ¿Ya tienen AlignmentScore? | No. Parser ≠ score. Semana 8: I1 e I4. |
| ¿Por qué no ML? | No hay etiquetas oro. Etiquetar a mano contaminaría el constructo. |
| ¿Por qué no Open Banking UK? | Queda en el objeto de la tesis; este piloto está congelado en OFB. |
| ¿I1 e I2 cuentan doble? | No son independientes. Se declaran como amenaza, no como 7 bancos distintos. |
