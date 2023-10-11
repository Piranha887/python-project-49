import random

from brain_games.utils import generate_random_number


def calculate_expression(number1, operator, number2) -> str:
    """Вычисление результата выражения."""
    if operator == '+':  # Используем строковые символы вместо констант
        return str(number1 + number2)
    elif operator == '-':
        return str(number1 - number2)
    elif operator == '*':
        return str(number1 * number2)
    else:
        raise ValueError("Неподдерживаемый оператор")


def choice_operator() -> str:
    operators = ['+', '-', '*']
    return random.choice(operators)


def generate_question_calc():
    """Генерация случайного выражения и правильного ответа."""
    number1, number2 = generate_random_number()
    operator = choice_operator()
    expression = f'{number1} {operator} {number2}'
    correct_answer = calculate_expression(number1, operator, number2)
    return expression, correct_answer
