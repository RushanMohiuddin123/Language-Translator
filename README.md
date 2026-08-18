# Voice Language Translator

A Python-based voice translation application that converts spoken input into text, translates it into a selected Indian language, and converts the translated text back into speech.

The project integrates **Speech Recognition, Google Translate, and Google Text-to-Speech (gTTS)** to provide an end-to-end voice translation workflow.

## Overview

The Voice Language Translator enables users to communicate across multiple Indian languages using voice input and audio output.

The application follows this workflow:

```text
Voice Input
    ↓
Speech Recognition
    ↓
Text
    ↓
Language Translation
    ↓
Translated Text
    ↓
Text-to-Speech
    ↓
Voice Output
```
## Features

* Voice input through a microphone
* Speech-to-text conversion using Google Speech Recognition
* Translation into multiple Indian languages
* Text-to-speech conversion using gTTS
* Audio playback of translated speech
* User-selectable target language
* Exception handling for speech recognition and translation errors
* Temporary audio file generation and automatic cleanup
* Simple command-line interface

## Supported Languages

| Language  | Language Code |
| --------- | ------------- |
| Hindi     | `hi`          |
| Marathi   | `mr`          |
| Gujarati  | `gu`          |
| Tamil     | `ta`          |
| Telugu    | `te`          |
| Kannada   | `kn`          |
| Malayalam | `ml`          |
| Bengali   | `bn`          |
| Punjabi   | `pa`          |
| Urdu      | `ur`          |


## Technologies Used

| Technology / Library | Purpose                              |
| -------------------- | ------------------------------------ |
| Python               | Core programming language            |
| SpeechRecognition    | Converts speech into text            |
| googletrans          | Translates text between languages    |
| gTTS                 | Converts translated text into speech |
| playsound            | Plays generated audio                |
| UUID                 | Generates unique temporary filenames |
| OS                   | File and temporary file management   |


## Project Structure

```text
Voice-Language-Translator/
│
├── translator.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Voice-Language-Translator.git
cd Voice-Language-Translator
```
### 2. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you haven't created `requirements.txt`, install the dependencies manually:

```bash
pip install SpeechRecognition
pip install googletrans==4.0.0-rc1
pip install gTTS
pip install playsound==1.2.2
pip install PyAudio
```

> **Note:** `PyAudio` is required for microphone access. Installation may vary depending on your operating system and Python version.

---

## Usage

Run the application:

```bash
python translator.py
```

The application displays the available languages:

```text
Available Indian Languages:

1. Hindi (hi)
2. Marathi (mr)
3. Gujarati (gu)
4. Tamil (ta)
5. Telugu (te)
6. Kannada (kn)
7. Malayalam (ml)
8. Bengali (bn)
9. Punjabi (pa)
10. Urdu (ur)

Enter the number of the target language:
```

After selecting a language:

1. Speak into the microphone.
2. The application recognizes your speech.
3. The recognized text is translated into the selected language.
4. The translated text is converted into speech.
5. The translated audio is played automatically.

---

## Example

### Input

```text
Enter the number of the target language: 1

Speak now...
You said: How are you?
```

### Translation

```text
Translated to hi: आप कैसे हैं?
```

### Output

The translated sentence is converted into speech and played through the system's audio output.

---

## Core Components

### Speech Recognition

The `get_audio_input()` function captures microphone input and uses Google's speech recognition service to convert spoken words into text.

### Translation

The `translate_text()` function uses `googletrans` to translate the recognized text into the selected target language.

### Text-to-Speech

The `speak_text()` function uses **Google Text-to-Speech (gTTS)** to generate an MP3 file from the translated text and plays it using `playsound`.

### Error Handling

The application handles common errors related to:

* Speech recognition
* Invalid language selection
* Translation
* Text-to-speech generation
* Audio playback

---

## Requirements

Create a `requirements.txt` file with:

```text
SpeechRecognition
googletrans==4.0.0-rc1
gTTS
playsound==1.2.2
PyAudio
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## Future Enhancements

The project can be further enhanced by adding:

* Real-time continuous translation
* Graphical User Interface using Tkinter or Streamlit
* Support for additional languages
* Translation history
* Automatic source-language detection
* Improved speech recognition
* Offline translation capabilities
* Mobile application integration
* Voice selection and customization
* Conversation mode for two-way translation

---

## Learning Outcomes

This project provided practical experience in:

* Python application development
* Speech Recognition
* Natural Language Processing concepts
* API and third-party library integration
* Text-to-Speech systems
* Exception handling
* File management
* Modular Python programming

---

## Limitations

* Internet connectivity is required for Google Speech Recognition, translation, and gTTS services.
* Speech recognition accuracy can depend on microphone quality and environmental noise.
* The `googletrans` library relies on an unofficial Google Translate interface and may occasionally experience compatibility or availability issues.

---

## Author

**Rushan Mohiuddin**

B.Tech – Electronics & Communication Engineering

---

## License

This project is intended for educational and learning purposes.

