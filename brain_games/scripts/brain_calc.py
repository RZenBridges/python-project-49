#!/usr/bin/env python3

import brain_games.scripts.brain_games as game_interface
from brain_games.games.calc import generate_equation


def main():
    name = game_interface.naming()
    print("What is the result of the expression?")
    correct_answers = 0
    continue_game = True
    while correct_answers < 3 and continue_game:
        equation, key = generate_equation()
        print(f"Question: {equation}")
        answer = input("Your answer: ")
        if int(answer) == key:
            correct_answers += 1
            print("Correct!")
        else:
            game_interface.losing(answer, key, name)
            continue_game = False
    else:
        game_interface.winning(correct_answers, name)


if __name__ == "__main__":
    main()
