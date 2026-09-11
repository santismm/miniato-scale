# Historia del diseño

Todo el trabajo se hizo entre el 10 y el 12 de septiembre de 2026, en conversación entre el autor y modelos de lenguaje (primero ChatGPT, después Claude). Cada versión se sometió a una crítica dura y se reconstruyó. Este documento cuenta qué se propuso, qué falló y por qué cambió.

## Punto de partida: la pregunta

El autor pidió una escala para incidentes de IA que fuera tan útil como Richter, Mercalli, Turín o Palermo: que sirviera para comunicar a públicos amplios, que se convirtiera en estándar de industria, y que llevara su nombre. Después precisó el objetivo: **ayudar a la sociedad a entender qué está pasando y a tomar conciencia de la evolución de los riesgos de la IA en el tiempo, a peor.**

Se repasaron primero las escalas clásicas y sus fallos: Richter se satura en terremotos grandes; Mercalli es subjetiva; Turín alarma con datos preliminares; Saffir-Simpson ignora la marejada; Fujita no puede medir un tornado en campo abierto. Esas lecciones se llevaron al diseño.

## v0 — Escala Santa María Morales (SMM 2.1)

**Qué era.** Una función continua de 0,0 a 10,0 con tres "anclas infranqueables": ningún incidente puramente digital podía superar 2,0; ningún incidente sin muertos podía superar 3,0; el 10,0 era la extinción humana. Vectores de propagación (R-Local, R-Swarm-Stealth, R-Competitive-Swarms), un modificador de verificación contrafactual (CRV-A "emerge puro", CRV-B "fallo de arnés") y un anexo con doce incidentes puntuados con decimales.

**Qué falló** (crítica completa en [`critica-v0.md`](critica-v0.md)):

- Los techos eran decisiones normativas presentadas como matemáticas. Un fraude que arruina a miles de hogares no podía pasar de 2,0; una puerta bloqueada sin lesionados entraba por encima.
- La "función" `SMM = f(I, A, C)` no estaba definida. Nadie podía calcular un 1,7 en lugar de un 1,5 sin preguntar al autor.
- "Logarítmica" no significaba nada concreto.
- La matriz mezclaba daño ocurrido, peligro potencial y sofisticación técnica, y sus niveles altos describían narrativas concretas (enjambres rivales, arsenales) en lugar de consecuencias.
- El CRV era infalsable: "no reproducido" no es "no reproducible".
- El anexo mezclaba hechos documentados con atribuciones no acreditadas.

**Decisión.** Abandonar la arquitectura entera y el nombre.

## v1 — AIRA y AIRA-10 (reglas `pilot-0.1`)

**Qué se construyó.** Primero AIRA, un marco de clasificación multidimensional: impacto (I0–I5), escalada (E0–E4), autonomía (A0–A4), confianza (C0–C3), dominios (D). Después, a petición del autor, AIRA-10: una proyección pública de 0 a 10 basada en consecuencias, con regla de máximo no compensatoria, condiciones terminales para 9 y 10, salidas por conjuntos cuando faltaba evidencia, y dos tablas piloto: mortalidad (1 muerte → 5, 10 → 6, 1 000 → 7, 1 000 000 → 8) y pérdidas económicas (1 000 M€ → 5, 100 000 M€ → 6, 10 billones → 7).

Se redactó un paper de 17 páginas en español con 14 referencias, propiedades formales, implementación en Python y 531 441 perfiles verificados. Después se aplicó a los 44 registros del catálogo de incidentes de agentes de METR y al incidente OpenAI–Hugging Face de 2026.

**Qué falló** (crítica completa en [`critica-v1.md`](critica-v1.md)):

- **La escala estaba mal repartida.** Casi todo incidente real caía entre 0 y 3. El mayor incidente agéntico documentado salía 3. Un instrumento así no puede mostrar empeoramiento.
- **Las dos rutas se contradecían.** El tipo de cambio implícito entre muertes y euros era 10⁹ €/muerte en el nivel 5 y 10¹⁰ €/muerte en el 6 y el 7, entre cien y mil veces por encima de cualquier valor estadístico de vida regulatorio.
- **El autor violó sus propias reglas al aplicarlas.** Puntuó Hugging Face como 3 contando la reconstrucción de clústeres, que el paper prohibía contar. Dio "85 % de confianza" a un valor que el paper definía como conjunto ordinal. Asignó nivel 1 a manipulaciones de evaluaciones autorizadas que el paper decía que no activaban el suelo.
- **Faltaba una regla para los incidentes dentro de evaluaciones**, que son el tipo más documentado.
- **La conversación descubrió que la cifra sin E era engañosamente tranquilizadora** y propuso la doble señal, pero el paper no la incorporaba.
- **Las rúbricas cualitativas eran un párrafo por dominio**, sin ejemplos ancla.
- **Vacíos bibliográficos**: el Reglamento de IA de la UE, la taxonomía de daños de CSET, el repositorio de riesgos del MIT.

