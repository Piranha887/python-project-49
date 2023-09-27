import prompt


def start_game(game):
    min_num_rand = 0
    max_num_rand = 100
    count = 3

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.RULES)

    for _ in range(count):
        question, correct_answer = \
            game.generate_number(min_num_rand, max_num_rand)

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

# Пример использования:
# start_game(some_game)
