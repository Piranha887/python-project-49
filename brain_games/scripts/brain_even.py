from brain_games.games.game_even import generate_question_even
from brain_games.engine import start_game
from brain_games.constants import RULE_EVEN


def main():
    start_game(RULE_EVEN, generate_question_even)


if __name__ == "__main__":
    main()
