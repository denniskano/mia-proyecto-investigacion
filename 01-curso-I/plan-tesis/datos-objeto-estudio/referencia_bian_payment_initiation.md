# Referencia BIAN — Payment Initiation (ilustrativo)

Ejemplo de **objeto de estudio** contrastado con el contrato OpenAPI en
`ejemplo_openapi_payment_initiation.yaml`. No fija un piloto único del proyecto.

## Pares reducidos (unidad de análisis)

| Elemento OpenAPI | Elemento BIAN (referencia) |
|------------------|----------------------------|
| `POST /payment-orders` | Behavior `Initiate` |
| `GET /payment-orders/{id}` | Behavior `Retrieve` |
| Esquema `PaymentOrder` (`amount`, `currency`) | Business object `Payment` / `PaymentAmount` |

## Service Domain (ilustrativo)

| Tipo BIAN | Elemento de referencia |
|-----------|------------------------|
| Service Domain | Payment Initiation (dominio de pagos) |
| Behavior | `Initiate`, `Retrieve`, `Update` |
| Business object | `PaymentInstruction`, `PaymentAmount`, `Party` |
| Relación de control | Orquestación iniciación → confirmación de estado |

## Lectura bajo el modelo S/E/C

| Score | Qué evaluaría en el extracto |
|-------|-------------------------------|
| **E (StructuralScore)** | Correspondencia `/payment-initiations` ↔ Behavior; anidamiento `components/schemas` ↔ Business object |
| **S (SemanticScore)** | Similitud `instructedAmount/currency` ↔ `PaymentAmount`; `creditor` ↔ `Party` |
| **C (CoverageScore)** | Proporción de Behavior y Business object del SD cubiertos por operaciones y esquemas del fragmento |
