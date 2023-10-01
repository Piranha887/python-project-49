import random


def generate_progression(min_num, max_num):
    """Функция для генерации арифметической прогрессии"""
    step_min = 1
    step_max = 10
    element_count_min = 5
    element_count_max = 10

    # Генерация начального числа прогрессии
    number_start = random.randint(min_num, max_num)
    # Генерация шага прогрессии
    step = random.randint(step_min, step_max)
    # Генерация количества элементов прогрессии
    elements = random.randint(element_count_min, element_count_max)

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
