import lxml
from lxml import etree

xml_as_string = '''
<ahmed>
  <type> ahmed2</type>
  <version>1.2</version>
</ahmed>
'''

xml_obj = etree.fromstring(xml_as_string)

print type(xml_obj)
print xml_obj

data = xml_obj.find('.//version')
print data
print data.text
print type(data)
print type(data.text)
print data.


