from threading import Thread
from time import sleep


def blocking():
    print('Blocking...')
    sleep(2)
    print('Unblock')


worker1 = Thread(target=blocking)
worker2 = Thread(target=blocking)
worker1.start()
worker2.start()

worker1.join()
worker2.join()

print('Start')
sleep(5)
print('End')

