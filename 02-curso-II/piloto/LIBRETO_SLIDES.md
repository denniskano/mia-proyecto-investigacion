# Libreto — Piloto OFB × BIAN (16 láminas, 12–14 min)

**Grupo 10** · Alex = marco, objeto, conclusiones · Jack = fuentes, modelos, números  
**PDF:** `Piloto_OFB_BIAN_slides.pdf`  
**Figuras:** `figuras/arquitectura-piloto.png` y `figuras/grafico-{fuentes,alignment,semantico,sec,catalogo}.png`

Decir los números de la lámina. No adelantar el gráfico de la siguiente. Si preguntan por Turnitin (87 % de similitud o el % de IA): es el plan de Guía 1, no este piloto. Si preguntan por Alta: nadie llega a 0,80.

## Abreviaturas

| Sigla | Significado en este piloto |
|---|---|
| OFB | Open Finance Brasil. La muestra: 38 APIs públicas, no un banco emisor. |
| BIAN | Banking Industry Architecture Network. La referencia: catálogo de Service Domains, release 14.0.0. |
| SD | Service Domain. Un dominio de negocio BIAN (SavingsAccount, PaymentOrderInitiation, CreditCard). |
| YAML | El archivo del contrato OpenAPI. OFB y BIAN entran así. |
| JSON | El inventario y la firma de OE1 (`inventario.json`, `oe1_firma.json`). |
| API | La interfaz que describe el contrato. OFB publica 38. |
| HTTP | El verbo de la operación: GET, PUT, POST. E no exige que OFB y BIAN usen el mismo. |
| GET | Consulta. Casi todas las operaciones OFB. |
| PUT | Escritura o control del recurso. Verbo dominante en BIAN. |
| POST | Creación. En I4, `POST /pix/payments` es el que toca el control record. |
| CSV | Tabla plana por contrato que sale del parser. Ahí no se copian tags CR/BQ. |
| OE1 | Objetivo específico 1: normalizar. En el piloto es el parser y la firma 296/296. |
| S | SemanticScore. Similitud de significado, solo sobre los pares que ya armó E. |
| E | StructuralScore. Emparejamiento greedy uno a uno de operaciones. Sin par, entra como 0. |
| C | CoverageScore. Cobertura del catálogo del SD: CR y BQ con par, sobre el total de CR y BQ. |
| v0 | Corrida léxica (Jaccard + TF-IDF). Las siete instancias quedan Nula. |
| v1 | La misma E y la misma C. Solo cambia S, con MiniLM. |
| MiniLM | `paraphrase-multilingual-MiniLM-L12-v2`. Embeddings de frase que cruzan portugués y inglés. |
| TF-IDF | Peso léxico de un token según cuánto se repite en el texto y cuán raro es en el corpus. Baseline de S v0, junto con Jaccard. |
| GPU | Tarjeta gráfica. v0 no la usa. |
| GPT | Modelo generativo. No entra en el piloto. |
| BERT | Modelo de lenguaje que aquí no se entrena. MiniLM es un primo chico y ya viene entrenado; no lo ajustamos. |
| CR | Control Record. Ficha principal del Service Domain. En el YAML de BIAN el tag es `CR - …`. |
| BQ | Behavior Qualifier. Comportamiento alrededor de esa ficha (cargo, depósito). Tag `BQ - …`. |
| I1–I6 | Las siete instancias oficiales. I3 se parte en I3a (Savings) e I3b (Current). |
| FIDO | Fast Identity Online. Mecanismo de enrollments: alta de un dispositivo, no una orden de pago. |
| Pix | Sistema brasileño de pagos instantáneos. En I4, `POST /pix/payments`. |
| IA | En la pregunta de Turnitin: texto marcado como escrito con inteligencia artificial. Es el plan de Guía 1, no estas láminas. |
| n | Tamaño de la muestra oficial: 7 instancias (I1, I2, I3a, I3b, I4, I5, I6). |
| `$ref` | Referencia interna de OpenAPI a un schema ya definido. El parser las resuelve. |
| PDF | Este libreto acompaña a `Piloto_OFB_BIAN_slides.pdf`. |

| # | Lámina | Quién | Tiempo |
|---|--------|-------|--------|
| 1 | Portada | Alex | 0:30 |
| 2 | Lo que entrega | Alex | 0:50 |
| 3 | Objeto vs piloto | Alex | 0:50 |
| 4 | Arquitectura | Jack | 1:00 |
| 5 | Fuentes | Jack | 0:50 |
| 6 | OE1 | Jack | 0:45 |
| 7 | Fórmula | Jack | 1:00 |
| 8 | Modelos | Jack | 0:50 |
| 9 | n = 7 | Jack | 0:40 |
| 10 | AlignmentScore | Jack | 0:50 |
| 11 | S léxico vs MiniLM | Jack | 0:45 |
| 12 | S / E / C | Jack | 0:45 |
| 13 | I1, I4, I6 | Jack | 1:10 |
| 14 | Catálogo extra | Jack | 0:40 |
| 15 | Conclusiones | Alex | 0:50 |
| 16 | Líneas | Alex | 0:40 |

