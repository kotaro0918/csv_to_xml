import xml.dom.minidom

xml_string = "<note><to>a</to><from>b</from><heading>no title</heading><body>test</body></note>"
dom = xml.dom.minidom.parseString(xml_string) # xml.dom.minidom.parse(file_name) ファイルをパースするとき
print(dom.toprettyxml())
