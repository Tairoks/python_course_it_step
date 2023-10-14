"""
Написать программу генератор случайных кубов. Используя модуль Queue (multiprocessing) создать программу генерирующую
список чисел возведенных в 3-ю степень. Списки должны помещаться в очередь и извлекаться из нее.
Пример вывода
[343.0, 1000.0, 216.0]
[64.0, 729.0, 216.0]
[125.0, 8.0, 64.0]
"""

from multiprocessing import Queue
import random


def generate_cubes(num: int):
    for i in range(1, num):
        yield [pow(random.randint(1, 1000), 3) for _ in range(i)]


if __name__ == '__main__':
    queue_ = Queue()
    gen = generate_cubes(4)
    queue_.put(next(gen))
    queue_.put(next(gen))
    queue_.put(next(gen))

    while not queue_.empty():
        print(queue_.get())
