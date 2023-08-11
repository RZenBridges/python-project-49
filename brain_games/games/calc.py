import random
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'
OPERATOR = {
    '+': add,
    '*': mul,
    '-': sub,
}


def generate_question_and_answer():
    num1 = random.randint(1, 10)
    num2 = random.randint(11, 100)
    action = random.choice(list(OPERATOR.keys()))
    answer = OPERATOR[action](num2, num1)
    return f'{num2} {action} {num1}', str(answer)
