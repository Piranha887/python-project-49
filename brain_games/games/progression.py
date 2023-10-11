from random import randint

from brain_games.constants import PROGRESSION_LENGTH
from brain_games.utils import generate_random_number


def generate_question_progression():
    """Функция для генерации арифметической прогрессии"""

    # Генерируем первый элемент прогрессии
    first_num = generate_random_number()

    # Генерируем разницу (шаг) между элементами прогрессии
    diff = generate_random_number()

    # Генерируем индекс пропущенного элемента в прогрессии
    missed_num_ind = randint(0, PROGRESSION_LENGTH - 1)

    # Создаем арифметическую прогрессию с пропущенным элементом
    progression = ' '.join([
        '..' if i == missed_num_ind else str(first_num + i * diff)
        for i in range(PROGRESSION_LENGTH)
    ])

    question = progression
    correct_answer = str(first_num + missed_num_ind * diff)
    return question, correct_answer
