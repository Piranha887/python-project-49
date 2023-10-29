from brain_games.constants import RULE_EVEN
from brain_games.engine import start_game
from brain_games.utils import generate_random_number


def start_even_game():
    return start_game(RULE_EVEN, generate_question_even)


def is_even(num) -> bool:
    """Checks whether a number is even"""
    return num % 2 == 0


def generate_question_even():
    """Generates a random number and the correct answer"""
    number = generate_random_number()
    correct_answer = 'yes' if is_even(number) else 'no'
    return number, correct_answer
