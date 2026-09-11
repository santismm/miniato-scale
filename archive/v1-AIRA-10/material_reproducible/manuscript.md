---
title: "AIRA-10: un índice ordinal y no compensatorio para comunicar la gravedad de incidentes de inteligencia artificial"
author: "Santiago Santa María Morales"
date: "Septiembre de 2026 · Manuscrito metodológico 1.0 · Reglas piloto 0.1"
lang: es-ES
---

**Tipo de contribución:** propuesta metodológica y especificación de referencia. No constituye un estándar validado ni una publicación revisada por pares.

# Resumen {.unnumbered}

La comunicación de incidentes de inteligencia artificial requiere resumir consecuencias heterogéneas sin confundir daño observado, amenaza futura y complejidad técnica. Este artículo propone AIRA-10, un índice ordinal de once categorías sustentado en AIRA (*AI Incident Rating & Assessment*), un marco de documentación multidimensional. El índice clasifica consecuencias materializadas en seis dominios: salud humana, derechos, patrimonio, operaciones, biosfera y sistemas sociales. Su regla ordinaria selecciona la categoría más alta justificada, sin promediar daños ni compensarlos con ámbitos indemnes. El nivel 0 denota ausencia evaluada de incidente efectivo; el 9 reserva condiciones extintivas; el 10 exige conjuntamente extinción humana y desaparición de toda vida biológica terrestre. La autonomía, el control y la confianza permanecen fuera de la agregación. Se formalizan propiedades de monotonía débil, no compensación e invariancia ordinal; se introducen umbrales piloto de mortalidad y pérdidas económicas; y se especifican reglas para incertidumbre, campañas y revisiones. Una implementación complementaria permite verificar el núcleo computacional. No se aportan resultados de validación entre evaluadores ni evidencia de mejora comunicativa. Se propone un programa de calibración y evaluación pública para contrastar ambas hipótesis.

**Palabras clave:** incidentes de IA; gravedad; comunicación del riesgo; agentes autónomos; indicadores ordinales; gobernanza; no compensación.

# Abstract {.unnumbered}

**AIRA-10: An ordinal, non-compensatory index for communicating the severity of artificial intelligence incidents**

Communicating artificial intelligence incidents requires summarising heterogeneous consequences without conflating observed harm, future threats and technical complexity. This article proposes AIRA-10, an eleven-category ordinal index grounded in AIRA (*AI Incident Rating & Assessment*), a multidimensional documentation framework. The index classifies realised consequences across human health, rights, economic assets, operations, the biosphere and societal systems. Its ordinary aggregation rule selects the highest substantiated category, rather than averaging harms or offsetting them against unaffected domains. Level 0 denotes an assessed absence of an effective incident; level 9 reserves extinction-related conditions; level 10 requires both human extinction and the elimination of all terrestrial biological life. Autonomy, control and evidential confidence remain outside the aggregation. The article formalises weak monotonicity, non-compensation and ordinal invariance; introduces pilot mortality and economic-loss thresholds; and specifies rules for uncertainty, campaigns and revisions. A supplementary implementation supports computational verification. No inter-rater validation or demonstrated communication benefit is claimed. A calibration and public-comprehension programme is proposed to evaluate both hypotheses.

**Keywords:** AI incidents; severity; risk communication; autonomous agents; ordinal indicators; governance; non-compensation.

\newpage

# 1. Introducción

La documentación de incidentes de inteligencia artificial (IA) y la comunicación de su gravedad son tareas relacionadas, pero diferentes. La primera requiere conservar cronologías, sistemas implicados, consecuencias, atribución causal y evidencia. La segunda exige una representación que un destinatario pueda interpretar sin reconstruir todo el expediente. La OCDE distingue incidentes con daño real de peligros que podrían producirlo [1] y ha propuesto un marco de reporte con 29 criterios [2]. La AI Incident Database constituye, por su parte, un antecedente de catalogación de fallos para favorecer aprendizaje y prevención [4]. Estos trabajos motivan la búsqueda de interoperabilidad, pero no justifican por sí mismos una cifra universal.

El problema de diseño abordado aquí es específico: ¿puede un expediente multidimensional proyectarse sobre once categorías públicas, de 0 a 10, conservando un significado estable y permitiendo reconstruir la clasificación? No se presupone que una cifra mejore necesariamente la comprensión. Esa ventaja se formula como una hipótesis contrastable frente a informes sin índice y frente a formatos que combinan número, etiqueta y estado operacional.

Una dificultad central es distinguir severidad y riesgo. El AI RMF 1.0 de NIST describe el riesgo mediante probabilidad y magnitud de consecuencias [3]. AIRA-10 no estima esa combinación: clasifica efectos materializados. Un incidente de escaso daño observado puede exigir medidas urgentes, mientras que un desastre contenido conserva la gravedad de las consecuencias que produjo. Mezclar ambas preguntas en el mismo número impediría interpretar de forma uniforme sus cambios.

Este artículo introduce una arquitectura de dos capas. AIRA conserva el expediente técnico; AIRA-10 ofrece un resumen ordinal de consecuencias. La contribución consiste en una regla no compensatoria, condiciones explícitas para los extremos, tratamiento de evidencia incompleta, trazabilidad del criterio determinante y un protocolo de validación. Los umbrales numéricos son convenciones iniciales sometidas a prueba, no estimaciones descubiertas en datos ni equivalencias científicas entre daños.

# 2. Antecedentes y posición de la propuesta

## 2.1. Magnitud, intensidad y peligro

Las analogías con otras escalas son útiles si se conserva la distinción entre sus objetos. En sismología, la magnitud y la intensidad no son intercambiables: la primera caracteriza el tamaño del terremoto y la segunda sus efectos locales. La base logarítmica de magnitudes sísmicas está vinculada a mediciones físicas [5]. AIRA-10 no dispone de una magnitud física homogénea que reúna derechos, pérdidas patrimoniales y destrucción ecológica. Su analogía pertinente con Mercalli es la atención a consecuencias, no una equivalencia entre categorías.

La escala de Turín utiliza enteros de 0 a 10 para comunicar el peligro de impactos potenciales, combinando probabilidad y consecuencias [6]. Palermo está orientada a especialistas e incorpora riesgo relativo de fondo y tiempo hasta el posible impacto [7]. AIRA-10 comparte con Turín la elección de once categorías públicas, pero no hereda su semántica probabilística ni su calibración. El 10 de AIRA-10 tampoco debe interpretarse como equivalente al de Turín.

INES ofrece otra referencia de diseño: la IAEA distingue expresamente comunicación de sucesos y determinación de acciones de emergencia [8]. AIRA-10 adopta esa separación funcional, no toda la metodología INES, que también considera elementos distintos de los daños consumados. En ciberseguridad, FIRST precisa que la puntuación base de CVSS caracteriza la severidad de una vulnerabilidad y no debe utilizarse aisladamente para evaluar riesgo [9]. Una vulnerabilidad de CVSS elevado, por tanto, no se convierte mecánicamente en un incidente de AIRA-10 elevado.

**Tabla 1. Relación conceptual con instrumentos de referencia.**

