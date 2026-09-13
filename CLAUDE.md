# Contexto para Claude — repositorio `miniato-scale`

Lee esto antes de tocar nada. Es el mapa del repo y las reglas que no debes romper.

## Qué es este proyecto

**The Miniato Scale**: una escala ordinal de 0 a 10 para comunicar la gravedad de incidentes de inteligencia artificial, más un boletín para ver si empeoran con el tiempo. Autor: Santiago Miniato Santa María Morales (Madrid, investigador independiente, santismm@gmail.com). Estado: propuesta metodológica, **versión pública 1.0, reglas `pilot-1.0`**, sin validación empírica todavía. Público en https://github.com/santismm/miniato-scale (remoto `public`). Licencias: CC BY 4.0 para texto, MIT para código.

Idea en una frase: el número mide solo consecuencias materializadas, tomando el máximo entre seis dominios (H salud, R derechos, F patrimonio, O operaciones, B biosfera, S sociedad); la pérdida de control (E), la autonomía (A) y la confianza en la evidencia (C) se muestran junto al número y nunca se suman a él. A partir del nivel 4 hay al menos una muerte o un daño que la calibración coloca a su altura (ancla θ = 10⁷ € por muerte estadística). Si falta evidencia, el resultado es un conjunto de niveles admisibles, no una cifra inventada.

## Dos numeraciones que conviven (no las confundas)

- **Hacia fuera** (paper, arXiv, cita): versión **1.0**, reglas **`pilot-1.0`**. El paper no menciona ninguna versión anterior ni el nombre AIRA. Esa es una decisión del autor y hay que respetarla en cualquier edición del paper.
- **Hacia dentro** (changelog, docs, archive, etiquetas git): el diseño pasó por v0 (SMM), v1 y v2.0 (AIRA-10), v2.1 a v2.6.1 (Miniato). `pilot-1.0` es idéntico a `pilot-0.3`; ningún cambio de regla. La correspondencia está al principio de `CHANGELOG.md`.

Regla: cualquier cambio en una regla de puntuación cambia el identificador de reglas; cambios de prosa no.

## Mapa del repo

| Ruta | Qué es | Toca / no toques |
|---|---|---|
| `paper/main.tex` | Fuente LaTeX del paper (inglés, resumen en español), 20 páginas. Compila con `tectonic main.tex`. | **Es el artefacto principal.** Si lo editas, recompila, comprueba páginas y que no aparezca "AIRA" ni versiones internas. |
| `paper/references.bib` | 34 referencias. Las de 2026 (OpenAI ×2, Hugging Face, METR) fueron verificadas el 12 sept 2026. | No inventes referencias. Verifica antes de añadir. |
| `paper/main.pdf` | PDF compilado del commit actual. | Regenéralo con el tex; no lo edites a mano. |
| `paper/ARXIV_SUBMISSION.md` | Checklist de envío a arXiv: borrador 8070629, código de aval **GQXIPU**, abstract en texto plano, metadatos, mensajes al avalador, estado de la búsqueda de avalador. | Actualiza el estado cuando avance el envío. |
| `paper/README.md` | Cómo compilar y qué falta para arXiv. | |
| `code/miniato.py` | Implementación de referencia (Python ≥ 3.10, sin dependencias). Agregación por máximo, rutas sanitaria y económica con θ y w, cotas rectangulares, reglas 1 y 2, bandera de control, recuentos del boletín. **No adjudica nada**: recibe niveles ya decididos por personas. | Si cambias una regla aquí, cámbiala también en el paper y sube el identificador de reglas. |
| `code/test_miniato.py` | 17 pruebas + enumeración exhaustiva de 9⁶ perfiles + prueba de partición para θ ∈ {10⁶, 3·10⁶, 10⁷, 3·10⁷}. Ejecuta `python3 test_miniato.py`. | Deben pasar siempre antes de un commit. |
| `code/example_cases.json` | Los seis casos de la tabla 5 del paper como registros, con justificación por dominio. | Mantén sincronizado con la tabla 5. |
| `code/verification_report.json` | Salida de la última ejecución de pruebas. | Se regenera solo. |
| `docs/escala-miniato.md` | Referencia rápida de la escala en español. Si discrepa del paper, manda el paper. | Actualiza si cambia una regla. |
| `docs/historia-del-diseno.md` | Cómo se llegó aquí: v0 → v1 → v2.0 → v2.1. | Histórico; solo añadir. |
| `docs/critica-v0.md`, `docs/critica-v1.md` | Las críticas que motivaron cada reconstrucción. | Histórico; no editar. |
| `docs/decisiones.md` | Registro de decisiones D1–D22 con alternativas descartadas y motivo. **Léelo antes de proponer cambios de diseño**: casi todo lo obvio ya se discutió. | Añade D23, D24… No reescribas las anteriores. |
| `docs/evaluaciones-previas.md` | Qué se puntuó bajo versiones antiguas (catálogo METR, caso Hugging Face) y cómo queda bajo las reglas actuales. | |
| `docs/hoja-de-ruta.md` | Decisiones pendientes y programa de validación. | Marca lo que se complete. |
| `archive/` | Versiones retiradas: v0 SMM, v1 AIRA-10 (paper + paquete reproducible), v2.0 AIRA-10 PDF. | **No citar como vigente. No borrar.** El autor decidió mantener la historia en el repo público. |
| `CHANGELOG.md` | Historial interno completo con la correspondencia público/interno. | Añade entradas arriba. |
| `CITATION.cff` | Cita; sin DOI hasta arXiv. | Añadir arXiv id y DOI cuando existan. |
| `README.md` | Portada del repo en español. | |

