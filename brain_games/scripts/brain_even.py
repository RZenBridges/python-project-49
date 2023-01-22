#!/usr/bin/env python3

import random
import brain_games.scripts.brain_games as game_interface


def num_is_even(number, ans):
    if number % 2 == 0 and ans == "yes":
        print("Correct!")
        return True
    elif number % 2 == 1 and ans == "no":
        print("Correct!")
        return True
    else:
        return False


def main():
    name = game_interface.main()
    correct_answers = 0
    continue_game = True
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    while correct_answers < 3 and continue_game:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        ans = input("Your answer: ")
        continue_game = num_is_even(number, ans)
        if continue_game == True:
            correct_answers +=1
        else:
            if ans == "yes":
                opp = "no"
            elif ans == "no":
                opp = "yes"
            game_interface.losing(ans, opp, name)
    else:
        game_interface.winning(correct_answers, name)


if __name__ == '__main__':
    main()
