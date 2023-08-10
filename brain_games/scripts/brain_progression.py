#!/usr/bin/env python3

from brain_games.engine import game_on
from brain_games import games


def main():
    ''' Starts a games that presents a number sequence with a gap'''
    ''' for the user to fill'''

    game_on(games.progression)


if __name__ == '__main__':
    main()
