# Tipologías — C17

- **De modelado:** el catálogo BIAN tiene 1 CR/BQ y C=0.00. OFB no cubre el desglose de behaviors; hallazgo esperado, no fallo del parser.
- **Estructural:** E=0.00 con 0/1 operaciones OFB emparejadas (las no emparejadas entran como 0 al promedio oficial).
- **Semántica:** S=0.00 en baseline léxico (sin embeddings). Los textos OFB están en portugués y los de BIAN en inglés.

Instancia **C17**: `OFB_insurances_2.0.0.yml` × `Underwriting.yaml`. Nivel oficial = pesos 1/3. No se etiquetó a mano para entrenar un clasificador.
