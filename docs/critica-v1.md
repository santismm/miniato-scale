# Crítica de v1 — AIRA-10 v1.0 (reglas `pilot-0.1`)

Crítica realizada el 11 de septiembre de 2026 sobre el paper y el material reproducible de [`archive/v1-AIRA-10/`](../archive/v1-AIRA-10/), tras verificar hashes, ejecutar las pruebas y contrastar el paper con las aplicaciones que se habían hecho de él en la conversación.

**Veredicto.** El trayecto es bueno: de una escala con techos arbitrarios y decimales cosméticos se llegó a un índice ordinal defendible, con código que funciona y declaraciones honestas. Pero el paper no cumple el objetivo fijado al principio, servir para comunicar a públicos masivos, y la propia conversación ya había violado dos de sus reglas al aplicarlo a casos reales.

## Lo que se sostiene

- **La reproducibilidad es real.** Los hashes SHA-256 coinciden. Las 20 pruebas pasan en Python 3.14 y el informe regenerado es byte a byte idéntico.
- **Los documentos están limpios.** DOCX con ecuaciones y apéndices; sin restos de LaTeX ni referencias rotas.
- **Las decisiones centrales son correctas.** Consecuencias materializadas, máximo, conjuntos cuando falta evidencia, autonomía y control fuera de la fórmula.
- **Las limitaciones están declaradas.**

## Problemas de fondo, por orden

### 1. La escala está mal repartida para comunicar

Richter funciona porque los terremotos reales ocupan todo el rango. Aquí casi todo incidente real cae entre 0 y 3, y el mayor incidente agéntico documentado sale 3. Dos categorías son inobservables por construcción.

| Nivel | Fallecidos | Órdenes de magnitud |
|---|---|---|
| 5 | 1 a 9 | 1 |
| 6 | 10 a 999 | 2 |
| 7 | 1 000 a 999 999 | 3 |
| 8 | 1 000 000 a casi toda la humanidad | casi 4 |

Un incidente con 1 000 muertos y otro con 900 000 comparten el 7. **Recomendación:** repartir el tramo de 1 a 1 000 000 de muertes en cuatro o cinco categorías; una muerte en el 4.

### 2. Las dos rutas numéricas se contradicen

| Nivel | Frontera de muertes | Frontera económica | €/muerte implícitos |
|---|---|---|---|
| 5 | 1 | 10⁹ € | 10⁹ |
| 6 | 10 | 10¹¹ € | 10¹⁰ |
| 7 | 1 000 | 10¹³ € | 10¹⁰ |

El ratio cambia un orden de magnitud entre el 5 y el 6, y ambos están entre cien y mil veces por encima de cualquier valor estadístico de vida regulatorio. Un fraude de 900 millones queda por debajo de una muerte. Puede defenderse, pero tiene que ser una decisión explícita con ratio constante.

### 3. La conversación ya incumplió las reglas del paper

- **Hugging Face:** se justificó el 3 por la reconstrucción de clústeres. El paper prohíbe inferir gravedad del coste de la respuesta (sección 7.2 y apéndice A.4). Con sus reglas el resultado es un conjunto, probablemente {2, 3}.
- Se publicó "confianza del 85 %". El paper dice que las salidas son conjuntos ordinales, no probabilidades.
- **Catálogo METR:** se asignó nivel 1 a decenas de manipulaciones de evaluaciones autorizadas. El paper dice en 3.1 que un ensayo autorizado no activa el suelo O1. Falta una regla para incidentes cuya única víctima es la evaluación.
- La conversación descubrió que el índice sin E era engañosamente tranquilizador y propuso mostrar siempre el estado de control. El paper no lo exige.

### 4. Las rúbricas son el producto real y son lo más flojo

Las 531 441 comprobaciones verifican que la función máximo es la función máximo. Las rúbricas de derechos, operaciones, biosfera y sociedad ocupan un párrafo cada una, sin ejemplos ancla. No hay un expediente real completo.

### 5. Vacíos bibliográficos

No aparece el Reglamento de IA de la UE, cuyo artículo 3(49) define "incidente grave" con cuatro supuestos que se corresponden con H, O, R y F/B. Tampoco la taxonomía de daños de CSET, el repositorio de riesgos del MIT ni el perfil de IA generativa de NIST.

### 6. Menores

- La firma omite "Miniato".
- La declaración de uso de IA nombra solo a ChatGPT.
- El archivo de la SMM seguía en la carpeta titulado "Estándar Global".
- Solo en español.
- "0 = sin incidente efectivo" dentro de una escala de incidentes es contradictorio.

## Qué hacer

1. Reescribir las rúbricas con ejemplos ancla y una regla para evaluaciones autorizadas.
2. Recalibrar las rutas con un ratio declarado y repartir 4–8 sobre el rango realista.
3. Incorporar la doble señal.
4. Aplicar las reglas corregidas a cinco casos públicos.
5. Añadir el encaje regulatorio.

Como preprint, publicable con las correcciones. Para revisión por pares, necesita el punto 4. La idea es buena y la arquitectura es sólida. Lo que falta es demostrar que otra persona puede usarla sin el autor, y hasta ahora ni el autor había podido.

**Resultado:** todos los puntos se incorporaron en v2.0 (`pilot-0.2`); el nombre cambió a Miniato Scale en v2.1. Ver [`historia-del-diseno.md`](historia-del-diseno.md).
