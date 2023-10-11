#!/usr/bin/env python3
from brain_games.constants import RULE_CALC, RULE_EVEN, RULE_GCD, RULE_PROGRESSION, RULE_PRIME
from brain_games.engine import start_game
from brain_games.games.calc import generate_question_calc
from brain_games.games.even import generate_question_even
from brain_games.games.gcd import generate_question_gcd
from brain_games.games.prime import generate_question_prime
from brain_games.games.progression import generate_question_progression


def run_script(rule):
    if rule == RULE_CALC:
        start_game(RULE_CALC, generate_question_calc)
    if rule == RULE_EVEN:
        start_game(RULE_EVEN, generate_question_even)
    if rule == RULE_GCD:
        start_game(RULE_GCD, generate_question_gcd)
    if rule == RULE_PROGRESSION:
        start_game(RULE_PROGRESSION, generate_question_progression)
    if rule == RULE_PRIME:
        start_game(RULE_PRIME, generate_question_prime)
