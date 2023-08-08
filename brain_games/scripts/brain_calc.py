#!/usr/bin/env python3

from brain_games.engine import game_on, GAME


def main():
    """ Starts a games that presents aa arithmetic expression"""
    """ for the user to calculate """

    game_on(GAME["calc"])


if __name__ == "__main__":
    main()
