# omirl_data_ingestion
Script per la gestione di dati da WS della rete ARPA Liguria OMIRL

- json2geojson converte i json utilizzati dal OMIRL (es. https://omirl.regione.liguria.it/Omirl/rest/stations/Idro) in un file geojson visualizzabile su un qualsiasi SW GIS

Si può aggiungere su una o più righe sul crontab (file /etc/crontab) con la seguente sintassi:
*/5 * * * * www-daya /usr/bin/python3 /...file_path.../omirl_data_ingestion/json2geojson.py Idro


