import random

from brain_games.constants import MIN_NUM_RAND, MAX_NUM_RAND


def generate_random_number() -> int:
    return random.randint(MIN_NUM_RAND, MAX_NUM_RAND)
