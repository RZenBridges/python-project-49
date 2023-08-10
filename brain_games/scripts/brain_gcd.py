#!/usr/bin/env python3

from brain_games import games
from brain_games.engine import run


def main():
    ''' Starts a games that presents two numbers for the user'''
    ''' to answer to find the greatest common divisor'''

    run(games.gcd)


if __name__ == '__main__':
    main()
