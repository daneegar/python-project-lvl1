#!/usr/bin/env python3
"""Don't know what I have to write here."""
# file <brain_games.py>

from .cli import welcome_user


def greet():
    """Greeting of new user function."""
    print('Welcome to the Brain Games!')


def main():
    """Run script."""
    greet()
    welcome_user()

if __name__ == '__main__':
    main()
