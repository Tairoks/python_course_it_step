"""
Для предыдущей задачи создайте точку входа в программу, чтобы ее можно было запускать из консоли. Позаботьтесь,
чтобы программа могла принимать на вход аргументы из консоли. Для этого воспользуйтесь модулем `sys`
"""
import sys
from currency import majcurrencies


if __name__ == '__main__':
    print(majcurrencies.translator(int(sys.argv[1]), sys.argv[2].upper()))