import xml.etree.ElementTree as ET
import re


def node_values(filename, path):
    path_parts = path.split('/')
    doc = ET.iterparse(filename, events=("start", "end"))
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass
                    
country_government = []
countries = node_values('mondial-3.0.xml', 'country')
for country in countries:
    name = (country.attrib['name']).strip()
    government = (country.attrib['government']).strip()
    if government not in country_government and len(name.split())==2:
        country_government.append(government)
print(country_government)