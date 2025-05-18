import subprocess as sp
import speech_recognition as sr
import webbrowser
import pyttsx3
from playsound import playsound
import musiclibrary
from openai import OpenAI
import requests
from gtts import gTTS
import os
import threading
import pyautogui
import advice
import joke



recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "3fc2f8290ee84eb5bd20bbf27e55b065"


def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    tts = gTTS(text=text, tld='co.in', lang='en', slow=False)
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")

def aiProcess(c):
    client = OpenAI(api_key="3fc2f8290ee84eb5bd20bbf27e55b065")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
            {"role": "user", "content": c}
        ]
    )

    return completion.choices[0].message.content

def open_application(app_name):
    application_paths = {
        "notepad": "notepad.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "discord": r"C:\Users\vinay\AppData\Local\Discord\Update.exe --processStart Discord.exe",
        "vscode": r"C:\Users\vinay\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    }
    
    app_name = app_name.lower()
    
    if app_name in application_paths:
        sp.Popen(application_paths[app_name])
        speak(f"Opening {app_name}")
    else:
        speak("Application not found")

def open_camera():
    try:
        speak("Opening camera")
        sp.Popen('start microsoft.windows.camera:', shell=True)
    except Exception as e:
        speak(f"Unable to open camera: {e}")


def shutdown_system():
    try:
        sp.run(["shutdown", "/s", "/t", "0"])
        speak("Shutting Down the system")
    except Exception as e:
        speak(f"Invalid Command: {e}")
def open_camera():
    sp.run('start.Microsoft.camera:', shell=True )


def take_screenshot():
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        speak("Screenshot taken and saved")
    except Exception as e:
        speak(f"Failed to take screenshot: {e}")

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")
    elif "open wikipedia" in c.lower():
        webbrowser.open("https://www.wikipedia.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ", 1)[1]
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Song {song} not found")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    elif "shutdown" in c.lower():
        shutdown_system()
    elif "restart" in c.lower():
        speak("Restarting the system")
        sp.run(["shutdown", "/r", "/t", "0"])
    elif "open" in c.lower():
        app_name = c.lower().split("open ", 1)[1]
        open_application(app_name)
    elif "open_camera" in c.lower():
        open_camera()
    elif "exit" in c or "stop" in c or "goodbye" in c:
        speak("Goodbye!")
        exit (0)
    elif "take_screenshot" in c.lower():
        take_screenshot()
    elif "advice" in c.lower():
        advice.get_advice(language='hi')
    elif"joke" in c.lower():
        joke.get_joke()
    else:
     speak("Command not recoganize")
    return True

if __name__ == "__main__":
    speak("Initializing Jarvis.......")

    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    c = r.recognize_google(audio)
                    processcommand(c)
                if not processcommand(c):
                    break  # Stop the loop if the c is to stop Jarvis
        except sr.RequestError as e:
            print(f"Error: {e}")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print(f"Error: {e}")
