from os.path import exists


def send_file(file_path: str) -> None:
    if not exists(file_path):
        raise FileExistsError("error")

    print(f'Send the file: {file_path}')


send_file(r'C:\Users\python\PycharmProjects\python_course_it_step\Code\example2_raise.py')


a = 10
b = 5


def division(x, y):
    if y == 0:
        raise ZeroDivisionError("You can't divide to zero")
    return x / y


print(division(a, b))
