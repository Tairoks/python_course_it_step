"""
Пусть есть 3 функции которые вызываются в следующей последовательности `bzz -> bar -> foo`. В функции `foo()` возникают
исключения `ZeroDivisionError` и `IndexError`.
Перехватите исключение `ZeroDivisionError` в функции `bar`, а `IndexError` в функции `bzz`.
"""


def foo(a):
    b = [1, 2, 3]
    x = 5 / a
    y = b[a]
    print(x, a, y)


def bar(a):
    foo(a)


def bzz(a):
    bar(a)


try:
    print(bzz(15))
except IndexError:
    print("Invalid number")


try:
    print(bar(0))
except ZeroDivisionError:
    print("You can't divide by zero")


# print(foo(15))
