import random

from brain_games.constants import STEP_MIN, STEP_MAX, \
    ELEMENT_COUNT_MIN, ELEMENT_COUNT_MAX
from brain_games.utils.generate_number import generate_random_number


def generate_question_progression():
    """Функция для генерации арифметической прогрессии"""

    # Генерация начального числа прогрессии
    number_start = generate_random_number()
    # Генерация шага прогрессии
    step = random.randint(STEP_MIN, STEP_MAX)
    # Генерация количества элементов прогрессии
    elements = random.randint(ELEMENT_COUNT_MIN, ELEMENT_COUNT_MAX)

    element_list = []
    for _ in range(elements):
        number_start += step
        element_list.append(str(number_start))
    # Генерация индекса пропущенного элемента
    missing_index = random.randint(0, elements - 1)

    correct_answer = str(element_list[missing_index])
    # Замена пропущенного элемента на '..'
    element_list[missing_index] = '..'
    # Формирование вопроса
    question = ' '.join(element_list)
    return question, correct_answer
