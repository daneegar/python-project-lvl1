from random import randrange

from brain_games.scripts.cli import welcome_user
from brain_games.scripts.cli import unsuccessful_bye
from brain_games.scripts.cli import successful_bye
from brain_games.scripts.cli import get_answer
from brain_games.scripts.cli import greet
from brain_games.scripts.cli import print_question
from brain_games.scripts.cli import print_result


class OperationInterface:

    def description(self) -> str:
        """Printing description"""
        pass

    def operation(self, lhs: int, rhs: int) -> int:
        """Making counting"""
        pass


class Add(OperationInterface):

    def description(self) -> str:
        return "+"

    def operation(self, lhs: int, rhs: int) -> int:
        return lhs + rhs


class Mut(OperationInterface):

    def description(self) -> str:
        return "*"

    def operation(self, lhs: int, rhs: int) -> int:
        return lhs * rhs


class Substraction(OperationInterface):

    def description(self):
        return "-"

    def operation(self, lhs: int, rhs: int) -> int:
        return lhs - rhs


class Expression:

    def evaluate(self) -> int:
        return self.operation.operation(self.lhs, self.rhs)

    def description(self) -> str:
        return str(self.lhs) + self.operation.description() + str(self.rhs)

    def __init__(self, operation: OperationInterface, lhs: int, rhs: int):
        self.operation = operation
        self.lhs = lhs
        self.rhs = rhs


def random_operations() -> {OperationInterface}:
    return {Mut(), Substraction(), Add()}


def description() -> str:
    return "What is the result of the expression?"


def interpret(answer: str) -> int:
    return int(answer)


def main():
    """Run brain even game"""
    greet()
    name = welcome_user()
    game_is_winned: bool = True
    print(description())
    for operation in random_operations():
        lhs = randrange(10)
        rhs = randrange(10)
        exp = Expression(operation, rhs, lhs)
        print_question(exp.description())
        answer = get_answer()
        while True:
            try:
                guess = interpret(answer)
                break
            except ValueError:
                print("Oops! It doesn't look like a number")
                answer = get_answer()

        is_correct = guess == exp.evaluate()
        if not is_correct:
            game_is_winned = False

        print_result(is_correct)

    if game_is_winned:
        successful_bye(name)
    else:
        unsuccessful_bye(name)


if __name__ == '__main__':
    main()
