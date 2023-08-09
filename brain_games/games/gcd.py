import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return f'{num1} {num2}', str(math.gcd(num1, num2))
