"""
Используя модуль sqlite3 создайте таблицу с марками автомобилей. В таблице должны быть
следующие поля: идентификатор, название, год выпуска, доп. информация. Создайте запрос отсортировав записи по возрастанию
значения года выпуска. Lambda
"""
import sqlite3


with sqlite3.connect(":memory:") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE cars (id, brand, year, extra)")
    cursor.execute("INSERT INTO cars VALUES(?, ?, ?, ?)", (1, "Saab", "2018", "{'engine': 1.8, 'num_of_doors': 4}"))
    cursor.execute("INSERT INTO cars VALUES(?, ?, ?, ?)", (2, "Nissan", "2008", "{'engine': 1.6, 'num_of_doors': 4}"))
    cursor.execute("INSERT INTO cars VALUES(?, ?, ?, ?)", (3, "Ford", "2011", "{'engine': 1.6, 'num_of_doors': 5}"))

    cursor.execute("SELECT * FROM cars")
    rec = cursor.fetchall()
    rec.sort(key=lambda x: x[2])
    print(rec)
