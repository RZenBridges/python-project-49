#!/usr/bin/env python3
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    welcome_user().capitalize()


def naming():
    print("Welcome to the Brain Games!")
    return welcome_user().capitalize()


if __name__ == "__main__":
    main()
