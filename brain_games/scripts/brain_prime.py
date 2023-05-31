#!/usr/bin/env python3

import brain_games.scripts.brain_games as game_interface
from brain_games.games.prime import generate_game


def main():
    """ Starts a games that presents two numbers for the user"""
    """ to answer to find the greates common divisor"""

    name = game_interface.naming()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for round in range(3):
        number, key = generate_game()
        print(f"Question: {number}")
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
