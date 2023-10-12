from threading import Thread, Lock
from time import sleep

count = 0
lock = Lock()


def counter(num):
    global count, lock

    with lock:
        local_count = count
        local_count += num
        sleep(0.5)
        count = local_count

        print(f'Counter: {count}')


worker1 = Thread(target=counter, args=(10, ))
worker2 = Thread(target=counter, args=(20, ))

worker1.start()
worker2.start()

worker1.join()
worker2.join()

print(count)
