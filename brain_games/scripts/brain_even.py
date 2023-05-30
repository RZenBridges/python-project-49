#!/usr/bin/env python3

import brain_games.scripts.brain_games as game_interface
from brain_games.games.even import num_is_even, generate_number


def main():
    """ Starts a games that presents a number for the user"""
    """ to answer if the number is even or not """
    name = game_interface.naming()
    correct_answers = 0
    continue_game = True
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while correct_answers < 3 and continue_game:
        number = generate_number()
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
