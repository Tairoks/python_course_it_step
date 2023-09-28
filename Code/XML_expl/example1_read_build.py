from xml.etree import ElementTree as ET
import json


#
# root = ET.parse('data/exmpl.xml')
# animals = []
# # print(root)
#
# elements = root.findall("animal")
# # print(list(map(lambda x: int(x.attrib.get("id")), elements)))
#
# animal = {}
#
# for element in elements:
#     animal["id"] = int(element.attrib.get("id"))
#     animal["type"] = element.find("type").text
#     animal["owner"] = element.find("owner").text
#
#     animals.append(animal)
#     # print(element.attrib.get("id"), "-> ", element.find("type").text, ";", element.find("owner").text)
#
# dct = {"animals": animals}
#
# print(dct)
#
# with open('data/animals.json', 'w') as file:
#     json.dump(dct, file)
#

#### WRITE XML ####

# root = ET.Element("numders")
#
# for i, n in enumerate(range(3), start=1):
#     elem = ET.SubElement(root, "number")
#     elem.attrib = dict(id=str(i))
#     elem.text = str(n * 10)

# print(ET.dump(root))

# tree = ET.ElementTree(root)
# tree.write('data/output.xml')

data = [
    {"id": 1, "name": "John", "surname": "Connor", "age": 15},
    {"id": 2, "name": "Sarah", "surname": "Connor", "age": 35},
    {"id": 3, "name": "Arnold", "surname": "T-800", "age": 55},
]


root = ET.Element("persons")


for item in data:
    elem = ET.SubElement(root, "person", attrib=dict(id=str(item["id"])))
    sub_elem1 = ET.SubElement(elem, "name", attrib=dict(lang="eng"))
    sub_elem2 = ET.SubElement(elem, "surname", attrib=dict(lang="eng"))
    sub_elem3 = ET.SubElement(elem, "age")
    sub_elem1.text = item["name"]
    sub_elem2.text = item["surname"]
    sub_elem3.text = str(item["age"])

# print(ET.dump(root))

tree = ET.ElementTree(root)
tree.write('data/output.xml')
