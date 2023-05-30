import random

YES = 'yes'
NO = 'no'


def generate_number():
    return random.randint(1, 100)


def return_opposit(answer):
    if answer == YES:
        return NO
    if answer == NO:
        return YES


def num_is_even(number, answer):
    """ Checks if the number is even and if the user's answer is correct"""
    if (number % 2 == 0 and answer == YES) or\
            (number % 2 == 1 and answer == NO):
        print("Correct!")
        return (True, return_opposit(answer))
    elif number % 2 == 0 and answer != YES:
        return (False, YES)
    elif number % 2 == 1 and answer != NO:
        return (False, NO)
