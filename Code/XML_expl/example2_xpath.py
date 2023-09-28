from xml.etree import ElementTree as ET

root = ET.parse('data/output.xml')

names = root.findall('./person/name')
print(list(map(lambda x: x.attrib, names)))
