# Tipologías — C04

- **REST/contrato:** OFB privilegia GET de consulta; BIAN publica PUT/POST de ciclo de vida. El matching no exige el mismo verbo.
- **Estructural:** E=0.32 con 4/7 operaciones OFB emparejadas (las no emparejadas entran como 0 al promedio oficial).
- **Semántica:** S=0.03 en baseline léxico (sin embeddings). Los textos OFB están en portugués y los de BIAN en inglés.

Instancia **C04**: `OFB_automatic-payments_2.0.0.yml` × `PaymentOrderInitiation.yaml`. Nivel oficial = pesos 1/3. No se etiquetó a mano para entrenar un clasificador.
