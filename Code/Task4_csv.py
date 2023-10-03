"""
Напишите свой iterable-класс и связанный с ним iterator-класс, который принимает строку и возвращает список из ее символов.
Метод __next__() должен считывать элементы не используя range() или цикл

>>> 'text'
['t']
['t', 'e']
['t', 'e', 'x']
"""


class MyIterable:
    def __init__(self, text):
        self.text = text
        self.list_of_chars = []
        self.count = 0

    def get_element(self, n):
        return self.text[n]

    def __next__(self):
        if len(self.list_of_chars) <= len(self.text):
            elem = self.get_element(self.count)
            self.list_of_chars.append(elem)
        else:
            raise StopIteration

        self.count += 1
        return self.list_of_chars


class MyIterator:
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        return MyIterable(self.text)


my_iter = iter(MyIterator('some text'))

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))