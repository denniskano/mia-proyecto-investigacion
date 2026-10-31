# Revisión de pares — Plan de tesis v2

**Fecha:** 30 oct 2026  
**Documento:** carpeta `plan-tesis-v2/` (MIA 403)  
**Criterios:** sílabo MIA 403 · Guía 1 (LaTeX) · piloto Sesión 5 (`inventario.json`) · consistencia interna  
**Veredicto:** **aprobable con correcciones aplicadas**. El diseño OFB × BIAN es coherente; había errores de cifra, de n muestral y de etiquetas P5/P6 que ya se corrigieron en esta pasada.

---

## Lo que está bien (no tocar)

1. **Objeto vs. muestra vs. referencia.** Objeto = OpenAPI bancario; muestra/piloto = OFB; referencia = BIAN. No se cuelan Nordea, CommBank ni Open Banking UK **en este piloto**.
2. **Continuidad Guía 1.** Se hereda S/E/C, umbrales, P1–P4, H1–H4 y el alcance «Guía 1 = diseño». El OG pasa de *diseñar* a *calcular* — correcto para MIA 403.
3. **Totales del piloto.** 41 / 235 / 6 746 / 10 906 y GET OFB 130/160 coinciden con `inventario.json`. BIAN summary = description 75/75: correcto.
4. **Leakage.** Prohibición de tags CR/BQ en OFB, de autoalineación BIAN↔BIAN y de ML supervisado: alineado con Sesión 5 y con Guía 1.
5. **Pares naturales.** accounts / payments / enrollments frente a los 3 SD del zip es la muestra defendible. Loans/cards quedan como *gap*, no como score inventado.
6. **Código de curso.** MIA 303 → MIA 403 está en el sílabo (prerrequisito).
7. **Ética.** YAML públicos; Ley 29733 no aplica.

---

## Hallazgos (gravedad) y estado

| # | Hallazgo | Gravedad | Estado |
|---|----------|----------|--------|
| 1 | `§6.2` no existía (los pares están en §4.1) | Alta (trazabilidad) | Corregido |
| 2 | I3 era 1 fila y 2 scores: n muestral ambiguo | Alta (método) | Corregido: I3a/I3b, **n = 7** |
| 3 | «Otras 32 APIs»: 38 − 5 YAML = **33** | Media | Corregido |
| 4 | «~88 % props sin description»: el consolidado es **61,9 %** (BIAN 90,4 %; OFB 38,1 %) | Alta (dato) | Corregido; la cifra 88 % venía de las diapositivas de Sesión 5 |
| 5 | «258 Service Domains BIAN» sin fuente en Guía 1 | Media | Corregido: «catálogo completo» |
| 6 | Fórmula de E contradecía E* (promedio solo de emparejadas *y* «sin par aportan 0») | Alta (protocolo) | Corregido: E oficial = media sobre **todas** las ops OFB |
| 7 | Denominador de C = CR + BQ + BO duplicaba el CR | Alta (constructo) | Corregido: catálogo = tags CR + BQ |
| 8 | P5/P6 del cronograma no coincidían con el sílabo (P5 = discusión sem. 12; P6 = borrador v1 sem. 14) | Alta (sílabo) | Corregido |
| 9 | Semana 8 pedía embeddings y a la vez «baseline léxico» | Media | Corregido: S v0 léxico / S v1 embeddings sem. 11 |
| 10 | H4 de la matriz añadía «los pesos no invierten el orden» (no está en el plan) | Baja | Corregido: sensibilidad = análisis, no hipótesis |
| 11 | I1/I2 e I3a/I3b no son independientes | Media (validez) | Declarado en §4.1 y amenazas |
| 12 | Cronograma sem. 1–5 parecía trabajo futuro | Baja | Marcado hecho / pendiente real |
| 13 | Sesión 5 `.md` mezcla EDA del extracto (12 ops) con totales 41/235 | Media (fuera de v2) | Corregido: `02-curso-II/sesion-05/` ya es OFB-only |
| 14 | El plan v2 había **estrechado el objeto** a OFB | Alta (planteamiento) | Corregido (30 oct, pase 2): objeto = OpenAPI bancario; OFB = piloto |

---

## Riesgos que un docente puede preguntar (no son errores)

- **C de I1 será baja:** 6 GET OFB vs. 1 CR + 9 BQ en SavingsAccount. Hay que decirlo en la defensa: parser al 100 % ≠ AlignmentScore Alto.
- **I6 (8 ops) vs. PaymentOrderInitiation (7 behaviors):** la regla greedy 1–1 deja al menos una operación OFB sin par.
- **Validez externa:** el piloto OFB no es un banco peruano ni agota el objeto (OpenAPI bancario).
- **Estado del arte OFB/BCB:** el plan lo deja como tarea de semana 3 (aún no escrito).
- **Figura Cap. II:** §5 es textual; el sílabo pide modelo conceptual.
- **Trámite de Plan de Tesis:** el sílabo asigna 3 puntos a evidencia formal de aprobación a la semana 14. Eso es administrativo, no de contenido.

---

## Criterio de salida de esta revisión

El paquete v2 ya se puede usar como P4 (plan + protocolo + evidencia OE1). Antes de la semana 8 falta: (i) párrafo de estado del arte OFB, (ii) figura del modelo conceptual, (iii) scores v0 de I1 e I4, (iv) limpiar el `.md` de Sesión 5 para que no contradiga el piloto ampliado.

*Grupo 10 · revisión aplicada el 30 oct 2026.*