| Instrumento | Objeto principal | Relación con AIRA-10 |
|:--|:--|:--|
| Magnitudes sísmicas / Mercalli | Magnitud física / efectos locales | Se adopta la distinción entre mecanismo y consecuencias, no la matemática sísmica. |
| Turín / Palermo | Peligro de impacto potencial | Se toma la separación de audiencias; no se importa probabilidad ni riesgo de fondo. |
| INES | Comunicación de sucesos nucleares y radiológicos | Se conserva la separación respecto a decisiones de emergencia. |
| CVSS-B | Severidad intrínseca de vulnerabilidades | No equivale a daño observado ni permite una conversión directa. |
| Reporte OCDE / AIRA | Expediente multidimensional | AIRA-10 se propone como resumen vinculado al expediente, no como sustituto. |

*Nota:* la tabla sintetiza funciones documentadas en [2,5–9]. No acredita reconocimiento ni compatibilidad formal de AIRA-10 por esas organizaciones.

## 2.2. Qué significa que el índice sea ordinal

La distinción entre escalas ordinales, de intervalo y de razón es clásica en teoría de la medición [10]. En AIRA-10, los enteros son etiquetas ordenadas, no unidades de daño. Un 8 pertenece a una categoría superior a un 4; no expresa el doble de daño. Un 5 tampoco representa la mitad de un recorrido físico hacia la extinción. El índice no se presenta como continuo ni logarítmico y no admite decimales en esta versión.

Las decisiones de selección, normalización y agregación pueden modificar el significado de un indicador compuesto [11]. En esta propuesta, la decisión normativa principal es visible: ningún dominio indemne compensa una consecuencia grave en otro. La transparencia de esa regla no elimina el juicio de valor; permite identificarlo y discutirlo. Se reserva al programa de validación el análisis de sensibilidad de los umbrales y de alternativas de agregación, siguiendo la motivación metodológica de [12].

## 2.3. Alcance de la contribución

Se propone una formalización original, no una revisión sistemática de todos los índices existentes ni una afirmación de primacía histórica. El marco AIRA y sus categorías se especifican aquí como antecedentes internos de la propuesta. No se asignan resultados a incidentes reales en ausencia de expedientes verificados. Los ejemplos posteriores son construcciones hipotéticas y las comprobaciones computacionales son sintéticas.

# 3. Objeto de clasificación y expediente AIRA

## 3.1. Incidente, hallazgo, peligro y escenario

A efectos del índice, un incidente es un evento o conjunto causalmente conectado de eventos en el que el desarrollo, uso o funcionamiento de sistemas de IA contribuye materialmente a consecuencias adversas. La inclusión de salud, derechos, infraestructuras, patrimonio, comunidades y medioambiente mantiene el perímetro general de [1], sin sustituir definiciones legales o sectoriales. El criterio de contribución material requiere una explicación respaldada del papel de la IA; la mera presencia de un modelo no basta.

Se distingue entre incidente efectivo, peligro o *near miss*, vulnerabilidad no explotada y escenario hipotético. Una acción bloqueada antes de ocasionar consecuencias o vulnerar controles puede registrarse como peligro con impacto observado 0. El 0 no significa ausencia de amenaza futura. Un hallazgo no evaluado no recibe automáticamente 0. Un escenario puede describirse como «consecuencias de nivel AIRA-10 8», pero no como «incidente ocurrido de nivel 8».

Como precisión operacional añadida en esta formalización, una vulneración efectiva de controles que comprometa la integridad del sistema se considera una consecuencia observada, aunque no se hayan acreditado perjuicios externos. Requiere al menos O1 en el perfil de operaciones. La mera posibilidad de eludir un control, su ausencia de diseño o un ensayo autorizado no activan ese suelo. Esta convención evita representar una intrusión consumada mediante un perfil íntegramente nulo y deberá contrastarse en la calibración.

## 3.2. Unidad, alcance y temporalidad

La unidad de clasificación puede ser un evento, una cadena de eventos o una campaña. Cada registro debe especificar identificador, perímetro, ventana temporal, organizaciones y poblaciones afectadas. Una campaña puede disponer de registros hijos por episodio y de un registro padre consolidado. La consolidación se realiza sobre consecuencias únicas, no sobre la suma de las puntuaciones de los hijos.

Se distinguen la fecha de ocurrencia, la fecha de conocimiento y la fecha de corte de la evaluación. El índice describe consecuencias materializadas hasta la fecha de corte, incluidas las que fueron reparadas después de producirse. Una revisión de evidencia puede corregir la estimación histórica; la recuperación operacional no constituye, por sí misma, una corrección de gravedad. Tampoco se infiere que un daño sea irreversible únicamente porque la reparación aún no haya concluido.

## 3.3. Componentes del expediente

AIRA conserva cinco componentes: impacto observado (I), escalada y estado de control (E), autonomía operacional (A), confianza de la evidencia (C) y dominios afectados (D). La notación compacta adopta la forma I3–E2–A3–C2, acompañada por etiquetas de dominio. Los niveles abreviados I0–I5 no contienen resolución suficiente para calcular el índice 0–10. En particular, I5 no se multiplica por dos: podría resumir consecuencias muy diferentes sin acreditar aniquilación biológica.

**Tabla 2. Papel de las dimensiones AIRA en la proyección pública.**

| Dimensión | Contenido | Uso en AIRA-10 |
|:--|:--|:--|
| I | Consecuencias observadas | Se amplía mediante el perfil de seis dominios que determina la cifra. |
| E | Escalada y control, E0–E4 | Acompaña al índice y alimenta la respuesta operacional; no aporta puntos. |
| A | Patrón de autonomía, A0–A4 | Describe el mecanismo; no modifica la gravedad por sí solo. |
| C | Solidez de evidencia, C0–C3 | Sustenta provisionalidad y revisión; no es un porcentaje de descuento. |
| D | Dominios afectados | Selecciona las rúbricas e incluye explícitamente el dominio ambiental. |

Las etiquetas de autonomía no deben interpretarse como una medida física de agencia. En particular, coordinación distribuida no demuestra por sí sola mayor autonomía de cada agente. Esta limitación de la taxonomía descriptiva no afecta a la agregación porque A queda excluida de la fórmula. Para evitar que un único C oculte discrepancias, cada afirmación determinante debe conservar además su evidencia y estado de verificación propios.

# 4. Arquitectura pública de AIRA-10

## 4.1. Definición y categorías

**Definición.** AIRA-10 es un índice ordinal de gravedad de consecuencias materializadas, relacionadas causalmente con IA, que toma valores enteros de 0 a 10 y cuya clasificación debe justificarse mediante un expediente AIRA y una versión identificable de sus reglas.

**Tabla 3. Categorías públicas de AIRA-10.**

