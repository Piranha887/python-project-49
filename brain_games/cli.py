import prompt


def welcome_user() -> str:
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    welcome_message = f'Hello, {name}!'
    print(welcome_message)
    return name
