import brain_games.scripts.brain_games as game_interface
import random


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return "no"
    return "yes"


def main():
    name = game_interface.main()
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    correct_answers = 0
    continue_game = True
    while correct_answers < 3 and continue_game:
        num = random.randint(1, 100)
        print(f"Question: {num}")
        key = is_prime(num)
        ans = input("Your answer: ")
        if ans == key:
            print("Correct!")
            correct_answers += 1
        else:
            game_interface.losing(ans, key, name)
            continue_game = False
    else:
        game_interface.winning(correct_answers, name)


if __name__ == "__main__":
    main()
