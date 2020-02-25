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

# assegno l'input dello script in maniera semplice
script, input1 = argv

try:
    indirizzo = "https://omirl.regione.liguria.it/Omirl/rest/stations/{}".format(input1)
except:
    print("Occorre specificare un input corretto es. python3 json2geojson.py Pluvio")
    sys.exit(2)

with urllib.request.urlopen("https://omirl.regione.liguria.it/Omirl/rest/stations/Pluvio") as url:
    data = json.loads(url.read().decode())
    #print(data)

print("DATI LETTI CORRETTAMENTE")
#exit()
#script, in_file, out_file = argv

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
     } for d in data]
}
#with open(os.path.join(sys.path[0], "my_file.txt"), "r") as f:

out_file="{}.json".format(input1)
print(out_file)
output = open(os.path.join(sys.path[0],out_file), 'w')
json.dump(geojson, output)
#print(geojson)



