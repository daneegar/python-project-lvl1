#!/usr/bin/env python3

# file <brain_even.py>

from random import randrange
from typing import List

from brain_games.scripts.cli import welcome_user
from brain_games.scripts.cli import get_answer
from brain_games.scripts.cli import successful_bye
from brain_games.scripts.cli import unsuccessful_bye
from brain_games.scripts.cli import print_result
from brain_games.scripts.cli import print_question

import prompt

def print_description():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def answer_interprener(answer: str):
    if answer == 'Yes' or answer == 'y':
        return True
    else:
        return False


def answer_checker(answer: int, number: int):
    return answer == (number % 2 == 0)


def game(numbers: List[int], name: str):
    result_is_successful = True

    for number in numbers:
        print_question(number)
        answer = answer_interprener(get_answer())
        guess = answer_checker(answer, number)
        print_result(guess)
        if not guess:
            result_is_successful = guess

    if result_is_successful:
        successful_bye(name)
    else:
        unsuccessful_bye(name)


def main():
    """Run brain even game"""
    name = welcome_user()
    print_description()
    numbers = []
    for _ in range(3):
        numbers.append(randrange(10))
    game(numbers, name)


if __name__ == '__main__':
    main()
