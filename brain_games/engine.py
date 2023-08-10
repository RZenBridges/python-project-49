from brain_games.cli import welcome_user

GAME_ROUNDS_COUNT = 3


def run(game, rounds=GAME_ROUNDS_COUNT):
    print('Welcome to the Brain Games!')
    player = welcome_user()
    print(game.DESCRIPTION)

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
