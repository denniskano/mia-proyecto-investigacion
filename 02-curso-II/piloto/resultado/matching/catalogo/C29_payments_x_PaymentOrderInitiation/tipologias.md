# Tipologías — C29

- **REST/contrato:** OFB privilegia GET de consulta; BIAN publica PUT/POST de ciclo de vida. El matching no exige el mismo verbo.
- **De modelado:** el catálogo BIAN tiene 4 CR/BQ y C=0.25. OFB no cubre el desglose de behaviors; hallazgo esperado, no fallo del parser.
- **Estructural:** E=0.29 con 3/6 operaciones OFB emparejadas (las no emparejadas entran como 0 al promedio oficial).
- **Semántica:** S=0.00 en baseline léxico (sin embeddings). Los textos OFB están en portugués y los de BIAN en inglés.

Instancia **C29**: `OFB_payments_4.0.0.yml` × `PaymentOrderInitiation.yaml`. Nivel oficial = pesos 1/3. No se etiquetó a mano para entrenar un clasificador.
