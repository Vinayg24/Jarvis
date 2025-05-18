import requests
from gtts import gTTS
from playsound import playsound
import os

def speak(text):
    tts = gTTS(text=text, tld='co.in', lang='en', slow=False)
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")

def get_joke():
    try:
        # Fetch random joke from an open joke API
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            joke = f"{joke_data['setup']}... {joke_data['punchline']}"
            speak(joke)
        else:
            speak("Sorry, I couldn't fetch a joke at the moment.")
    except Exception as e:
        speak(f"An error occurred while fetching the joke: {e}")






'''
  Hindi: 'hi'
English: 'en'
Spanish: 'es'
French: 'fr'
German: 'de'
Italian: 'it'



  '''      