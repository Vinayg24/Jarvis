import requests
from gtts import gTTS
from playsound import playsound
import os

def speak(text, lang='en'):
    """Convert text to speech in the specified language"""
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")

def translate_text(text, target_lang='hi'):
    """Translate the given text to the target language using Google Translate API"""
    try:
        # Google Translate API endpoint
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={target_lang}&dt=t&q={text}"
        response = requests.get(url)
        if response.status_code == 200:
            translated_text = response.json()[0][0][0]
            return translated_text
        else:
            return None
    except Exception as e:
        print(f"Error in translation: {e}")
        return None

def get_advice(language='en'):
    """Fetch advice and speak it in the specified language"""
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        if response.status_code == 200:
            advice_data = response.json()
            advice = advice_data['slip']['advice']
            
            if language != 'en':
                # Translate the advice if the target language is not English
                translated_advice = translate_text(advice, target_lang=language)
                if translated_advice:
                    speak(translated_advice, lang=language)
                else:
                    speak("Sorry, I couldn't translate the advice.", lang=language)
            else:
                speak(advice, lang=language)
        else:
            speak("Sorry, I couldn't fetch advice at the moment.")
    except Exception as e:
        speak(f"An error occurred while fetching the advice: {e}")


