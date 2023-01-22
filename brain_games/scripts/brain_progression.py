import random
import brain_games.scripts.brain_games as game_interface


def progression_generator():
    start = random.randint(1, 15)
    step = random.randint(1, 10)
    progression = [start]
    for i in range(9):
        progression.append(progression[-1] + step)
    sqnc = [str(i) for i in progression]
    ind = random.randint(0, 9)
    hidden = sqnc[ind]
    sqnc[ind] = '..'
    return (' '.join(sqnc), hidden)


def main():
    name = game_interface.main()
    print("What number is missing in the progression?")
    correct_answers = 0
    continue_game = True
    while correct_answers < 3 and continue_game:
        progression, key = progression_generator()
        print(f"Question: {progression}")
        ans = input("Your answer: ")
        if int(ans) == int(key):
            correct_answers += 1
            print("Correct!")
        else:
            game_interface.losing(ans, key, name)
            continue_game = False
    else:
        game_interface.winning(correct_answers, name)


if __name__ == "__main__":
    main()
