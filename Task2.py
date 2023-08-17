"""
Реализовать функцию поиска наиболее распространенных слов в файле.
Используйте файл `files_HW/lorem_ipsum.txt`. ПРИМЕЧАНИЕ: Помните о точках, запятых, заглавных буквах и т.д.
"""

from collections import Counter

sorted_words = []

with open('Code/files_HW/lorem_ipsum.txt', 'r') as file_1:
    for words in file_1.readlines():
        words_ = words.strip().split(' ')
        if [''] == words_:
            continue
        else:
            for i in words_:
                if ',' in i:
                    sorted_words.append(i.strip(',').lower())
                if '.' in i:
                    sorted_words.append(i.strip('.').lower())
                else:
                    sorted_words.append(i.lower())

print(Counter(sorted_words).most_common()[:3])
