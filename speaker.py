import pyttsx3

def speak(content):
    engine = pyttsx3.init()
    engine.say(content)
    engine.runAndWait()

