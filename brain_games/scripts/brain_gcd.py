
import random
import brain_games.scripts.brain_games as introduction

def main():
    name = introduction.main().capitalize()
    print("Find the greatest common divisor of given number.")
    correct_answers = 0
    continue_game = True
    while correct_answers < 3 and continue_game:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f"Question: {a} {b}")
        ans = int(input("Your answer: "))
        a_range = []
        b_range = []
        for num in range(1, a+1):
            if a % num == 0:
                a_range.append(num)
        for num in range(1, b+1):
            if b % num == 0:
                b_range.append(num)
        common_d = max(set(a_range) & set(b_range))
        if common_d == ans:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{ans} is a wrong answer ;('. Correct answer was '{common_d}'.")
            print(f"Let's try again, {name}!")
            continue_game = False
    else:
        if correct_answers == 3:
            print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
