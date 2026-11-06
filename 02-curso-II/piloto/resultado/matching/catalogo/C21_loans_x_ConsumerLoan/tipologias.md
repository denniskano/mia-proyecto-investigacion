# Tipologías — C21

- **De modelado:** el catálogo BIAN tiene 11 CR/BQ y C=0.18. OFB no cubre el desglose de behaviors; hallazgo esperado, no fallo del parser.
- **Estructural:** E=0.14 con 2/5 operaciones OFB emparejadas (las no emparejadas entran como 0 al promedio oficial).
- **Semántica:** S=0.00 en baseline léxico (sin embeddings). Los textos OFB están en portugués y los de BIAN en inglés.

Instancia **C21**: `OFB_loans_2.5.0.yml` × `ConsumerLoan.yaml`. Nivel oficial = pesos 1/3. No se etiquetó a mano para entrenar un clasificador.
