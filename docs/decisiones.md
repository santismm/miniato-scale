# Decisiones de diseño

Registro de decisiones con las alternativas descartadas y el motivo. Formato breve tipo ADR. Numeración estable; una decisión revertida se marca, no se borra.

## D1. Medir consecuencias materializadas, no riesgo

**Decisión.** El índice clasifica daño ocurrido hasta una fecha de corte.
**Alternativas.** Índice de riesgo (probabilidad × magnitud, como NIST); índice de "peligrosidad" del comportamiento.
**Motivo.** Un número que unas veces significa daño y otras miedo no puede interpretarse de forma uniforme ni contarse en el tiempo. El riesgo y la urgencia se comunican por separado (D5, D6).

## D2. Regla de máximo, sin compensación

**Decisión.** Nivel = máximo entre los seis dominios.
**Alternativas.** Media aritmética; suma ponderada; modelo compuesto tipo JRC.
**Motivo.** Ningún ámbito indemne debe diluir un daño grave. El perfil (5,3,2,4,0,0) daría 2,3 de media; el máximo da 5. Coste asumido: pierde amplitud (un 5 en un dominio y seis 5 empatan). El expediente conserva el vector y el boletín restaura magnitud en unidades nativas.

## D3. Enteros de 0 a 10, ordinal, sin decimales

**Decisión.** Once categorías enteras.
**Alternativas.** Escala continua 0,0–10,0 (v0); escala abierta sin techo; escala 0–1000.
**Motivo.** Los decimales aportaban apariencia de resolución sin rúbrica que los distinguiera. Una escala sin techo o de 0–1000 pierde la comunicabilidad que era el objetivo. El 10 fijo es una elección del autor (D8).

## D4. Un solo ancla θ = 10⁷ € por muerte estadística

**Decisión.** La ruta económica se define a través de la sanitaria por encima de θ.
**Alternativas.** Tablas independientes (v1, con ratios implícitos de 10⁹ a 10¹⁰ €/muerte); ratio mucho mayor para que la muerte domine siempre.
**Motivo.** Un ratio inconsistente entre niveles es un defecto, no una postura. θ está en el orden de los valores estadísticos de vida regulatorios y es un parámetro declarado que el programa de validación varía. Compartir nivel no declara equivalencia moral.

## D5. E, A y C fuera de la fórmula

**Decisión.** Control, autonomía y confianza se muestran, no se suman.
**Alternativas.** Sumar puntos por autonomía o por evasión (v0); descontar por baja confianza.
**Motivo.** Sumar autonomía inflaría incidentes sin daño; descontar por confianza convertiría una posible catástrofe con evidencia incompleta en un incidente moderado. La confianza se expresa como conjunto de niveles admisibles (D7).

## D6. Tarjeta obligatoria con bandera de control

**Decisión.** La cifra nunca se publica sola. Bandera cuando E ≥ 3.
**Alternativas.** Solo cifra; dos cifras (daño y riesgo) compitiendo.
**Motivo.** Descubierto al aplicar v1 al caso Hugging Face: "AIRA 3" sonaba a "no fue para tanto" en un incidente con pérdida grave de control. Dos cifras confundirían; una cifra y un estado no.

## D7. Conjuntos de niveles admisibles, no probabilidades

**Decisión.** Si la evidencia no fija un nivel, se publica {2, 3}, no "3 con 85 %".
**Alternativas.** Punto estimado con confianza numérica; desconocido = 0.
**Motivo.** No hay base para probabilidades calibradas. Un desconocido tratado como 0 es la mentira más frecuente en catálogos de incidentes.

## D8. 9 y 10 como anclas lógicas

**Decisión.** 9 = extinción humana o colapso global irreversible de ecosistemas complejos; 10 = extinción humana y desaparición de toda vida terrestre.
**Alternativas.** 10 = extinción humana; sacar lo existencial fuera de la escala numérica; escala sin techo.
**Motivo.** El autor definió el 10 como aniquilación de toda vida. Se acepta el coste de dos categorías inobservables y se declara en el paper.

