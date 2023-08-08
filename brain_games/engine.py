from brain_games.scripts import brain_games as game_interface


def play_game(generate_game, rounds=3):

    for round in range(rounds):
        task, key = generate_game()
        print(f"Question: {' '.join(task) if type(task) == tuple else task}")
        user_answer = input("Your answer: ")

        if user_answer == key and rounds - round != 1:
            print("Correct!")
            continue
        return user_answer == key, user_answer, key


def game_on(description, generate_game):
    print(description)

    player = game_interface.naming()
    victory, user_answer, key = play_game(generate_game)

    if victory:
        game_interface.winning(player)
    else:
        game_interface.losing(user_answer, key, player)
