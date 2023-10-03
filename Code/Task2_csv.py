"""
Реализовать  возможности  перезаписи  файла из Задания 1, добавления новых строк в существующий файл,
построчного чтения из файла и конвертацию всего содержимого в формат JSON
"""
import csv
import json


with open('output_task1.csv', 'r') as file:
    data = {"names": []}
    reader = csv.DictReader(file)
    for row in reader:
        data["names"].append(row)

    print(data)

with open('names.json', 'w') as json_file:
    json.dump(data, json_file)
