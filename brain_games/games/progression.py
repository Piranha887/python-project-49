from random import randint

from brain_games.constants import PROGRESSION_LENGTH, RULE_PROGRESSION
from brain_games.engine import start_game
from brain_games.utils import generate_random_number


def generate_arithmetic_progression(first_num, diff, missed_num_ind,
                                    progression_length):
    """Generate an arithmetic progression with a missing element"""
    progression = ['..' if i == missed_num_ind else
                   str(first_num + i * diff)
                   for i in range(progression_length)]
    return ' '.join(progression)


def get_progression_and_missed_num():
    """Generate a question and the correct answer"""
    first_num = generate_random_number()
    diff = generate_random_number()
    missed_num_ind = randint(0, PROGRESSION_LENGTH - 1)

    progression = generate_arithmetic_progression(first_num,
                                                  diff, missed_num_ind,
                                                  PROGRESSION_LENGTH)

    question = progression
    correct_answer = first_num + missed_num_ind * diff

    return question, str(correct_answer)


def start_progression_game():
    return start_game(RULE_PROGRESSION,
                      get_progression_and_missed_num)
