"""
Реализуйте декоратор `@call_once`, который запускает функцию или метод один раз и кэширует (сохраняет) результат.
Все последовательные вызовы этой функции должны возвращать кэшированный результат независимо от аргументa.
"""


def call_once(func):
    cache = None

    def wrapper(*args):
        nonlocal cache
        if not cache:
            cache = func(*args)
            return cache
        else:
            return cache

    return wrapper


@call_once
def func1(a, b):
    return a + b


print(func1(2, 6))
print(func1(9, 4))
