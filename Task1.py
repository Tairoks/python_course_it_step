"""
Откройте файл `files_HW/unsorted_names.txt` в папке данных. Сортируйте имена и
записывайте их в новый файл `sorted_names.txt` Каждое имя должно начинаться с новой строки,
как в следующем примере:
```python
Adele
Adrienne
...
Willodean
Xavier
```
"""

names = []

with open('Code/files_HW/unsorted_names.txt', 'r') as file_1:
    for i in file_1.readlines():
        names.append(i)

names.sort()

with open('Code/files_HW/sorted_names.txt', 'w') as file_2:
    file_2.writelines(names)
