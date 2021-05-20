#! usr/bin/env python
#Script per aggiornare le misure della rete OMIRL nei layer della vista 3D realizzata con il Plugin Qgis2threejs
# si lancia in maniera diversa a seconda dei dati che si intendono recuperare
# - python3 update3Dvalue.py Idro 84
# - python3 update3Dvalue.py Pluvio 85
# - python3 update3Dvalue.py Press 86
# - python3 update3Dvalue.py Termo 87
# il valore numerico è l'id del layer nel file scene.js generato dal Plugin Qgis2threejs
# Gter copyleft 2020
# author: Roberto Marzocchi
###############################################################################

import json
import os
from sys import argv

script, input1, input2 = argv
try:
    jsonFilePath = '/home/gter/nextcloud-data/progetto_concerteaux/files/vector/omirl_data_ingestion/{}.json'.format(input1)
    id_layer = int(input2)
except:
    print("Occorre specificare un input corretto es. python3 update3Dvalue.py Pluvio 85")
    sys.exit(2)

jsFilePath = '/home/gter/nextcloud-data/progetto_concerteaux/files/media/3D/data/index/scene.js'
list_json = {}

if os.path.exists(jsonFilePath): #check if the file esists
    #reads the .json file
    json_file = open(jsonFilePath, 'r')
    json_file_reader = json_file.read()
    sjson = json.loads(json_file_reader)
    json_feat = sjson['features']
    for i in json_feat:
        list_json[i['properties']['shortCode']] = [i['properties']['refDate'], str(i['properties']['value'])]
    #print(list_json)
else:
    print('Il file {} non è stato trovato'.format(jsonFilePath))

if os.path.exists(jsFilePath): #check if the file esists
    print('Found!')
    #reads the .js file as a json
    js_file = open(jsFilePath, 'r')
    js_file_reader = js_file.read()
    obj = js_file_reader[js_file_reader.find('{') : js_file_reader.rfind('}')+1]
    sjs = json.loads(obj)
    js_feat = sjs['layers']
    #replaces date a value of the specified layer with date and value form the json file
    for index, x in enumerate(js_feat):
        if x["id"] == id_layer:
            #print('entro in if')
            js_features = x["data"]["blocks"][0]["features"]
            for k in js_features:
                if k["prop"][9] in list_json:
                    k["prop"][8] = list_json[k["prop"][9]][0]
                    k["prop"][12] = list_json[k["prop"][9]][1]
                    print(k["prop"][8])
                    print(k["prop"][12])
else:
    print('Il file {} non è stato trovato'.format(jsFilePath))

#write changes in the js file
with open(jsFilePath, 'w', encoding='utf-8') as fjs:
    text = 'app.loadJSONObject({});'.format(json.dumps(sjs, ensure_ascii=False, indent=2))
    fjs.write(text)
    fjs.close()

print('File scene.js salavato correttamente.')
