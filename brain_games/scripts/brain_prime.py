#!/usr/bin/env python3

from brain_games.engine import game_on, GAME


def main():
    """ Starts a games that presents two numbers for the user"""
    """ to answer to find the greates common divisor"""

    game_on(GAME["prime"])


if __name__ == "__main__":
    main()
