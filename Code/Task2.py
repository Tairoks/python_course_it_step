"""
написать программу, которая отправляет 10 запросов на API и возвращает данные о сортах пива.
Выполните парсинг json файла и запишите новый файл, содержащий следующие данные: id, сорт пива, содержание алкоголя
Используйте библиотеки asyncio и aiohttp. URL = 'https://random-data-api.com/api/v2/beers'
"""
import asyncio
import aiohttp
import json


URL = 'https://random-data-api.com/api/v2/beers'


async def make_request(url):
    async with aiohttp.ClientSession() as session:
        return await session.get(url)


async def launch():
    beers = []
    responses = await asyncio.gather(*map(make_request, [URL] * 10))
    data = [await resp.json() for resp in responses]
    # print(data)
    for item in data:
        beers.append(await parse_json(item))

    print(beers)

    with open('beers.json', 'w') as file:
        json.dump(beers, file)


async def parse_json(data: dict) -> dict:
    beer = dict(
        id=data.get('id'),
        brand=data.get('brand'),
        alcohol=data.get('alcohol')
    )
    return beer


asyncio.run(launch())
