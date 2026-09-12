# La escala Miniato — Referencia rápida en español (reglas `pilot-0.3`)

Este documento resume el paper [`paper/main.pdf`](../paper/main.pdf). Cuando haya discrepancia, manda el paper.

## 1. Dos capas

| Capa | Qué es | Para quién |
|---|---|---|
| **Expediente Miniato** | Registro técnico: impacto (I), control (E), autonomía (A), confianza (C), dominios (D), evidencia, atribución. Notación compacta `I3-E2-A3-C2`. | Equipos de respuesta, reguladores, investigadores. |
| **Escala Miniato** (índice) | Una cifra de 0 a 10 que resume las **consecuencias materializadas** del expediente. | Público, prensa, legisladores. |

El expediente documenta el incidente; la escala comunica su gravedad.

## 2. Principios

1. **Solo consecuencias.** La cifra clasifica daño ocurrido hasta una fecha de corte. Lo que podría pasar es un *peligro*, y se etiqueta como tal.
2. **Sin compensación.** El nivel es el máximo entre dominios. Un ámbito indemne nunca rebaja un daño grave en otro.
3. **Un solo ancla.** Muertes y euros están en la misma escalera mediante θ = 10 millones de euros por muerte estadística.
4. **Doble señal.** La pérdida de control se muestra junto a la cifra, nunca dentro.
5. **Incertidumbre honesta.** Si falta evidencia, se publica un conjunto de niveles admisibles, no un cero ni una suposición.
6. **Contable en el tiempo.** Las tendencias se cuentan por nivel, no se promedian.
7. **Reproducible.** Dos evaluadores con el mismo expediente deben llegar al mismo nivel sin consultar al autor.

## 3. Dominios del perfil de impacto

| Dominio | Cubre |
|---|---|
| **H** | Vida y salud humana |
| **R** | Derechos, libertades y privacidad |
| **F** | Patrimonio, pérdidas económicas y subsistencia |
| **O** | Operaciones y servicios esenciales |
| **B** | Biosfera y biodiversidad |
| **S** | Efectos sociales, institucionales y sistémicos |

Ciberseguridad, reputación y litigio no son dominios: sus efectos acreditados se registran donde caen.

## 4. La fórmula

Perfil `s = (sH, sR, sF, sO, sB, sS)`, cada uno entre 0 y 8.

```
M(s) = max(sH, sR, sF, sO, sB, sS)

G = 10  si extinción humana Y desaparición de toda vida terrestre
G = 9   si extinción humana O colapso global irreversible de ecosistemas complejos (sin cumplir 10)
G = M(s) en los demás casos
```

Ninguna combinación de puntuaciones ordinarias llega a 9 o 10. Esos predicados nunca se rellenan por defecto.

## 5. Rutas numéricas

**Unidades de daño** `U = muertes + 0,1 × lesiones permanentes graves`.

| Nivel | Unidades de daño U | Pérdida L (€ constantes 2025) |
|---|---|---|
| 1 | — | 0 < L < θ/100 (10⁵ €) |
| 2 | — | θ/100 ≤ L < θ/10 |
| 3 | ≥ 1 lesión permanente grave, U < 1 | θ/10 ≤ L < θ |
| 4 | 1 ≤ U < 10 | 10⁷ ≤ L < 10⁸ |
| 5 | 10 ≤ U < 10² | 10⁸ ≤ L < 10⁹ |
| 6 | 10² ≤ U < 10³ | 10⁹ ≤ L < 10¹⁰ |
| 7 | 10³ ≤ U < 10⁵ | 10¹⁰ ≤ L < 10¹² |
| 8 | U ≥ 10⁵ | L ≥ 10¹² |

Ambas son **suelos**, nunca techos. Cero muertes confirmadas no implica nivel bajo. "No hay muertos confirmados" no es "se ha confirmado que no hay muertos".

Todas las fronteras económicas son proporcionales a θ, así que la función sigue siendo una partición cuando θ varía en el análisis de sensibilidad. La pérdida L es la realizada y atribuible, sin duplicar entre partes. Incluye las pérdidas de las víctimas y el coste necesario de restaurar o sustituir activos destruidos o inutilizados; excluye el esfuerzo de respuesta, el endurecimiento preventivo, las mejoras discrecionales, las exposiciones no materializadas y las ganancias del atacante.

## 6. Reglas especiales

