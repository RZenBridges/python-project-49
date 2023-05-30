#!/usr/bin/env python3

import brain_games.scripts.brain_games as game_interface
from brain_games.games.gcd import generate_game


def main():
    """ Starts a games that presents two numbers for the user"""
    """ to answer to find the greatest common divisor"""

    name = game_interface.naming()
    print("Find the greatest common divisor of given numbers.")
    correct_answers = 0
    continue_game = True

    while correct_answers < 3 and continue_game:
        number_1, number_2, key = generate_game()
        print(f"Question: {number_1} {number_2}")
        user_answer = int(input("Your answer: "))
        if user_answer == key:
            correct_answers += 1
            print("Correct!")
        else:
            game_interface.losing(user_answer, key, name)
            continue_game = False
    else:
        game_interface.winning(correct_answers, name)


if __name__ == "__main__":
    main()
