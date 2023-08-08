#!/usr/bin/env python3

from brain_games.engine import game_on
from brain_games.games import progression


def main():
    """ Starts a games that presents a number sequence with a gap"""
    """ for the user to fill"""

    game_on(progression.DESCRIPTION, progression.generate_game)


if __name__ == "__main__":
    main()