## D9. Primera muerte en el nivel 4

**Decisión.** 1–9 unidades de daño → 4; 10 → 5; 100 → 6; 1 000 → 7; 100 000 → 8.
**Alternativas.** Primera muerte en el 5 (v1); en el 3.
**Motivo.** En v1 el rango realista se comprimía en 0–3 y el 7 abarcaba tres órdenes de magnitud. Con esta distribución, el tramo que sí ocurre (1 a 100 000 muertes) ocupa cinco escalones y la frase pública "a partir del 4 alguien ha muerto" es memorable.

## D10. Lesiones permanentes graves con peso 0,1

**Decisión.** U = muertes + 0,1 × lesiones permanentes graves; cualquier lesión permanente grave es al menos 3.
**Alternativas.** No cuantificar lesiones (v1); pesos por tipo de lesión.
**Motivo.** Sin regla, un incidente con 500 amputaciones y cero muertos quedaba sin ruta numérica. 0,1 es una convención declarada, del orden de los pesos de discapacidad, y se varía en la validación.

## D11. Regla 2: incidentes contenidos en evaluaciones son nivel 0 con etiqueta *peligro*

**Decisión.** Reward hacking y manipulación de tests dentro de un perímetro autorizado no son daño.
**Alternativas.** Nivel 1 por "integridad experimental comprometida" (como se hizo en la conversación con el catálogo METR); excluirlos del registro.
**Motivo.** Inflarlos convierte el catálogo en ruido; excluirlos oculta la clase de comportamiento más documentada. Nivel 0 con E y A visibles conserva la señal sin fingir daño. Si el sistema sale del perímetro, es vulneración (regla 1).

## D12. Regla 4: la remediación no cuenta ni descuenta

**Decisión.** El coste de la respuesta no eleva el nivel; reparar no lo baja.
**Motivo.** Sin esta regla, una organización que responde con fuerza parece haber sufrido más daño, y una que repara rápido parece no haberlo sufrido. Descubierto al puntuar mal el caso Hugging Face en v1.

## D13. Tendencias por recuentos de superación, no por promedios

**Decisión.** El boletín publica N≥k por periodo, L_max y libro de daños en unidades nativas.
**Alternativas.** Media de AIRA-10; índice acumulado ponderado.
**Motivo.** Un ordinal no se promedia. La sismología resolvió esto con la relación frecuencia–magnitud de Gutenberg y Richter. Se exige declarar cobertura para no confundir más reporte con más daño.

## D14. Inglés como idioma del paper

**Decisión.** Paper en inglés con resumen en español; documentación del repositorio en español.
**Motivo.** El objetivo declarado es la adopción internacional. El autor y su comunidad inmediata leen en español.

## D15. Nombre: Miniato Scale (sustituye a AIRA-10)

