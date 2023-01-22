#!/usr/bin/env python3

import random
import brain_games.scripts.brain_games as game_interface


def num_is_even(number, ans):
    """ Checks if the number is even and if the user's answer is correct"""
    if number % 2 == 0 and ans == 'yes':
        print("Correct!")
        return (True, 'no')
    elif number % 2 == 1 and ans == 'no':
        print("Correct!")
        return (True, 'yes')
    elif number % 2 == 1 and ans != 'no':
        return (False, 'no')
    elif number % 2 == 0 and ans != 'yes':
        return (False, 'yes')


def main():
    """ Starts a games that apresents a number for the user to answer if the number is even or not """
    name = game_interface.naming()
    correct_answers = 0
    continue_game = True
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while correct_answers < 3 and continue_game:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        ans = input("Your answer: ")
        continue_game, opp = num_is_even(number, ans)
        if continue_game:
            correct_answers += 1
        else:
            game_interface.losing(ans, opp, name)
    else:
        game_interface.winning(correct_answers, name)


if __name__ == '__main__':
    main()
