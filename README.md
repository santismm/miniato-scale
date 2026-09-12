# The Miniato Scale

**Una escala pública de gravedad para incidentes de inteligencia artificial, y un boletín para ver si empeoran.**
*A public severity scale for AI incidents, and a bulletin for tracking whether they are getting worse.*

Autor: Santiago Miniato Santa María Morales (Madrid). Estado: **propuesta metodológica v2.2, reglas `pilot-0.2`, sin validación empírica todavía.**

---

## Qué es

Los terremotos tienen magnitud, los huracanes categoría, los sucesos nucleares un nivel INES. Los incidentes de IA tienen titulares. Este proyecto propone:

1. **El expediente Miniato**, el registro técnico de un incidente: impacto observado (I), estado de control (E), autonomía (A), confianza en la evidencia (C) y dominios afectados (D).
2. **La escala Miniato**, un índice ordinal de 0 a 10 que resume el expediente en una cifra con significado estable: **consecuencias materializadas**, nunca miedo, sofisticación ni riesgo futuro.
3. **La tarjeta pública**: la cifra nunca se publica sola. Va con etiqueta, bandera de pérdida de control y estado de la evidencia.
4. **El boletín Miniato**: recuentos por nivel y periodo, nivel máximo alcanzado y libro de daños en unidades nativas, para que la sociedad vea la evolución sin promediar ordinales.

La frase que resume la escala: **a partir del 4, alguien ha muerto o ha ocurrido un daño de gravedad equivalente declarada.**

| Nivel | Etiqueta | Ancla |
|---|---|---|
| 0 | Sin daño | Ausencia evaluada de consecuencias. Puede llevar etiqueta *peligro*. |
| 1 | Leve | Pérdidas < 100 000 €. Toda vulneración efectiva de controles es al menos 1. |
| 2 | Limitado | 100 000 € a 1 M€. |
| 3 | Significativo | 1 a 10 M€; una lesión permanente grave; privación de libertad. |
| 4 | Grave | **Una muerte**; 10 a 100 M€. |
| 5 | Severo | 10 muertes; 100 M€ a 1 000 M€. |
| 6 | Desastre | 100 muertes; 1 000 a 10 000 M€. |
| 7 | Catástrofe | 1 000 muertes; 10 000 M€ a 1 billón €. |
| 8 | Catástrofe extrema | 100 000 muertes; ≥ 1 billón €. |
| 9 | Extintivo | Extinción humana o colapso global de ecosistemas complejos. |
| 10 | Aniquilación biológica total | Extinción humana y de toda vida terrestre. Ancla lógica. |

Referencia rápida completa en español: [`docs/escala-miniato.md`](docs/escala-miniato.md).

## Estructura del repositorio

```
paper/      Preprint v2.2 en LaTeX (inglés, con resumen en español) y PDF compilado
code/       Implementación de referencia en Python, pruebas y casos de ejemplo
docs/       Documentación en español: escala, historia, críticas, decisiones, hoja de ruta
archive/    Versiones anteriores (v0 SMM, v1 y v2.0 AIRA-10) conservadas por trazabilidad
```

## Empezar

```sh
cd code && python3 test_miniato.py && python3 miniato.py example_cases.json
cd ../paper && tectonic main.tex
```

## Cómo se llegó aquí

El diseño pasó por tres versiones y un cambio de nombre en dos días. Cada una se sometió a una crítica dura y se reconstruyó. La historia completa está en [`docs/historia-del-diseno.md`](docs/historia-del-diseno.md); las críticas que motivaron cada cambio, en [`docs/critica-v0.md`](docs/critica-v0.md) y [`docs/critica-v1.md`](docs/critica-v1.md); las decisiones de diseño y sus alternativas descartadas, en [`docs/decisiones.md`](docs/decisiones.md).

## Por qué "Miniato"

Las escalas que la cultura recuerda llevan nombre de persona o de lugar: Richter, Mercalli, Beaufort, Fujita, Torino, Palermo. Un acrónimo explica la fórmula; un nombre propio se convierte en concepto. Las versiones 1.0 y 2.0 se llamaron AIRA-10, pero AIRA ya está ocupado por varios marcos de evaluación de riesgo de IA sin relación con este. Entre los apellidos del autor, "Miniato" tiene la superficie semántica más limpia: no existe ninguna "Miniato Scale" en ciencia, técnica ni IA, y el único ruido es San Miniato, en Toscana. "Santa María" arrastra la carabela, un volcán y decenas de ciudades. La revisión completa del razonamiento está en [`docs/decisiones.md`](docs/decisiones.md), decisión D15.

El uso previsto: *"The incident was a Miniato 4."*

## Estado y decisiones pendientes

- No hay validación entre evaluadores ni experimento de comprensión pública. El programa está en [`docs/hoja-de-ruta.md`](docs/hoja-de-ruta.md).

## Licencia

- Paper y documentación (`paper/`, `docs/`, `archive/`, este README): [Creative Commons Attribution 4.0](LICENSE) (CC BY 4.0). Puedes usar, adaptar y redistribuir la escala citando al autor.
- Código (`code/`): [MIT](code/LICENSE).

## Citar

Ver [`CITATION.cff`](CITATION.cff). Mientras no haya DOI:

> Miniato Santa María Morales, S. (2026). *The Miniato Scale: Communicating the Severity of Artificial Intelligence Incidents and Tracking Their Evolution.* Preprint v2.2, rules pilot-0.2. https://github.com/santismm/miniato-scale

## Uso de IA

Este trabajo se desarrolló mediante un proceso explícitamente multimodelo asistido por IA, declarado como parte del método: Google Gemini 3.6 Flash (revisión inicial de escalas y primer borrador), OpenAI GPT-5.6 Sol (crítica de v0, diseño del expediente y del primer índice 0–10, paper v1, primeras aplicaciones, búsqueda de nombre) y Anthropic Claude Fable 5.1 (crítica de v1, recalibración, paper actual, implementación pilot-0.2 y documentación). El reparto de funciones es el que el autor registra de sus historiales de sesión. Los modelos no son autores: el planteamiento, cada decisión normativa, las clasificaciones y la decisión de publicar son del autor.
