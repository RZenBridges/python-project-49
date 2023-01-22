
import random
import brain_games.scripts.brain_games as game_interface


def is_int_divisor(divisor, num, output: list):
    """Adds divisor to the output if num % divisor = 0"""
    if num % divisor == 0:
        output.append(divisor)


def common_d_finder(a, b):
    """Finds the biggest common ineger divisor for 2 input  numbers"""
    a_range = []
    b_range = []
    for i in range(1, a + 1):
        is_int_divisor(i, a, a_range)
    for i in range(1, b + 1):
        is_int_divisor(i, b, b_range)
    return max(set(a_range) & set(b_range))


def main():
    name = game_interface.naming()
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
