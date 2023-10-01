import random


def is_prime(number):
    """Проверка, является ли число простым"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question(min_num, max_num):
    number = random.randint(min_num, max_num)
    correct_answer = "yes" if is_prime(number) else "no"
    return number, correct_answer
