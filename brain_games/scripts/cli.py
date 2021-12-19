#!/usr/bin/env python3
"""Don't know what I have to write here."""
import prompt


def greet():
    """Greeting of new user function."""
    print('Welcome to the Brain Games!')


def welcome_user():
    """Invite naming user."""
    name = prompt.string('May I have your name? ').strip()
    sentence = ''.join(['Hello', ' ', name, '!'])
    print('Hello, {}!'.format(name))
    return name


def print_question(arg):
    """Printing common question"""
    print('Question: {}'.format(arg))


def successful_bye(name: str):
    print('Congratulations, {}!'.format(name))


def unsuccessful_bye(name: str):
    print('See you next time,', name + '!')


def get_answer():
    return prompt.string("Your answer: ").strip()


def print_result(result: bool):
    if result:
        print("Correct!")
    else:
        print("Incorrect!")
