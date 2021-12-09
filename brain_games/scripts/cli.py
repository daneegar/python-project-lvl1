#!/usr/bin/env python3
"""Don't know what I have to write here."""
import prompt


def welcome_user():
	"""Invite to name user."""
	name = prompt.string('May I have your name? ').strip()
	sentence = ''.join(['Hello', ' ', name, '!'])
	print(sentence)
	return name
