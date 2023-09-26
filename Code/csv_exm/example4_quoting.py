import csv

# Используем словари для записи в csv_exm файл DictWriter

quoting = csv.QUOTE_ALL

with open('data/output.csv', 'w') as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["name", "surname", "age"],
        quoting=quoting
    )
    writer.writeheader()
    writer.writerow({
        "name": "Nick",
        "surname": "Smith",
        "age": 25
    })

