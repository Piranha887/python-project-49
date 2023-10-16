import prompt

from brain_games.constants import COUNT_OF_ROUNDS


def start_game(rule, generate_question):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')

    print(rule)

    for _ in range(COUNT_OF_ROUNDS):
        question, correct_answer = generate_question()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is the wrong answer. Correct answer was '{correct_answer}'\nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
