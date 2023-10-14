"""
Используя Pool выполнить серию запрсов на различные страницы Википедии и определить статус страницы:
если возвращаемый статус код == 200, то статус == страница существует, если код 400, то - страница не существует.
В списке должно быть не менее 5 url-ов. измерьте время выполнения кода без ThreadPoolExecutor и с ним
"""

from multiprocessing import Pool
import requests


URLS = [
    'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
    'https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%98%D0%B7%D0%B1%D1%80%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5_%D1%81%D1%82%D0%B0%D1%82%D1%8C%D0%B8',
    'https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%9F%D0%BE%D0%BC%D0%BE%D1%89%D1%8C_%D0%BD%D0%B0%D1%87%D0%B8%D0%BD%D0%B0%D1%8E%D1%89%D0%B8%D0%BC',
    'https://docs.python.org/3/library/exceptions.html#exception-hierarchy',
    'https://www.urldecoder.org/'
]

statuses = []


def make_request(url):
    resp = requests.get(url)
    if resp.ok:
        return statuses.append(resp.status_code)
    return resp.status_code


if __name__ == '__main__':
    with Pool(len(URLS)) as executor:
        print(executor.map(make_request, URLS))
        # print(result)
