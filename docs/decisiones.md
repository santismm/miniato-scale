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