---

## 1. Portada — Alex (0:30)

Buenas. Somos el Grupo 10, Alex Mancilla y Jack Paitan. En Guía 1 diseñamos cómo se mediría la alineación. Hoy el piloto ya la mide: un contrato OpenAPI bancario contra un Service Domain de BIAN v14.

La muestra es Open Finance Brasil. La referencia es el catálogo oficial, 258 Service Domains. Tres condiciones en la franja de abajo: catálogo real, score reproducible, sin leakage.

## 2. Lo que el piloto ya entrega — Alex (0:50)

Señalar los cuatro números de izquierda a derecha.

296 YAML firmados: 38 de OFB más 258 de BIAN. 258 Service Domains oficiales, no un recorte. Siete instancias I1 a I6, porque I3 se parte en dos. Cinco de esas siete pasan a Baja cuando el SemanticScore deja de ser léxico y pasa a MiniLM.

Abajo, tres precisiones. El parser OE1 firma 296 de 296: operaciones y schemas extraídos sobre esperados dan 1,00. El AlignmentScore es el promedio de S, E y C, con umbrales fijos; nadie etiquetó Alta, Media, Baja o Nula a mano. MiniLM corre sobre los mismos pares estructurales, no arma pares nuevos. El primer Baja fuera de esas siete es credit-cards contra CreditCard, 0,46: lo retomamos en la lámina 14.

## 3. Objeto intacto · piloto acotado — Alex (0:50)

Leer la tabla por filas, no de memoria.

El objeto de la tesis sigue siendo el contrato OpenAPI bancario. No cambió. La referencia es el catálogo BIAN v14. OFB es la muestra: 38 APIs, la última estable. La unidad que recibe un score es una instancia, un YAML de OFB emparejado con un Service Domain, no el catálogo entero.

La fila «No entra» hay que decirla: no hay YAML de un banco emisor, no inventamos un Service Domain, y no puntuamos las 38 APIs contra los 258 dominios. OFB no redefine la tesis. Es el corpus público con el que se ejecuta el procedimiento.

## 4. Cómo se trabajó — Jack (1:00)

Recorrer la figura de izquierda a derecha. Cuatro columnas.

Fuentes oficiales: OFB, 38 YAML y 160 operaciones; BIAN v14, 258 dominios y 4 580 operaciones, bajados con `descargar_bian.py` del release 14.0.0. La caja dorada de esa columna es la regla: sin banco emisor, sin recorte de 12 operaciones, sin inventar un SD.

Parser OE1: `procesar_openapi.py` saca paths, métodos, schemas y el corpus. La caja verde es la firma, 296 de 296. Parser al 100 % habilita la medida. No es un AlignmentScore Alto.

Matching, tres cajas. `matching_v0.py` es el baseline de las siete instancias: S léxico, E greedy, C sobre CR y BQ. La caja dorada es `matching_s1.py`: MiniLM solo recalcula S, sobre pares ya congelados; E y C no se tocan. `mapa_ofb_bian.py` es el catálogo extra (loans, cards) y no sustituye esas siete.

Scores: el promedio (S + E + C) / 3 y las carpetas `resultado/matching`, `matching_s1` y `catalogo`. La franja de abajo es lo que no hicimos: copiar tags CR/BQ al CSV de OFB, puntuar BIAN contra BIAN, inventar un SD, etiquetar el nivel a mano, ni cruzar 38 por 258.

## 5. Fuentes — Jack (0:50)

Señalar el gráfico y la lista de la izquierda.

OFB aporta 38 YAML y 160 operaciones, casi todas GET: es una API de consulta. BIAN aporta 258 Service Domains y 4 580 operaciones, con PUT dominante: es un modelo de control del recurso. Por eso el StructuralScore no exige el mismo verbo HTTP. Si exigiéramos GET = GET, OFB saldría en cero por diseño del estándar, no por desalineación.

160 contra 4 580 es asimetría de catálogo, no un error de descarga. No recortamos 12 operaciones y no metimos el YAML de un banco emisor.

## 6. Procesamiento OE1 — Jack (0:45)

Cuatro pasos, en orden. `descargar_bian.py` baja los 258 OpenAPI oficiales. `procesar_openapi.py` lee paths, methods, schemas, `$ref` y el corpus. La firma es contrato a contrato: extraídos dividido esperados. Sale 1,00. Lo que queda en disco es CSV, `inventario.json` y `oe1_firma.json`.

