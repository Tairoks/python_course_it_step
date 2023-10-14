import asyncio
from asyncio import sleep


# def func1(num):
#     return num ** 2
#
#
# def func2(num):
#     return num ** 3
#
#
# def main():
#     print(func1(10))
#     print(func2(5))
#
#
# main()


async def func1(num):
    await sleep(0.5)
    return num ** 2


async def func2(num):
    await sleep(0.5)
    return num ** 3


async def main():
    task1 = asyncio.create_task(func1(10), name="Cor1")
    task2 = asyncio.create_task(func2(5), name="Cor2")

    tasks = await asyncio.gather(task1, task2)
    print(sum(tasks))


asyncio.run(main())
