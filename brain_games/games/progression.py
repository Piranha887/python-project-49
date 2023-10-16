from random import randint

from brain_games.constants import PROGRESSION_LENGTH, RULE_PROGRESSION
from brain_games.engine import start_game
from brain_games.utils import generate_random_number


def run_script_progression():
    return start_game(RULE_PROGRESSION, generate_question_progression())


def generate_question_progression():
    """Function to generate an arithmetic progression"""

    # Generate the first element of the progression
    first_num = generate_random_number()

    # Generate the difference (step) between progression elements
    diff = generate_random_number()

    # Generate the index of the missing element in the progression
    missed_num_ind = randint(0, PROGRESSION_LENGTH - 1)

    # Create an arithmetic progression with the missing element
    progression = ' '.join([
        '..' if i == missed_num_ind else str(first_num + i * diff)
        for i in range(PROGRESSION_LENGTH)
    ])

    question = progression
    correct_answer = str(first_num + missed_num_ind * diff)
    return question, correct_answer