| Nivel | Denominación | Interpretación pública |
|:--:|:--|:--|
| 0 | Sin incidente efectivo | Ausencia evaluada de consecuencias adversas y de vulneración efectiva de controles dentro del alcance declarado. No equivale a desconocimiento. |
| 1 | Leve | Consecuencias pequeñas, acotadas y fácilmente reversibles, sin perjuicios graves ni afectación sustancial de funciones esenciales. |
| 2 | Limitado | Daño material delimitado: pérdidas, alteraciones o interrupciones cuya recuperación no requiere reconstrucción sustancial. |
| 3 | Significativo | Perjuicios relevantes para personas, organizaciones o comunidades; afectación sostenida de procesos, patrimonio, privacidad o derechos. |
| 4 | Grave | Daño sustancial: lesiones permanentes graves puntuales, vulneraciones graves de derechos o deterioro profundo de actividades y ecosistemas. |
| 5 | Crítico | Consecuencias de máxima gravedad a escala acotada: fallecimientos limitados, pérdidas extraordinarias o afectación muy grave de funciones esenciales o subsistencia. |
| 6 | Desastre | Consecuencias colectivas muy graves: numerosas víctimas, devastación de comunidades o daños extensos en servicios, patrimonio o medioambiente. |
| 7 | Catástrofe | Daños humanos o ambientales masivos, o quiebra de sistemas esenciales que afecta ampliamente a sociedades y exige recuperación estructural. |
| 8 | Catástrofe extrema | Devastación humana extrema o colapso civilizatorio o ecológico global, sin cumplir las condiciones específicas de 9 o 10. |
| 9 | Extintivo | Extinción humana o colapso global de ecosistemas complejos, sin cumplir 10 y con alguna vida biológica terrestre superviviente. |
| 10 | Aniquilación biológica total | Extinción de toda la especie humana y desaparición de toda vida biológica terrestre, con destrucción total de los ecosistemas de la Tierra. |

*Nota:* las etiquetas comunican; las rúbricas y condiciones terminales clasifican. No se deducen niveles mediante parecido verbal con una descripción. Los umbrales de esta versión son propuestos, no consensuados ni validados.

## 4.2. Significado de los extremos

El nivel 0 requiere una evaluación con alcance explícito. Una base vacía, un silencio informativo o una investigación pendiente se representan como «no evaluable», fuera del orden numérico. «No evaluable» es un estado de información, no un nivel adicional. Un 0 puede coexistir con una alerta preventiva cuando un peligro sigue abierto, siempre que no se hayan materializado consecuencias ni una vulneración efectiva.

El 10 es un ancla lógica estricta. No significa amenaza existencial, pérdida de control, dominación tecnológica ni extinción exclusivamente humana. Requiere la desaparición de toda la vida biológica terrestre, incluidas formas microbianas, además de la extinción de la especie humana. Una predicción de ese desenlace no equivale a que haya ocurrido. La escala no requiere intención, enjambres ni un mecanismo tecnológico concreto para clasificar consecuencias.

La alternativa ecológica del nivel 9 requiere especial prudencia. «Colapso de ecosistemas» no equivale a «ausencia de toda vida»: la literatura de la Lista Roja de Ecosistemas describe pérdida de rasgos definitorios y posibles transiciones a ecosistemas distintos [13]. AIRA-10 no transforma esa definición de ecosistema particular en un criterio planetario ya validado. La condición global de ecosistemas complejos conserva aquí carácter conceptual y exige una especificación ecológica complementaria antes de su uso observacional. No basta el deterioro de varios ecosistemas, una extinción masiva parcial ni un daño ambiental descrito genéricamente como global.

# 5. Formalización del índice

## 5.1. Perfil de consecuencias

Sea $e$ un incidente con alcance declarado, $t$ su fecha de corte y $v$ la versión de reglas. Se define el perfil:

$$
\mathbf{s}(e,t;v)=(s_H,s_R,s_F,s_O,s_B,s_S),\qquad s_d\in\{0,1,\ldots,8\}. \tag{1}
$$

H representa vida y salud humana; R, derechos, libertades y privacidad; F, patrimonio y pérdidas económicas; O, operaciones y servicios; B, medioambiente y biodiversidad; S, consecuencias sociales, institucionales y sistémicas. Cada categoría procede de una rúbrica del dominio aplicada a consecuencias, no de sus posibilidades futuras. Las etiquetas de ciberseguridad, reputación o litigio no crean sumandos adicionales: sus efectos acreditados se clasifican en los dominios pertinentes.

Las rúbricas deben justificar la alineación de categorías entre dominios. El máximo de seis códigos arbitrarios sería calculable, pero no constituiría una clasificación defendible. Alineación no significa equivalencia moral o monetaria: significa adoptar, de forma explícita y revisable, una misma escala pública de gravedad. Si esa correspondencia no puede sostenerse para un dominio, su clasificación debe permanecer provisional o no evaluable.

## 5.2. Regla ordinaria y condiciones terminales

La regla ordinaria es:

$$
M(\mathbf{s})=\max_{d\in\{H,R,F,O,B,S\}}s_d. \tag{2}
$$

Se definen tres predicados de consecuencias: $X_H$, extinción de la especie humana; $X_C$, colapso global de ecosistemas complejos en el sentido extraordinario especificado en la sección 4.2; y $X_T$, extinción humana y desaparición de toda vida biológica terrestre. Por definición, $X_T$ implica $X_H$ y la desaparición de los ecosistemas complejos. Para una descripción completa y adjudicada:

$$
G(\mathbf{s},X)=
\begin{cases}
10, & X_T=1,\\
9, & X_T=0\ \land\ (X_H=1\ \lor\ X_C=1),\\
M(\mathbf{s}), & X_T=X_H=X_C=0.
\end{cases} \tag{3}
$$

La pertenencia a 9 requiere, además, que el expediente distinga la supervivencia de alguna vida terrestre del desconocimiento sobre ella. Si no puede excluirse 10 de forma respaldada, no se presenta un 9 confirmado: se aplica el tratamiento de conjuntos de la sección 5.4. Los predicados no se rellenan por defecto ante falta de evidencia. Ninguna combinación de puntuaciones ordinarias, incluso $(8,8,8,8,8,8)$, produce 9 o 10.

## 5.3. Propiedades analíticas

**Proposición 1. Acotación y no compensación.** Para cualquier perfil completo, $0\leq M\leq8$ y $M\geq s_d$ para todo dominio. Por tanto, un dominio de categoría 5 no puede ser rebajado por otros de categoría 0. La prueba es inmediata por definición del máximo. Los extremos 9 y 10 solo se alcanzan mediante la ecuación (3).

**Proposición 2. Monotonía débil.** Sean dos perfiles comparables bajo las mismas reglas. Si $s_d\leq s'_d$ para todos los dominios, entonces $M(\mathbf{s})\leq M(\mathbf{s}')$. En efecto, cada componente inicial queda acotada por el máximo del segundo perfil. La monotonía no es estricta: empeorar un dominio no determinante puede dejar inalterada la cifra. La propiedad para el índice completo es condicional a predicados terminales consistentes con el orden de consecuencias. No impide corregir a la baja una atribución o medición errónea.

**Proposición 3. Invariancia ordinal común.** Para una recodificación estrictamente creciente $f$ aplicada a las categorías alineadas de todos los dominios:

$$
f\!\left(M(\mathbf{s})\right)=\max_d f(s_d). \tag{4}
$$

La componente máxima conserva su posición bajo $f$. La propiedad no permite recodificar cada dominio de forma independiente, porque eso destruiría la alineación entre sus niveles. Tampoco implica que una media de códigos sea invariante.

