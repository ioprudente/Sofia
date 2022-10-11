from ast import Break
from email import message
from gettext import find
from hashlib import new
from http.client import OK
from timeit import repeat
import wikipedia
import pyttsx3
import speech_recognition as recognition
from speaker import speak
from listen import listen
from jokes import getRandomJoke
from findMathOperation import find_math_operation
from dateAndTime import hour, data
from searchOnWikipedia import searchOnWikipedia
from notFoundMessages import get_not_found_message
from music import playlists
from news import news

engine = pyttsx3.init()

def setWikipediaProsperties():
    wikipedia.set_lang('pt')

def main():

    setWikipediaProsperties()
    while True:
        try:
            transcription = listen()
            
            name_found = transcription == 'Sofia'

            if name_found:
                speak('Oi, o que você quer saber ?')
                continue
            
            shoud_quit = transcription == 'vai dormir'
            if shoud_quit:
                speak('Valeu')
                return

            name =  transcription.find('Qual é o seu nome') >= 0
            if name:
                speak('Meu nome é Sofia')
                continue

            aboutSofia = transcription.find('Fale sobre você') >= 0
            if aboutSofia:
                speak('Sou a Sofia, sua assistente virtual')
                continue       

            transcribe = transcription == 'transcreva'
            if transcribe:
                speak('Modo de transcrição ativado')
                transcribe = listen()
                print(transcribe)
                continue

            repeat = transcription == 'repita'
            if repeat:
                speak('Modo de repetição ativado')
                transcription = listen()
                speak(transcription) 
                continue

            actual_time = transcription.find('quantas') >= 0 and transcription.find('horas') >= 0
            if actual_time:
                time = hour()
                speak(time)
                continue

            actual_data = transcription.find('data') >= 0
            if actual_data:
                data_today = data()
                speak(data_today)
                continue
                
            math_operation = find_math_operation(transcription)
            math_operation_found = bool(math_operation) and len(math_operation[0]) >= 3
    
            if math_operation_found:
                add_found = math_operation[0][0] == 'soma' or math_operation[0][0] == 'some'

                if add_found:
                    first_number = int(math_operation[0][1])
                    second_number = int(math_operation[0][2])

                    sum = first_number + second_number
                    speak(sum)
                    continue
            
            if math_operation_found:
                subtract_found = math_operation[0][0] == 'subtraia'
            
                if subtract_found:
                    first_number = int(math_operation[0][1])
                    second_number = int(math_operation[0][2])

                    subtract= first_number - second_number
                    speak(subtract)
                    continue

            if math_operation_found:
                divide_found = math_operation[0][0] == 'divida'
            
                if divide_found:
                    first_number = int(math_operation[0][1])
                    second_number = int(math_operation[0][2])

                    divide = first_number // second_number
                    speak(divide)
                    continue
            
            music_found = transcription.find('música') >= 0
            if music_found:
                speak('Vou tocar as musiquinhas')
                playlists('musics')
                break

            news_found = transcription.find('notícias') >= 0
            if  news_found:
                breaking_news = news()
                speak(breaking_news)
                continue
            
            joke_found = transcription.find('piada') >= 0
            tell_me_found = transcription.find('conte') >= 0 or transcription.find('conta') >= 0

            if joke_found and tell_me_found:
                joke = getRandomJoke()
                speak(joke)
                continue
            
            response = searchOnWikipedia(transcription)
            speak(response)

        except Exception:
                speak(get_not_found_message())
                
main()
