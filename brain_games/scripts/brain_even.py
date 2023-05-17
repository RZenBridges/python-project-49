#!/usr/bin/env python3

import random
import brain_games.scripts.brain_games as game_interface

YES = 'yes'
NO = 'no'


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


def main():
    """ Starts a games that presents a number for the user"""
    """ to answer if the number is even or not """
    name = game_interface.naming()
    correct_answers = 0
    continue_game = True
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while correct_answers < 3 and continue_game:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ")
        continue_game, opposite = num_is_even(number, user_answer)
        if continue_game:
            correct_answers += 1
        else:
            game_interface.losing(user_answer, opposite, name)
    else:
        game_interface.winning(correct_answers, name)


if __name__ == '__main__':
    main()
