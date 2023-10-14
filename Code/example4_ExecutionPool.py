import concurrent.futures
import urllib.request

URLS = ['https://vk.com',
        'https://russian.rt.com/',
        'https://www.youtube.com/',
        'https://mail.ru/',
        'https://www.google.ru/',
        'https://timeweb.com/ru/',
        'https://yandex.ru/']

# скачивает одну страницу
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# используем оператор `with` для обеспечения быстрой очистки потоков
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # загружаем и отмечаем каждый будущий результат своим URL-адресом
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print(f'{url} сгенерировано исключение: {exc}')
        else:
            print(f'{url} скачано {len(data)} bytes')