La tabla son tres controles, no el universo. accounts 2.4.2: 6 de 6 operaciones y 31 de 31 schemas. payments 4.0.0: 6 de 6 y 56 de 56. Loan.yaml y CreditCard.yaml ya están en disco: 24 de 24 y 28 de 28. Esos dos importan en la lámina 14: el hueco de préstamos y tarjetas no era que BIAN no los publicara.

Cerrar con la frase de la lámina: parser al 100 % no implica AlignmentScore Alto. Solo habilita medir.

## 7. Qué se mide — Jack (1:00)

Cuatro definiciones, y después la tabla de umbrales.

E es el StructuralScore. El emparejamiento es greedy y uno a uno: cada operación OFB busca como máximo un behavior BIAN. Si no hay par, esa operación entra como 0 y baja el promedio. No se tira.

S es el SemanticScore. Solo se calcula sobre los pares que E ya aceptó. No hay pares semánticos sueltos. Si E no emparejó, MiniLM no inventa el par.

C es la cobertura del Service Domain. CR es el control record, la ficha principal del dominio. BQ son los behavior qualifiers, el desglose de comportamientos. C es cuántos de esos CR y BQ tienen par, dividido el total de CR y BQ del SD. No se calcula con los tags de OFB.

AlignmentScore es el promedio simple: (S + E + C) / 3. Los pesos iguales están fijos en este piloto.

Umbrales, de arriba abajo. Desde 0,80, Alta: cobertura usable del SD. De 0,60 a 0,79, Media. De 0,40 a 0,59, Baja: hay desalineación dominante, pero ya hay correspondencia. Debajo de 0,40, Nula. El nivel sale del umbral. No hay un modelo que clasifique.

## 8. Modelos — Jack (0:50)

Leer la tabla por filas.

S v0 es Jaccard más TF-IDF: baseline léxico, sin GPU. Sirve de techo. S v1 es MiniLM-L12 multilingual (`paraphrase-multilingual-MiniLM-L12-v2`) porque OFB está en portugués y BIAN en inglés. E son reglas de nombre, path y verbo HTTP, y otra vez: GET no tiene que ser PUT. C es el ratio de CR y BQ del YAML de BIAN, no de los tags de OFB. El nivel usa 0,80, 0,60 y 0,40, sin etiquetas a mano.

La frase de abajo es la que defiende el diseño. MiniLM corre sobre los pares de E. No reabre el matching. No es un clasificador. El piloto mide. No usamos GPT, no entrenamos un BERT, y no puntuamos BIAN contra BIAN.

## 9. Siete instancias — Jack (0:40)

Esta es la muestra oficial. No es un muestreo estadístico de las 38 APIs.

I1: accounts 2.4.2 contra SavingsAccount. I2: el mismo accounts contra CurrentAccount. I3a y I3b: opendata-accounts 1.0.1 contra Savings y contra Current. I4: payments 4.0.0 contra PaymentOrderInitiation. I5: automatic-payments 2.0.0 contra el mismo PaymentOrderInitiation. I6: enrollments 2.1.0 contra PaymentOrderInitiation, a propósito un par que no debería alinear.

I1 con I2, e I3a con I3b, comparten YAML. Esos scores no son siete observaciones independientes. El mapa extra de la lámina 14 no sustituye estas siete: I1 a I6 se quedan.

## 10. AlignmentScore — Jack (0:50)

Señalar las dos series del gráfico. v0 es la barra o el punto léxico. v1 es MiniLM.

En v0 las siete quedan Nula. El léxico portugués contra inglés no pasa de 0,40. En v1, I1, I2, I3a, I3b e I5 cruzan 0,40 y quedan en Baja. I4 se queda Nula, en 0,35. I6 sigue en 0.

Los números, por si preguntan: I1 sube de 0,26 a 0,44. I2 de 0,33 a 0,50. I3a y I3b de 0,25 a 0,41. I5 de 0,28 a 0,47. I4 de 0,18 a 0,35, y no cruza. I6 se queda en 0,00. E y C son los mismos en v0 y en v1. Lo que se mueve es S.

Nadie llega a 0,80. No vamos a llamar a esto un éxito de cobertura.

## 11. Por qué MiniLM — Jack (0:45)

El gráfico compara S léxico contra S MiniLM en las mismas instancias.

Jaccard y TF-IDF comparan bolsas de tokens. `conta` no es el string `SavingsAccountFacility`, así que S v0 queda en 0,00 o 0,01. MiniLM pone esos textos en un espacio común y el coseno sube: en I1, S pasa de 0,01 a 0,56. El S oficial es el promedio del coseno de los pares estructurales. Un umbral interno de 0,55 se reporta como sensibilidad; no recorta ese promedio.

