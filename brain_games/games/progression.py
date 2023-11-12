from random import randint

from brain_games.constants import PROGRESSION_LENGTH, RULE_PROGRESSION
from brain_games.engine import start_game
from brain_games.utils import generate_random_number


def generate_missing_element_index():
    """Generate the index of the missing element in the progression"""
    return randint(0, PROGRESSION_LENGTH - 1)


def generate_arithmetic_progression(first_num, diff, missed_num_ind):
    """Generate an arithmetic progression with a missing element"""
    progression = ['..' if i == missed_num_ind else str(first_num + i * diff)
                   for i in range(PROGRESSION_LENGTH)]
    return ' '.join(progression)


def generate_question_progression():
    """Generate a question and the correct answer"""
    first_num = generate_random_number()
    diff = generate_random_number()
    missed_num_ind = generate_missing_element_index()

    progression = generate_arithmetic_progression(first_num,
                                                  diff, missed_num_ind)

    question = progression
    correct_answer = str(first_num + missed_num_ind * diff)

    return question, correct_answer


def start_progression_game():
    return start_game(RULE_PROGRESSION, generate_question_progression)
