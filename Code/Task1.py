"""
Реализовать класс Account с методами deposit и withdraw. В каждом методе должны присутствовать
механизмы блокировки потока lock. Также реализовать класс пользователь (наследуется от Thread) и переопределить
в нем метод run. На вход классу подаются 2 атрибута - имя пользователья и операция,
которую он совершает (deposit или withdraw). Задача  блокировать возможность выполннения операции во время ее использования
другим пользователем.
"""
from threading import Lock, Thread
from time import sleep


class Account:
    money = 10
    lock = Lock()

    def deposit(self, s=10):
        with self.lock:
            print(self.money, 'money')
            sleep(3)
            self.money += s
            print(self.money, 'money')
            print('make deposit')

    def withdraw(self, s=10):
        with self.lock:
            print(self.money, 'money')
            sleep(2)
            if self.money >= s:
                self.money -= s
                print('make withdraw')
            else:
                print('Not enough money')


class User(Thread):
    def __init__(self, name, operation):
        super().__init__(name=name)
        self.name = name
        self.operation = operation

    def run(self):
        print(f'{self.name} try to make {self.operation}')
        acc = Account()
        func = getattr(acc, self.operation)
        func()
        print(f'{self.name} made {self.operation}')


user1 = User('Alex', 'deposit')
user2 = User('Max', 'withdraw')

user1.start()
user2.start()

user1.join()
user2.join()
