# Tanveer et al., 2025 — Towards Secure APIs: RESTful API Vulnerability Detection

| Campo | Contenido |
|-------|-----------|
| **ID** | E5-04 |
| **Eje** | E5 — Testing y calidad API (borde) |
| **Tipo** | survey |
| **PDF** | `bibliografia/estado-del-arte/Tanveer et al. - 2025 - Towards Secure APIs A Survey on RESTful API Vulnerability Detection.pdf` |
| **Estado ficha** | completada |

## 1. Referencia

- **Autores:** Fatima Tanveer, Faisal Iradat, Waseem Iqbal, Awais Ahmad
- **Año:** 2025
- **Título:** Towards Secure APIs: A Survey on RESTful API Vulnerability Detection
- **Venue / DOI:** Computers, Materials & Continua, Vol. 84(3) · DOI 10.32604/cmc.2025.067536

## 2. Objetivo del estudio

Revisar métodos de **detección de vulnerabilidades** en APIs RESTful; proponer taxonomía específica de fallas REST (autenticación, BOLA, inyección, IDOR, etc.) y analizar análisis estático y pruebas de penetración.

## 3. Dominio y fuente de datos

- **Dominio:** ciberseguridad de APIs REST; incidentes y brechas reportadas en industria.
- **Corpus:** revisión sistemática de literatura y prácticas de detección (static analysis, pentesting, fuzzing de seguridad).

## 4. Técnicas usadas

- Systematic review con taxonomía de vulnerabilidades REST-specific.
- Clasificación de métodos de detección y herramientas.
- Análisis de gaps entre investigación y despliegue práctico.

## 5. Métricas de evaluación

- Análisis cualitativo de cobertura de tipos de vulnerabilidad.
- Estadísticas de brechas industriales citadas; no métricas de alineación semántica.

## 6. Limitaciones (según autores)

- Alcance REST (no GraphQL/SOAP); investigación fragmentada.
- Limitaciones de despliegue de métodos en producción; llamado a metodologías integradas.

## 7. Vacío u oportunidad para OpenAPI–BIAN

**Seguridad operativa** excluida en Cap. 1.5. No evalúa si un contrato refleja el modelo BIAN; útil solo para delimitar E5 y §3.6 (problema distinto al AlignmentScore documental).

## 8. Cita para el plan de tesis

- **Usar en:** §3.5 (E5) · §1.5/§1.6 (exclusión auditoría de seguridad)
- **Frase clave (1 línea):** La detección de vulnerabilidades REST aborda riesgos de seguridad, no la coherencia semántica OpenAPI–BIAN.

## 9. Notas de lectura (opcional, no va al documento final)

- ¿Aporta técnica para S, E o C? **No**.
- ¿Menciona OpenAPI + ontología/esquema? **REST/OpenAPI** en contexto seguridad; **no** BIAN.