MiniLM no reabre E. Si el greedy emparejó mal, el coseno se calcula igual sobre ese par.

## 12. E y C ya existían — Jack (0:45)

El gráfico desarma el promedio. Había estructura. S era el cuello de botella.

I3a y I3b tienen E = 0,56, que es 2 de 2 pares, y C = 0,20. Open data cubre poco del Service Domain: el SD de cuentas tiene del orden de 10 CR/BQ y el YAML abierto solo toca una parte. Por eso el promedio se queda justo encima de 0,40 aunque S ya no es cero.

I6 en cero no es un fallo del parser. Es un rechazo: enrollments no comparte recurso con PaymentOrderInitiation. Lo vemos en la lámina siguiente.

## 13. I1, I4 e I6 — Jack (1:10)

Los 0,26 y 0,18 de los títulos son el AlignmentScore v0. El emparejamiento es el de E, y E no cambió con MiniLM. I1 en v1 ya es Baja (0,44). El problema del greedy sigue ahí.

I1, accounts contra SavingsAccount. GET /accounts cae en Retrieve, y ese sí es el control record. El path con accountId cae en RetrieveCharge. El de balances cae en RetrieveDeposit. Charge no es la ficha de la cuenta. El greedy igual lo cuenta, y eso infla C: hay un par, pero el par es el behavior equivocado.

I4, payments contra PaymentOrderInitiation. POST /pix/payments sí toca Initiate, el control record. GET del paymentId cae en Retrieve. Las dos operaciones de /consents se quedan sin par. El consentimiento de OFB no es un behavior qualifier de Payment Order. Por eso C = 0,25 y, aunque S sube a 0,52, el promedio v1 queda en 0,35, Nula.

I6 = 0. enrollments es FIDO, un alta de dispositivo. PaymentOrderInitiation es una orden de pago. No comparten recurso. Cero pares es el instrumento rechazando un par falso, no un archivo que no se parseó.

## 14. Catálogo extra — Jack (0:40)

Señalar el gráfico. La lectura es una sola: el hueco de loans y cards era de disco, no de BIAN.

`Loan.yaml` y `CreditCard.yaml` son oficiales del release 14. En la lámina 6 ya estaban firmados. Al emparejarlos, credit-cards contra CreditCard da 0,46, Baja, con 7 de 7 pares. loans contra Loan queda Nula, 0,27, 4 de 5 pares. opendata-loans y opendata-creditcards también quedan Nula (0,28 y 0,30). investments contra InvestmentAccount, 0,19.

I1 a I6 no se reemplazan con esta tabla. Y no se puntúa 38 por 258. Hay APIs OFB sin par natural en este mapa: admin, common, resources, webhook, participants, capitalization-bonds, credit-fixed-incomes. Esas se quedan en el inventario.

## 15. Qué se concluye — Alex (0:50)

Cuatro frases, en el orden de la lámina.

El procedimiento S/E/C ya corre sobre un corpus público, versionado y firmado. Nula en v0 es un hallazgo: es el techo del léxico portugués contra inglés. MiniLM mueve cinco instancias a Baja sin leakage, porque no reabre los pares ni copia tags de BIAN a OFB. I6 en cero valida el instrumento: rechaza un par que no comparte recurso. credit-cards contra CreditCard, 0,46 Baja, muestra que el Service Domain existía; faltaba descargarlo.

Nula o Baja no tumba el piloto. Muestra que el score se puede calcular y se puede leer.

## 16. Líneas que no cruzamos — Alex (0:40)

Cuatro prohibiciones, y el cierre.

No copiamos tags CR/BQ al CSV de OFB: eso sería leakage, el contrato «sabría» la respuesta. No puntuamos BIAN contra BIAN para llamarlo un banco. No inventamos un Service Domain y no hacemos el producto 38 por 258. No entrenamos un clasificador de Alta, Media, Baja y Nula con etiquetas a mano.

Cierre: el piloto mide alineación. No produce un modelo que aprenda el nivel.

---

## Si preguntan

**Turnitin, 87 % o el porcentaje de IA.** Es el plan de Guía 1 ya enviado, no este piloto.

**¿Por qué no hay Alta?** El umbral es 0,80. El mejor oficial es I2 en 0,50. credit-cards llega a 0,46. El piloto no sube el umbral para fabricar un Alta.

**¿I1 es Nula o Baja?** Nula en v0 (0,26). Baja en v1 (0,44). La lámina 13 muestra el greedy, que es el mismo en las dos versiones.

**¿Por qué I1 e I2 no suman como dos bancos?** Comparten el YAML accounts 2.4.2. Cambian el Service Domain, no el contrato.
