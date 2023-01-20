#!/usr/bin/env python3

import random
import prompt


def hello():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name.capitalize()}!")
    return name


def main():
    name = hello()
    correct_answers = 0
    continue_game = True
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    while correct_answers < 3 and continue_game:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        ans = input("Your answer: ")
        if number % 2 == 0 and ans == "yes":
            correct_answers += 1
            print("Correct!")
        elif number % 2 == 1 and ans == "no":
            correct_answers += 1
            print("Correct!")
        else:
            continue_game = False
            if ans == "yes":
                opp = "no"
            elif ans == "no":
                opp = "yes"
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{opp}'")
            print(f"Let's try again, {name.capitalize()}!")
    if correct_answers == 3:
        print(f"Congratulation, {name.capitalize()}!")


if __name__ == '__main__':
    main()
