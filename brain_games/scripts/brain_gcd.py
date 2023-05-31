#!/usr/bin/env python3

import brain_games.scripts.brain_games as game_interface
from brain_games.games.gcd import generate_game


def main():
    """ Starts a games that presents two numbers for the user"""
    """ to answer to find the greatest common divisor"""

    name = game_interface.naming()
    print("Find the greatest common divisor of given numbers.")

    for round in range(3):
        numbers, key = generate_game()
        print(f"Question: {numbers[0]} {numbers[1]}")
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
