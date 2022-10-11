import random

not_found_messages = [
    'Não entendi, tente novamente',
    'Poderia falar de novo',
    'Desculpa não entendi, pode repetir?'
]

def get_not_found_message():

    if not_found_messages:
        number_of_not_found_messages = len(not_found_messages)
        not_found_messages_index = random.randint(0, number_of_not_found_messages)

        return not_found_messages[not_found_messages_index]
