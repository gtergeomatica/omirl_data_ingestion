#! usr/bin/env python
#Script per convertire i json della rete OMIRL in geojson
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
    indirizzo = "https://omirl.regione.liguria.it/Omirl/rest/charts/MONTG/{}".format(input2,input1)
except:
    print("Occorre specificare un input corretto es. python3 json2geojson.py Idro MONTG")xm
    sys.exit(2)

#leggo il file xml
file = urllib.request.urlopen(indirizzo)
data = file.read()
file.close()

root = et.fromstring(data

serie = root.attrib['dataSeries']

print(serie)

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



