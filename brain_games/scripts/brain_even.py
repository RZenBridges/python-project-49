#!/usr/bin/env python3

from brain_games import games
from brain_games.engine import run


def main():
    ''' Starts a games that presents a number for the user'''
    ''' to answer if the number is even or not '''

    run(games.even)


if __name__ == '__main__':
    main()
