from threading import Thread, Lock
from time import sleep


count = 0
lock = Lock()


def counter(by):
    global count

    local_count = count
    local_count += by
    sleep(0.2)

    count = local_count
    print(f'Count {count}')


worker1 = Thread(target=counter, args=(10, ))
worker2 = Thread(target=counter, args=(20, ))

worker1.start()
worker2.start()

worker1.join()
worker2.join()

print(count)