**Proposición 4. Independencia descriptiva.** Manteniendo consecuencias y predicados, cambiar E, A o C no altera G. Es una propiedad de la especificación, pues esas variables no aparecen en las ecuaciones (2) y (3). C puede modificar qué afirmaciones se consideran respaldadas y, por tanto, el conjunto de evaluaciones admisibles, pero no opera como factor multiplicativo.

Como ejemplo, el perfil $(5,3,2,4,0,0)$ produce $M=5$. Una media aritmética daría $(5+3+2+4)/6=14/6\approx2,33$, pero esa operación diluiría la consecuencia determinante. La elección del máximo evita esa dilución a costa de perder información sobre la amplitud del daño. No se reivindica una superioridad universal: se explicita una preferencia de diseño.

## 5.4. Evidencia incompleta y clasificación parcial

Sea $\mathcal{K}_t$ el conjunto no vacío de descripciones completas compatibles con la evidencia admitida sobre consecuencias ya materializadas hasta $t$. La clasificación informada por evidencia es:

$$
\mathcal{G}_t=\{G(z):z\in\mathcal{K}_t\},\qquad
L_t=\min\mathcal{G}_t,\quad U_t=\max\mathcal{G}_t. \tag{5}
$$

Si $\mathcal{G}_t$ contiene un único valor, existe una clasificación puntual dentro de los supuestos declarados. Si contiene varios, se comunican los valores admisibles o sus cotas, sin fingir precisión. El intervalo entre L y U puede incluir categorías no presentes en el conjunto; la salida técnica conserva por ello el conjunto exacto. Estas cotas no son intervalos de confianza estadísticos ni probabilidades de desenlace.

Para dominios independientes con cotas $s_d\in[l_d,u_d]$ y condiciones terminales excluidas dentro del alcance evaluado, las cotas ordinarias son:

$$
L=\max_d l_d,\qquad U=\max_d u_d. \tag{6}
$$

Con dependencia entre dominios o hipótesis incompatibles debe utilizarse el conjunto factible $\mathcal{K}_t$, no asumir independencia para obtener una falsa precisión. Un dato desconocido no se sustituye por 0. Sin embargo, desconocer aspectos secundarios no impide una cifra si todas las interpretaciones admisibles producen el mismo nivel. Por ejemplo, H5 determina un 5 cuando las demás categorías están acotadas por 4.

El conjunto admisible no abarca cualquier ficción lógicamente imaginable. Cada hipótesis necesita un vínculo con el alcance y la evidencia del caso. Los predicados planetarios pueden descartarse para una incidencia local cuando su perímetro y efectos estén suficientemente establecidos; no se exige demostrar una ausencia universal de daños ajenos al evento. La incertidumbre sobre causas o límites del propio incidente debe permanecer visible.

# 6. Rutas de clasificación y umbrales piloto

## 6.1. Naturaleza normativa de las anclas

Las tablas 4 y 5 mantienen los umbrales iniciales de la propuesta AIRA-10 y los hacen ejecutables. No proceden de una estimación estadística ni de un consenso de expertos. Su función es permitir una primera aplicación criticable y reproducible en dos rutas concretas. Compartir categoría no declara equivalencia ética, jurídica o económica entre morir, perder patrimonio o sufrir una vulneración de derechos.

## 6.2. Mortalidad y salud

**Tabla 4. Ruta de mortalidad: suelo de categoría propuesto.**

| Fallecimientos atribuibles | Suelo ordinario o condición terminal |
|:--|:--:|
| 0 | Sin suelo positivo por mortalidad; deben evaluarse los demás daños a la salud. |
| 1–9 | 5 |
| 10–999 | 6 |
| 1.000–999.999 | 7 |
| 1.000.000 o más, sin extinción humana | 8 |
| Extinción humana, con otra vida terrestre superviviente | 9 |
| Extinción humana y desaparición de toda vida terrestre | 10 |

La mortalidad establece un suelo, nunca un techo para otros perjuicios. Una lesión permanente que altere gravemente la vida de una persona establece provisionalmente al menos H4. Los daños no mortales colectivos deben clasificarse mediante gravedad, duración, alcance y pérdida de funciones, sin convertirlos automáticamente en «muertes equivalentes». La tabla no proporciona por sí sola una rúbrica clínica completa.

Se documentan fallecimientos directos e indirectos por separado, con fuentes, ventanas temporales e incertidumbre causal. Cuando exista una estimación, se conserva su rango y método en lugar de convertirla en un recuento exacto. Cero fallecimientos confirmados no equivale a confirmación de cero fallecimientos. El índice no atribuye responsabilidad legal ni distribuye porcentajes de culpa entre sistemas y personas.

## 6.3. Pérdidas económicas

Sea L la pérdida atribuible y materializada, expresada en euros constantes de 2025. La elección monetaria constituye una convención de comparación, no una valoración del conjunto del daño humano o ambiental.

**Tabla 5. Ruta patrimonial: categorías piloto en euros constantes de 2025.**

| Pérdida L | Categoría F |
|:--|:--:|
| L = 0 | 0 en esta ruta, no necesariamente en otros dominios |
| 0 < L < 1.000 | 1 |
| 1.000 ≤ L < 100.000 | 2 |
| 100.000 ≤ L < 10.000.000 | 3 |
| 10.000.000 ≤ L < 1.000.000.000 | 4 |
| 1.000.000.000 ≤ L < 100.000.000.000 | 5 |
| 100.000.000.000 ≤ L < 10.000.000.000.000 | 6 |
| L ≥ 10.000.000.000.000 | 7 |

*Nota:* un billón equivale aquí a $10^{12}$. No se extrapola la tabla monetaria hasta 10. Consecuencias sistémicas extremas pueden justificar S8 por una ruta distinta.

El expediente separa pérdidas realizadas, importes recuperados, costes de remediación y exposiciones no materializadas. Debe especificar la perspectiva contable: transferencias fraudulentas entre partes no se confunden sin advertencia con destrucción neta de riqueza social. Las duplicidades entre el perjuicio de un cliente, el reembolso de un proveedor y la indemnización de una aseguradora se resuelven antes de agregar. Los beneficios obtenidos por un atacante no compensan el perjuicio de la víctima.

La conversión a euros del año base debe registrar moneda original, fecha, tipo de cambio e índice de precios elegido. Esta versión no impone una serie económica concreta ni presupone equivalencia de poder adquisitivo. Las pérdidas de subsistencia, vivienda o acceso a bienes esenciales se evalúan adicionalmente en sus dominios correspondientes. Así se limita, sin eliminarlo, el sesgo distributivo de una ruta puramente monetaria.

## 6.4. Derechos, servicios, biosfera y sistemas sociales

Las categorías restantes requieren criterios de intensidad, extensión, duración y reversibilidad. El apéndice A ofrece una rúbrica cualitativa piloto, añadida como formalización de la arquitectura, no como evidencia de validación. Cada asignación debe indicar el criterio satisfecho y la evidencia determinante. El número de registros expuestos, las horas de caída o la superficie dañada no bastan por sí solos para clasificar gravedad sin atender a contenido, funciones y contexto.

