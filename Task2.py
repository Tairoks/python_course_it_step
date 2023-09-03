"""
Создайте иерархию для класса `Bird` из 3 классов:

2.1 Класс `Bird` с атрибутом name и методами `fly` и `walk`.

2.2 Класс `FlyingBird` с атрибутами `name` и `ration` (должен иметь значение по-умолчанию) и такими же методами

2.3 Класс `NonflyingBird` с такими же характеристиками, но без метода `fly`

2.4 Класс `SuperBird`, который может делать все: ходить, летать, плавать и есть Обратите внимание на метод `eat`
"""


class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f'{self.name} flying'

    def walk(self):
        return f'{self.name} walking'


class FlyingBird(Bird):
    def __init__(self, name, ration):
        Bird.__init__(self, name)
        self.ration = ration

    def walk(self):
        return f'{self.name} walking'

    def fly(self):
        return f'{self.name} flying'


class NonflyingBird(FlyingBird):
    def __init__(self, name, ration):
        super().__init__(name, ration)

    def fly(self):
        if self.__class__ == NonflyingBird:
            pass


class SuperBird(FlyingBird, Bird):
    def __init__(self, name, ration):
        super().__init__(name, ration)

    def fly(self):
        return f'{self.name} flying'

    def eat(self):
        return f'{self.name} eating {self.ration}'


bird = Bird('Bird')
print(bird.fly())
print(bird.walk())
fl_bird = FlyingBird('crow', 'nut')
print(fl_bird.fly())
print(fl_bird.walk())
n_fly = NonflyingBird('penguin', 'fish')
print(n_fly.walk())
print(n_fly.fly())
s_bird = SuperBird('eagle', 'mause')
print(s_bird.fly())
print(s_bird.walk())
print(s_bird.eat())
