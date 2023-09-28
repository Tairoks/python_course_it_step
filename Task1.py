"""
Создайте  функцию,  которая  будет  создавать  CSV  файл  на  основе  данных,  введенных
пользователем  через  консоль.  Файл  должен  содержать следующие  колонки:  имена,  фамилии,
даты  рождений  и  город  проживания.
"""
import csv


def make_file(data: list) -> None:
    fields = ["name", "surname", "date", "city"]
    with open("output_task1.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=fields, lineterminator='\n')

        writer.writeheader()
        writer.writerow({
            "name": data[0],
            "surname": data[1],
            "date": data[2],
            "city": data[3]
        })


def write_road(data: list):
    with open("output_task1.csv", "a") as file:
        writer = csv.writer(file, lineterminator='\n')

        writer.writerow(data)


def main():
    list_of_data = input().split()
    make_file(list_of_data)
    while True:
        words = input().split()
        if 'end' in words:
            break
        else:
            write_road(words)


if __name__ == '__main__':
    main()
    print()

#TODO: Преобразовать файл таким образом, чтобы можно было добавлять записи к уже существующим
#TODO: Выполнить цикл из нескольких вводов до ввода команды "end"
#TODO: Подумать, как убрать пустую строку в файле между записями
