import random

YES = 'yes'
NO = 'no'


def reverse_answer(answer):
    if answer == YES:
        return NO
    if answer == NO:
        return YES


def generate_number():
    number = random.randint(1, 100)
    if number % 2 == 0:
        key = YES
    else:
        key = NO
    return number, key
