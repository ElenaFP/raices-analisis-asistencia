# Análisis de Faltas y Retrasos de Asistencia

## Descripción del Proyecto

Este proyecto procesa datos de asistencia de alumnos a partir de archivos CSV exportados desde el sistema de gestión educativa. Ofrece **dos herramientas** para el análisis:

1. **`analisis_faltas_y_retrasos.py`** - Script Python para uso técnico y procesamiento automatizado
2. **`index.html`** - Aplicación web interactiva para docentes (recomendada para uso general)

Ambas herramientas analizan las faltas y retrasos de asistencia por curso, calculando estadísticas detalladas para las tres evaluaciones y el total del curso académico.

## Características Principales

### 1. Procesamiento de Datos

El script lee archivos CSV con información de asistencia de alumnos y procesa:
- **Faltas de asistencia** de las tres evaluaciones (FALTAS_ASISTENCIA_1EV, 2EV, 3EV)
- **Retrasos de asistencia** de las tres evaluaciones (RETRASOS_ASISTENCIA_1EV, 2EV, 3EV)
- **Identificación única de alumnos** mediante el campo NIA (Número de Identificación del Alumno)

#### Filtros Aplicados

El sistema implementa dos filtros importantes para garantizar la precisión de los datos:

1. **Filtro de asignaturas pendientes**: Se ignoran todos los registros con `ESTADO = "pendiente"`, ya que estos corresponden a asignaturas de cursos anteriores y no deben contabilizarse en las estadísticas del curso actual.

2. **Filtro de duplicados por materia**: Si un mismo NIA aparece múltiples veces con la misma `MATERIA_GENERAL` y `ESTADO = "matriculada"`, solo se procesa la primera ocurrencia. Esto evita duplicar las faltas y retrasos cuando un alumno tiene registros duplicados en el sistema.

### 2. Agrupaciones Inteligentes de Cursos

El script implementa agrupaciones automáticas para consolidar datos:

#### Cursos de Bachillerato
- Todos los cursos que empiezan por **"1º de Bachillerato"** se agrupan en una única categoría
  - Incluye: Ciencias, Humanidades y Ciencias Sociales, etc.
- Todos los cursos que empiezan por **"2º de Bachillerato"** se agrupan en una única categoría
  - Incluye: Ciencias, Humanidades y Ciencias Sociales (Ciencias Sociales), Humanidades, etc.

#### Programas de Diversificación Curricular
- **"1º Programa de Diversificación Curricular (LOMLOE)"** → se agrupa con **"3º de E.S.O. (LOMLOE)"**
- **"2º Programa de Diversificación Curricular (LOMLOE)"** → se agrupa con **"4º de E.S.O. (LOMLOE)"**

### 3. Estadísticas Calculadas

Para cada curso y evaluación, el script calcula:
- **Total de alumnos únicos** (usando NIA para evitar duplicados)
- **Total de faltas**
- **Total de retrasos**
- **Media de faltas por alumno** (total faltas / número de alumnos)
- **Media de retrasos por alumno** (total retrasos / número de alumnos)

**Ordenación:** Los cursos se muestran ordenados por nivel educativo (1º ESO → 2º ESO → 3º ESO → 4º ESO → 1º Bach → 2º Bach) en lugar de por número de faltas, facilitando la lectura y comparación.

### 4. Salidas Generadas

El script genera **dos tipos de salidas**:

#### A. Salida por Pantalla
Muestra 4 tablas formateadas con las estadísticas de:
1. 1ª Evaluación
2. 2ª Evaluación
3. 3ª Evaluación
4. Total del Curso (suma de las tres evaluaciones)

Cada tabla incluye una fila de **TOTAL GENERAL** con los totales y medias del centro.

#### B. Archivos CSV
Genera 4 archivos CSV con los mismos datos:
- `{AÑO}_1EV.csv` - Primera Evaluación
- `{AÑO}_2EV.csv` - Segunda Evaluación
- `{AÑO}_3EV.csv` - Tercera Evaluación
- `{AÑO}_TOTAL.csv` - Total del Curso

Donde `{AÑO}` se obtiene automáticamente del campo `C_ANNO` del CSV de entrada.

## Estructura de los CSV Generados

Cada archivo CSV contiene las siguientes columnas:

