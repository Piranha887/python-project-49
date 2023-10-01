import random

# Правила игры
RULES = 'What is the result of the expression?'


def calculate_expression(number1, operator, number2):
    """Вычисление результата выражения."""
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2


def generate_question(min_num, max_num):
    """Генерация случайного выражения и правильного ответа."""
    operators = ['+', '-', '*']
    number1 = random.randint(min_num, max_num)
    number2 = random.randint(min_num, max_num)
    operator = random.choice(operators)
    expression = f'{number1} {operator} {number2}'
    correct_answer = str(calculate_expression(number1, operator, number2))
    return expression, correct_answer
