from multiprocessing import Process, Pool
# from concurrent.futures import
import time

result = 0


# функция принимает одно число и преобразует его. Здесь можно запустить например поиск факториала или чисел фибоначи


# def foo(num):
#     if num == 1 or num == 0:
#         return 1
#     else:
#         return num * foo(num - 1)


def foo(num):
    return pow(num, 3)


# start = time.time()
#
# for i in range(10000000):
#     result += foo(i)
#
# print(time.time() - start)

if __name__ == '__main__':
    start = time.time()
    with Pool(4) as executor:
        executor.map(foo,  range(10000000))
    print(time.time() - start)
#
# proc1 = Process(target=foo, args=(10000000,))
# proc2 = Process(target=foo, args=(10000000,))
#
# start = time.time()
# proc1.start()
# proc2.start()
#
# proc1.join()
# proc2.join()
#
# print(time.time()-start)
