"""
Реализовать пользовательский словарь (в виде класса), который будет запоминать 10 последних измененных ключей.
Используя метод `get_history` вернуть эти ключи. Подумайте какой подход здесь лучше использовать
"""


class HistoryChanges:
    dc = {}
    lst = []

    def set_value(self, k, v):
        if len(self.lst) == 3:
            del self.lst[0]
            self.lst.append(k)
            self.dc[k] = v
        else:
            self.lst.append(k)
            self.dc[k] = v

    def get_history(self):
        return self.lst


add = HistoryChanges()
add.st_changes('first_key', 1)
add.st_changes('first_key1', 2)
add.st_changes('first_key2', 3)
add.st_changes('first_key3', 4)
add.st_changes('first_key4', 5)
add.st_changes('first_key1', 6)
print(add.get_history())
# print(add.dc)
# print(add.lst)
