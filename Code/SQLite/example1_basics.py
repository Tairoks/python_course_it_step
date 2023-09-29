import sqlite3

try:

    connection = sqlite3.connect('my_db.db', timeout=5)
    # connection.execute('CREATE TABLE "users" ('
    #                    'id INTEGER PRIMARY KEY,'
    #                    'first_name VARCHAR(20),'
    #                    'last_name VARCHAR(20),'
    #                    'birthdate VARCHAR(20))')
except sqlite3.OperationalError as e:
    print(e)
# connection.execute('INSERT INTO "users"(id, first_name, last_name, birthdate)'
#                    'VALUES (1, "Ivan", "Ivanov", "1989-10-25"), (2, "Peter", "Petrov", "1986-11-20")')
# connection.commit()
else:
    users = connection.execute('SELECT * FROM "users"')
    print(users.fetchall()[0])
finally:
    connection.close()

