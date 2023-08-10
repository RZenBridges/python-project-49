#!/usr/bin/env python3

from brain_games.engine import game_on
from brain_games import games


def main():
    ''' Starts a game that presents an arithmetic expression'''
    ''' for the user to calculate '''

    game_on(games.calc)


if __name__ == '__main__':
    main()
