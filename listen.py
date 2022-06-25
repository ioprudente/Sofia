import speech_recognition as recognition

from speaker import speak

recognizer = recognition.Recognizer()

def listen():
    with recognition.Microphone() as microphone:

        recognizer.adjust_for_ambient_noise(microphone, duration=2)
        audio = recognizer.listen(microphone, 10)

        transcriptions = recognizer.recognize_google(audio, language='pt-BR')
        transcription = str(transcriptions)

        return transcription
