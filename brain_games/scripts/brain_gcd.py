#!/usr/bin/env python3
from brain_games.games.game_gcd import generate_question_gcd
from brain_games.engine import start_game
from brain_games.constants import RULE_GCD


def main():
    start_game(RULE_GCD, generate_question_gcd)

    if __name__ == '__main__':
        main()