| Columna | Descripción |
|---------|-------------|
| CURSO | Nombre del curso |
| ALUMNOS | Número de alumnos únicos en el curso |
| FALTAS | Total de faltas del curso |
| RETRASOS | Total de retrasos del curso |
| MEDIA_FALTAS | Promedio de faltas por alumno |
| MEDIA_RETRASOS | Promedio de retrasos por alumno |

La última fila de cada CSV contiene **TOTAL GENERAL** con los totales y medias del centro.

## Herramientas Disponibles

### 🌐 Aplicación Web (RECOMENDADA)

**Archivo:** `index.html`

#### ¿Para quién?
Ideal para docentes y personal no técnico. No requiere conocimientos de programación.

#### Características
- ✅ **Interfaz visual moderna e intuitiva**
- ✅ **Navegación por pestañas** - organiza las evaluaciones (1ª, 2ª, 3ª, Total) en pestañas individuales
- ✅ **Un solo archivo** - fácil de compartir por email
- ✅ **Sin instalación** - funciona directamente en el navegador
- ✅ **Offline** - no necesita conexión a internet
- ✅ **Multiplataforma** - Windows, Mac, Linux
- ✅ **Responsive** - funciona en móviles, tablets y ordenadores
- ✅ **Descarga individual** - botón para exportar cada evaluación como CSV
- ✅ **Muestra el año del curso** - detecta automáticamente el año académico y lo muestra en subtítulo y títulos de cada evaluación
- ✅ **Orden educativo** - cursos ordenados por nivel (1º ESO a 2º Bach)
- ✅ **Carga múltiple** - permite cargar varios CSVs consecutivamente con limpieza automática de datos anteriores
- ✅ **Drag & Drop** - arrastra y suelta archivos CSV sobre el área de carga con feedback visual

#### Cómo usar
1. **Abrir**:
   - Online: `https://elenafp.github.io/raices-analisis-asistencia`
   - Local: Doble clic en `index.html`
2. **Cargar CSV**:
   - Opción 1: Clic en "Seleccionar archivo CSV"
   - Opción 2: Arrastra y suelta el archivo sobre el área de carga
3. **Ver resultados**: Navega por las pestañas para ver cada evaluación
4. **Descargar**: Botón "Descargar CSV" disponible en cada tabla

#### Compatibilidad
- ✅ Google Chrome
- ✅ Mozilla Firefox
- ✅ Microsoft Edge
- ✅ Safari
- ✅ Cualquier navegador moderno

---

### 🐍 Script Python

**Archivo:** `analisis_faltas_y_retrasos.py`

#### ¿Para quién?
Ideal para usuarios técnicos, procesamiento automatizado o integración en sistemas.

#### Requisitos
- Python 3.x
- No requiere librerías externas (solo usa la biblioteca estándar)

#### Ejecución
```bash
python3 analisis_faltas_y_retrasos.py <archivo.csv>
```

**Ejemplo:**
```bash
python3 analisis_faltas_y_retrasos.py DescargaExpGesExpDat_20251223_130245_105367.CSV
```

Si no proporcionas el archivo como argumento, el script mostrará un mensaje de ayuda.

### Ejemplo de Salida por Pantalla

```
===================================================================================================================
FALTAS Y RETRASOS DE ASISTENCIA - 1ª EVALUACIÓN (Curso 2024)
===================================================================================================================
CURSO                                ALUMNOS     FALTAS   RETRASOS    MEDIA FALTAS  MEDIA RETRASOS
-------------------------------------------------------------------------------------------------------------------
1º de E.S.O. (LOMLOE)                    130       1692        158           13.02            1.22
2º de E.S.O. (LOMLOE)                    133       2817        353           21.18            2.65
3º de E.S.O. (LOMLOE)                     90       1771        183           19.68            2.03
4º de E.S.O. (LOMLOE)                     84       2036        117           24.24            1.39
1º de Bachillerato                       122       2857        315           23.42            2.58
2º de Bachillerato                       104       2624        234           25.23            2.25
===================================================================================================================
TOTAL GENERAL:                           663      13797       1360           20.81            2.05
===================================================================================================================
CSV generado: 2024_1EV.csv
```

**Nota:** Los cursos aparecen ordenados por nivel educativo para facilitar la lectura.

