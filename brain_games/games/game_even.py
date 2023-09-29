from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    """Проверяет чётность числа"""
    return 'yes' if num % 2 == 0 else 'no'


def generate_question(min_num, max_num):
    """Генерирует случайное число и верный ответ"""
    number = randint(min_num, max_num)
    correct_answer = is_even(number)
    return number, correct_answer
