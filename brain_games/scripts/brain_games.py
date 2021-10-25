# file <brain_games.py>
#!/usr/bin/env python3
from . import cli
from .cli import welcome_user

def greet():
    print('Welcome to the Brain Games!')

def main():
    greet()
    welcome_user()

if __name__ == '__main__':
    main()
