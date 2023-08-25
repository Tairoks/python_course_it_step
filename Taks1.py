"""
Напишите программу по следующему описанию:

1) Есть класс `Person`, конструктор которого принимает три параметра (не учитывая `self`) – имя, фамилию и квалификацию
специалиста. Квалификация имеет значение заданное по умолчанию, равное единице.

2) У класса `Person` есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике.

3) Класс `Person` содержит деструктор, который выводит на экран фразу "До свидания, мистер …" (вместо троеточия должны
выводиться имя и фамилия объекта).

4) В основной ветке программы создайте три объекта класса `Person`. Посмотрите информацию о сотрудниках и увольте самое
слабое звено.

4) В конце программы добавьте функцию `input()`, чтобы скрипт не завершился сам, пока не будет нажат Enter. Иначе вы
сразу увидите как удаляются все объекты при завершении работы программы.
"""


class Person:

    def __init__(self, name, surname, qua=1):
        self.name = name
        self.surname = surname
        self.qua = qua

    def info_person(self):
        print(f'name: {self.name}')
        print(f'surname: {self.surname}')
        print(f'qualification: {self.qua}')

    def __del__(self):
        if self.qua == 1:
            print(f'Goodbye mister {self.name}{self.surname}')


person1 = Person('Tom', 'Cruise', 6)

person1.info_person()
i = input()
person2 = Person('Johnny', 'Depp', 4)

person2.info_person()
i = input()
person3 = Person('Tobey', 'Maguire')

person3.info_person()
i = input()