## Datos Importantes del Análisis

### Observaciones del Curso 2024-2025

**1ª Evaluación:**
- Mayor media de faltas: 2º de Bachillerato (25.23 faltas/alumno)
- Menor media: 1º de E.S.O. (13.02 faltas/alumno)

**2ª Evaluación:**
- Mayor media de faltas: 2º de Bachillerato (32.44 faltas/alumno)
- Se observa un aumento generalizado de faltas respecto a la 1ª evaluación

**3ª Evaluación:**
- Mayor media de faltas: 4º de E.S.O. (29.68 faltas/alumno)
- 2º de Bachillerato reduce significativamente sus faltas (16.88)

**Total del Curso:**
- **4º de E.S.O.** tiene la mayor media: **84.98 faltas/alumno**
- **2º de E.S.O.** tiene más faltas totales: **10486 faltas**
- **Media general del centro**: 68.91 faltas/alumno y 5.81 retrasos/alumno
- **Total**: 663 alumnos, 45687 faltas y 3854 retrasos en todo el curso

## Estructura del Código

### Script Python (`analisis_faltas_y_retrasos.py`)

#### Componentes Principales

1. **Lectura y procesamiento de datos**
   - Lectura del CSV con `csv.DictReader`
   - Captura del año del curso desde `C_ANNO`
   - Uso de `defaultdict` para acumular estadísticas

2. **Agrupación de cursos**
   - Lógica condicional para agrupar cursos relacionados
   - Identificación de alumnos únicos mediante sets de NIAs

3. **Función `mostrar_tabla()`**
   - Muestra datos formateados en pantalla
   - Genera archivos CSV de salida
   - Calcula totales y medias
   - Incluye el año del curso en los títulos

4. **Ordenación de cursos**
   - Función `orden_curso()` para ordenar por nivel educativo
   - Orden lógico: 1º ESO → 2º ESO → 3º ESO → 4º ESO → 1º Bach → 2º Bach

5. **Generación de salidas**
   - 4 llamadas a `mostrar_tabla()` para cada evaluación y el total
   - Cálculo de totales acumulados del curso
   - Nombres de archivo con año del curso

### Aplicación Web (`index.html`)

#### Tecnologías Utilizadas

- **HTML5** - Estructura de la aplicación
- **CSS3** - Diseño moderno con gradientes, animaciones y responsive design
- **JavaScript Vanilla** - Lógica de procesamiento (sin dependencias externas)

#### Componentes Principales

1. **Parser de CSV personalizado**
   - Maneja comillas y campos especiales
   - Compatible con formato CSV estándar
   - No requiere librerías externas

2. **Procesamiento de datos**
   - Misma lógica de agrupación que el script Python
   - Uso de objetos JavaScript y Sets para NIAs únicos
   - Cálculos en tiempo real
   - Detección automática del año del curso

3. **Ordenación de cursos**
   - Función `ordenCurso()` para ordenar por nivel educativo
   - Mismo orden que el script Python
   - Aplicado tanto en tablas como en CSVs descargados

4. **Gestión de archivos**
   - Drag & Drop: arrastrar y soltar archivos CSV
   - Feedback visual con animación cuando se arrastra sobre el área
   - Validación de tipo de archivo (solo .csv)
   - Reseteo completo de datos al cargar un nuevo CSV
   - Limpieza de variables globales y tablas anteriores
   - Prevención de mezcla de datos entre archivos

5. **Renderizado dinámico**
   - Generación de tablas HTML dinámicas
   - Actualización del subtítulo y títulos de evaluaciones con el año del curso
   - Resaltado de totales
   - Visualización clara del año en cada sección

6. **Exportación de CSV**
   - Generación de archivos CSV desde el navegador
   - Descarga automática con nombres basados en el año
   - Formato compatible con Excel y otras herramientas
   - Mantiene el orden educativo de los cursos

## Notas Técnicas

