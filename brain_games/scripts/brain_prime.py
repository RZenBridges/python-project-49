#!/usr/bin/env python3

from brain_games.engine import play_game
from brain_games.games.prime import generate_game
from brain_games.scripts import brain_games as game_interface


def main():
    """ Starts a games that presents two numbers for the user"""
    """ to answer to find the greates common divisor"""

    player = game_interface.naming()
    description = 'Answer "yes" if given number is prime. '\
                  'Otherwise answer "no".'
    victory, user_answer, key = play_game(description, generate_game)

    if victory:
        game_interface.winning(player)
    else:
        game_interface.losing(user_answer, key, player)


if __name__ == "__main__":
    main()
