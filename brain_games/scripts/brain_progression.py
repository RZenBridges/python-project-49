import random
import brain_games.scripts.brain_games as game_interface


def generate_progression():
    start = random.randint(1, 15)
    step = random.randint(1, 10)
    progression = [str(i) for i in list(range(start, start+step*10, step))]
    hide_index = random.randint(0, 9)
    hidden_element = progression[hide_index]
    progression[hide_index] = '..'
    return (' '.join(progression), hidden_element)


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
