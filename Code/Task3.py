"""
Используя ProcessPoolExecutor, напишите программу проверки числа на простоту. Для примера использовать большие числа:
112272535095293, 112582705942171.
Число является простым если делится на себя и на 1. Результатом работы программы должно являтся логическое выпажение -
True или False.

def if_prime(x):
    if x <= 1:
        return 0
    elif x <= 3:
        return x
    elif x % 2 == 0 or x % 3 == 0:
        return 0
    i = 5
    while i**2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0
        i += 6
    return x

"""
from multiprocessing import Pool
import time

def if_prime(x):
    if x <= 1:
        return 0
    elif x <= 3:
        return x
    elif x % 2 == 0 or x % 3 == 0:
        return 0
    i = 5
    while i**2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0
        i += 6
    return x


res = 0

# start = time.time()
# for i in range(1000000):
#     res += if_prime(i)
# end = time.time()
# print(end - start)


if __name__ == '__main__':
    start = time.time()
    with Pool(8) as executor:
        res = sum(executor.map(if_prime, list(range(1000000))))
    end = time.time()
    print(end - start)
