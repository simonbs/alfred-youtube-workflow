##
# By @simonbs
# http://simonbs.dk/
##

from xml.etree import ElementTree as ET

def list_to_xml(the_list):
  xml_items = ET.Element("items")
  for item in the_list:
    xml_item = ET.SubElement(xml_items, "item")
    for key in item.keys():
      if key is "uid" or key is "arg":
        xml_item.set(key, item[key])
      else:
        child = ET.SubElement(xml_item, key)
        child.text = item[key]
  print ET.tostring(xml_items)