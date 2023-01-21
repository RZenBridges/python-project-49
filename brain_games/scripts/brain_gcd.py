
import random
import brain_games.scripts.brain_games as game_interface


def common_d_finder(a, b):
    a_range = []
    b_range = []
    for num in range(1, a + 1):
        if a % num == 0:
            a_range.append(num)
    for num in range(1, b + 1):
        if b % num == 0:
            b_range.append(num)
    return max(set(a_range) & set(b_range))


def main():
    name = game_interface.main()
    print("Find the greatest common divisor of given number.")
    correct_answers = 0
    continue_game = True
    while correct_answers < 3 and continue_game:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f"Question: {a} {b}")
        ans = int(input("Your answer: "))
        common_d = common_d_finder(a, b)
        if common_d == ans:
            print("Correct!")
            correct_answers += 1
        else:
            game_interface.losing(ans, common_d, name)
            continue_game = False
    else:
        game_interface.winning(correct_answers, name)


if __name__ == "__main__":
    main()
