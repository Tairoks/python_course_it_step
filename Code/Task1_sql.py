"""
Создайте таблицу «материалы» из следующих полей: идентификатор, вес, высота
и доп. характеристики материала. Поле доп. характеристики материала должно хранить в себе
массив,  каждый  элемент  которого  является  кортежем  из  двух  значений,  первое  –  название
характеристики, а второе – её значение. [('density', 1), ('type', 'wood')]
"""
import sqlite3


def adapt_tuple(data):
    return str(data)


def convert_tuple(data):
    return list(data)


sqlite3.register_adapter(list, adapt_tuple)
sqlite3.register_converter('list', convert_tuple)

conn = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()

cur.execute('CREATE TABLE "materials"('
            'id INTEGER PRIMARY KEY,'
            'weight REAL,'
            'height REAL,'
            'extra list)')
cur.execute('INSERT INTO materials VALUES(?, ?, ?, ?)', (1, 2.5, 3.5, [('density', 1.5), ('type', 'wood')]))

cur.execute('SELECT * FROM materials')
record = cur.fetchall()
print(record)
conn.close()
