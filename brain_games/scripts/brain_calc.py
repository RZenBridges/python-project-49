#!/usr/bin/env python3

import brain_games.scripts.brain_games as game_interface
from brain_games.games.calc import generate_equation


def main():
    """ Starts a games that presents aa arithmetic expression"""
    """ for the user to calculate """

    name = game_interface.naming()
    print("What is the result of the expression?")
    correct_answers = 0
    continue_game = True

    while correct_answers < 3 and continue_game:
        equation, key = generate_equation()
        print(f"Question: {equation}")
        user_answer = input("Your answer: ")
        if int(user_answer) == key:
            correct_answers += 1
            print("Correct!")
        else:
            game_interface.losing(user_answer, key, name)
            continue_game = False
    else:
        game_interface.winning(correct_answers, name)


if __name__ == "__main__":
    main()
