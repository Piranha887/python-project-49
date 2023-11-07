import random

from brain_games.constants import RULE_CALC, OPERATORS
from brain_games.engine import start_game
from brain_games.utils import generate_random_number


def calculate_expression(number1, operator, number2):
    """Calculate the result of an expression."""
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    else:
        raise ValueError("Unsupported operator")

    return result


def generate_question_calc():
    """Generate a random expression and the correct answer."""
    number1, number2 = generate_random_number(), generate_random_number()
    operator = random.choice(OPERATORS)
    correct_answer = calculate_expression(number1, operator, number2)
    expression = f'{number1} {operator} {number2}'

    return expression, correct_answer


def start_calc_game():
    return start_game(RULE_CALC, generate_question_calc)
