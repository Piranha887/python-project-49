import prompt

from brain_games.constants import COUNT_OF_ROUNDS


def start_game(rule, generate_question_and_answer):
    name = prompt.string("Welcome to the Brain Games!"
                         "May I have your name? ")
    print(f"Hello, {name}!"
          f"{rule}")

    for _ in range(COUNT_OF_ROUNDS):
        question, correct_answer = generate_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is the wrong answer."
                f" Correct answer was '{correct_answer}'."
                f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