**Decisión.** Conservar la arquitectura (dos capas, máximo, conjuntos, E/A/C fuera de la fórmula) y recalibrar todo lo demás.

## v2.0 — AIRA-10 (reglas `pilot-0.2`)

**Qué cambió:**

| Aspecto | v1 | v2 |
|---|---|---|
| Primera muerte | Nivel 5 | **Nivel 4** |
| Reparto de mortalidad | 1 / 10 / 1 000 / 1 000 000 → 5 / 6 / 7 / 8 | 1 / 10 / 100 / 1 000 / 100 000 → 4 / 5 / 6 / 7 / 8 |
| Ruta económica | Tabla independiente | Definida a través de la sanitaria por encima de θ = 10⁷ € por muerte |
| Lesiones | Sin regla cuantitativa | Unidades de daño U = muertes + 0,1 × lesiones permanentes graves |
| Incidentes en evaluaciones | Sin regla | Regla 2: nivel 0 con etiqueta *peligro* si no salió del perímetro |
| Remediación | Mencionada | Regla 4 explícita: nunca cuenta como daño ni lo rebaja |
| Tarjeta pública | Cifra + estado | Cifra + etiqueta + **bandera de control obligatoria** + estado de evidencia |
| Evolución temporal | Ausente | **Boletín**: N≥k por periodo, L_max, libro de daños, cobertura; señales de empeoramiento |
| Encaje legal | Ausente | Correspondencia con el art. 3(49) del Reglamento de IA de la UE |
| Casos reales | Ninguno | Seis, de nivel 0 a 6, incluida la corrección del error de v1 sobre Hugging Face |
| Rúbricas | Un párrafo por dominio | Bandas con ejemplos ancla por dominio |
| Idioma | Español | Inglés con resumen en español |
| Referencias | 14 | 28 |

**Qué se conservó:** la separación AIRA / AIRA-10, la regla del máximo, los conjuntos de niveles admisibles, la independencia de E, A y C, las condiciones terminales para 9 y 10, y la honestidad sobre lo que no está validado.

**Qué sigue abierto:** todo lo empírico. Ver [`hoja-de-ruta.md`](hoja-de-ruta.md).

## v2.1 — La escala Miniato (reglas `pilot-0.2`), versión actual

**Qué cambió.** Solo el nombre y la declaración de autoría; ninguna regla.

- AIRA-10 pasa a llamarse **Miniato Scale**; el marco técnico, **expediente Miniato**; el boletín, **boletín Miniato**.
- La firma pasa a **Santiago Miniato Santa María Morales**.
- La declaración de uso de IA nombra los tres modelos empleados y sus funciones por fase.

**Por qué.** Tras publicar v2.0 se comprobó que AIRA ya lo usan varios marcos de evaluación de riesgo de IA (*Artificial Intelligence Risk Assessment*, *AI-Induced Risk Audit*, *AI Integrated Risk Architecture*, una certificación sanitaria). Además, las escalas que la cultura recuerda llevan nombre de persona o de lugar, no acrónimo. Se compararon Santa María, Miniato, Madrid, Santa María–Morales, Santiago y Morales; la búsqueda desempató a favor de Miniato por unicidad y ausencia de ruido. Detalle en [`decisiones.md`](decisiones.md), D15 y D17.

## Sobre el nombre

El autor quería desde el principio que la escala llevara su nombre, como Richter o Mercalli. En v0 se llamó Santa María Morales. En v1 y v2.0 se cambió a AIRA por un argumento de posicionamiento que resultó equivocado en la práctica: el acrónimo estaba ocupado y no era memorable. En v2.1 la escala recupera un apellido del autor, Miniato, y el autor firma con él.
