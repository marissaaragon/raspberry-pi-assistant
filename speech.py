import pyttsx3
from config import TTS_RATE
import speech_recognition as sr


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', TTS_RATE)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)
        text = text.lower()
        return text