import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    number = random.randint(1, 100)
    answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), answer
