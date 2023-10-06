from brain_games.utils.generate_number import generate_random_number


def is_prime(number):
    """Проверка, является ли число простым"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question_prime():
    number = generate_random_number()
    correct_answer = "yes" if is_prime(number) else "no"
    return number, correct_answer
