import math
import random


def generate_numbers():
    a, b = random.randint(1, 100), random.randint(1, 100)
    return a, b, math.gcd(a, b)
