from multiprocessing import Pipe, Process
from multiprocessing.dummy.connection import Connection


def parent_data(parent: Connection) -> None:
    parent.send([1, 2, 3, 4])
    parent.close()


# можно добавить обработку полученных данных в дочернем процессе
def child_data(child: Connection) -> None:
    lst = child.recv()
    res = list(map(lambda x: x ** 3, lst))
    child.send(res)
    child.close()


if __name__ == '__main__':
    parent, child = Pipe()

    proc1 = Process(target=parent_data, args=(parent, ))
    proc2 = Process(target=child_data, args=(child, ))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

    # print(child.recv())
    print(parent.recv())
