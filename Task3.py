"""
Создайте XML файл с вложенными элементами и воспользуйтесь языком поиска XPATH. Попробуйте осуществить поиск содержимого
по созданному документу XML, усложняя свои запросы и добавляя новые элементы, если потребуется.
"""


from xml.etree import ElementTree as ET


root = ET.Element('data.xml')

elem1 = ET.SubElement(root, 'person', attrib={'id': '1'})
elem2 = ET.SubElement(root, 'person', attrib={'id': '2'})
elem1_name = ET.SubElement(elem1, 'name', )
elem1_name.text = 'Jones'
elem1_surname = ET.SubElement(elem1, 'surname')
elem1_surname.text = 'Heel'
elem2_name = ET.SubElement(elem2, 'name')
elem2_name.text = 'Emet'
elem2_surname = ET.SubElement(elem2, 'surname')
elem2_surname.text = 'Brown'

tree = ET.ElementTree(root)
tree.write('data.xml')


root = ET.parse('data.xml')

names1 = root.findall('./person/name')
names2 = root.findall('./person/surname')

names = list(map(lambda x: x.text, names1))
surnames = list(map(lambda x: x.text, names2))


lst_of_pars = [{'name': names[0], 'surname': surnames[0]}, {'name': names[1], 'surname': surnames[1]}]
print(lst_of_pars)

