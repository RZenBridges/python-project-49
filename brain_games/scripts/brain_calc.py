#!/usr/bin/env python3

import random
import brain_games.scripts.brain_games as game_interface


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return b - a


def phrase_generator():
    a = random.randint(1, 10)
    b = random.randint(11, 100)
    operator = {"+": add, "*": multiply, "-": subtract}
    action = random.choice(["+", "*", "-"])
    key = operator[action](a, b)
    return (f"{b} {action} {a}", key)


def main():
    name = game_interface.main()
    print("What is the result of the expression?")
    correct_answers = 0
    continue_game = True
    while correct_answers < 3 and continue_game:
        equation, key = phrase_generator()
        print(f"Question: {equation}")
        ans = input("Your answer: ")
        if int(ans) == key:
            correct_answers += 1
            print("Correct!")
        else:
            game_interface.losing(ans, key, name)
            continue_game = False
    else:
        game_interface.winning(correct_answers, name)


if __name__ == "__main__":
    main()
