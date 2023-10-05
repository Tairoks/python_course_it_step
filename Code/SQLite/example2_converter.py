import json
import sqlite3


def adapt_json(data):
    return json.dumps(data)


def convert_json(raw_data):
    return json.loads(raw_data)


sqlite3.register_adapter(dict, adapt_json)
sqlite3.register_converter('json', convert_json)

conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cursor = conn.cursor()

cursor.execute('CREATE TABLE test(attr json)')
cursor.execute('INSERT INTO test(attr) VALUES (?)', ({'test': 1, 'aaa': 2},))
cursor.execute('INSERT INTO test(attr) VALUES (?)', ({'test': 2, 'aaa': 4},))

cursor.execute('SELECT * FROM test')
record = cursor.fetchone()
print(type(record[0]))
