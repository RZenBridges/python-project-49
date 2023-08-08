import brain_games.games
from brain_games.scripts import brain_games as game_interface


GAME = {
    "calc": (brain_games.games.calc.generate_game,
             "What is the result of the expression?"),
    "even": (brain_games.games.even.generate_game,
             'Answer "yes" if the number is even, otherwise answer "no".'),
    "gcd": (brain_games.games.gcd.generate_game,
            "Find the greatest common divisor of given numbers."),
    "prime": (brain_games.games.prime.generate_game,
              'Answer "yes" if given number is prime. Otherwise answer "no".'),
    "progression": (brain_games.games.progression.generate_game,
                    "What number is missing in the progression?"),
}


def play_game(generate_game, rounds=3):

    for round in range(rounds):
        task, key = generate_game()
        print(f"Question: {' '.join(task) if type(task) == tuple else task}")
        user_answer = input("Your answer: ")

        if user_answer == key and rounds - round != 1:
            print("Correct!")
            continue
        return user_answer == key, user_answer, key


def game_on(game):
    description, generate_game = game
    print(description)

    player = game_interface.naming()
    victory, user_answer, key = play_game(generate_game)

    if victory:
        game_interface.winning(player)
    else:
        game_interface.losing(user_answer, key, player)
