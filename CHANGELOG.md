# Changelog

## v2.1 — 2026-09-12 — reglas `pilot-0.2` (sin cambios de reglas)

- **Renombrado**: AIRA-10 → **Miniato Scale**; marco AIRA → expediente Miniato; boletín AIRA → boletín Miniato. Motivo en `docs/decisiones.md` D15.
- Título del paper: *The Miniato Scale: Communicating the Severity of Artificial Intelligence Incidents and Tracking Their Evolution*.
- Firma: Santiago Miniato Santa María Morales.
- Declaración de asistencia de IA ampliada: Google Gemini 3.6 Flash, OpenAI GPT-5.6 Sol y Anthropic Claude Fable 5.1, con funciones por fase (D17).
- Código renombrado a `miniato.py` / `test_miniato.py`; API sin cambios.

## v2.0 — 2026-09-12 — reglas `pilot-0.2` (nombre AIRA-10)

- Paper reescrito en inglés como preprint arXiv: *AIRA-10: A Public Severity Scale for Artificial Intelligence Incidents and a Bulletin for Tracking Their Evolution*.
- Primera muerte en el nivel 4; mortalidad repartida 1/10/100/1 000/100 000 → 4/5/6/7/8.
- Ancla único θ = 10⁷ € por muerte estadística; ruta económica definida a través de la sanitaria por encima de θ.
- Unidades de daño con lesiones permanentes graves (w = 0,1).
- Regla 2: incidentes contenidos en evaluaciones autorizadas → nivel 0 con etiqueta *peligro*.
- Regla 4: la remediación no cuenta como daño ni lo rebaja.
- Tarjeta pública obligatoria con bandera de control (E ≥ 3) y estado de evidencia.
- Boletín AIRA: recuentos N≥k por periodo, L_max, libro de daños, cobertura, señales de empeoramiento.
- Correspondencia con el art. 3(49) del Reglamento de IA de la UE.
- Rúbricas con ejemplos ancla por dominio.
- Seis casos retrospectivos (niveles 0 a 6), con corrección explícita del error de v1 sobre Hugging Face.
- Código: `health_floor` con lesiones, `economic_floor` con θ, `evaluation_contained`, `control_flag`, `exceedance_counts`. 16 pruebas, enumeración exhaustiva de 9⁶ perfiles, comprobación de alineación de rutas.
- 28 referencias (14 en v1).

## v1.0 — 2026-09-11 — reglas `pilot-0.1` (archivada)

- Marco AIRA (I, E, A, C, D) y proyección AIRA-10 con regla de máximo y condiciones terminales.
- Paper de 17 páginas en español, 14 referencias, implementación Python con 20 pruebas.
- Aplicado en conversación al catálogo METR (44 registros) y al incidente OpenAI–Hugging Face.
- Superada por la crítica de `docs/critica-v1.md`.

## v0 — 2026-09-11 — Escala Santa María Morales 2.1 (retirada)

- Escala continua 0,0–10,0 con techos de 2,0 (digital) y 3,0 (sin muertos), vectores de propagación y modificador CRV.
- Retirada por la crítica de `docs/critica-v0.md`.
