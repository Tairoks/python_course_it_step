"""
Написать класс MyIterator, который будет выводить треугольник из "*" при вызове методов next()
"""



class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.num = 0
        self.astr = ""

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.limit:
            self.astr += "*"
            return self.astr
        raise StopIteration("End")


my_iter = MyIterator(5)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
