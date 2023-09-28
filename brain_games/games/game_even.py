from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_parity(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generation(min_num_rand, max_num_rand):
    number = randint(min_num_rand, max_num_rand)
    correct_answer = check_parity(number)
    return number, correct_answer
