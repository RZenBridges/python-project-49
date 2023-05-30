import random


OPERATOR = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "-": lambda x, y: y - x
}


def generate_equation():
    a = random.randint(1, 10)
    b = random.randint(11, 100)
    action = random.choice(list(OPERATOR.keys()))
    key = OPERATOR[action](a, b)
    return (f"{b} {action} {a}", key)
