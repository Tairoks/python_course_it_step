"""
Написать класс, который описывает пользователя (class User), сделать ему приватный атрибут age, который передается в
конструктор, публичный атрибут name, который так же передается в конструктор.
1 Написать getter и setter для атрибута age.
2 Добавить в setter проверку на валидный возраст (не отрицательное, целое число)
"""


class User:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def setter(self, num):
        if '-' in str(num):
            print("Number can't be negative")
        if '.' in str(num):
            print("Number can't be negative")
        else:
            self.__age = num

    def getter(self):
        print(self.__age)


U = User('Johan', 45)

U.setter(-72)
U.getter()
