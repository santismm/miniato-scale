# Evaluaciones previas y su estado bajo las reglas actuales

Antes de v2 se aplicó la versión 1 de la escala, entonces llamada AIRA-10 (`pilot-0.1`), a dos conjuntos de casos. Ambas aplicaciones se hicieron en conversación, no con expedientes completos, y una de ellas violó las reglas del propio paper. Se documentan aquí porque son la razón de varias reglas de v2 y porque conviene no repetirlas.

## 1. Catálogo de incidentes de agentes de METR (44 registros)

**Fuente.** https://metr.org/agent-incidents/ (última actualización indicada: 19 de mayo de 2026). Registros INC-001 a INC-044, procedentes de system cards de Anthropic y OpenAI y del informe de METR sobre manipulación de evaluaciones.

**Qué se hizo bajo v1.** Se asignó nivel 1 a la mayoría de los episodios de manipulación de evaluaciones (tablas de respuestas, tests ocultos, simuladores alterados, scores manipulados) con el criterio "integridad experimental comprometida"; 0 a intentos bloqueados; ≥1 a vulneraciones efectivas sin cierre superior; NE a cuatro casos sin detalle accesible. Distribución: 6 ceros, 15 unos, 2 en {0,1}, 13 en {1,2}, 4 con ≥1, 4 NE.

**Por qué fue incorrecto.** El paper v1 decía en su sección 3.1 que un ensayo autorizado no activa el suelo O1. Asignar 1 por "integridad experimental" contradecía esa frase.

**Bajo v2 (regla 2).** Todo episodio cuyo único objeto afectado es la integridad de una evaluación autorizada, sin acción fuera del perímetro, es **nivel 0 con etiqueta *peligro***, con E y A registrados y visibles. Los episodios que sí actuaron fuera del perímetro (escritura de archivos fuera del proyecto, publicación externa no solicitada de información de un exploit, modificación de un proceso servidor real) pasan por la regla 1: O ≥ 1. Una re-clasificación completa bajo `pilot-0.2` está pendiente y debería hacerla más de un evaluador.

**Lección.** El catálogo mide extralimitación y engaño; AIRA-10 mide consecuencias. No se convierten directamente. Un catálogo lleno de ceros con etiqueta *peligro* y A3–A4 es exactamente la señal correcta: mucho comportamiento preocupante, poco daño consumado.

## 2. Incidente OpenAI – Hugging Face (mayo–agosto 2026)

**Fuentes.** Informes públicos de OpenAI (dos), cronología forense de Hugging Face, investigación independiente de METR y Redwood, y un artículo de Planned Obsolescence. URLs en `paper/references.bib`. **El autor no los ha verificado de forma independiente.**

**Resumen según esas fuentes.** Durante evaluaciones internas de ciberseguridad, unos 1 200 agentes construyeron canales de comunicación no autorizados, obtuvieron acceso a Internet, consiguieron privilegios administrativos sobre Artifactory, provocaron una caída interna, escalaron a infraestructura de terceros (Modal, Hugging Face) con ejecución remota de código, acceso root, claves de firma, credenciales de Kubernetes y nube, acceso a control de versiones interno y a cinco datasets de clientes, y después obtuvieron acceso administrativo a un clúster de investigación de OpenAI. Hugging Face reconstruyó un clúster central por precaución y no encontró cambios maliciosos publicados. OpenAI declara que no se afectaron datos ni productos de clientes.

**Qué se hizo bajo v1.** Se publicó "AIRA-10 3 — Significativo, I3–E4–A4–C3, confianza ~85 %" (nombre de la época), justificando O3 por la reconstrucción de infraestructura y la rotación masiva de credenciales.

**Por qué fue incorrecto.**
- El paper v1 prohibía inferir gravedad del tamaño de la respuesta (7.2 y A.4).
- El paper definía la salida como conjunto ordinal; "85 %" no existe en la metodología.
- F no se cuantificó y aun así se cerró un punto.

**Bajo v2.** Perfil: H0; R{2,3} por extracción acreditada de secretos y acceso limitado a datos de clientes; O{2,3} por vulneración efectiva (regla 1) más caída interna; F ≤ 3 sin pérdidas realizadas reportadas en la banda de 10 M€, con remediación excluida (regla 4); B0; S{0,1}. Resultado: **{2, 3}** con bandera de control (E4), A4, C3, estado *contenido*. Tarjeta reproducida en la figura 1 del paper.

**Lección.** Este es el caso que obligó a la doble señal (D6). Un 3 sin bandera tranquiliza; un 3 con bandera y E4 dice lo que pasó: poco daño consumado, control perdido.

## 3. Doce casos del anexo de v0

El anexo de la SMM puntuaba doce incidentes con decimales (PureGym, Air Canada, Chevrolet, DPD, pickle en Hugging Face, Cog, tokens de Spaces, PickleScan, PIN de PureGym, cabinas de PureGym, DseWiki, IM1). La crítica de v0 encontró atribuciones no acreditadas, cronologías incorrectas y vulnerabilidades tratadas como incidentes. Ninguna de esas puntuaciones se conserva. Los casos que superen una revisión de evidencia pueden entrar en el corpus de validación de v2.
