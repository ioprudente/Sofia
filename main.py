from ast import Break
import wikipedia
import pyttsx3
import speech_recognition as recognition
from speaker import speak
from listen import listen
from jokes import getRandomJoke
from  findMathOperation import find_math_operation
from  dateAndTime import hour, data
from searchOnWikipedia import searchOnWikipedia

engine = pyttsx3.init()


def setWikipediaProsperties():
    wikipedia.set_lang('pt')

def main():

    setWikipediaProsperties()
    while True:
        try:
            transcription = listen()
            print(transcription)

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
                speak(
                    'Sou a Sofia, uma futura IA de primeira'
                    'categoria criada pela Isabella,'
                    'aliás, segue ela nas redes sociais,'
                    '@ioprudente, atualmente não aprendo'
                    'mas estou me esforçando pra isso.')
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
            
            joke_found = transcription.find('piada') >= 0
            tell_me_found = transcription.find('conte') >= 0 or transcription.find('conta') >= 0

            if joke_found and tell_me_found:
                joke = getRandomJoke()
                speak(joke)
                continue
            
            response = searchOnWikipedia(transcription)
            speak(response)
            
        except Exception:
            speak('Não entendi, tente novamente')
            print(Exception)
            
main()