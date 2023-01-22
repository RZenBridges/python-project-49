#!/usr/bin/env python3
import brain_games.cli


def main():
    print("Welcome to the Brain Games!")
    name = brain_games.cli.welcome_user()
    return name.capitalize()


def winning(correct_answers, name):
    if correct_answers == 3:
        print(f"Congratulations, {name}!")


def losing(right, wrong, name):
    print(f"'{right}' is a wrong answer ;('. Correct answer was '{wrong}'.")
    print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()
