import random

from brain_games.constants import OPERATOR_PLUS, OPERATOR_MINUS, \
    OPERATOR_MULTIPLY
from brain_games.utils.generate_number import generate_random_number


def calculate_expression(number1, operator, number2):
    """Вычисление результата выражения."""
    if operator == OPERATOR_PLUS:
        return number1 + number2
    elif operator == OPERATOR_MINUS:
        return number1 - number2
    elif operator == OPERATOR_MULTIPLY:
        return number1 * number2


def generate_question_calc():
    """Генерация случайного выражения и правильного ответа."""
    operators = [OPERATOR_PLUS, OPERATOR_MINUS, OPERATOR_MULTIPLY]
    number1, number2 = generate_random_number()
    operator = random.choice(operators)
    expression = f'{number1} {operator} {number2}'
    correct_answer = str(calculate_expression(number1, operator, number2))
    return expression, correct_answer
