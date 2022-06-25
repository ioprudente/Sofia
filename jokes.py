import random 

jokes = [
    'Por que o Batman colocou o batmóvel no seguro?'
    'Porque ele tem medo que Robin',
    'Como o Batman conheceu o Robin?'
    'Pelo bat-papo',
    'Onde comprar comida para um Super-Herói?'
    'No Super-Mercado',
    'Por que o Luke Skywalker escondeu seus livros?'
    'Porque ele não quer que a Princesa Leia',
    'Qual a diferença entre o Frankstein e o Robocop?'
    'O Frankstein foi operado em hospital público, o Robocop em um particular',
    'Por que o bombeiro não caminha?'
    'Porque ele socorre',
    'Por que o motoboy foi demitido?'
    'Porque não estava capacetado para o trabalho',
    
]

def getRandomJoke():
    number_of_jokes = len(jokes)
    random_joke_index = random.randint(0, number_of_jokes)
    
    return jokes[random_joke_index]
    