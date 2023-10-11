import math
from brain_games.utils import generate_random_number


def find_gcd(number1, number2) -> str:
    """Находит наибольший общий делитель двух чисел"""
    return str(math.gcd(number1, number2))


def generate_question_gcd():
    """Генерация случайных чисел, вопроса и правильного ответа"""
    number1, number2 = generate_random_number()
    question = f'{number1} {number2}'
    correct_answer = find_gcd(number1, number2)
    return question, correct_answer
