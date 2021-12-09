#!/usr/bin/env python3

# file <brain_even.py>

from random import randrange
from .cli import welcome_user

import prompt


def welcome():
    print('Answer "yes" if the number is even, otherwise answer "no".')

def successfulBye(name):
    print('Congratulations,', name+'!')

def unsuccessfulBye(name):
    print('See you next time,', name+'!')

def printQuestion(number):
    print('Question: ', number)


def getAnswer():
    return prompt.string("Your answer: ").strip()


def answerInterprener(answer):
    if answer == 'Yes' or answer == 'y':
        return True
    else:
        return False


def answerChecker(answer, number):
    return answer == (number % 2 == 0)


def printResult(result):
    if result:
        print("Correct!")
    else:
        print("Uncorrect!")


def game(numbers, name):
    resultIsSuccessful = True

    for number in numbers:
        printQuestion(number)
        answer = answerInterprener(getAnswer())
        guess = answerChecker(answer, number)
        printResult(guess)
        if guess == False:
            resultIsSuccessful = guess

    if resultIsSuccessful:
        successfulBye(name)
    else:
        unsuccessfulBye(name)

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
