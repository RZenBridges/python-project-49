#!/usr/bin/env python3

from brain_games import games
from brain_games.engine import run


def main():
    ''' Starts a games that presents a number sequence with a gap'''
    ''' for the user to fill'''

    run(games.progression)


if __name__ == '__main__':
    main()
