import math

from brain_games.constants import RULE_GCD
from brain_games.engine import start_game
from brain_games.utils import generate_random_number


def get_gcd(number1, number2) -> int:
    """Calculate the greatest common divisor of two numbers."""
    return math.gcd(number1, number2)


def get_num_pair_and_gcd() -> tuple:
    """Generates random numbers, a question, and the correct answer"""
    number1, number2 = generate_random_number(), generate_random_number()
    num_pair = f'{number1} {number2}'
    correct_answer = get_gcd(number1, number2)
    return num_pair, str(correct_answer)


def start_gcd_game():
    return start_game(RULE_GCD, get_num_pair_and_gcd)
