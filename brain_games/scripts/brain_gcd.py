import math
import random
import brain_games.scripts.brain_games as game_interface


def main():
    name = game_interface.naming()
    print("Find the greatest common divisor of given numbers.")
    correct_answers = 0
    continue_game = True
    while correct_answers < 3 and continue_game:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f"Question: {a} {b}")
        user_answer = int(input("Your answer: "))
        common_d = math.gcd(a, b)
        if common_d == user_answer:
            print("Correct!")
            correct_answers += 1
        else:
            game_interface.losing(user_answer, common_d, name)
            continue_game = False
    else:
        game_interface.winning(correct_answers, name)


if __name__ == "__main__":
    main()
