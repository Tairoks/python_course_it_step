"""
Написать рекурсивную функцию `get_fib(n: int) -> int` поиска значения n-го числа Фибоначчи
"""


def get_fib(n: int) -> int:
    if n in (1, 2):
        return 1
    return get_fib(n - 1) + get_fib(n - 2)


n = int(input())
print(get_fib(n))