"""
Написать функцию, которая возвращает среднее геометрическое для чисел a и b (не использовать модуль `math`). Выполните
обработку исключений при помощи `try-except`
"""


def average(a, b):
    return (a * b) ** 0.5


try:
    print(average(2, 12.5))
except NameError:
  print("The entered variables do not exist")
except (SyntaxError, TypeError):
    print("Incorrect data entry")
