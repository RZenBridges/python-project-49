import random
import brain_games.scripts.brain_games as game_interface

YES = 'yes'
NO = 'no'


def is_prime(number):
    if number == 1:
        return "yes"
    for i in range(2, number):
        if number % i == 0:
            return "no"
    return "yes"


def guess_result(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        return False


def draw_game():
    random_number = random.randint(1, 100)
    correct_answer = is_prime(random_number)
    return random_number, correct_answer


def main():
    name = game_interface.naming()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers = 0
    continue_game = True
    while correct_answers < 3 and continue_game:
        number, correct_answer = draw_game()
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
