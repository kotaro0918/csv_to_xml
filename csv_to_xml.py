import csv
import dicttoxml
with open('data.csv','r') as f:
    dreader = csv.DictReader(f)
    d_list = [row for row in dreader]
xml = dicttoxml.dicttoxml(d_list, attr_type=False, root=False)
print(xml.decode('utf-8'))