import math
import random


def generate_game():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    return (str(number_1), str(number_2)), str(math.gcd(number_1, number_2))
