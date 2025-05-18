import requests
from gtts import gTTS
from playsound import playsound
import os
from datetime import datetime

def speak(text, lang='en'):
    """Convert text to speech in the specified language"""
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")


def greet():
    current_hour = datetime.now().hour

    if current_hour < 12:
        greeting = "Good morning!"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"

    speak(f"{greeting} How can I assist you today?")