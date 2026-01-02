# AI Subtitle Generator / Generador de Subtítulos con IA

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)

## English

**AI Subtitle Generator** is a powerful desktop application that automatically generates and translates subtitles from video files. Inspired by CapCut's ease of use, it processes videos locally using robust AI models.

### Features
*   **Audio Extraction**: Automatically extracts audio from video files.
*   **Automatic Transcription**: Uses `faster-whisper` for high-accuracy, local speech-to-text.
*   **Language Detection**: Automatically detects the spoken language with confidence reporting.
*   **Translation**: Translates subtitles to your desired language using `deep-translator` (Google Translate backend).
*   **SRT Generation**: Outputs standard `.srt` files compatible with most players and editors.
*   **Modern GUI**: Clean, dark-themed interface built with `CustomTkinter`.
*   **Portable**: Available as a standalone executable including all dependencies and AI models (no internet required for transcription).

### Installation
1.  Go to the **[Releases](../../releases)** page.
2.  Download the `AutoSubtitles.zip` file (or the latest version).
3.  Extract the zip file.
4.  Run `AutoSubtitles.exe`.

### Usage
1.  Click **"Select Video"** to choose your input file.
2.  (Optional) Select a target language for translation if you want subtitles in a different language.
3.  Click **"Generate Subtitles"**.
4.  Wait for the process to complete. The logs will show the progress.
5.  Technicolor! The `.srt` file will be saved in the same location as your video.

### Development
To run from source:
```bash
# Clone the repo
git clone https://github.com/ecx567/AI_Subtitle_Generator.git
cd AI_Subtitle_Generator

# Create venv
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install deps
pip install -r requirements.txt

# Run
python main.py
```

---

## Español

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
