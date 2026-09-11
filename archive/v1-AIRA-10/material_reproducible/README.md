# AIRA-10 — Material complementario

Manuscrito: «AIRA-10: un índice ordinal y no compensatorio para comunicar la gravedad de incidentes de inteligencia artificial».
Autor: Santiago Santa María Morales.
Reglas de investigación: `pilot-0.1`. Fecha de preparación: 11 de septiembre de 2026.

## Alcance

Este paquete implementa la agregación ordinal, las rutas numéricas piloto de mortalidad y pérdida económica y un cálculo de cotas con dominios rectangulares. No investiga hechos, no establece causalidad, no puntúa automáticamente las rúbricas cualitativas y no decide prioridades de emergencia. No es un producto certificado ni un estándar validado.

## Reproducción

Requiere Python 3.10 o posterior y únicamente su biblioteca estándar. Descomprimir el paquete, abrir una terminal en su carpeta y ejecutar:

```sh
python test_aira10.py
python aira10.py example_record.json
```

El primer comando ejecuta 20 pruebas unitarias y una enumeración exhaustiva de 531.441 perfiles ordinarios, 2.834.352 transiciones adyacentes y 1.062.882 comprobaciones de recodificación. Escribe `verification_report.json`. No utiliza datos de incidentes reales ni mide acuerdo entre personas. El segundo imprime el resultado del ejemplo.

## Interpretación de entradas

El orden de los seis dominios es H, R, F, O, B, S. Cada cota es `[mínimo, máximo]`, con categorías enteras entre 0 y 8. `null` significa desconocido y abarca 0–8, no cero confirmado. Las cotas representan consecuencias ya materializadas compatibles con evidencia y alcance explícitos, no escenarios de daño futuro.

`terminal_candidates` debe proporcionarse explícitamente. `none` significa que las condiciones terminales se han descartado dentro del alcance de la evaluación; no se debe usar como sustituto de una investigación ausente. Las otras etiquetas son `human_extinction`, `complex_ecosystem_collapse` y `total_biological_annihilation`. Su verdad debe adjudicarse fuera del programa. El programa no comprueba hechos biológicos ni simula desenlaces.

`effective_breach=true` exige un suelo de integridad operacional O1; no se utiliza para vulnerabilidades no explotadas ni ensayos autorizados. Los metadatos E/A/C se conservan, pero no cambian el nivel.

`possible_levels` es un conjunto de categorías, no una distribución de probabilidad. Un conjunto unitario puede coexistir con evidencia provisional si todas las interpretaciones admitidas producen la misma categoría. Cuando existen dependencias entre dominios, debe sustituirse el rectángulo por un conjunto factible conjunto; esta implementación no resuelve ese problema.

Las cantidades monetarias se introducen como cadenas decimales, enteros o `Decimal`, en euros constantes de 2025 previamente calculados. El código no convierte monedas ni consulta inflación. Los umbrales son convenciones piloto, no equivalencias normativas oficiales. Cero muertes produce suelo 0 por mortalidad, no necesariamente H0.

## Archivos

- `aira10.py`: núcleo y adaptador de línea de comandos.
- `test_aira10.py`: pruebas sintéticas reproducibles.
- `verification_report.json`: resultados de la ejecución efectivamente realizada.
- `example_record.json`: ejemplo completamente hipotético.
- `references.bib`: referencias para gestores bibliográficos.
- `manuscript.md`: fuente editable del artículo.

## Estado editorial

No se afirma revisión por pares, validación empírica, financiación ni aval institucional. Afiliación, correspondencia y declaraciones editoriales quedan a revisión y aprobación del autor. No se ha efectuado depósito público ni asignado un DOI. No se incluye una concesión de licencia elegida en nombre del autor; las condiciones de distribución pública deberán ser decididas por él.

Se empleó asistencia de IA en la preparación del texto y el material computacional. La declaración del manuscrito describe ese uso y la necesidad de aprobación humana antes del envío.
