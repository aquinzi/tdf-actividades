'''
get the entities in json and convert to jekyll collections (markdown + yml block).

'''

import os, sys
import json

args = sys.argv[1:]

if len(args) == 0:
	print ("must run with input folder and output folder")
	exit()

INPUT_FOLDER = args[0]
OUTPUT_FOLDER = args[1]

if not os.path.exists(INPUT_FOLDER):
	print("Input folder doesnt exist")
	exit()
	
if not os.path.exists(OUTPUT_FOLDER):
	print("Output folder doesnt exist")
	exit()	
	

ENTITY_TEMPLATE_BASE = '''
---
nombre: {nombre}
categoria: {actividad}
ultima-actualizacion: {last_update}
{extra_propierties}
---
'''

ENTITY_TEMPLATE_OPTIONAL = '''
direccion: 
  - lugar: {direccion}
  - geo: {lat: {geo_lat}, lon: {geo_lon}}
horario:
  - {dia: {dia}, hora: {hora}, nota: {nota}}
precio: {precio}
nota: {nota}
url: [{urls}]
telefono: [{telefono}]
email: {email}

'''

ENTITY_TEMPLATE_OPTIONAL_BLOCK = (
	("horario", '''horario:''','''
  - {dia: {dia}, hora: {hora}, nota: {nota}}''') #id, key, list-item
  , ("direccion", '''direccion:''','''
  - lugar: {direccion}''') 
  , ("geo_only", '','''
  - geo: {lat: {geo_lat}, lon: {geo_lon}}''') 
  , ("direccion_titleonly", '''direccion:''','') 
)

ENTITY_TEMPLATE_OPTIONAL_INLINE = (
	  ("precio", "precio: {precio}") #id, template
	, ("nota", "nota: {nota}") 
	, ("url", "url: [{urls}]") 
	, ("telefono", "telefono: [{telefonos}]") 
	, ("email", "email: [{email}]") 
)
	
	
	
	
	
exit()


for root, subFolders, files in os.walk(os.getcwd()):
	for filename in files:
		filePath = os.path.join(root, filename)
		
		if not filePath.endswith(".json") or filename.startswith("_"): 
			continue
			
		print (" processing: " + filePath)
		
		current_text = ""
		with open(filePath, 'r', encoding='utf-8-sig') as readme:
			current_text = readme.read()
		
		tmp_file = json.loads(current_text)
		
		category_key = tmp_file["nombre"].lower()
		entities = tmp_file["lugares"]
		
		for entity in entities:
			document_filename = entity["nombre"].lower().replace(" ","-") + ".md"
			
			final_file = ""
			
			if not entity["nombre"]:
				print ("it has no name, it was a filler")
				continue
				
			final_file = ENTITY_TEMPLATE_BASE.format(
				nombre=entity["nombre"]
				, actividad=category_key
				, last_update=entity["last-update"]
				, extra_propierties=""
				
			)
			

	
		
'''
with open(os.path.join(os.getcwd(),"actividades_merged.csv"), 'w', encoding='utf-8-sig') as saveme:
	saveme.writelines(final_file)
	
'''