**Decisión (v2.1).** La escala pública se llama *Miniato Scale*; el expediente, *Miniato record*; el boletín, *Miniato bulletin*. Uso previsto: "a Miniato 4 incident".
**Decisión anterior (v1, v2.0, revertida).** AIRA-10 (*AI Incident Rating & Assessment*), con el argumento de poner primero el problema y después la autoría.
**Alternativas evaluadas.** Santa María Scale; Santa María–Morales Scale; Madrid Scale; Santiago Scale; Morales Scale.
**Motivo.**
- AIRA ya está ocupado en el mismo espacio conceptual: *Artificial Intelligence Risk Assessment* (informe de la UIT), *AI-Induced Risk Audit* (arXiv 2026), *AI Integrated Risk Architecture*, una certificación sanitaria y varios productos de *AI readiness*. Un acrónimo congestionado impide que alguien diga "fue un X 6" sin ambigüedad.
- Las escalas que la cultura retiene llevan nombre de persona o lugar (Richter, Mercalli, Beaufort, Fujita, Torino, Palermo). El nombre no explica la fórmula; se convierte en concepto.
- Entre los apellidos del autor, *Santa María* arrastra la carabela de Colón (miles de páginas de "Santa Maria scale model 1:65"), un volcán activo en Guatemala y decenas de ciudades. *Morales* y *Santiago* son demasiado frecuentes; *Santiago* además parece topónimo. *Madrid* exigiría un acto fundacional en Madrid que no ha ocurrido.
- *Miniato* no tiene ninguna escala homónima en ciencia, técnica ni IA. El único ruido es San Miniato (Toscana), que no compite. Fonéticamente encaja con Mercalli, Fujita, Palermo. Permite construir la entidad semántica desde cero.
**Revisión del razonamiento aportado (Claude, 12 sept 2026).** El desempate es correcto y lo suscribo. Tres matices: (1) el razonamiento incluía una quinta dimensión, "engaño/detectabilidad", y unas etiquetas de nivel (4 Severe, 5 Critical) que no forman parte de `pilot-0.2`; no se adoptan, la calibración v2 se mantiene íntegra; (2) proponía "Miniato 3" para el caso Hugging Face, pero bajo `pilot-0.2` el resultado es {2, 3} con bandera de control; (3) ninguna búsqueda hecha confirma disponibilidad de marca; eso exige consultar EUIPO, OMPI y USPTO, y sigue pendiente. Que el autor nombre la escala con su propio apellido es legítimo y tiene precedente: Torino y Palermo fueron bautizadas por sus proponentes.
**Consecuencia.** La firma del paper pasa a "Santiago Miniato Santa María Morales" para que la genealogía del nombre sea transparente.

## D16. Licencias: CC BY 4.0 para texto, MIT para código

**Decisión (12 sept 2026).** Paper, documentación y archivo bajo CC BY 4.0; código bajo MIT.
**Alternativas.** Sin licencia (todos los derechos reservados); Apache-2.0 para el código; CC BY-SA.
**Motivo.** Una escala que aspira a adoptarse necesita poder reutilizarse con atribución obligatoria: eso es CC BY. Apache-2.0 añade una cláusula de patentes irrelevante para un código de referencia de 200 líneas. CC BY-SA obligaría a derivados a la misma licencia y frenaría su uso en documentos institucionales.

## D17. Declarar el proceso multimodelo como parte del método

**Decisión.** El paper nombra los tres modelos usados (Google Gemini 3.6 Flash, OpenAI GPT-5.6 Sol, Anthropic Claude Fable 5.1) y las funciones de cada uno por fase, y afirma que no son autores.
**Alternativas.** Declaración genérica ("se usaron modelos de lenguaje"); omitirla; listar los modelos como coautores.
**Motivo.** Una declaración genérica oculta algo científicamente interesante: una metodología humana construida mediante crítica y formalización adversarial entre modelos distintos. Listar modelos como coautores es incorrecto: no pueden asumir responsabilidad. El reparto de funciones se declara "según lo registra el autor de sus historiales", porque ningún modelo puede verificar desde fuera lo que hicieron los otros.

## D18. Revisión v2.2 tras una crítica metodológica externa

**Contexto (12 sept 2026).** El autor recibió una revisión externa del preprint v2.1 con 15 hallazgos. Se aceptaron todos los que señalaban errores comprobables y la mayoría de los metodológicos.

