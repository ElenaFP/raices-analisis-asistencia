# 📊 Análisis de Faltas y Retrasos de Asistencia

Herramienta web para analizar faltas y retrasos de asistencia de alumnos por evaluaciones. Diseñada específicamente para centros educativos que usan el sistema **Raíces**.

## 🎯 ¿Qué hace esta herramienta?

Procesa datos de asistencia exportados desde Raíces y genera estadísticas detalladas por curso:

- **Faltas y retrasos** de cada evaluación (1ª, 2ª, 3ª)
- **Total del curso** académico completo
- **Medias por alumno** para cada curso
- **Exportación a CSV** de cada evaluación

## 🔒 Privacidad y Seguridad

### ✅ Tus datos NUNCA salen de tu ordenador

Esta aplicación funciona **100% en tu navegador (client-side)**:

- ❌ **NO sube archivos** a ningún servidor
- ❌ **NO almacena datos** en ninguna base de datos
- ❌ **NO envía información** por internet
- ✅ **Procesamiento local**: Todo el análisis se hace en tu navegador
- ✅ **Privacidad total**: Los datos de tus alumnos están seguros
- ✅ **RGPD/LOPD compatible**: No hay transmisión de datos personales

Una vez cargada la página web, puedes **desconectar internet** y seguirá funcionando perfectamente.

## 🚀 Cómo usar

### Paso 1: Obtener los datos desde Raíces

Para exportar los datos de asistencia desde el sistema Raíces:

1. Accede a **Raíces** con tus credenciales
2. Ve a la sección **"Explotación de datos"**
3. Selecciona **"Evaluación"**
4. Selecciona **"Alumnos con materia y notas"**
5. Haz clic en **"CSV"** para descargar el archivo
6. Guarda el archivo en tu ordenador

El archivo descargado tendrá un nombre similar a:
```
DescargaExpGesExpDat_YYYYMMDD_HHMMSS_XXXXXX.CSV
```

### Paso 2: Analizar los datos

#### Opción A: Uso en línea (Recomendado)

1. Ve a la aplicación web: [https://elenafp.github.io/raices-analisis-asistencia](https://elenafp.github.io/raices-analisis-asistencia)
2. Carga el archivo CSV:
   - **Opción 1**: Haz clic en "Seleccionar archivo CSV"
   - **Opción 2**: Arrastra y suelta el archivo sobre el área de carga
3. Las 4 tablas se generan automáticamente:
   - 1ª Evaluación
   - 2ª Evaluación
   - 3ª Evaluación
   - Total del Curso
4. Descarga los resultados en CSV usando los botones de cada tabla

#### Opción B: Uso local (Offline)

1. Descarga el archivo `index.html` de este repositorio
2. Haz doble clic en el archivo para abrirlo en tu navegador
3. Sigue los mismos pasos que en la Opción A

## 📋 Información mostrada

Para cada curso, la herramienta calcula:

| Columna | Descripción |
|---------|-------------|
| **CURSO** | Nombre del curso (1º ESO, 2º ESO, etc.) |
| **ALUMNOS** | Número de alumnos únicos en el curso |
| **FALTAS** | Total de faltas del curso |
| **RETRASOS** | Total de retrasos del curso |
| **MEDIA FALTAS** | Promedio de faltas por alumno |
| **MEDIA RETRASOS** | Promedio de retrasos por alumno |

## 🎓 Agrupaciones automáticas

La herramienta agrupa automáticamente:

### Bachillerato
- Todos los cursos de **1º de Bachillerato** (Ciencias, Humanidades, CC.SS.) → **1º de Bachillerato**
- Todos los cursos de **2º de Bachillerato** (Ciencias, Humanidades, CC.SS.) → **2º de Bachillerato**

### Diversificación Curricular
- **1º Programa de Diversificación** → Se agrupa con **3º de E.S.O.**
- **2º Programa de Diversificación** → Se agrupa con **4º de E.S.O.**

## ✨ Características

- ✅ **Interfaz visual moderna** e intuitiva
- ✅ **Un solo archivo HTML** - fácil de compartir
- ✅ **Sin instalación** - funciona directamente en el navegador
- ✅ **Offline** - no necesita conexión a internet
- ✅ **Multiplataforma** - Windows, Mac, Linux
- ✅ **Responsive** - funciona en móviles, tablets y ordenadores
- ✅ **Drag & Drop** - arrastra archivos CSV sobre el área de carga
- ✅ **Exportación CSV** - descarga los resultados de cada evaluación
- ✅ **Año automático** - detecta y muestra el año académico
- ✅ **Orden educativo** - cursos ordenados por nivel (1º ESO → 2º Bach)

## 🚀 Despliegue en GitHub Pages

Este repositorio está configurado para desplegarse automáticamente en GitHub Pages usando GitHub Actions.

### Configuración (solo necesitas hacerlo una vez)

1. **Sube el repositorio a GitHub**
2. **Configura GitHub Pages**:
   - Ve a Settings → Pages
   - En "Source", selecciona: **GitHub Actions**
3. **¡Listo!** Cada vez que hagas push a `main`, se desplegará automáticamente

Tu aplicación estará disponible en:
```
https://elenafp.github.io/raices-analisis-asistencia
```

### ¿Qué incluye el despliegue?

El workflow de GitHub Actions (`.github/workflows/deploy.yml`) se encarga de:
- ✅ Desplegar automáticamente cuando hay cambios en `main`
- ✅ Servir `index.html` como página principal
- ✅ Incluir todos los archivos del repositorio (README.md, script Python, etc.)

## 🛠️ Para desarrolladores

### Script Python alternativo

El repositorio incluye también un script Python (`analisis_faltas_y_retrasos.py`) para usuarios técnicos que prefieran trabajar desde la terminal.

#### Requisitos
- Python 3.x
- No requiere librerías externas

#### Uso
```bash
python3 analisis_faltas_y_retrasos.py <archivo.csv>
```

**Ejemplo:**
```bash
python3 analisis_faltas_y_retrasos.py DescargaExpGesExpDat_20251223_130245_105367.CSV
```

El script genera automáticamente los 4 archivos CSV (1EV, 2EV, 3EV, TOTAL) en el mismo directorio.

Si ejecutas el script sin argumentos, mostrará un mensaje de ayuda con las instrucciones de uso.

### Tecnologías utilizadas

- **HTML5** - Estructura
- **CSS3** - Diseño moderno con gradientes y animaciones
- **JavaScript Vanilla** - Procesamiento (sin dependencias externas)

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso libre en centros educativos.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un *issue* o *pull request* si tienes sugerencias o mejoras.

## 📞 Soporte

Si encuentras algún problema o tienes preguntas:
- Abre un [Issue](https://github.com/ElenaFP/raices-analisis-asistencia/issues) en GitHub
- Consulta la documentación completa en [vibe.md](vibe.md)

---

**Nota**: Esta herramienta ha sido desarrollada específicamente para analizar datos exportados desde el sistema de gestión educativa **Raíces** de la Comunidad de Madrid.
# raices-analisis-asistencia
