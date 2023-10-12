from threading import Thread
from time import sleep


WORK = True


def handler(name: str, time_to_sleep: int):
    while WORK:
        print(f"Thread {name} is working. Going to sleep for {time_to_sleep}")
        sleep(time_to_sleep)


worker1 = Thread(name="Thread1", target=handler, args=('Thread1', 2))
worker2 = Thread(name="Thread2", target=handler, args=('Thread2', 3))

worker1.start()
worker2.start()

print("Start program")
sleep(10)

print("End")

WORK = False
