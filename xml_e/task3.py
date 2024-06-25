import xml.etree.ElementTree as ET
import xml
# class ElementRecipe:


if __name__ == "__main__":
    tree = ET.parse('Task3.xml')

    root = tree.getroot()

    parent_map = {c: p for p in tree.iter() for c in p}
    namespace = {'ota': root.tag[root.tag.find('{')+1:root.tag.find('}')]}
    element: xml.etree.ElementTree.Element
    for element in root.iter():
        tag = element.tag[element.tag.find('}')+1:]
        if tag in ('ContactInfo', 'MultimediaDescription', 'ImageFormat') or 'rds' in tag:
            childs = element.findall(f'.//ota:*', namespace)
            root_el = parent_map.get(element)
            # TODO fix err below
            # root_el.remove(element)
            # root_el.extend(childs)
        if element.attrib.get("Caption"):
            attr = element.attrib.get("Caption")
            element.extend(ET.Element(
                "Caption",
                text=element.attrib.get("Caption")
            ))
            element.attrib.pop("Caption")

    tree.write("test.xml", encoding='utf-8', xml_declaration=True, )
