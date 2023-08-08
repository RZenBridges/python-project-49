from brain_games.scripts import brain_games as game_interface

ROUNDS = 3


def game_on(description, generate_game, rounds=ROUNDS):
    print(description)

    player = game_interface.naming()

    for round in range(1, rounds + 1):
        task, answer = generate_game()
        print(f"Question: {' '.join(task) if type(task) == tuple else task}")
        user_answer = input("Your answer: ")

        if user_answer == answer and round != rounds:
            print("Correct!")
            continue

        if user_answer == answer:
            print(f"Congratulations, {player}!")
        else:
            print(f"'{user_answer}' is a wrong answer ;('. "
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {player}!")
        break
