#!/usr/bin/env python3
from brain_games.games.game_prime import generate_question_prime
from brain_games.engine import start_game
from brain_games.constants import RULE_PRIME


def main():
    start_game(RULE_PRIME, generate_question_prime)


if __name__ == '__main__':
    main()
