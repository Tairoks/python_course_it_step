"""
Используя ElementTree выполнить парсинг xml файла следующего содержания

<data>
    <items>
        <item name="item1">10</item>
        <item name="item2">20</item>
        <item name="item3">30</item>
        <item name="item4">40</item>
    </items>
</data>

На выходе программы должны получить список {'attrib': 'value'}. Сохраните полученный список в json формате

"""
import json
from xml.etree import ElementTree as ET

attrs = []

root = ET.parse('data/data.xml')
items = root.findall('./items/item')

for item in items:
    attrs.append({item.attrib.get("name"): item.text})

print(attrs)

with open('data/items.json', "w") as file:
    json.dump(attrs, file)
