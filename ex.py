import csv
import re 
import dicttoxml
import xml.dom.minidom
with open('data.csv','r') as f:
    dreader = csv.DictReader(f)
    d_list = [row for row in dreader]
def divide_addess(ad1):
  for i in range(len(d_list)):
    ad1=d_list[i].pop("住所")
    matches = re.match(r'(...??[都道府県])((?:旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|蒲郡|四日市|姫路|大和郡山|廿日市|下松|岩国|田川|大村)市|.+?郡(?:玉村|大町|.+?)[町村]|.+?市.+?区|.+?[市区町村])(.+)' , ad1)
    (d_list[i]["adressLocality"],d_list[i]["addressRegion"],d_list[i]["postalCode"])=(matches[2],matches[1],matches[3])
if __name__ == '__main__':
  divide_addess(d_list)

for i in range(len(d_list)):

