import prompt

from brain_games.cli import welcome_user
from brain_games.constants import COUNT_ATTEMPTS


def start_game(rule, generate_question):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')

    print(rule)

    for _ in range(COUNT_ATTEMPTS):
        question, correct_answer = generate_question()

        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;"
                  f"(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
