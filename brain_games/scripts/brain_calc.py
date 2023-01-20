#!/usr/bin/env python3

import random
import brain_games.scripts.brain_games as calc_game


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return b - a


def main():
    name = calc_game.main()
    print("What is the result of the expression?")
    correct_answers = 0
    continue_game = True
    while correct_answers < 3 and continue_game:
        a = random.randint(1, 10)
        b = random.randint(11, 100)
        operator = {"+": add, "*": multiply, "-": subtract}
        action = random.choice(["+","*","-"])
        key = operator[action](a, b)
        print(f"Question: {b} {action} {a}")
        ans = input("Your answer: ")
        if int(ans) == key:
            correct_answers += 1
            print("Correct!")
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{key}'")
            print(f"Let's try again, {name.capitalize()}!")
            continue_game = False
    else:
        if correct_answers == 3:
            print(f"Congratulations, {name.capitalize()}!")

if __name__ == "__main__":
    main()
