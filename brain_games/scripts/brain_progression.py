#!/usr/bin/env python3

from brain_games.engine import play_game
from brain_games.games.progression import generate_game
from brain_games.scripts import brain_games as game_interface


def main():
    """ Starts a games that presents a number sequence with a gap"""
    """ for the user to fill"""

    player = game_interface.naming()
    description = "What number is missing in the progression?"
    victory, user_answer, key = play_game(description, generate_game)

    if victory:
        game_interface.winning(player)
    else:
        game_interface.losing(user_answer, key, player)


if __name__ == "__main__":
    main()
