"""
Создайте  функцию,  которая  будет  создавать  CSV  файл  на  основе  данных,  введенных
пользователем  через  консоль.  Файл  должен  содержать следующие  колонки:  имена,  фамилии,
даты  рождений  и  город  проживания.
"""
import csv
import os


def make_file(writer: csv.DictWriter, data: list) -> None:
    writer.writerow({
        "name": data[0],
        "surname": data[1],
        "date": data[2],
        "city": data[3]
    })


def main():
    fields = ["name", "surname", "date", "city"]
    with open("output_task1.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=fields, lineterminator='\n')
        if os.stat("output_task1.csv").st_size == 0:
            writer.writeheader()
        else:
            while True:
                data = input()
                if data == 'end':
                    break
                else:
                    make_file(writer, data.split())


if __name__ == '__main__':
    main()
