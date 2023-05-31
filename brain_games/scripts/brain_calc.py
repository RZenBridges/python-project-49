#!/usr/bin/env python3

import brain_games.scripts.brain_games as game_interface
from brain_games.games.calc import generate_game


def main():
    """ Starts a games that presents aa arithmetic expression"""
    """ for the user to calculate """

    name = game_interface.naming()
    print("What is the result of the expression?")

    for round in range(3):
        equation, key = generate_game()
        print(f"Question: {equation}")
        user_answer = input("Your answer: ")

        if user_answer == key:
            print("Correct!")
        else:
            game_interface.losing(user_answer, key, name)
            break
    else:
        game_interface.winning(name)


if __name__ == "__main__":
    main()
