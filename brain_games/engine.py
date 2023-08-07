def play_game(game_description, generate_game, rounds=3):
    print(game_description)

    for round in range(rounds):
        task, key = generate_game()
        print(f"Question: {' '.join(task) if type(task) == tuple else task}")
        user_answer = input("Your answer: ")

        if user_answer == key and rounds - round != 1:
            print("Correct!")
            continue
        return user_answer == key, user_answer, key
