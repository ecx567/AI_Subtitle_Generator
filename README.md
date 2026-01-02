# AI Subtitle Generator

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)

🌐 **Multi-Language Support**
[English](README.md) | [Español](README.es.md)

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
