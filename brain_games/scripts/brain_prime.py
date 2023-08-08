#!/usr/bin/env python3

from brain_games.engine import game_on
from brain_games.games import prime


def main():
    """ Starts a games that presents two numbers for the user"""
    """ to answer to find the greates common divisor"""

    game_on(prime.DESCRIPTION, prime.generate_game)


if __name__ == "__main__":
    main()
