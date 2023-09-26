import csv

# создание собственного диалекта для записи файла в csv_exm через класс


class MyDialect(csv.Dialect):
    delimiter = "|"
    quotechar = "*"
    quoting = csv.QUOTE_NONNUMERIC
    lineterminator = "\n"


csv.register_dialect("test", MyDialect)

with open("data/output.csv", "w") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["name", "surname", "age"],
        dialect=MyDialect
    )

    writer.writeheader()
    writer.writerow({"name": "Nick", "surname": "Smith", "age": 25})
    writer.writerow({"name": "Alex", "surname": "Doe", "age": 30})


