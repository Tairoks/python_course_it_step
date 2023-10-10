"""
Имеется файл data.csv, (можно взять любые данные и конвертировать их в csv (см. ссылку ниже)) содержащий информацию в
csv-формате. Напишите функцию read_csv() для чтения данных из этого файла. Она должна возвращать список словарей,
интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей.
Функция read_csv() не должна принимать аргументов
"""


import csv
import os


fields = ['Name', 'Surname', "Date"]


with open('data.csv', 'a') as file:
    writer = csv.DictWriter(file, fieldnames=fields, lineterminator='\n')
    if os.stat("data.csv").st_size == 0:
        writer.writeheader()
        writer.writerow({'Name': 'Johan', 'Surname': 'Ivanov', 'Date': 1999})
        writer.writerow({'Name': 'Moki', 'Surname': 'Mokanu', 'Date': 1998})
        writer.writerow({'Name': 'Rihanna', 'Surname': 'Robyn', 'Date': 1994})
        writer.writerow({'Name': 'John', 'Surname': 'Conor', 'Date': 1981})


def read_csv():
    read_dicts = []
    with open('data.csv', 'r') as file1:
        reader = csv.DictReader(file1, fieldnames=fields)
        for i in reader:
            read_dicts.append(i)
    print(read_dicts)


read_csv()
