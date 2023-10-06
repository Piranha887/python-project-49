#!/usr/bin/env python3
from brain_games.games.game_calc import generate_question_calc
from brain_games.engine import start_game
from brain_games.constants import RULE_CALC


def main():
    start_game(RULE_CALC, generate_question_calc)


if __name__ == '__main__':
    main()