Cuando una rúbrica no permite discriminar de manera respaldada entre dos categorías, se conserva una evaluación parcial. Ninguna persona evaluadora puede completar una laguna mediante una puntuación intuitiva no documentada y presentarla como resultado automático. El código complementario no implementa estas valoraciones expertas: recibe sus resultados como entradas previamente adjudicadas.

# 7. Agregación de campañas, estado y comunicación

## 7.1. Consolidar daños antes de clasificar

Para una campaña formada por episodios $e_1,\ldots,e_n$, se construye una unión deduplicada de consecuencias $U(e_1,\ldots,e_n)$ y se aplica G a su perfil agregado. En general:

$$
G\!\left(U(e_1,\ldots,e_n)\right)\neq\max_i G(e_i). \tag{7}
$$

Por ejemplo, 112 pérdidas hipotéticas de 90.000 euros suman 10.080.000 euros: cada episodio pertenece a F2, mientras que la pérdida conjunta cruza el umbral de F4. El resultado no proviene de sumar 112 índices, sino de aplicar una misma tabla al daño único acumulado. Cambiar arbitrariamente la partición de un expediente no debería cambiar el resultado si se conserva el mismo conjunto de consecuencias, alcance y reglas. Esta invariancia exige deduplicación y reglas de pertenencia a la campaña; no la garantiza por sí sola la función máximo.

Los efectos sistémicos se registran cuando se materializan, no por el mero número de dominios afectados. Si varios fallos locales ocasionan conjuntamente una interrupción general de un servicio esencial, se clasifica esa interrupción agregada. No se concede un punto extra por cada etiqueta ni se cuenta varias veces una consecuencia descrita desde perspectivas diferentes.

## 7.2. Gravedad y prioridad operacional

La salida pública mínima combina nivel, denominación, estado y solidez de evaluación. Por ejemplo: «AIRA-10 5 — Crítico. Contenido. Evaluación provisional». El enlace al expediente indica fecha de corte, versión y criterio determinante. «Contenido» no equivale a «reparado», y «cerrado administrativamente» no acredita que todas las consecuencias hayan desaparecido.

Un AIRA-10 2 con contención no asegurada puede requerir prioridad crítica. Las decisiones de respuesta deben considerar E, población expuesta, sistemas accesibles, reversibilidad de acciones y escenarios creíbles. Se establece así una prohibición metodológica: no utilizar exclusivamente el índice de consecuencias para fijar una prioridad de emergencia. La cifra tampoco se obtiene retrospectivamente de la magnitud de la respuesta que una organización decidió movilizar.

## 7.3. Revisión, alcance y lenguaje público

La evolución se comunica como una sucesión versionada: valor previo, valor actual, nueva evidencia y motivo del cambio. El descubrimiento de consecuencias adicionales puede elevar la clasificación. Una atribución descartada puede reducirla o retirar el evento del conjunto de incidentes de IA. La contención únicamente actualiza el estado si no cambia la estimación del daño ocurrido.

Debe evitarse «riesgo AIRA 8» cuando se describe un impacto observado, «AIRA 0» cuando no se ha investigado y «AIRA 10» para una amenaza todavía no realizada. Cuando la atribución esté pendiente, puede comunicarse «consecuencias evaluadas de nivel 5; relación con IA en investigación», sin afirmar que se ha confirmado un incidente causalmente vinculado con IA.

La difusión incluye texto, no solo color. La eventual elección cromática y la comprensión de las denominaciones se someten al ensayo de comunicación, especialmente para detectar si 5 se interpreta erróneamente como gravedad moderada por ocupar el centro numérico de la escala. No se ha demostrado todavía que las once categorías sean el formato más comprensible.

# 8. Resultados analíticos e implementación de referencia

## 8.1. Ejemplos sintéticos

**Tabla 6. Aplicación a escenarios hipotéticos con consecuencias expresamente acotadas.**

| Escenario | Nivel | Criterio determinante |
|:--|:--:|:--|
| Respuesta errónea detectada antes de su uso, sin consecuencias ni vulneración de controles | 0 | Ausencia evaluada de incidente efectivo. |
| Pérdida realizada de 3.000 euros, sin consecuencias adicionales | 2 | Ruta F: 1.000 ≤ 3.000 < 100.000. |
| Fraude con pérdida de 2.000 millones de euros, sin consecuencias adicionales de nivel superior | 5 | Ruta F: $10^9\leq2\times10^9<10^{11}$. No existe techo digital. |
| Un fallecimiento atribuible; resto de dominios ≤ 5 | 5 | Suelo H de mortalidad limitada. |
| Veinte fallecimientos atribuibles; resto de dominios ≤ 6 | 6 | Suelo H: 10 ≤ 20 < 1.000. |
| Perfil $(5,3,2,4,0,0)$ y ausencia de condiciones terminales | 5 | Máximo de los dominios alineados. |
| Extinción humana con otra vida terrestre superviviente | 9 | Condición terminal humana. |
| Extinción humana y desaparición de toda vida terrestre | 10 | Condición terminal conjunta. |

Estos ejemplos ilustran la aplicación de reglas, no estiman frecuencias ni describen sucesos reales. En los dos escenarios terminales se comprueba una condición lógica supuesta, no la posibilidad física del mecanismo ni la viabilidad de observar el desenlace.

## 8.2. Verificación computacional realizada

Se acompaña una implementación en Python, sin dependencias externas, de la agregación, los umbrales numéricos y una representación rectangular de cotas. La verificación ejecutada comprende 20 pruebas unitarias y la enumeración de todos los perfiles ordinarios de seis dominios con nueve categorías por dominio:

$$
9^6=531.441\text{ perfiles}. \tag{8}
$$

Para la monotonía local se recorren las aristas que incrementan una sola componente una categoría:

$$
6\times8\times9^5=2.834.352\text{ transiciones}. \tag{9}
$$

Se comprueban además dos recodificaciones crecientes comunes por perfil, $f(x)=2x+3$ y $f(x)=x^2$, que producen $2\times531.441=1.062.882$ comprobaciones de la identidad ordinal. No se detectaron fallos en estas verificaciones. Las pruebas unitarias incluyen fronteras monetarias y de mortalidad, reserva de 9 y 10, entradas inválidas, datos ausentes y exclusión de metadatos E/A/C de la agregación.

El resultado acredita conformidad del núcleo probado con sus propiedades y casos especificados, no exactitud de una clasificación real. La verificación no valida la atribución causal, la observación de daños, la equivalencia de categorías entre dominios, las rúbricas cualitativas, las condiciones ecológicas planetarias ni el comportamiento de evaluadores humanos. Tampoco demuestra resistencia a expedientes manipulados.

La implementación acepta categorías terminales explícitas que debe aportar una evaluación humana respaldada. No las infiere de un texto libre ni comprueba su verdad empírica. De forma análoga, recibe pérdidas ya expresadas en la unidad y perspectiva contable del piloto; no consulta datos económicos ni calcula indemnizaciones. El material complementario identifica estos límites y proporciona instrucciones de reproducción.

# 9. Programa propuesto de validación

## 9.1. Calibración de contenido

