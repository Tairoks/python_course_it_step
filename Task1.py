"""
Реализуйте класс-итератор EvenRange, который принимает начало и конец интервала в качестве аргументов `__init__` и дает
только чётные числа во время итерации.
Если пользователь пытается итерироваться после того, как он дал все возможные числа, должно быть напечатано `Out of
numbers!` Примечание: Не используйте функцию `range()`
"""


class EvenRange:
    def __init__(self, st, en):
        self.st = st
        self.en = en

    def __next__(self):
        if self.st % 2 != 0:
            self.st += 1
            return self.st
        elif self.st % 2 == 0 and self.st < self.en - 1:
            self.st += 2
            res = self.st
            return res
        else:
            raise StopIteration('Out of numbers!')

    def __iter__(self):
        return self


cls = EvenRange(1, 10)
print(next(cls))
print(next(cls))
print(next(cls))
print(next(cls))
print(next(cls))
print(next(cls))
