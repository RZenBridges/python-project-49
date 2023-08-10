import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def generate_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return f'{num1} {num2}', str(gcd(num1, num2))
