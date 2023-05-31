#!/usr/bin/env python3

import brain_games.scripts.brain_games as game_interface
from brain_games.games.progression import generate_game


def main():
    """ Starts a games that presents a number sequence with a gap"""
    """ for the user to fill"""

    name = game_interface.naming()
    print("What number is missing in the progression?")

    for round in range(3):
        progression, key = generate_game()
        print(f"Question: {progression}")
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
