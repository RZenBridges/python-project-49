#!/usr/bin/env python3

import brain_games.scripts.brain_games as game_interface
from brain_games.games.even import generate_game


def main():
    """ Starts a games that presents a number for the user"""
    """ to answer if the number is even or not """

    name = game_interface.naming()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    continue_game = True

    while correct_answers < 3 and continue_game:
        number, key = generate_game()
        print(f"Question: {number}")
        user_answer = input("Your answer: ")
        if user_answer == key:
            correct_answers += 1
            print("Correct!")
        else:
            game_interface.losing(user_answer, key, name)
            continue_game = False
    else:
        game_interface.winning(correct_answers, name)


if __name__ == '__main__':
    main()