## Cómo verificar que todo está coherente

```sh
cd code && python3 test_miniato.py && python3 miniato.py example_cases.json
cd ../paper && tectonic main.tex && pdfinfo main.pdf | grep Pages     # esperado: 20
grep -c "AIRA" main.tex                                                  # esperado: 0
grep -o "Preprint, version [0-9.]*" main.tex                            # esperado: 1.0
```

Paquete arXiv: `tectonic --keep-intermediates main.tex`, luego empaquetar `main.tex references.bib main.bbl` en un tar.gz; borrar los intermedios después y restaurar `main.pdf` con `git checkout -- main.pdf` si cambió por bytes.

## Decisiones cerradas que no hay que reabrir

- Nombre **Miniato Scale** (D15). No AIRA, no Santa María Scale.
- Regla del máximo, sin compensación (D2). No promedios.
- θ = 10⁷ € por muerte y w = 0,1 son convenciones declaradas (D4, D10); se varían en el programa de validación, no a ojo.
- Primera muerte en el nivel 4 (D9). Niveles 9 y 10 son anclas (D8).
- Incidentes contenidos en evaluaciones autorizadas: nivel 0 con etiqueta *peligro* (D11).
- El esfuerzo de respuesta no es daño; el coste de restaurar activos destruidos sí entra en L (D12, D21).
- La cifra nunca se publica sola: tarjeta con bandera de control y estado de evidencia (D6).
- Una cota sobre un dominio desconocido exige una estimación documentada que cubra todo L; la ausencia de cifra no es una cota (D21). Por eso el caso de 2026 es "≥ 2" y el neerlandés "≥ 5".
- Se declara la asistencia de IA (Gemini, GPT, Claude) como parte del método (D17). No se oculta ni se elimina.

## Estado del envío a arXiv (13 sept 2026)

Borrador 8070629 creado con contacto, acuerdo, autor, CC BY 4.0 y categoría cs.AI. Bloqueado en "You are not endorsed". Aval solicitado a Edoardo Cetin (verificado en arXiv como avalador de cs.AI) por LinkedIn el 12 sept, 23:44, con el código GQXIPU. Siguiente paso cuando llegue el aval: subir `miniato-scale-arxiv-v1.0.tar.gz` (está en la carpeta padre del repo), pegar los metadatos de `paper/ARXIV_SUBMISSION.md`, cruce cs.CY, vista previa y que el autor pulse Enviar.

## Cosas que no debes hacer sin preguntar al autor

- Enviar mensajes o correos en su nombre.
- Pulsar el botón final de envío en arXiv.
- Cambiar licencias, nombre de la escala o firma.
- Reescribir la historia del repo público o borrar `archive/`.
- Cambiar reglas de puntuación sin subir el identificador de reglas y anotar la decisión en `docs/decisiones.md`.

## Contexto del proceso

El paper pasó cuatro revisiones externas críticas entre el 11 y el 12 de septiembre de 2026; todas están incorporadas y documentadas en D18–D22. Las críticas fueron duras y útiles. Si recibes otra, aplica la misma disciplina: verifica cada afirmación de la crítica antes de aceptarla (en la última, el "resumen humanizado" propuesto inventaba el método entero), aplica lo que sea correcto, anota lo que rechazas y por qué.
