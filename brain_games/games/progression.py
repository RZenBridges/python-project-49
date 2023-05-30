import random


def generate_game():
    start = random.randint(1, 15)
    step = random.randint(1, 10)
    progression = [str(i) for i in list(range(start, start + step * 10, step))]
    hide_index = random.randint(0, 9)
    hidden_element = int(progression[hide_index])
    progression[hide_index] = '..'
    return ' '.join(progression), hidden_element
