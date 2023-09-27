"""
Реализуйте генератор, который будет бесконечно генерировать нечётные числа.
"""


def inf_gen(num):
    if num % 2 != 0:
        while True:
            yield num
            num += 2
    if num % 2 == 0:
        num += 1
        while True:
            yield num
            num += 2


gen = inf_gen(6)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
