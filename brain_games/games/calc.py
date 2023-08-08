import random


DESCRIPTION = "What is the result of the expression?"
OPERATOR = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "-": lambda x, y: y - x
}


def generate_game():
    num1 = random.randint(1, 10)
    num2 = random.randint(11, 100)
    action = random.choice(list(OPERATOR.keys()))
    key = str(OPERATOR[action](num1, num2))
    return f"{num2} {action} {num1}", key
