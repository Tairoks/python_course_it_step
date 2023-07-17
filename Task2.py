"""
Напишите функцию `search_value(i: int) -> bool`, которая рекурсивно ищет в сложном объекте значение. Сложный объект -
это будет список списков списков. Например, `[1, 2, [3, 4, [5, [6, []]]]]`.
Функция должна рекурсивно заходить внутрь вложенных массивов, а если это другой тип данных игнорировать его. Возвращать
логическое значение
"""


def search_value(i: int, l: list):
    for x, val in enumerate(l):
        if isinstance(val, list):
            if len(val) == 0:
                continue
            elif search_value(i, val) == False:
                continue
            else:
                return search_value(i, val)
        elif isinstance(val, int):
            if val == i:
                return val, True
    return False


i = int(input())
l = [1, 2, [3, 4, [5, [6, []]]]]
print(search_value(i, l))