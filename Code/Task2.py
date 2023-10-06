"""
Выполнить отправку 10 запросов на https://www.python.org/ в виде обычной функции и разделив на потоки.
Результаты запросов response.status_code сохранить в виде списка. Для отправки запросов испрпользовать библиотеку requests
"""
import requests
import time

from threading import Thread


websites = ['https://www.python.org/'] * 10
result = []


def make_request(url):
    resp = requests.get(url)
    result.append(resp.status_code)


start = time.time()
# for website in websites:
#     make_request(website)

print(len(result))
print(time.time() - start) # 7.53386116027832


threads = [Thread(target=make_request, args=(website,)) for website in websites]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(len(result))
print(time.time() - start)  # 7.53386116027832
                            # 1.2786953449249268
