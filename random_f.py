import secrets
import random
import prng

def python_rand(i: int) -> bool:
    return random.choice([False, True])

random.seed(1)

GENERATOR = prng.get_prng(secrets.randbelow(2 ** 64), 100)

def custom_rand(i: int) -> bool:
    return GENERATOR.update()[0]