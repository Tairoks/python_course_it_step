import multiprocessing as mp
from multiprocessing import cpu_count, Queue
import time


fruits = ['apple', 'orange', 'lemon', 'banana']
count = 0

if __name__ == '__main__':
    q = Queue()
    print('Insert into queue')
    for fruit in fruits:
        q.put(f'{count} - {fruit}')
        count += 1

    print('\nGetting objects from q')
    while not q.empty():
        print(q.get())



# print(cpu_count())
#
# result = []
#
#
# def foo(num):
#     for i in range(num):
#         result.append(pow(i, 3))
#     print(sum(result))
#
#
# if __name__ == '__main__':
#
#     proc1 = mp.Process(target=foo, args=(10000000,))
#     proc2 = mp.Process(target=foo, args=(10000000,))
#
#     start = time.time()
#     proc1.start()
#     proc2.start()
#
#     proc1.join()
#     proc2.join()
#
#     print(time.time()-start)




