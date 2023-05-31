import random


def generate_game():
    number = random.randint(1, 100)
    key = 'yes' if number % 2 == 0 else 'no'
    return number, key
