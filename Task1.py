"""
Написать декоратор `@do_twice`, который будет вызывать любую функцию дважды.
"""


def go_twice(func):

    def wrapper(*args):
        func(*args)
        func(*args)

    return wrapper


@go_twice
def func1(a, b):
    print(a + b)


func1(2, 6)
