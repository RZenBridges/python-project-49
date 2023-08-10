import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_game():
    start = random.randint(1, 15)
    step = random.randint(1, 10)
    progression = [str(i) for i in range(start, start + step * 10, step)]
    hide_index = random.randint(0, 9)
    answer = progression[hide_index]
    progression[hide_index] = '..'
    return ' '.join(progression), answer
