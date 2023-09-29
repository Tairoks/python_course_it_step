import sqlite3


def to_uppercase(raw_string: str) -> str:
    return raw_string.upper()


conn = sqlite3.connect(":memory:")
conn.create_function('upper1', 1, to_uppercase)

cur = conn.cursor()

cur.execute('CREATE TABLE "names"(first_name CHAR(20))')
cur.execute('INSERT INTO names VALUES ("Ivan"), ("Nikolai"), ("Peter")')
cur.execute('SELECT upper1(first_name) FROM names WHERE first_name="Ivan"')
rec = cur.fetchall()
print(rec)





