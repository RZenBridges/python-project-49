#!/usr/bin/env python3

from brain_games.engine import game_on
from brain_games.games.prime import generate_game


def main():
    """ Starts a games that presents two numbers for the user"""
    """ to answer to find the greates common divisor"""

    game_on('Answer "yes" if given number is prime. Otherwise answer "no".',
            generate_game)


if __name__ == "__main__":
    main()
