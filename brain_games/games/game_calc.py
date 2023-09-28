import random

RULES = 'What is the result of the expression?'


def calculate_expression(expression):
    number1, operator, number2 = expression.split()
    number1 = int(number1)
    number2 = int(number2)

    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2


def generation(min_num_rand, max_num_rand):
    operators = ['+', '-', '*']
    number1 = random.randint(min_num_rand, max_num_rand)
    number2 = random.randint(min_num_rand, max_num_rand)
    operator = random.choice(operators)
    expression = f'{number1} {operator} {number2}'
    correct_answer = str(calculate_expression(expression))
    return expression, correct_answer
