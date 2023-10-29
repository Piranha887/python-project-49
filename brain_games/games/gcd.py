import math

from brain_games.constants import RULE_GCD
from brain_games.engine import start_game
from brain_games.utils import generate_random_number


def start_gcd_game():
    return start_game(RULE_GCD, generate_question_gcd)


def find_gcd(number1, number2) -> str:
    """Finds the greatest common divisor of two numbers"""
    return str(math.gcd(number1, number2))


def generate_question_gcd():
    """Generates random numbers, a question, and the correct answer"""
    number1, number2 = generate_random_number()
    question = f'{number1} {number2}'
    correct_answer = find_gcd(number1, number2)
    return question, correct_answer