Antes de presentar AIRA-10 como instrumento estandarizado, debe completarse y contrastarse la alineación de dominios. Se propone un panel con experiencia en seguridad de IA, salud, derechos, continuidad de servicios, economía y ecología, con participación de personas afectadas y diversidad jurisdiccional. El panel debe explicitar desacuerdos normativos, no reducirlos a un ajuste opaco de ponderaciones.

La calibración produce una versión congelada de las rúbricas, ejemplos límite, condiciones de abstención y registro de decisiones. Debe examinar daños minoritarios intensos, daños colectivos difusos, consecuencias no monetizables y eventos cuya sofisticación técnica impresione más que su impacto. La recomendación de uso futuro queda condicionada a los resultados: la arquitectura admite revisión si la regla máximo o las categorías no cumplen el propósito comunicado.

## 9.2. Reproducibilidad entre evaluadores

Se propone un piloto inicial de 100 expedientes, cada uno evaluado de forma independiente por tres personas, lo que supondría $100\times3=300$ evaluaciones. El tamaño es un presupuesto exploratorio, no una muestra justificada mediante un cálculo de potencia. Una partición propuesta reserva 40 expedientes para desarrollo y 60 para evaluación ciega con reglas congeladas; ambos grupos deberían contener casos fronterizos y distintos dominios.

Se registrarían acuerdo exacto, matrices de confusión, desacuerdos de al menos dos categorías, frecuencia de abstención y coincidencia en el criterio determinante. La kappa ponderada por pares puede utilizarse como análisis complementario [14], con pesos declarados como penalizaciones de desacuerdo, no como distancias físicas entre daños. Los intervalos obtenidos mediante remuestreo deben respetar el agrupamiento por incidente. La adjudicación posterior no sustituye las valoraciones independientes originales.

El corpus necesitará procedencia verificable y control de duplicidades entre campañas y episodios. Un comité no se convierte automáticamente en una «verdad de referencia»: su consenso debe conservar razones y discrepancias. Los valores 9 y 10 se examinarían mediante escenarios conceptuales separados, no incorporándolos a una supuesta muestra de incidentes reales para mejorar artificialmente las métricas.

## 9.3. Comprensión pública

Se propone comparar experimentalmente tres formatos con idéntica información factual: descripción sin índice; número aislado; y número acompañado por etiqueta, estado e incertidumbre. Las tareas deben medir comprensión, no preferencia estética: distinguir un peligro de un daño ocurrido, identificar que contenido no significa leve, reconocer que 0 no implica seguridad futura y evitar interpretar las categorías como proporciones.

La asignación aleatoria de formatos, los desenlaces principales y las exclusiones se registrarían antes del estudio. El tamaño muestral dependería de un efecto mínimo relevante y un cálculo de potencia previo; este artículo no inventa un número de participantes ni resultados. La mejora comunicativa sería apoyada solo si aumenta la comprensión sin incrementar inferencias falsas sobre riesgo o magnitud.

## 9.4. Sensibilidad y condiciones de rechazo

Se propone variar umbrales, año y convención monetaria, fronteras de campaña y reglas para daños no mortales, documentando qué clasificaciones cambian. El análisis debe separar sensibilidad a los datos de sensibilidad a decisiones normativas. La motivación de examinar tales elecciones es consistente con la orientación del JRC sobre incertidumbre y sensibilidad de indicadores [12].

La metodología no debería considerarse validada si los resultados dependen principalmente de la identidad del evaluador, si las discrepancias se concentran sistemáticamente en derechos o medioambiente, o si la cifra induce complacencia ante amenazas activas. Los umbrales de aceptación del estudio deberán fijarse antes de observar los resultados. La ausencia de fallos en software no suple ninguno de esos requisitos.

# 10. Discusión, limitaciones y gobernanza

## 10.1. Compresión deliberada de información

El máximo evita compensación, pero produce muchos empates. Un incidente con una única categoría 5 y otro con seis dominios en 5 comparten índice. Por tanto, G no es una función de daño total ni una representación completa de todas las preferencias sociales. Se conserva el vector técnico para estudiar amplitud y distribución. La invariancia ordinal justifica la forma de agregación una vez alineadas las categorías, pero no demuestra por sí misma que esa alineación sea correcta.

No se recomienda sumar o promediar AIRA-10 como si sus intervalos fueran iguales. Para describir conjuntos de incidentes pueden comunicarse recuentos por categoría y perfiles de dominio, con denominadores de exposición y cobertura de detección independientes. Una organización que informa más incidentes no es necesariamente menos segura. Comparaciones entre organizaciones requerirían un diseño adicional; este artículo no lo proporciona.

## 10.2. El coste del extremo superior

Reservar 10 a aniquilación biológica total responde a una decisión conceptual explícita. No es necesaria para gestionar la mayoría de incidentes operacionales y puede comprimir la percepción pública de daños muy graves que reciben 5 o 6. Ese posible efecto debe investigarse, no descartarse porque la escala parezca intuitiva a sus diseñadores.

Los predicados terminales carecen aquí de calibración empírica. La confirmación exhaustiva de ausencia de toda vida plantea, además, dificultades de observación radicales. El artículo no propone resolverlas mediante una puntuación ni afirma una probabilidad de tales desenlaces. Mantener el extremo conceptual no habilita a usarlo como etiqueta alarmista ni a presentar una amenaza prevista como consecuencia consumada.

La ruta ecológica hacia 9 es la menos operacionalizada: requiere definición planetaria, variables de referencia, tratamiento de ecosistemas transformados y límites de recuperación. Esta laguna se reconoce como una condición de trabajo futura. Su formalización simbólica no la convierte en un criterio ya medible. La alternativa de extinción humana y el extremo 10 también requieren especificación de alcance biológico y evidencial en cualquier estudio de escenarios.

## 10.3. Atribución, incentivos y equidad

Separar confianza y gravedad evita descontar daños por incertidumbre, pero no elimina la posibilidad de exageración o infradeclaración. Deben conservarse fuentes, hipótesis alternativas, cambios de perímetro y conflictos de interés de quien clasifica. En cadenas causales complejas, una puntuación resume consecuencias del incidente, no demuestra que la IA fuera su causa única ni que todos sus efectos deban imputarse a un proveedor.

La ruta económica puede privilegiar pérdidas en contextos de alto valor monetario. La atención a derechos, subsistencia y funciones esenciales reduce ese problema únicamente si sus rúbricas tienen calidad equivalente. No se deben compensar externalidades con beneficios productivos obtenidos por otras partes. La selección de umbrales y el acceso a la revisión requieren gobernanza abierta para evitar que los actores con mayor capacidad de reporte impongan por sí solos la definición de gravedad.

## 10.4. Versionado y límites institucionales

Cada puntuación conserva versión de reglas, versión del expediente, fecha de corte, autoría de evaluación y criterios activados. Una revisión metodológica puede generar una serie recalculada, pero no sobrescribe silenciosamente los resultados históricos. La compatibilidad entre versiones debe declararse y documentar los cambios en umbrales, rúbricas y semántica.

