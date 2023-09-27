"""
Реализуйте генератор `show_letters(some_str: str)`, выводящий все символы строки на печать, но только в том случае,
если они являются буквами (остальные игнорируются).
"""


def show_letters(some_str: str):
    for let in some_str:
        if let.isdigit():
            continue
        else:
            yield let


str = 'He66ll23o7Wo48rl12d'
letters = show_letters(str)
try:
    print(next(letters))
    print(next(letters))
    print(next(letters))
    print(next(letters))
    print(next(letters))
    print(next(letters))
    print(next(letters))
    print(next(letters))
    print(next(letters))
    print(next(letters))
    print(next(letters))
    print(next(letters))
except StopIteration:
    print('Text is showing')
    