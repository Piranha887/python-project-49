from brain_games.utils import generate_random_number


def is_even(num) -> bool:
    """Проверяет чётность числа"""
    return num % 2 == 0


def generate_question_even():
    """Генерирует случайное число и верный ответ"""
    number = generate_random_number()
    correct_answer = 'yes' if is_even(number) else 'no'
    return number, correct_answer
