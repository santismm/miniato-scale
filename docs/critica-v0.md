# Crítica de v0 — Escala Santa María Morales (SMM 2.1)

Crítica realizada el 11 de septiembre de 2026 sobre [`archive/v0-SMM/Escala-SMM-v2.1.md`](../archive/v0-SMM/Escala-SMM-v2.1.md). Se reproduce en forma resumida; el texto original era más extenso.

**Veredicto.** La idea de un lenguaje común para graduar incidentes de IA merece desarrollarse. Pero esta versión no está preparada para presentarse como "especificación técnica formal" ni como "estándar global". Contiene una propuesta de clasificación interesante revestida de una precisión matemática que el documento no demuestra. No se arregla retocando puntuaciones: necesita resolver qué mide, cómo lo mide y qué evidencia permite asignar cada resultado.

## 1. La regla principal es el principal defecto

Dos techos absolutos: 2,0 para lo digital, 3,0 para lo que no tiene muertos. Es una decisión normativa que da prioridad absoluta a la naturaleza física del daño y luego a la existencia de muertes, presentada como si se desprendiera de las matemáticas.

| Escenario | Consecuencia de las reglas |
|---|---|
| Fraude automatizado que arruina a miles de hogares, sin daño físico | No puede superar 2,0 |
| Un sistema bloquea brevemente una puerta sin lesionar a nadie | Entra por encima de 2,0 |
| Fallo que causa numerosas lesiones irreversibles, sin muertes | Limitado a 3,0 |
| Accidente con una muerte | Entra por encima de 3,0 |

**Qué cambiar:** o acotar el nombre y la finalidad (escala de consecuencias físico-vitales), o eliminar los techos universales por tipo de daño y desarrollar criterios para salud, derechos, patrimonio, servicios y medioambiente. La definición de incidente de la OCDE incluye todos ellos.

## 2. La "arquitectura matemática" no es una arquitectura

`SMM = f(I, A, C) ∈ [0, 10]` solo declara que existe una función acotada. No la define. Faltan unidades, escalas de entrada, reglas de agregación, tratamiento de desconocidos y justificación de umbrales. "Logarítmica" no especifica qué magnitud se transforma ni qué significa avanzar una unidad. Los intervalos (0,0–0,5, 0,6–1,2) no son exhaustivos: ¿dónde va un 0,55?

**Prueba decisiva:** ¿puede otra persona obtener 1,7 en lugar de 1,5 o 1,9 siguiendo instrucciones explícitas, sin preguntar al autor? No. Los decimales aportan apariencia de resolución, no resolución.

## 3. Mezcla daño ocurrido, peligro potencial y sofisticación técnica

Son tres preguntas distintas: qué daño se produjo, qué podría ocurrir, cómo actuó el sistema. La matriz las mezcla. La fila 7,1–9,0 sitúa la pérdida de control de arsenales sin aclarar si es alternativa o acumulativa a los techos, y en cualquiera de los dos casos choca con ellos.

**Qué cambiar:** separar severidad observada, potencial de escalada y solidez de la evidencia. La OCDE ya distingue incidentes de *hazards*.

## 4. La parte superior está diseñada alrededor de un relato

"Conflicto de enjambres", "Armas masivas", "Escenario extintivo" con toma de control por inteligencias sintéticas. Son narrativas causales, no gravedad. Una catástrofe causada por un único sistema debería clasificarse por sus consecuencias. El 70 % de la amplitud numérica (3,0–10,0) queda reservada a lo vital y existencial; hay que demostrar que esa distribución sirve al uso previsto.

## 5. El CRV es la parte menos defendible

CRV-A "no simulable en entornos previos": no reproducido no significa no reproducible. CRV-A y CRV-B no son excluyentes. No hay verificación contrafactual definida (qué se mantiene, qué se cambia, qué se observa). Se asignó CRV-A a casos de inyección de instrucciones sin ninguna prueba de que fueran "no simulables".

**Qué cambiar:** sustituir por campos comprobables: reproducción realizada o pendiente, controles presentes y ausentes, factores causales respaldados, cuestiones desconocidas. Retirar "emerge puro".

## 6. Los "vectores de autonomía" no miden una misma dimensión

R-Local es alcance; R-Supply-Chain es vía de propagación; R-Swarm-Stealth combina organización y ocultación; R-Physical es dominio afectado; R-Competitive-Swarms es relación entre agentes. Un incidente podría pertenecer a varios y la notación no lo permite.

## 7. El anexo necesita revisión de evidencia

| Caso | Problema |
|---|---|
| PureGym octubre 2020 | Atribuido a "algoritmo local generativo" sin evidencia. No confirmable como incidente de IA generativa. |
| PureGym agosto 2025 | El relato primario localizado describe una integración personal con Apple Wallet, no bots monopolizando reservas. |
| PickleScan enero 2025 | Cronología incorrecta: JFrog sitúa la notificación en junio de 2025 y la corrección en septiembre. |
| Replicate/Cog | Vulnerabilidad demostrada, no incidente dañino observado. Wiz indica que no se comprometieron datos de clientes. |
| Modelos maliciosos en Hugging Face | JFrog, febrero 2024: separar el conjunto de ~100 modelos del mecanismo concreto analizado. |
| IM1 / Hugging Face | METR distingue ~1 200 agentes en la comunicación de ~700 en el ataque, y su investigación excluye el posterior compromiso de OpenAI. "Máxima sofisticación registrada hasta la fecha" es un superlativo sin universo de comparación. |

## 8. No explica qué decisión permite tomar

Quién clasifica, con qué evidencia mínima, cuándo se revisa, cómo se resuelven discrepancias, qué significa que falten datos. "No hay fallecidos confirmados" no es "se ha confirmado que no hubo fallecidos". Falta la unidad de análisis: ejecución, campaña, vulnerabilidad o cadena de consecuencias.

## 9. El lenguaje promete más de lo que entrega

"Estándar Global", "certidumbre técnica", "anclas infranqueables". Comandos LaTeX sin renderizar en la página 3, una fila partida entre páginas, una página con un solo caso.

## Cómo rehacerla

| Prioridad | Entregable |
|---|---|
| Definir el objeto | Qué cuenta como incidente de IA, qué queda fuera, si se clasifican consecuencias, peligro o ambos por separado. |
| Construir las reglas | Guía exhaustiva con criterios observables, desconocidos, casos frontera. Sin decimales hasta justificarlos. |
| Depurar la evidencia | Registro de casos con fuentes primarias, cronología, papel causal de la IA. |
| Someterla a prueba | Varios evaluadores independientes sobre casos no usados para diseñarla. |
| Preparar el uso real | Formulario, historial de revisiones, ejemplos resueltos, implementación de referencia. |

La pregunta que debe superar la siguiente versión: ¿pueden dos evaluadores independientes, con la misma evidencia, obtener una clasificación explicable y útil sin consultar al autor?
