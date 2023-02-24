import xml.dom.minidom
import dicttoxml

xml_string = "<item><address><addressLocality>千代田区</addressLocality><addressRegion>東京都</addressRegion><postalCode>100-0002</postalCode><streetAddress>皇居外苑</streetAddress></address><familyName>山田</familyName><givenName>太郎</givenName><telephone>03-1234-5678</telephone><birthDate>2001-1-1</birthDate></item>"
dom = xml.dom.minidom.parseString(xml_string) # xml.dom.minidom.parse(file_name) ファイルをパースするとき
print(dom.toprettyxml())