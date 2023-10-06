from threading import Thread
from threading import current_thread


class MyThread(Thread):
    def run(self):
        print(f"Work with thread {self.name}")


# MyThread(name='Thread1').start()
# MyThread(name='Thread2').start()


def foo():
    pass


worker = Thread(name='worker1', target=foo)
print(worker.name)
worker.name = 'worker_2'
print(worker.name)
print(worker.is_alive())
print(worker.isDaemon())


# current = current_thread()
#
# try:
#     current.start()
# except RuntimeError as error:
#     print(error)
