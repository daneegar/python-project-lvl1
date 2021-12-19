#!/usr/bin/env python3
"""Don't know what I have to write here."""
import prompt


def welcome_user():
    """Invite to name user."""
    name = prompt.string('May I have your name? ').strip()
    sentence = ''.join(['Hello', ' ', name, '!'])
    print(sentence)
    return name


def successful_bye(name: str):
    print('Congratulations,', name + '!')


def unsuccessful_bye(name: str):
    print('See you next time,', name + '!')


def get_answer():
    return prompt.string("Your answer: ").strip()