| Regla | Contenido |
|---|---|
| **1. Suelo por vulneración efectiva** | Escapar de un perímetro autorizado, obtener acceso administrativo no autorizado o modificar datos de producción es una consecuencia real: O ≥ 1 aunque no haya daño externo. Un intento bloqueado, una vulnerabilidad no explotada o un ensayo autorizado no lo activan. |
| **2. Incidentes contenidos en evaluaciones** | Si lo único afectado es la integridad de una evaluación autorizada (reward hacking, manipulación de tests) y el sistema no actuó fuera del perímetro: nivel 0 con etiqueta *peligro*; E y A se registran y muestran. Si salió del perímetro, aplica la regla 1. Si el resultado corrompido se usó después fuera del experimento (una afirmación de seguridad publicada, una decisión de despliegue), ese uso es una consecuencia y se clasifica en O o S. |
| **3. Campañas** | Se clasifica la unión deduplicada de consecuencias, no el máximo de los episodios ni su suma. Solo el registro padre entra en los recuentos del boletín. Partir un expediente no debe cambiar el resultado. |
| **4. El esfuerzo de respuesta no es daño** | El nivel nunca se infiere del tamaño de la respuesta (investigación, credenciales rotadas, reconstrucciones preventivas). Se distinguen cuatro gastos: pérdidas directas de las víctimas y coste necesario de restaurar activos destruidos, que entran en L; mejoras adicionales y gasto discrecional, que no. Y reparar no rebaja el nivel: un 6 reparado sigue siendo 6 con estado *contenido*. |
| **5. Revisiones** | Versionadas: valor previo, valor actual, nueva evidencia, motivo. La contención cambia el estado, no el nivel. |
| **6. Atribución** | Solo causa directa o contribución material producen un nivel publicado. Los demás casos se comunican como "consecuencias de nivel k; relación con IA en investigación". |

## 7. La tarjeta pública

```
Miniato ≥ 2   Limitado o superior
[!] Se perdió el control (E4 máximo durante el incidente)
Autonomía: A4 (multiagente distribuido)
Evidencia: confirmada (C3)
Estado: contenido
Dominio determinante: R (extracción de credenciales y secretos)
Niveles admisibles: {2, 3}   Reglas: pilot-0.3   Corte: 2026-08-26
```

- La bandera `[!]` aparece siempre que E ≥ 3.
- Evidencia *provisional* si C ≤ 1, *confirmada* si C ≥ 2.
- Prohibido: "riesgo Miniato 8" para un impacto observado; "Miniato 0" para un evento no investigado; "Miniato 10" para una amenaza no realizada.

## 8. El boletín

Por periodo T (trimestre o año). Se cuentan solo los registros padre consolidados; un incidente pertenece al periodo en que empezó el daño, y las consecuencias descubiertas después se publican como revisión de ese periodo, no como incidente nuevo.

- **N≥k**: número de incidentes cuyo nivel cierto (cota inferior) alcanza k. Se publica para k = 1, 3, 4, 6, con la versión "posible" (cota superior).
- **L_max**: nivel máximo alcanzado.
- Recuento de registros nivel 0 con etiqueta *peligro* y de registros con bandera de control.
- **Libro de daños** en unidades nativas: muertes, lesiones, euros, personas con derechos vulnerados.
- **Cobertura**: fuentes, población que reporta, cambios de reglas.

"Empeora" significa una de tres cosas, siempre con la advertencia de cobertura: sube N≥k para un k fijo; sube la proporción de registros de nivel 4 o superior, o se desplaza hacia arriba la distribución acumulada de niveles; sube la proporción de registros con bandera de control. La pendiente de log N≥k contra k, por analogía con Gutenberg–Richter, es solo un estadístico exploratorio: depende del espaciado numérico de categorías ordinales.

Nunca se promedia la escala Miniato. Nunca se clasifica a organizaciones por número de incidentes reportados.

## 9. Correspondencia con el Reglamento de IA de la UE

Artículo 3(49), "incidente grave": (a) muerte o daño grave a la salud → Miniato ≥ 3, y ≥ 4 si hubo muerte; (b) perturbación grave e irreversible de infraestructura crítica → O ≥ 4; (c) infracción de derechos fundamentales → R ≥ 3; (d) daño grave a propiedad o medioambiente → F ≥ 4 o B ≥ 4. Todo incidente grave según la UE es Miniato ≥ 3. Lo contrario no se cumple; la escala Miniato no es una determinación legal.

## 10. Casos aplicados (tabla 5 del paper)

| Caso | Nivel | E/A/C |
|---|---|---|
| Reward hacking dentro de un sandbox de evaluación autorizado (*ilustración sintética, no un caso documentado*) | 0 (peligro) | E2/A3/C3 |
| Moffatt v. Air Canada, 2024 | 1 | E0/A1/C3 |
| Detención errónea por reconocimiento facial, Detroit 2020 | 3 | E0/A1/C3 |
| Atropello mortal de vehículo automatizado, Tempe 2018 | 4 | E0/A2/C3 |
| Escándalo de ayudas a la infancia, Países Bajos 2013–2019 | {5, 6} (R determinante; F acotado en [0,6] por el alcance documentado) | E1/A1/C2 |
| Fuga multiagente e intrusión en terceros, 2026 | ≥ 2 [!] (O 2–3, R 1–2, F no establecido) | E4/A4/C3 |

Clasificaciones del autor a partir de documentos públicos, provisionales hasta el estudio entre evaluadores. Los casos se eligieron para cubrir el rango: muestran que las reglas pueden producir dispersión, no que los incidentes reales se distribuyan así. Entre Tempe (4, sin bandera) y el caso de 2026 (≥ 2, con bandera) no puede establecerse un orden de gravedad con la evidencia disponible; lo que los distingue es la bandera, no el nivel.
