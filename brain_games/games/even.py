from brain_games.constants import RULE_EVEN
from brain_games.engine import start_game
from brain_games.utils import generate_random_number


def is_even(num) -> bool:
    """Checks whether a number is even"""
    return num % 2 == 0


def get_number_and_even_answer() -> tuple:
    """Generate a random number and determine if it's even,
     returning the number and the answer 'yes' or 'no'."""
    number = generate_random_number()
    correct_answer = 'yes' if is_even(number) else 'no'
    return number, correct_answer


def start_even_game():
    return start_game(RULE_EVEN, get_number_and_even_answer)
