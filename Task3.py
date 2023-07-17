"""
В первый год в пруду живет 120 лягушек.
Каждый год из пруда вылавливают 50 лягушек, а оставшиеся размножаются и их становится в два раза больше.
Так количество лягушек в год k может быть описано формулой:
F_k = 2(F_k-1 - 50)
"""


def get_number_of_frogs(year: int, first_year=120) -> int:
    if year == 1:
        return first_year
    return get_number_of_frogs(year - 1, 2 * (first_year - 50))


n = int(input())
print(get_number_of_frogs(n))
