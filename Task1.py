"""
Реализовать программу-напоминание с таймером. Программа должна спрашивать:
"О чём вам напомнить?" и "Через сколько минут (секунд)?" По прошествии указанного времени нужно вывести заданный текст.
Дополните функционал программы работой с потоком.
Пример работы программы:
```
python
О чём вам напомнить?
Попить воды
Через сколько секунд?
20
Пока поток работает, мы можем сделать что-нибудь ещё
Попить воды
```
"""


from threading import Thread
from time import sleep, asctime


def reminder(s: str, t: int):
    sleep(t)
    print(f'***{s}***. \nTime: {asctime()[11:16]}')


def start():
    threads = Thread(target=reminder, args=(text, num))
    threads.start()


if __name__ == '__main__':
    while True:
        text = input('Enter reminder text: ')
        num = int(input('Enter reminder timer: '))
        if text == 'end':
            break
        else:
            start()
            print('start')
