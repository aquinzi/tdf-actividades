'''
converts geojson to yaml (dirty way)
'''

import json
import os,sys

INPUT_FILE = ""
OUTPUT_FILE  = ""



YAML_BLOCK = '''
- id: {id}
  nombre: '{nombre}'
  direccion: {direccion}
  {geo}
  gstreetview: "{gstreetview}"
  imagen: "{imagen}"
  ultima-actualizacion: {last-update}
  horario: {horario}
  email: {email}
  url: [{url}]
  telefono: [{telefono}]
  nota: |
    {nota}
  marker-symbol: {marker-symbol}
'''

# for below, normal search & replace 
YAML_BLOCK_GEOKEYS = '''geo: {lat: [lat], lon: [lon]}'''

YAML_BLOCK_HORARIOS = '''
  - {dia: "[dia]", hora: "[hora]", nota: "[nota]" }'''


args = sys.argv[1:]

if not os.path.exists(args[0]):
	print (" geojson file doesn't exist")
	exit()

if not os.path.exists(args[1]):
	print (" output folder doesn't exist. We only create the file, not the folders")
	exit()

INPUT_FILE = args[0]
OUTPUT_FILE = args[1]

# keep same name as geojson file
OUTPUT_FILE = os.path.join(OUTPUT_FILE, os.path.splitext(os.path.basename(INPUT_FILE))[0] + ".yml") 

geojson = ""
with open(INPUT_FILE,'r',encoding="utf-8") as tmp:
	geojson = tmp.read()

geojson = json.loads(geojson)
geojson = geojson['features']

# start processing
final_yaml = ""
geojson_keys = (
	'id', 'nombre', 'direccion', 'email', 'nota', "url", "telefono",
	"last-update", "marker-symbol", "nota", "gstreetview", "imagen", 
	"horario", "geometry"
	)

keys_specific_processing = ("url", "telefono", "horario", "geometry")

for feature in geojson:
	place = feature['properties']

	place_yaml = {
		"id": "", "nombre": "",
		"direccion": "",
		"email": "", "url": "", "telefono": "",
		"fecha": "",
		"nota": "",
		"gstreetview": "", "imagen": "",
		"horario": "",
		"geo": "", "marker-symbol":""
	}
	
	if not place['nombre']:
		continue

	print (" processing place: " + place['nombre'])

	for key in geojson_keys:

		if not key in place and not key == "geometry":
			continue



		if not key in keys_specific_processing:
			place_yaml[key] = place[key]
		else:
			if key == "url":
				for i,_ in enumerate(place['url']):
					place['url'][i] = '"' + place['url'][i] + '"'
				
				place_yaml[key] = ",".join(place['url'])

			if key == "telefono":
				place_yaml[key] = ",".join(place[key])

			if key == "horario":
				mas_horarios = list()
				
				for horario in place[key]:
					dia  = horario['dia']
					hora = horario['hora']
					
					if "nota" in horario:
						nota = horario['nota']
					else:
						nota = ""

					mas_horarios.append(
						YAML_BLOCK_HORARIOS.replace(
							"[dia]",dia).replace("[hora]",hora).replace("[nota]",nota)
					   )
				
				place_yaml[key] = "".join(mas_horarios)

			if key == "geometry":
				tmp = ""
				tmp = YAML_BLOCK_GEOKEYS.replace("[lat]", 
					str(feature['geometry']['coordinates'][1])).replace("[lon]", 
					str(feature['geometry']['coordinates'][0]))

				place_yaml['geo']	= tmp

	if not "horario" in place:
		#must keep one blank for reference
		place_yaml['horario'] = YAML_BLOCK_HORARIOS.replace(
			"[dia]","").replace("[hora]","").replace("[nota]","")


	final_yaml += YAML_BLOCK.format(**place_yaml)


with open(OUTPUT_FILE,'w',encoding="utf-8") as tmp:
	tmp.writelines(final_yaml)

print (" finished. Have a nice day! ")