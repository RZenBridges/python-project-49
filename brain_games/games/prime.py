import random

YES = 'yes'
NO = 'no'


def is_prime(number):
    if number == 1:
        return "yes"
    for i in range(2, number):
        if number % i == 0:
            return "no"
    return "yes"


def generate_game():
    random_number = random.randint(1, 100)
    correct_answer = is_prime(random_number)
    return random_number, correct_answer