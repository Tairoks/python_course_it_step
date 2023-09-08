"""
Реализовать класс `Material`, который представляет однородный материал
(вещество). Атрибуты класса name и density являются приватными. Метод `get_material()`
должен возвращать строку, разделенную «;»
```python
Output:
steel;7850.0
```


Создать класс `Subject`, который представляет объект, состоящий из однородного материала.
Атрибуты класса: `name`, `material`, `volume` (объем) должны быть приватными. Реализовать
методы класса `get_mass()` (приватный), который возвращает массу объекта
(=density*volume) и `get_subject()`, который возвращает строку со всеми атрибутами (плюс
масса (mass)), разделенную «;»

```python
Output:
wire;steel;7850.0;0.03;235.5
```

Определите класс `Runner` (интерфейс для управления внутренними классами), где:
1. Создайте объект, представляющий стальную проволоку (steel_wire) объемом 0,03 м
2. Вывести содержимое объекта на консоль, используя метод get_subject().
3. Обновите материал проволоки на медь (copper) (плотность = 8500.0 и выведите его массу)

```python
Output:
The wire mass is 255.0 kg
```

В этой задаче нет отношения наследования между сущностями (материал и предмет).
Наследование возникает, когда одна сущность является частным случаем другой. Например,
металл (или другое твердое вещество) и материал. Другими словами, металл является
материалом. Предмет состоит из материала, а не является материалом. Поэтому предмет не может
быть наследником от материала.
Обратите внимание, что у конкретного материала плотность является константой, что нужно
отразить при создании класса. Например, у стали плотность 7850.0 и никакая другая.
"""


class Material:
    def __init__(self, name, density):
        self.__name = name
        self.__density = density

    def __str__(self):
        return f'{self.__name}; {self.__density}'

    def get_list(self):
        lst = [self.__name, self.__density]
        return lst


class Subject:
    def __init__(self, name, material, volume):
        self.__density = None
        self.__name = name
        self.__volume = volume
        self.__material = material

    def get_mass(self, density):
        self.__density = density
        return self.__volume * self.__density[1]

    def __str__(self):
        return f'{self.__name};{self.__material};{self.__volume};{self.get_mass(self.__density)}'


class Runner:
    def get_subject(self, lst):
        return f'{lst[0]} mass is {lst[-1]}'


clas1 = Material('steel', 7850.0)
print(clas1)


clas2 = Subject('wire', clas1, 0.03)
clas2.get_mass(clas1.get_list())
print(clas2)
clas2_ = str(clas2).split(';')


run = Runner()
print(run.get_subject(clas2_))
