import random
import brain_games.scripts.brain_games as game_interface


def main():
    name = game_interface.main()
    print("What number is missing in the progression?")
    correct_answers = 0
    continue_game = True
    while correct_answers < 3 and continue_game:
        start = random.randint(1, 15)
        step = random.randint(1, 10)
        progression = [start]
        for i in range(9):
            progression.append(progression[-1] + step)
        sqnc = [str(i) for i in progression]
        ind = random.randint(0, 9)
        hidden = sqnc[ind]
        sqnc[ind] = '..'
        print(f"Question: {' '.join(sqnc)}")
        ans = input("Your answer: ")
        if int(ans) == int(hidden):
            correct_answers += 1
            print("Correct!")
        else:
            game_interface.losing(ans, hidden, name)
            continue_game = False
    else:
        game_interface.winning(correct_answers, name)


if __name__ == "__main__":
    main()
