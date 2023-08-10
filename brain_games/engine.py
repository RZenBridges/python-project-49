from brain_games.scripts import brain_games as game_interface

ROUNDS = 3


def game_on(game, rounds=ROUNDS):
    print(game.DESCRIPTION)

    player = game_interface.naming()

    for _ in range(rounds):
        question, answer = game.generate_game()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')

        if user_answer != answer:
            print(f"'{user_answer}' is a wrong answer ;(. "
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {player}!")
            return

            print('Correct!')
        print(f'Congratulations, {player}!')
