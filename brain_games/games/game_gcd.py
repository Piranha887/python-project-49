from brain_games.utils.generate_number import generate_random_number


def is_gcd(number1, number2):
    """Используем алгоритм Евклида для нахождения наиб. общего делителя"""
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return str(number1)


def generate_question_gcd():
    """Генерация случайных чисел, вопроса и правильного ответа"""
    number1 = generate_random_number()
    number2 = generate_random_number()
    question = f'{number1} {number2}'
    correct_answer = is_gcd(number1, number2)
    return question, correct_answer
