# Cronograma 16 semanas — MIA 403 (Trello)

**Grupo 10** · Alex Mancilla Antay · Dennis Jack Paitan Cano  
**Tablero sugerido:** listas `Backlog` · `Semana N` · `En curso` · `Hecho` · `Bloqueado`  
**Etiquetas:** `P1`–`P7` (producto sílabo) · `OE1`–`OE4` · `OFB` · `BIAN` · `defensa`

El ciclo empírico de 12 semanas del PPT (`Plan_Tesis_AlineacionBIAN.pptx`) se **superpone** a las semanas 5–16 del sílabo: S1–S4 del PPT ya ocurrieron en Sesión 5 (pares + parser + EDA).

---

## Productos del sílabo

| ID | Producto | Semana | Estado al abrir v2 |
|----|----------|--------|--------------------|
| P1 | Diagnóstico + hoja de ruta | 1 | Este plan §2 + este cronograma |
| P2 | Capítulo I + estado del arte | 3 | Objeto intacto + piloto OFB en `PLAN_TESIS_V2.md` §3 |
| P3 | Marco + consistencia + método | 6 | §5–7 + `matriz-consistencia-ofb.md` |
| P4 | Plan de Tesis + piloto + protocolo | 8 | Carpeta `plan-tesis-v2/` + Sesión 5 |
| — | Defensa intermedia | 9 | Exposición del plan + evidencia OE1 |
| P5 | Resultados y discusión avanzados | 12 | Pendiente (ejecución) |
| P6 | Borrador integral v1 + Turnitin | 14 | Pendiente |
| P7 | Borrador integral v2 + defensa | 16 | Pendiente |

---

## Semanas 1–8 — Plan + piloto (hasta defensa intermedia)

| Sem. | Meta sílabo | Tarjetas Trello | Dueño | Hecho cuando |
|------|-------------|-----------------|-------|--------------|
| 1 | Diagnóstico | Objeto = OpenAPI bancario; **piloto = OFB**; listar brechas Guía 1 | Alex | **Hecho** en esta carpeta (`diagnostico-guia1-a-guia2.md`) |
| 2 | Cap. I | Reescribir problema/OG/OE con instancia `OFB × SD` | Alex | **Hecho** (`PLAN_TESIS_V2.md` §3) |
| 3 | Estado del arte | Añadir fila OFB vs. open banking al Anexo B (no rehacer 14 papers) | Alex | Pendiente: 1 párrafo + 2–3 citas OFB/BCB |
| 4 | Cap. II | Modelo conceptual OFB (REST GET) vs. BIAN (CR/BQ) | Jack | **Borrador** §5; falta figura propia |
| 5 | Operacionalización | Matriz 8 cols OFB; congelar I1–I6 (n = 7 scores) | Jack | **Hecho** (`matriz-consistencia-ofb.md`) |
| 6 | Cap. III | Diseño ejecutable; amenazas actualizadas | Jack | **Hecho** (`sesion-06/` + §7 + `protocolo-empirico.md`) |
| 7 | Protocolo | Congelar versiones; baseline estructural (sin embeddings) | Jack | **Hecho** (papel: `sesion-07/` + protocolo v1); falta script matching v0 |
| 8 | **P4** | Plan PDF + piloto OE1 + **I1 e I4 con score v0** | Ambos | Entrega aula + zip piloto |

**Criterio de la semana 8:** no hace falta AlignmentScore definitivo de las 6 instancias; sí I1 (`accounts` × SavingsAccount) e I4 (`payments` × PaymentOrderInitiation).

---

## Semana 9 — Defensa intermedia

| Tarjeta | Contenido (8–10 min) |
|---------|----------------------|
| Slide 1 | Título (OpenAPI bancario ↔ BIAN) + piloto OFB |
| Slide 2 | Continuidad Guía 1 → Guía 2 |
| Slide 3 | Pregunta + OG + VD = AlignmentScore |
| Slide 4 | Piloto: 38 OFB + 3 BIAN; pares I1–I6 |
| Slide 5 | EDA: GET vs PUT; leakage CR/BQ; summary=description |
| Slide 6 | I1 e I4: S, E, C, score v0 (aunque sea baseline) |
| Slide 7 | Amenazas + lo que **no** se mide (loans sin SD) |
| Slide 8 | Hoja de ruta 10–16 |

---

## Semanas 10–16 — Ejecución (alineado al sílabo)

| Sem. | Meta sílabo | Tarjetas | Dueño | Entrega |
|------|-------------|----------|-------|---------|
| 10 | Evidencia reproducible | OE2 estructural en las 7 instancias; baseline token + ruta + HTTP | Jack | `E_por_instancia.csv` |
| 11 | Resultados v1 | OE3 (embeddings) + OE4 (C, AlignmentScore, sensibilidad) | Jack | Tablas de las 7 instancias |
| 12 | **P5** Discusión | Tipologías, contraste con literatura, limitaciones, validez | Alex | Cap. discusión v1 |
| 13 | Borrador integral v1 | Integrar Caps. I–III + resultados + discusión | Ambos | Borrador v1 |
| 14 | **P6** + Turnitin | Conclusiones, formato, Turnitin | Ambos | Borrador v1 completo |
| 15 | Defensa simulada | Ensayo 12–15 min; *short paper* opcional | Ambos | Observaciones atendidas |
| 16 | **P7** | Defensa final + evidencias | Ambos | Borrador v2 + repo |

---

## Tablero Trello (columnas y WIP)

```
Backlog → Semana actual → En curso (WIP=2) → Revisión pareja → Hecho → Bloqueado
```

**Tarjetas permanentes (no borrar)**

- `LEAKAGE` — no copiar tags CR/BQ a OFB; no puntuar BIAN↔BIAN como resultado.
- `VERSIONES` — freeze: accounts 2.4.2, payments 4.0.0, BIAN 14.0.0.
- `PARES` — solo I1–I6 reciben AlignmentScore; el resto es inventario OE1.
- `SIN-ML` — no etiquetar Alta/Media/Baja a mano para entrenar.

---

## Dependencias

```
Sesión 5 (OE1 + EDA)
        │
        ▼
Plan v2 (P4) ──► Defensa sem. 9
        │
        ├── OE2 (E) ──┐
        └── OE3 (S) ──┼──► OE4 (C + AlignmentScore) ──► P5–P7
                      │
              catálogo BIAN del SD
```

Si en semana 10–11 falta un SD BIAN para loans/cards: **no** se inventa el par; se documenta como gap (ya en Sesión 5).