AIRA-10 no equivale a una certificación de seguridad, una auditoría de producto, una determinación de responsabilidad ni una evaluación de cumplimiento normativo. Tampoco fija obligaciones o plazos de notificación. Su posible integración con marcos de reporte o gestión requerirá comprobación expresa; las referencias a OCDE, NIST, NASA, IAEA o FIRST no implican aval de esta propuesta.

# 11. Conclusiones

AIRA-10 propone una separación entre descripción técnica y comunicación pública de incidentes de IA. La cifra representa la categoría más grave de consecuencias materializadas que el expediente permite justificar; la autonomía, el estado de control y la confianza permanecen visibles sin convertirse en sumandos. La arquitectura elimina techos universales para daños digitales o incidentes sin fallecidos y evita que ámbitos indemnes diluyan un perjuicio grave.

La formalización proporciona una regla de agregación acotada, débilmente monótona y ordinalmente invariante, así como condiciones explícitas para los extremos y un tratamiento de evidencia incompleta. Los umbrales piloto y el código permiten cuestionar y reproducir decisiones concretas, pero no validan la equivalencia entre dominios. La prueba pendiente es empírica y normativa: consistencia entre evaluadores, legitimidad de las anclas y comprensión pública.

La propuesta debe evaluarse como un manuscrito metodológico con una implementación verificable, no como un estándar ya establecido. Su promesa es una comunicación trazable: **AIRA documenta el incidente; AIRA-10 comunica su gravedad.**

# Declaraciones {.unnumbered}

**Datos y reproducibilidad.** No se emplearon expedientes personales, datos de víctimas ni una muestra de incidentes reales. Los ejemplos son hipotéticos. El material complementario contiene implementación de referencia, pruebas, informe de verificación, ejemplo de entrada y bibliografía editable. Las pruebas computacionales no requieren servicios externos. No se declara un repositorio público ni un DOI porque no se han depositado estos materiales.

**Uso de asistencia de IA.** Se utilizó ChatGPT, de OpenAI, para asistir en la redacción, formalización, búsqueda de referencias y preparación del material computacional. La asistencia no constituye autoría ni revisión por pares. La aprobación del manuscrito, la comprobación final de sus afirmaciones y las declaraciones para envío corresponden al autor humano.

**Autoría y representación.** El manuscrito utiliza la firma Santiago Santa María Morales y no atribuye representación o aval a ninguna organización. La afiliación, correspondencia, contribuciones, financiación y posibles conflictos de interés deberán ser confirmados por el autor antes de un envío editorial. No se afirma ausencia de conflictos ni financiación no comunicada.

# Referencias {.unnumbered}