**Aceptado y aplicado.**
- Ecuación económica mal definida al variar θ: ahora todas las bandas son proporcionales a θ (θ/100, θ/10, θ). Verificado con una prueba que recorre las cuatro θ del análisis de sensibilidad.
- "Todo incidente grave de la UE es Miniato ≥ 3" no se sostenía: sustituido por una correspondencia de materia y un campo separado en el expediente.
- Cota F ≤ 3 en el caso Hugging Face sin evidencia: retirada; el caso queda en "≥ 2". Regla explícita: una cota sobre un dominio desconocido solo es admisible cuando el alcance documentado excluye pérdidas mayores.
- Tarjeta contradictoria (titular 3 con conjunto {2,3}; E4 junto a "contenido"): el titular muestra la clasificación resuelta; E es el máximo durante el incidente y la contención es un campo aparte.
- θ y w: se retira "aseguran gravedad comparable"; se declara correspondencia normativa a evaluar; w no se deriva de los pesos de discapacidad.
- Pendiente de Gutenberg–Richter: exploratoria; señal de mezcla por proporción de nivel ≥ 4 y distribución acumulada.
- Boletín: unidad de recuento (solo registros padre) y tres fechas (inicio, descubrimiento, clasificación); asignación al periodo de inicio.
- Frontera 0/1: ejemplos de H1 y R1 corregidos; regla 2 ampliada a resultados corrompidos usados fuera del experimento.
- Rúbricas: bandas emparejadas (B, O, S, R7–R8) separadas con criterios; tabla de definiciones de E, A y C.
- Regla 4: el coste necesario de restaurar activos destruidos entra en L; el esfuerzo de respuesta y las mejoras no.
- Antecedentes: Harm Severity Scale de Mylius (AIID, 2025) y MIT AI Incident Tracker citados y comparados.
- Tabla retrospectiva: caso sintético etiquetado como tal; referencia ACLU para Detroit; F de Países Bajos acotado por alcance, no por cantidades exigidas.
- Editorial: "a Miniato level", cuatro componentes en la notación, "regla de agregación explícita" en lugar de "única elección normativa", "una única ancla declarada", "inobservable por cualquier evaluador humano", "diseñada para mantener un significado" en lugar de "siempre significa lo mismo".
- Validación: "prerregistrado" pasa a "criterios propuestos, a prerregistrar con fecha y versión"; medición del acuerdo sobre conjuntos; separación entre incertidumbre de evidencia e indeterminación de la regla.
- Código: URL del repositorio en el paper.

**No aplicado, con motivo.** La crítica sugería mantener F "desconocido" también en el caso neerlandés. Se acotó F en [0,6] porque el alcance documentado (decenas de miles de familias, decenas de miles de euros cada una) excluye pérdidas de 10³·θ o más; eso es una cota por alcance, admitida por la sección 5.3, no una cota por ausencia de informe.

## D19. Revisión v2.3 tras una segunda crítica externa

**Contexto (12 sept 2026).** Segunda revisión externa sobre v2.2, centrada en coherencia entre reglas, tabla, resumen y conclusiones, y en rastros de redacción asistida.

**Aceptado y aplicado.**
- Hallazgo principal: "la primera [Tempe] tiene el nivel más alto" no se deducía de 4 frente a ≥ 2. Retirado en texto, resumen y conclusión; sustituido por lo que sí distingue a ambos casos (clasificación puntual y sin bandera frente a cota inferior con bandera).
- "Non-fatal" → "sin daño físico comunicado en las fuentes examinadas".
- R1/R2: definición operativa de salida (revisada por una persona antes de cualquier efecto) frente a decisión (surtió efecto sin esa revisión), ejemplo fronterizo y regla de prioridad al máximo.
- Fuentes del caso 2026 desagregadas por hecho; METR delimitado a su alcance real.
- Mylius y MIT Tracker: vinculados, no independientes.
- Estilo: apertura del resumen sobre la carencia concreta en lugar del contraste retórico; antítesis no técnicas reformuladas; proposiciones renombradas como propiedades de diseño.

**No aplicado, con motivo.** No se eliminaron las distinciones técnicas formuladas como oposición (consecuencia/peligro, ordinal/probabilístico, gravedad/prioridad): la propia crítica reconoce que cumplen una función. No se redujo la declaración de uso de IA: la crítica confirma que es explícita y correcta.

## D20. Revisión v2.4 y reglas `pilot-0.3`

