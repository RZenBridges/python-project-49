import brain_games.scripts.brain_games as game_interface
from brain_games.games.progression import generate_progression


def main():
    name = game_interface.naming()
    print("What number is missing in the progression?")
    correct_answers = 0
    continue_game = True
    while correct_answers < 3 and continue_game:
        progression, key = generate_progression()
        print(f"Question: {progression}")
        user_answer = input("Your answer: ")
        if int(user_answer) == int(key):
            correct_answers += 1
            print("Correct!")
        else:
            game_interface.losing(user_answer, key, name)
            continue_game = False
    else:
        game_interface.winning(correct_answers, name)


if __name__ == "__main__":
    main()