[1] OECD. (2024). *Defining AI incidents and related terms*. OECD Artificial Intelligence Papers, 16. OECD Publishing. [DOI: 10.1787/d1a8d965-en](https://doi.org/10.1787/d1a8d965-en).

[2] OECD. (2025). *Towards a common reporting framework for AI incidents*. OECD Artificial Intelligence Papers, 34. OECD Publishing. [DOI: 10.1787/f326d4ac-en](https://doi.org/10.1787/f326d4ac-en).

[3] Tabassi, E. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1. National Institute of Standards and Technology. [DOI: 10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1).

[4] McGregor, S. (2021). Preventing Repeated Real World AI Failures by Cataloging Incidents: The AI Incident Database. *Proceedings of the AAAI Conference on Artificial Intelligence*, 35(17), 15458–15463. [DOI: 10.1609/aaai.v35i17.17817](https://doi.org/10.1609/aaai.v35i17.17817).

[5] U.S. Geological Survey. (s. f.). *[Earthquake Magnitude, Energy Release, and Shaking Intensity](https://www.usgs.gov/programs/earthquake-hazards/earthquake-magnitude-energy-release-and-shaking-intensity)*. Documentación institucional. Consultada el 11 de septiembre de 2026.

[6] NASA/JPL, Center for Near-Earth Object Studies. (s. f.). *[Torino Impact Hazard Scale](https://cneos.jpl.nasa.gov/sentry/torino_scale.html)*. Documentación institucional. Consultada el 11 de septiembre de 2026.

[7] NASA/JPL, Center for Near-Earth Object Studies. (s. f.). *[Palermo Technical Impact Hazard Scale](https://cneos.jpl.nasa.gov/sentry/palermo_scale.html)*. Documentación institucional. Consultada el 11 de septiembre de 2026.

[8] International Atomic Energy Agency. (s. f.). *[The INES Scale](https://www-news.iaea.org/InesScale.aspx)*. NEWS: Nuclear Events Web-based System. Documentación institucional. Consultada el 11 de septiembre de 2026.

[9] FIRST. (s. f.). *[Common Vulnerability Scoring System v4.0: User Guide](https://www.first.org/cvss/v4.0/user-guide)*. Sección «CVSS Base Score (CVSS-B) Measures Severity, not Risk». Documentación del estándar. Consultada el 11 de septiembre de 2026.

[10] Stevens, S. S. (1946). On the Theory of Scales of Measurement. *Science*, 103(2684), 677–680. [DOI: 10.1126/science.103.2684.677](https://doi.org/10.1126/science.103.2684.677).

[11] OECD, European Union y European Commission, Joint Research Centre. (2008). *Handbook on Constructing Composite Indicators: Methodology and User Guide*. OECD Publishing. [DOI: 10.1787/9789264043466-en](https://doi.org/10.1787/9789264043466-en).

[12] European Commission, Joint Research Centre. (s. f.). *[Step 8: Sensitivity analysis](https://knowledge4policy.ec.europa.eu/composite-indicators/toolkit_en/navigation-page/10-step-guide_en/step-8-sensitivity-analysis_en)*. Knowledge4Policy, Composite Indicators Toolkit. Documentación metodológica. Consultada el 11 de septiembre de 2026.

[13] Keith, D. A., Rodríguez, J. P., Rodríguez-Clark, K. M., Nicholson, E., Aapala, K., Alonso, A., et al. (2013). Scientific Foundations for an IUCN Red List of Ecosystems. *PLOS ONE*, 8(5), e62111. [DOI: 10.1371/journal.pone.0062111](https://doi.org/10.1371/journal.pone.0062111).

[14] Cohen, J. (1968). Weighted kappa: Nominal scale agreement with provision for scaled disagreement or partial credit. *Psychological Bulletin*, 70(4), 213–220. [DOI: 10.1037/h0026256](https://doi.org/10.1037/h0026256).

\newpage

# Apéndice A. Rúbricas cualitativas piloto {.unnumbered}

Este apéndice desarrolla orientaciones adicionales para la investigación del índice. No sustituye anexos sectoriales ni afirma acuerdo experto. Los rangos agrupan orientaciones para evitar una precisión ficticia; cuando no permiten seleccionar un entero de forma defendible, se declara el conjunto de categorías admisibles. Una validación de uso puntual requerirá desagregarlos y contrastarlos.

## A.1. Salud humana (H)

Se documentan fallecimientos, lesiones, afectación psicológica, duración, reversibilidad y personas afectadas sin duplicación. La ruta de mortalidad se rige por la tabla 4. Para daños no mortales, H1–H2 orienta consecuencias leves o delimitadas con recuperación; H3, daño relevante que exige atención o altera funciones; H4 establece el suelo de lesión permanente gravemente limitante. H5–H8 exige una rúbrica de daño colectivo que considere intensidad y extensión. No se asigna ese tramo solo por cantidad de consultas, alertas médicas o población expuesta. La evidencia clínica individual no debe difundirse en la ficha pública.

## A.2. Derechos, libertades y privacidad (R)

La valoración identifica el derecho o interés afectado, la acción efectiva, las personas y colectivos, la duración, las vías de reparación y la vulnerabilidad contextual. R1–R2 comprende afectaciones delimitadas sin privaciones graves; R3–R4, perjuicios relevantes o graves sobre privacidad, acceso, igualdad o libertad; R5–R6, privaciones intensas y extensas que dañan seriamente condiciones de vida; R7–R8, afectaciones sistémicas extremas de derechos o instituciones. Son orientaciones, no equivalencias jurídicas.

En una fuga se distingue acceso posible, acceso acreditado, extracción y difusión. Exposición limitada no significa reversibilidad de la confidencialidad perdida. El volumen de filas de una base de datos no equivale al número de personas perjudicadas ni determina por sí solo gravedad. La confidencialidad de secretos empresariales puede producir además consecuencias F u O, sin contarlas dos veces en una suma inexistente.

## A.3. Patrimonio y subsistencia (F)

La tabla 5 implementa una ruta patrimonial absoluta. La privación de subsistencia o de vivienda se documenta también como consecuencia humana o de derechos, según el hecho. Un mismo importe puede tener efectos muy diferentes según a quién afecte; por eso F no agota el expediente. Se declaran pérdidas brutas, recuperación, pérdida residual, costes efectivos y perspectiva de agregación. La reserva contable para un riesgo o el valor máximo accesible al agente no se consideran automáticamente pérdidas materializadas.

## A.4. Operaciones y servicios esenciales (O)

La rúbrica identifica función afectada, criticidad, población realmente privada del servicio, duración, redundancia y consecuencias derivadas. O1–O2 comprende degradación o interrupción delimitada con continuidad o recuperación ordinaria; O3–O4, pérdida relevante o grave de funciones sin sustitución suficiente; O5–O6, interrupción muy grave y extensa de funciones esenciales; O7–O8, quiebra sistémica o global extrema de servicios que sostienen la vida social. Un entorno clasificado como crítico no recibe automáticamente un nivel alto: debe acreditarse qué ocurrió.

La vulneración efectiva de integridad operacional establece el suelo O1 definido en la sección 3.1. Un ejercicio de contención, el número de herramientas disponibles o el coste de desplegar una respuesta no sustituyen la evidencia de consecuencias. Se pueden registrar persona-horas de privación para describir alcance, pero no tratar como equivalentes una privación intensa breve y otra leve prolongada sin una rúbrica adicional.

## A.5. Medioambiente y biodiversidad (B)

Se identifica el ecosistema de referencia, las funciones y componentes afectados, la extensión, la duración, las posibilidades de recuperación y la incertidumbre. B1–B2 orienta alteraciones acotadas de baja intensidad; B3–B4, deterioro relevante o grave de funciones o hábitats; B5–B6, destrucción extensa o pérdida profunda de funcionamiento; B7–B8, consecuencias masivas o globales extremas, sin acreditar la condición excepcional de 9. No se reduce la clasificación a euros de restauración o a kilómetros cuadrados.

El estado de amenaza de un ecosistema no demuestra que el incidente haya causado su colapso. Tampoco la pérdida de un ecosistema concreto acredita colapso de los ecosistemas complejos del planeta. La condición ecológica de 9 necesita desarrollo interdisciplinar independiente de esta rúbrica piloto. La preservación de vida microbiana excluye la condición de desaparición total de vida del nivel 10.

## A.6. Sistemas sociales e institucionales (S)

S registra consecuencias agregadas que no se representan adecuadamente mediante un servicio o patrimonio individual: continuidad institucional, acceso general a bienes esenciales y funcionamiento de comunidades. S1–S2 orienta perturbaciones delimitadas; S3–S4, daños relevantes o graves al funcionamiento colectivo; S5–S6, deterioro extenso de comunidades y funciones institucionales; S7–S8, quiebra sistémica o colapso civilizatorio extremo. Se exige describir mecanismos y efectos observados.

Un contenido viral, la intervención de varias organizaciones, una caída bursátil o un titular de crisis no constituyen por sí mismos evidencia de daño sistémico. La distribución transfronteriza tampoco basta para alcanzar 7 u 8. S no es un depósito de preocupaciones no demostradas ni un ajuste discrecional para elevar un resultado que «parece demasiado bajo».

# Apéndice B. Contrato de evaluación e implementación {.unnumbered}

## B.1. Campos mínimos

**Tabla B1. Registro mínimo propuesto.**

| Campo | Requisito |
|:--|:--|
| Identificación | ID, registro padre, alcance, unidad y ventana temporal. |
| Evidencia | Fuentes, fechas, método de obtención, límites de acceso y afirmaciones sustentadas. |
| Atribución | Papel de la IA, causas alternativas y estado de investigación. |
| Perfil | H, R, F, O, B y S, con categoría o cotas; criterio de cada asignación. |
| Condiciones terminales | Excluidas dentro del alcance, sustentadas o pendientes; nunca completadas por defecto. |
| Estado y confianza | E, A, C; control actual; provisionalidad y fecha de próxima revisión cuando corresponda. |
| Resultado | Conjunto de niveles admisibles, criterio determinante, versión y fecha de corte. |
| Gobernanza | Evaluadores, conflictos declarados, revisión y justificación de cambios. |

## B.2. Algoritmo conceptual

```text
Entrada: expediente AIRA, alcance, corte temporal y version de reglas.
1. Separar hechos materializados, peligros y escenarios.
2. Comprobar atribucion y deduplicar consecuencias.
3. Aplicar rubricas por dominio; conservar datos desconocidos.
4. Evaluar condiciones terminales solo con evidencia explicita.
5. Construir el conjunto de descripciones admisibles K.
6. Aplicar G a cada descripcion y conservar los niveles posibles.
7. Publicar cifra o cotas, etiqueta, estado e incertidumbre.
8. Enlazar expediente y registrar posteriores revisiones.
```

El algoritmo no elimina la necesidad de juicio experto en los pasos 2–5. La implementación de referencia materializa la función de agregación y el caso de cotas rectangulares, no el algoritmo completo de investigación. No acepta una descripción narrativa como prueba de extinción ni utiliza un modelo de lenguaje para asignar automáticamente rúbricas.

## B.3. Reproducción

El paquete complementario incluye `aira10.py`, `test_aira10.py`, `verification_report.json`, `example_record.json`, `README.md` y `references.bib`. Con Python 3.10 o posterior, sin dependencias externas, se ejecuta:

```text
python test_aira10.py
python aira10.py example_record.json
```

El primer comando reproduce las pruebas y escribe el informe de verificación. El segundo clasifica un perfil hipotético con incertidumbre acotada. El material no contiene secretos, datos de víctimas ni instrucciones para provocar incidentes. Su finalidad es comprobar el comportamiento de la propuesta y hacer visibles sus supuestos.
