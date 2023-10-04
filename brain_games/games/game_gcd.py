import random

RULES = 'Find the greatest common divisor of given numbers.'


def is_gcd(number1, number2):
    """Используем алгоритм Евклида для нахождения наибольшего общего делителя"""
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return str(number1)


def generate_question(min_num, max_num):
    """Генерация случайных чисел, вопроса и правильного ответа"""
    number1 = random.randint(min_num, max_num)
    number2 = random.randint(min_num, max_num)
    question = f'{number1} {number2}'
    correct_answer = is_gcd(number1, number2)
    return question, correct_answer
