import lxml
from lxml import etree
xml_str = '<interfaces><interface>Eth1/1</interface></interfaces>'
xml_data = etree.fromstring(xml_str)

intf = xml_data.find('.//interface')
print intf.text

print type(intf)
print dir(intf)

print (intf)
