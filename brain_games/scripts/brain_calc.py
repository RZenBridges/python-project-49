#!/usr/bin/env python3

from brain_games.engine import game_on
from brain_games.games.calc import generate_game


def main():
    """ Starts a games that presents aa arithmetic expression"""
    """ for the user to calculate """

    game_on("What is the result of the expression?", generate_game)


if __name__ == "__main__":
    main()
