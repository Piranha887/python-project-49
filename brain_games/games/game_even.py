from brain_games.utils.generate_number import generate_random_number


def is_even(num):
    """Проверяет чётность числа"""
    return 'yes' if num % 2 == 0 else 'no'


def generate_question_even():
    """Генерирует случайное число и верный ответ"""
    number = generate_random_number()
    correct_answer = is_even(number)
    return number, correct_answer
