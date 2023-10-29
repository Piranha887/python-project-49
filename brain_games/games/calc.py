import random

from brain_games.constants import RULE_CALC
from brain_games.engine import start_game
from brain_games.utils import generate_random_number


def start_calc_game():
    return start_game(RULE_CALC, generate_question_calc)


def calculate_expression_and_generate_operator(number1, operators, number2) -> list[str]:
    """Calculate the result of an expression."""
    operator = random.choice(operators)
    if operator == '+':  # Using string symbols instead of constants
        return ['+', str(number1 + number2)]
    elif operator == '-':
        return ['-', str(number1 - number2)]
    elif operator == '*':
        return ['*', str(number1 * number2)]
    else:
        raise ValueError("Unsupported operator")


def generate_question_calc():
    """Generate a random expression and the correct answer."""
    number1, number2 = generate_random_number()
    operators = ['+', '-', '*']
    correct_answer = calculate_expression_and_generate_operator(number1, operators, number2)
    operator = correct_answer[0]
    expression = f'{number1} {operator} {number2}'

    return expression, correct_answer[1]
