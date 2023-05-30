import random

YES = 'yes'
NO = 'no'


def generate_game():
    number = random.randint(1, 100)
    if number % 2 == 0:
        key = YES
    else:
        key = NO
    return number, key
