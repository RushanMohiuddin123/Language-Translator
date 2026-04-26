import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os
import uuid


LANGUAGES = {
    'Hindi': 'hi',
    'Marathi': 'mr',
    'Gujarati': 'gu',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Kannada': 'kn',
    'Malayalam': 'ml',
    'Bengali': 'bn',
    'Punjabi': 'pa',
    'Urdu': 'ur'
}


def get_audio_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f" You said: {text}")
        return text
    except Exception as e:
        print(f" Speech Recognition Error: {e}")
        return ""


def translate_text(text, target_lang='hi'):
    try:
        translator = Translator()
        result = translator.translate(text, dest=target_lang)
        print(f"Translated to {target_lang}: {result.text}")
        return result.text
    except Exception as e:
        print(f"Translation Error: {e}")
        return ""


def speak_text(text, lang='hi'):
    filename = f"voice_{uuid.uuid4().hex}.mp3"
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"Text-to-Speech Error: {e}")


def main():
    # Show available Indian languages
    print("🇮🇳 Available Indian Languages:")
    for i, (name, code) in enumerate(LANGUAGES.items(), start=1):
        print(f"{i}. {name} ({code})")
    
    # ask user to select a target language
    try:
        choice = int(input("\nEnter the number of the target language: "))
        lang_code = list(LANGUAGES.values())[choice - 1]
    except (IndexError, ValueError):
        print("Invalid selection. Defaulting to Hindi (hi).")
        lang_code = 'hi'

    # 🚀 Run translation
    input_text = get_audio_input()
    if input_text:
        translated_text = translate_text(input_text, lang_code)
        if translated_text:
            speak_text(translated_text, lang_code)

if __name__ == "__main__":
    main()
