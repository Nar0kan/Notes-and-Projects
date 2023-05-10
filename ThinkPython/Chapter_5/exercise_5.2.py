from random import choice


def do_n(func, n: int) -> None:
    for i in range(n):
        func()


def print_hi() -> None:
    print(choice(['Hello', 'hi', 'Greetings!', 'yo!', 'Whats up?']))


do_n(print_hi, 5)