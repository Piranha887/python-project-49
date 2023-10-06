#!/usr/bin/env python3
from brain_games.constants import RULE_PROGRESSION
from brain_games.games.game_progression import generate_question_progression
from brain_games.engine import start_game


def main():
    start_game(RULE_PROGRESSION, generate_question_progression)


if __name__ == '__main__':
    main()
