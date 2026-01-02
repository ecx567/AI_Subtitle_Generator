# Generador de Subtítulos con IA

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)

🌐 **Multi-Language Support**
[English](README.md) | [Español](README.es.md)

**AI Subtitle Generator** es una potente aplicación de escritorio que genera y traduce automáticamente subtítulos a partir de archivos de video. Inspirada en la facilidad de uso de CapCut, procesa videos localmente utilizando modelos robustos de IA.

### Características
*   **Extracción de Audio**: Extrae automáticamente el audio de los archivos de video.
*   **Transcripción Automática**: Utiliza `faster-whisper` para una conversión de voz a texto local y de alta precisión.
*   **Detección de Idioma**: Detecta automáticamente el idioma hablado y reporta su nivel de confianza.
*   **Traducción**: Traduce los subtítulos al idioma deseado utilizando `deep-translator` (Google Translate).
*   **Generación de SRT**: Crea archivos `.srt` estándar compatibles con la mayoría de reproductores y editores.
*   **GUI Moderna**: Interfaz limpia y oscura construida con `CustomTkinter`.
*   **Portable**: Disponible como un ejecutable independiente que incluye todas las dependencias y modelos de IA (no requiere internet para transcripción).

### Instalación
1.  Ve a la página de **[Releases](../../releases)**.
2.  Descarga el archivo `AutoSubtitles.zip` (o la última versión disponible).
3.  Extrae el archivo zip.
4.  Ejecuta `AutoSubtitles.exe`.

### Uso
1.  Haz clic en **"Seleccionar Video"** para elegir tu archivo.
2.  (Opcional) Selecciona un idioma de destino si deseas traducir los subtítulos.
3.  Haz clic en **"Generar Subtítulos"**.
4.  Espera a que termine el proceso. Los registros mostrarán el progreso.
5.  ¡Listo! El archivo `.srt` se guardará en la misma ubicación que tu video.

### Desarrollo
Para ejecutar desde el código fuente:
```bash
# Clonar el repositorio
git clone https://github.com/ecx567/AI_Subtitle_Generator.git
cd AI_Subtitle_Generator

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python main.py
```
