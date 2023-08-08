#!/usr/bin/env python3

from brain_games.engine import game_on
from brain_games.games.gcd import generate_game


def main():
    """ Starts a games that presents two numbers for the user"""
    """ to answer to find the greatest common divisor"""

    game_on("Find the greatest common divisor of given numbers.",
            generate_game)


if __name__ == "__main__":
    main()
