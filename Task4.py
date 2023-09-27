"""
Реализуйте генератор, который будет генерировать числа Фибоначчи.
"""


def num_of_fibonachi():
    fib1 = fib2 = 1
    while True:
        fib1, fib2 = fib2, fib1 +fib2
        yield fib1


fib = num_of_fibonachi()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
