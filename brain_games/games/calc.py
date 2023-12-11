import random

from brain_games.constants import RULE_CALC, OPERATORS
from brain_games.engine import start_game
from brain_games.utils import generate_random_number


def calculate_math_expression(number1, operator, number2) -> int:
    """Calculate the result of an expression."""
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    else:
        raise ValueError("Unsupported operator")


def get_math_expression_and_result():
    """Generate a random expression and the correct answer."""
    number1, number2 = generate_random_number(), generate_random_number()
    operator = random.choice(OPERATORS)
    result = calculate_math_expression(number1, operator, number2)
    expression = f'{number1} {operator} {number2}'

    return expression, str(result)


def start_calc_game():
    return start_game(RULE_CALC, get_math_expression_and_result)
