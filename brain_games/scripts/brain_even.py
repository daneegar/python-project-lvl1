#!/usr/bin/env python3

# file <brain_even.py>

from random import randrange
from typing import List

from brain_games.scripts.cli import welcome_user

import prompt


def welcome():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def successful_bye(name):
    print('Congratulations,', name + '!')


def unsuccessful_bye(name):
    print('See you next time,', name + '!')


def print_question(number):
    print('Question: ', number)


def get_answer():
    return prompt.string("Your answer: ").strip()


def answer_interprener(answer):
    if answer == 'Yes' or answer == 'y':
        return True
    else:
        return False


def answer_checker(answer, number):
    return answer == (number % 2 == 0)


def print_result(result):
    if result:
        print("Correct!")
    else:
        print("Uncorrect!")


def game(numbers: List[int], name: str):
    resultIsSuccessful = True

    for number in numbers:
        print_question(number)
        answer = answer_interprener(get_answer())
        guess = answer_checker(answer, number)
        print_result(guess)
        if not guess:
            result_is_successful = guess

    if resultIsSuccessful:
        successful_bye(name)
    else:
        unsuccessful_bye(name)


def main():
    """Run brain even game"""
    name = welcome_user()
    welcome()
    numbers = []
    for _ in range(3):
        numbers.append(randrange(10))
    game(numbers, name)


if __name__ == '__main__':
    main()
