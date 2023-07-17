"""
Напишите рекурсивную функцию `get_list(n: int, lst=[]) -> list`, чтобы сгенерировать и вернуть список от 1 до N.
Аргументом функции является только N.
"""


def get_list(n: int, lst=[]) -> list:
    if n > 0:
        get_list(n - 1)
        lst.append(n)
    return lst


n = int(input())
print(get_list(n))