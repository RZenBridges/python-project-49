#!/usr/bin/env python3

from brain_games import games
from brain_games.engine import run


def main():
    ''' Starts a game that presents an arithmetic expression'''
    ''' for the user to calculate '''

    run(games.calc)


if __name__ == '__main__':
    main()
