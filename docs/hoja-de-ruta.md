# Hoja de ruta

## Decisiones del autor (bloquean el envío a arXiv)

- [x] Nombre de firma: "Santiago Miniato Santa María Morales" (decidido el 12 de septiembre de 2026 junto con el nombre de la escala).
- [x] Correo de correspondencia (santismm@gmail.com) y afiliación (investigador independiente), fijados el 12 de septiembre de 2026.
- [ ] Licencia del repositorio y del preprint. Recomendación: CC BY 4.0 para texto, MIT o Apache-2.0 para código.
- [ ] Verificar que las tres URL de 2026 citadas (OpenAI, Hugging Face, METR) existen y sostienen lo que la tabla 5 les atribuye.
- [ ] Decidir si el repositorio pasa a público.
- [ ] Búsqueda de marca para MINIATO / MINIATO SCALE en EUIPO, OMPI y USPTO, y registro de dominios principales.

## Antes del preprint

- [ ] Generar `main.bbl` con `tectonic --keep-intermediates main.tex` y empaquetar para arXiv (cs.CY, cruce cs.AI).
- [ ] Re-clasificar los 44 registros del catálogo METR bajo `pilot-0.2` con dos evaluadores, y añadirlos como apéndice o como primer boletín de ejemplo.
- [ ] Un expediente AIRA completo, rellenado campo a campo, como ejemplo en `docs/`.

## Programa de validación (sección 11 del paper)

### Calibración de contenido
- [ ] Panel con seguridad de IA, salud, derechos, servicios esenciales, economía y ecología, con representación de comunidades afectadas.
- [ ] Revisar la alineación de cada banda de rúbrica con h(U).
- [ ] Salida: rúbricas congeladas con ejemplos frontera y condiciones de abstención.

### Reproducibilidad entre evaluadores
- [ ] Corpus de 100 expedientes públicos: 40 para desarrollo, 60 para evaluación ciega.
- [ ] Tres evaluadores independientes por expediente.
- [ ] Estadístico principal: α de Krippendorff ordinal. Aceptación prerregistrada: α ≥ 0,80 global, ningún dominio < 0,67, sin desacuerdos sistemáticos de dos niveles concentrados en R o B.
- [ ] Adjudicación posterior que no sustituye las puntuaciones independientes.

### Comprensión pública
- [ ] Experimento aleatorizado con tres formatos: narrativa sin nivel; cifra sola; tarjeta completa.
- [ ] Medir: distinguir peligro de daño; entender que "contenido" no es "leve"; entender que 0 no es "seguro"; no leer niveles como proporciones.

### Sensibilidad
- [ ] Reclasificar el corpus con θ ∈ {10⁶, 3·10⁶, 10⁷, 3·10⁷} y w ∈ {0,05, 0,1, 0,2}.
- [ ] Fronteras de campaña alternativas.
- [ ] Separar sensibilidad a datos de sensibilidad a convenciones.

### Condiciones de rechazo
La metodología no está validada si el acuerdo depende de la identidad del evaluador, si los desacuerdos se concentran en un dominio, o si la tarjeta aumenta la complacencia ante amenazas activas.

## Trabajo futuro identificado

- Criterio planetario operativo para el predicado ecológico del nivel 9.
- Rúbrica de daño colectivo no mortal por encima de H4.
- Conjunto factible conjunto para dominios correlacionados (el código actual solo hace cotas rectangulares).
- Índice de cobertura de detección y reporte para normalizar el boletín cuando exista reporte obligatorio (art. 73 del Reglamento de IA de la UE).
- Traducción completa del paper al español una vez congelada la versión enviada.
