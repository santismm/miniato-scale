# Changelog

## v2.3 — 2026-09-12 — reglas `pilot-0.2` (coherencia texto–resultados tras segunda revisión externa)

- Retirada la afirmación "Tempe tiene el nivel más alto": con 4 frente a ≥ 2 no se deduce un orden; el texto lo dice y explica qué sí distingue a ambos casos.
- "Non-fatal" sustituido por "sin daño físico comunicado en las fuentes examinadas", en coherencia con la regla sobre ausencia de evidencia.
- Frontera R1/R2 definida operativamente (salida frente a decisión), con ejemplo fronterizo y regla de prioridad al máximo.
- Cada hecho del caso de 2026 asignado a la fuente que lo documenta; se explicita que METR no cubre el compromiso posterior de OpenAI.
- Mylius (AIID) y MIT AI Incident Tracker presentados como esfuerzos vinculados, no independientes.
- Estilo: apertura del resumen reformulada sobre la carencia concreta; antítesis reducidas; "Proposition" pasa a "Property".
- Detalle en `docs/decisiones.md` D19.

## v2.2 — 2026-09-12 — reglas `pilot-0.2` (revisión mayor tras crítica externa)

- Ecuación económica con bandas proporcionales a θ; prueba de partición para θ ∈ {10⁶, 3·10⁶, 10⁷, 3·10⁷}.
- Relación con el art. 3(49) del Reglamento de IA reformulada como correspondencia de materia; campo separado en el expediente.
- Caso Hugging Face: cota F ≤ 3 retirada; resultado "≥ 2" con O determinante y R 1–2.
- Tarjeta pública: titular con la clasificación resuelta (punto, conjunto o cota inferior); E como máximo durante el incidente, contención como campo aparte.
- Boletín: unidad de recuento y fechas definidas; pendiente Gutenberg–Richter demotada a exploratoria.
- Regla 2 ampliada; regla 4 renombrada "el esfuerzo de respuesta no es daño" con cuatro tipos de gasto.
- Rúbricas: bandas emparejadas separadas; nueva tabla de E, A y C.
- Antecedentes: Mylius (AIID 2025) y MIT AI Incident Tracker; referencias ACLU (Detroit), US DOT (VSL), Salomon et al. (pesos de discapacidad). 34 referencias.
- Caso sintético etiquetado; F del caso neerlandés acotado por alcance.
- Correcciones editoriales señaladas por la revisión. Detalle en `docs/decisiones.md` D18.

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
