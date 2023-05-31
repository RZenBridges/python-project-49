#!/usr/bin/env python3
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    welcome_user().capitalize()


def naming():
    print("Welcome to the Brain Games!")
    return welcome_user().capitalize()


def winning(name):
    print(f"Congratulations, {name}!")


def losing(wrong, right, name):
    print(f"'{wrong}' is a wrong answer ;('. Correct answer was '{right}'.")
    print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()
