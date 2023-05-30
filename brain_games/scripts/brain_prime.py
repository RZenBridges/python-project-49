import brain_games.scripts.brain_games as game_interface
from brain_games.games.prime import guess_result, generate_game


def main():
    name = game_interface.naming()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers = 0
    continue_game = True
    while correct_answers < 3 and continue_game:
        number, correct_answer = generate_game()
        print(f"Question: {number}")
        user_answer = input("Your answer: ")
        continue_game = guess_result(user_answer, correct_answer)
        if continue_game:
            correct_answers += 1
        else:
            game_interface.losing(user_answer, correct_answer, name)
    else:
        game_interface.winning(correct_answers, name)


if __name__ == "__main__":
    main()
