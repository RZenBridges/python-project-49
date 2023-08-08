#!/usr/bin/env python3

from brain_games.engine import game_on
from brain_games.games import calc


def main():
    """ Starts a game that presents an arithmetic expression"""
    """ for the user to calculate """

    game_on(calc.DESCRIPTION, calc.generate_game)


if __name__ == "__main__":
    main()
