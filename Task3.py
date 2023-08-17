"""
Файл `files_HW/students.csv` хранит информацию о студентах в формате CSV: имена студентов, возраст и среднюю отметку.

1. Реализуйте функцию, которая получает путь к файлу и возвращает имена лучших учеников
```
python
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))
#>>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
```

2. Реализуйте функцию, которая получает путь к файлу с информацией srudents и записывает информацию о студенте в новый
файл csv в порядке убывания возраста. Результат:
```
python
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
```
"""

import csv


def get_top_performers(file_path, number_of_top_students=5):
    list_of_students = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        # создает словарь из всех студентов и их средних оценок
        for i in reader:
            if i[0] == 'student name':
                continue
            else:
                list_of_students[i[0]] = i[2]
    list_of_bests = {}
    # создает список из лучших оценок учеников в указанном количестве
    avg = sorted([float(i) for i in list_of_students.values()], reverse=True)[:number_of_top_students]
    for j in avg:
        for i in list_of_students:
            if str(j) == list_of_students[i]:
                list_of_bests[i] = j
    print(list_of_bests)


get_top_performers('Code/files_HW/students.csv')
