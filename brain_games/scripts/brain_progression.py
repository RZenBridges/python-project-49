#!/usr/bin/env python3

from brain_games.engine import game_on, GAME


def main():
    """ Starts a games that presents a number sequence with a gap"""
    """ for the user to fill"""

    game_on(GAME["progression"])


if __name__ == "__main__":
    main()
