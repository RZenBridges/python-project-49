import random
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'
OPERATOR = {
    '+': lambda x, y: add(x, y),
    '*': lambda x, y: mul(x, y),
    '-': lambda x, y: sub(y, x),
}


def generate_question_and_answer():
    num1 = random.randint(1, 10)
    num2 = random.randint(11, 100)
    action = random.choice(list(OPERATOR.keys()))
    answer = OPERATOR[action](num1, num2)
    return f'{num2} {action} {num1}', str(answer)
