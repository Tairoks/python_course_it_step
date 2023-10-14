"""
Написать программу-эмулятор ресторана, в котором есть официант и повар.
Официант принимает заказы и выдает, а повар готовит еду. При написании использовать возможности библиотеки asyncio

пример вывода
Новый заказ: Паста
Новый заказ: Салат Цезарь
Новый заказ: Отбивные
Салат Цезарь - готово
Паста - готово
Отбивные - готово
"""
import asyncio


async def cook(order: str):
    time_to_cook = 0
    print('Start to cook {}'.format(order))
    if order == 'pasta':
        time_to_cook = 10
    elif order == 'ceaser salad':
        time_to_cook = 5
    elif order == 'beef':
        time_to_cook = 15
    await asyncio.sleep(time_to_cook)
    print('{} - is ready!'.format(order))


async def waiter():
    order1 = asyncio.create_task(cook('pasta'), name="Pasta")
    order2 = asyncio.create_task(cook('beef'), name="Beef")
    order3 = asyncio.create_task(cook('ceaser salad'), name="Salad")

    await order1
    await order2
    await order3


asyncio.run(waiter())
