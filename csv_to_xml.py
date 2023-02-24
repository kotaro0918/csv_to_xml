import csv
import re 
import dicttoxml
import sys
import xml.dom.minidom
with open('data.csv','r') as f:
    dreader = csv.DictReader(f)
    d_list = [row for row in dreader]
def divide_addess(ad1):
  for i in range(len(d_list)):
    ad1=d_list[i].pop("住所")
    matches = re.match(r'(...??[都道府県])((?:旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|蒲郡|四日市|姫路|大和郡山|廿日市|下松|岩国|田川|大村)市|.+?郡(?:玉村|大町|.+?)[町村]|.+?市.+?区|.+?[市区町村])(.+)' , ad1)
    d_list[i]["address"]={"addressLocality":matches[2],"addressRegion":matches[1],"postalCode":d_list[i].pop("郵便番号"),"streetAddress":matches[3]}
    (d_list[i]["familyName"],d_list[i]["givenName"],d_list[i]["telephone"])=(d_list[i].pop("姓"),d_list[i].pop("名"),d_list[i].pop("電話番号"))
    d_list[i]["birthDate"]=d_list[i].pop("生年月日").replace('/','-')
if __name__ == '__main__':
  divide_addess(d_list)
s = dicttoxml.dicttoxml(d_list, attr_type=False, root=False)
print(s.decode('utf-8'))