"""
Создайте простые словари и сконвертируйте их в JSON. Сохраните JSON в файл и попробуйте загрузить данные из файла
"""


import json

dct_1 = {"Axe": "top", "Bane": "top", "Arc Warden": "mid", "Ancient Apparition": "bot", "Phantom Assassin": "bot"}
dct_2 = {"Marci": "top", "Slardar": "top", "Storm Spirit": "mid", "Naga Siren": "bot", "Skywrath Mage": "bot"}
dct_3 = {"Witch Doctor": "top", "Tidehunter": "top", "Queen of Pain": "mid", "Nature's Prophet": "bot", "Lion": "bot"}
dct_4 = {"Undying": "top", "Timbersaw": "top", "Invoker": "mid", "Faceless Void": "bot", "Keeper of the Light": "bot"}

dct = [dct_1, dct_2, dct_3, dct_4]

with open("Dota_drafts.json", "w") as file1:
    dc_ = {"Drafts": dct}
    json.dump(dc_, file1)

with open("Dota_drafts.json", "r") as file2:
    dct_load = json.load(file2)

print(dct_load)
