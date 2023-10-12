"""
сравнение выполнения вычислений в разных потоках и в одном основном потоке
GIL
"""
from threading import Thread
import time


def counter():
    for i in range(1000000):
        i += 1


start = time.time()
worker1 = Thread(target=counter)
worker1.start()
worker1.join()
worker2 = Thread(target=counter)
worker2.start()
worker2.join()

# counter()
# counter()

print(time.time() - start)
# 0.07900071144104004
# 0.07599759101867676