### Comunes a Ambas Herramientas
- **Filtros de datos**: Se ignoran asignaturas con ESTADO "pendiente" y se eliminan duplicados de la misma MATERIA_GENERAL por NIA
- **Manejo de valores vacíos**: Los campos vacíos o no numéricos se convierten a 0
- **Codificación**: Los archivos se manejan con codificación UTF-8
- **Delimitador**: El CSV de entrada usa coma (`,`) como delimitador
- **Precisión**: Las medias se redondean a 2 decimales en los CSV
- **Agrupaciones**: Ambas herramientas aplican las mismas reglas de agrupación
- **Ordenación**: Los cursos se ordenan por nivel educativo (1º ESO → 2º Bach)
- **Año del curso**: Se detecta automáticamente del campo C_ANNO del CSV
- **Cálculos**: Los resultados son idénticos en ambas herramientas

### Específicas de Cada Herramienta

#### Script Python
- Sin interfaz gráfica, orientado a terminal
- Genera automáticamente los 4 CSV en el mismo directorio
- Ideal para procesamiento batch o automatización
- Requiere Python instalado

#### Aplicación Web
- Interfaz visual moderna y amigable
- Descarga de CSV bajo demanda (botón por tabla)
- Procesamiento 100% en el navegador (privacidad total)
- No requiere instalación de software

## ¿Qué Herramienta Usar?

### Usa la **Aplicación Web** si:
- ✅ Eres docente sin conocimientos técnicos
- ✅ Quieres una interfaz visual clara
- ✅ Necesitas compartir la herramienta con otros docentes
- ✅ Prefieres no instalar software adicional
- ✅ Quieres procesar datos ocasionalmente

### Usa el **Script Python** si:
- ✅ Tienes conocimientos técnicos
- ✅ Necesitas procesar múltiples archivos automáticamente
- ✅ Quieres integrar el análisis en otros sistemas
- ✅ Prefieres trabajar en terminal/consola
- ✅ Necesitas modificar o extender la funcionalidad

## Archivos del Proyecto

```
📁 raices-analisis-asistencia/
├── 📄 index.html                              # Aplicación web (RECOMENDADA)
├── 🐍 analisis_faltas_y_retrasos.py          # Script Python
├── 📖 README.md                               # Documentación para usuarios
├── 📋 vibe.md                                 # Documentación técnica completa
├── 🚀 DEPLOY.md                               # Guía de despliegue paso a paso
├── 🚫 .gitignore                              # Excluye archivos privados
├── 📁 .github/workflows/
│   └── deploy.yml                             # GitHub Actions para despliegue
├── 📊 DescargaExpGesExpDat_*.CSV              # Archivo CSV de entrada (no se sube a Git)
└── 📑 2024_*.csv                              # Archivos CSV generados (no se suben a Git)
```

## Autor y Fecha

Proyecto desarrollado en diciembre de 2025 para el análisis de asistencia escolar.

### Versiones

- **v1.0** (Diciembre 2025) - Script Python inicial
- **v2.0** (Diciembre 2025) - Añadida aplicación web HTML autocontenida
- **v2.1** (Diciembre 2025) - Ordenación por nivel educativo y visualización del año del curso
- **v2.1.1** (Diciembre 2025) - Mejora en visualización del año en aplicación web (subtítulo + títulos de evaluaciones)
- **v2.2** (Diciembre 2025) - Reseteo completo de datos al cargar nuevo CSV en aplicación web
- **v2.3** (Diciembre 2025) - Funcionalidad Drag & Drop para cargar archivos CSV arrastrándolos
- **v2.4** (Diciembre 2025) - README.md para GitHub con instrucciones de uso y exportación desde Raíces
- **v2.5** (Diciembre 2025) - Script Python acepta archivo CSV como parámetro de línea de comandos
- **v3.0** (Diciembre 2025) - Preparación para GitHub Pages: renombrado a index.html, workflow de GitHub Actions, renombrado script Python
- **v3.0.1** (Diciembre 2025) - Configuración final: nombre del repositorio (raices-analisis-asistencia), URLs actualizadas, guía de despliegue (DEPLOY.md)
- **v3.1** (Diciembre 2025) - Implementación de filtros de datos: ignorar asignaturas pendientes y eliminar duplicados por MATERIA_GENERAL
- **v3.2** (Diciembre 2025) - Actualización de interfaz: Diseño unificado con el proyecto de aprobados e implementación de navegación por pestañas para las evaluaciones.
- **v3.3** (Diciembre 2025) - Añadido banner de navegación inter-aplicaciones y normalización de títulos para coherencia visual.