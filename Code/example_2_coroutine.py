import functools

# def is_divider(num: int) -> None:
#     print('Enter the coroutine')
#     while True:
#         value = yield
#         if num % value == 0:
#             print(value)


# cor = is_divider(100)
# cor.send(None)
# cor.send(18)
# cor.send(11)
# cor.send(50)
# cor.close()


def coroutine(func):
    @functools.wraps(wrapped=func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res.send(None)
        return res

    return wrapper


@coroutine
def is_divider(num: int) -> None:
    print('Enter the coroutine')
    while True:
        value = yield
        if num % value == 0:
            print(value)


cor = is_divider(100)
cor.send(11)
cor.send(50)
cor.close()
