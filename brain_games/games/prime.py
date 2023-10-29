from brain_games.constants import RULE_PRIME
from brain_games.engine import start_game
from brain_games.utils import generate_random_number


def start_prime_game():
    return start_game(RULE_PRIME, generate_question_prime)


def is_prime(number) -> bool:
    """Check if a number is prime"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question_prime():
    number = generate_random_number()
    correct_answer = "yes" if is_prime(number) else "no"
    return number, correct_answer
