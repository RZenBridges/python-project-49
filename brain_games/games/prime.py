import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return 'no'
    return 'yes'


def generate_game():
    number = random.randint(1, 100)
    correct_answer = is_prime(number)
    return str(number), str(correct_answer)