**Contexto (12 sept 2026).** Tercera revisión externa. Da por cerrados la comparación Tempe/2026, "non-fatal", la relación Mylius–MIT y la desagregación de fuentes; deja abierto R1/R2 y pide tres ajustes.

**Aceptado y aplicado.**
- R1/R2: la v2.3 distinguía salida de decisión por la existencia de revisión humana. Eso introducía un rasgo del proceso en una escala que, por P1, clasifica consecuencias, y permitía rebajar a R1 un rechazo discriminatorio ratificado por una persona. Ahora R2 exige solo que la decisión adversa surtiera efecto; la revisión humana que no lo impidió cambia la atribución causal, no el daño. R1 tiene un ejemplo positivo (ranking sesgado que retrasa revisiones días, corregido antes de ningún rechazo).
- Identificador de reglas: al cambiar un criterio de rúbrica, `pilot-0.2` → `pilot-0.3`, en paper, código y documentación.
- "Cuatro regiones": atribuido a OpenAI (26 ago), no a Hugging Face.
- Resumen inglés: enumeración de resultados; resumen español: pérdida de control durante el incidente frente a contención en la fecha de corte.

## D21. Versión de cierre v2.5

**Contexto (12 sept 2026).** Cuarta revisión externa: favorable a publicar como propuesta metodológica tras correcciones acotadas.

**Aplicado.**
- Cota neerlandesa retirada. En D18 se había defendido F ∈ [0,6] por alcance documentado; la revisión señaló que esa cota no cubría todos los componentes de L (restauración incluida) y tenía razón. F queda desconocido y el caso se comunica como cota inferior 5. Se acepta que un ejemplo menos determinado refuerza la credibilidad de la regla de incertidumbre.
- Ejemplo de R1: el ranking que retrasaba revisiones era una decisión de prioridad con efecto, es decir, R2. Sustituido por resúmenes estereotipados vistos por personal y corregidos sin afectar a ninguna decisión.
- Historial: el paper explica la propuesta vigente y remite al changelog; la afirmación de rutas sin cambios se limita a pilot-0.2 → pilot-0.3.
- Promedios: formulación precisa (sin intervalos iguales, la media no se interpreta como gravedad media); retirada la afirmación de que la sismología "resolvió" el problema.
- Prioridad operativa: ni el nivel ni la bandera la determinan por sí solos.
- Trazabilidad: `example_cases.json` incluye la justificación de cada dominio, también los no determinantes; el esquema del expediente lo exige.

**No aplicado.** Nombre, arquitectura, regla del máximo, tarjeta y boletín se mantienen, como recomienda la propia revisión. Siguiente hito: aplicación por evaluadores ajenos al diseño, no otra versión del texto.

## D22. Revisión de estilo v2.6

**Contexto (12 sept 2026).** Un análisis externo aplicó una lista de indicios de redacción asistida por IA al paper y propuso humanizarlo. El documento declara esa asistencia, así que el objetivo no era ocultarla sino leerse mejor sin perder precisión.

**Aplicado.** Ritmo de frases variado en resumen, introducción, principios y conclusión; principios P1–P7 en prosa breve en lugar de lista paralela; contribuciones en un párrafo; advertencias consolidadas (resumen, final de la introducción, Limitaciones); motivación práctica de las reglas 2 y 4; conectores de plantilla sustituidos; conclusión con pasos concretos en lugar de recapitulación.

**Rechazado.** El texto de resumen e introducción "humanizado" que acompañaba al análisis inventaba el método: índice logarítmico con fórmula, parámetros δ y γ, ISO 31000, seguridad aérea, Knight Capital, corpus de 100 casos históricos. Ninguno existe en la escala. Humanizar no puede significar describir otro artículo. También se rechazó eliminar toda mención al estado no validado fuera de Limitaciones: un resumen debe decir qué es el trabajo.

**No cambiado.** "Essential" se mantiene donde forma parte de "servicios esenciales", término del Reglamento de IA; "anchor" se mantiene como nombre técnico de θ.
