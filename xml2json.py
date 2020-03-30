#! usr/bin/env python
#Script per convertire gli XML per i grafici della rete OMIRL in json per highchart
# si lancia in maniera diversa a seconda dei dati che si intendono recuperare
# - python3 json2geojson.py Pluvio
# - python3 json2geojson.py Termo
# - python3 json2geojson.py Idro
# - python3 json2geojson.py Press
# Gter copyleft 2020
# author: Roberto Marzocchi
###############################################################################
import os,sys

from sys import argv
#from os.path import exists

import simplejson as json 

import urllib.request, json
import xml.etree.ElementTree as et

import datetime

# assegno l'input dello script in maniera semplice
script, input1, input2 = argv

try:
    indirizzo = "https://omirl.regione.liguria.it/Omirl/rest/charts/{0}/{1}".format(input2,input1)
except:
    print("Occorre specificare un input corretto es. python3 xml2json.py Idro MONTG")
    sys.exit(2)

#leggo il file xml
print(indirizzo)
file = urllib.request.urlopen(indirizzo)
data = file.read()
file.close()

#print(data)

root = et.fromstring(data)

print(len(root))
print(root[1].attrib)
#serie = root.attrib
print(root[5][1][0].text)


out_file="{}_{}.json".format(input2, input1)
print(out_file)
output = open(os.path.join(sys.path[0],out_file), 'w')

output.write('[')
comma_count0=0
for dataSeries in root[5]:
    if dataSeries.tag =='data':
        if comma_count0 > 0:
            output.write(',')
        comma_count0 += 1
        output.write('[')
        comma_count1=0
        for item in dataSeries:
            if comma_count1>0:
                output.write(',')
            output.write(item.text)
            comma_count1+=1
        output.write(']')
output.write(']')

exit()

print("DATI LETTI CORRETTAMENTE")
#exit()
#script, in_file, out_file = argv


print(len(data))

#refDate = 2020-02-27T09:15:00


data_reference=datetime.datetime.utcnow() - datetime.timedelta(minutes=60)

print(data_reference)

#date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')

# Filter python objects with list comprehensions
data_updated = [x for x in data if datetime.datetime.strptime(x['refDate'],'%Y-%m-%dT%H:%M:%S') > data_reference ]


print(len(data_updated))

#exit()

geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["lon"], d["lat"]],
            },
        "properties" : d,
     } for d in data_updated]
}
#with open(os.path.join(sys.path[0], "my_file.txt"), "r") as f:

out_file="{}.json".format(input1)
print(out_file)
output = open(os.path.join(sys.path[0],out_file), 'w')
json.dump(geojson, output)
#print(geojson)



