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
	try:
		os.makedirs(OUTPUT_FOLDER)
	except OSError:
		print("output folder doesn't exist and can't be created. Exiting")
		exit()

	
# as we're using it as a "database" we must keep all keys EXCEPT geokeys
# because if it's linked to the "places" file we dont need it 
# remember to include at least ONE horarios, even if it's empty 

ENTITY_TEMPLATE_BASE = '''---
nombre: {nombre}
categoria: {actividad}
ultima-actualizacion: {last_update}
direccion: 
  - lugar: {direccion}{geokeys}
horario: {horarios}
precio: {precio}
nota: | 
  {nota}
url: [{urls}]
telefono: [{telefonos}]
email: {email}
---

'''

# for the following just use normal search and replace. We have 
# problems with str.format and the curly braces of yaml

ENTITY_TEMPLATE_OPTIONAL_GEOKEYS = '''
  - geo: {lat: [lat], lon: [lon]}'''

ENTITY_TEMPLATE_OPTIONAL_HORARIOS = '''
  - {dia:"[dia]", hora:"[hora]", nota:"[nota]" }'''


def clean_filename(s):
	'''Removes invalid chars from the string, making it 
	safe for a url

	:param:s string the string to clean 
	'''

	tmp = s.lower().replace(" ","-").replace('"',"").replace("'",""
	     ).replace("(","").replace(")","")
	
	tmp = tmp.replace("á","a").replace("é","e").replace(
	    "í","i").replace("ó","o").replace("ú","u")
	
	#tmp = tmp.replace("ô","o").replace("û","u")

	return tmp
		
		
		
TOTAL_ENTITIES     = 0
ENTITIES_CONVERTED = 0 

for root, subFolders, files in os.walk(INPUT_FOLDER):
	for filename in files:
		filePath = os.path.join(root, filename)
		
		if not filePath.endswith(".json") or filename.startswith("_"): 
			continue
			
		print ("\n\n processing: " + filePath)
		
		current_text = ""
		with open(filePath, 'r', encoding='utf-8-sig') as readme:
			current_text = readme.read()
		
		tmp_file = json.loads(current_text)
		
		category_key = clean_filename(tmp_file["nombre"])
		
		if category_key == "especifico-para-adultos-mayores-mas-de-60-años":
			category_key = "adultos-mayores"
		
		entities = tmp_file["lugares"]
		
		TOTAL_ENTITIES += len(entities)
		
		for entity in entities:
			document_filename = clean_filename(entity["nombre"]) + ".md"
			
			final_file = ""
			final_path_folder = os.path.join(OUTPUT_FOLDER, category_key)
			final_path = os.path.join(final_path_folder, document_filename)
			
			if not entity["nombre"]:
				print (" it has no name, it was a filler")
				continue
				
			ENTITIES_CONVERTED += 1
			
			if os.path.exists(final_path):
				print (" already exist. Skipping.")
				continue
				
			# process data
			new_entity = {
				'nombre':"" ,'actividad':"" ,'last_update':""
				,'direccion':"" ,'geokeys':""
				,'horarios':"" ,'precio':"" ,'nota':""
				,'urls':"" ,'telefonos':"" ,'email':""
			}

			new_entity['nombre'] = entity["nombre"]
			new_entity['actividad'] = category_key
			
			if "last-update" in entity:
				new_entity['last_update'] = entity["last-update"]
			
			if "direccion" in entity:
				new_entity['direccion'] = entity["direccion"]			
				
			if "geo" in entity:
				new_entity['geokeys'] = ENTITY_TEMPLATE_OPTIONAL_GEOKEYS.replace(
				"[lat]",str(entity['geo']['lat'])).replace("[lon]",str(entity['geo']['lon']))
					
			
			# horarios, we must keep one, even if it's blank
			if not "horario" in entity:
				new_entity['horarios'] = ENTITY_TEMPLATE_OPTIONAL_HORARIOS.replace(
					"[dia]","").replace("[hora]","").replace("[nota]","")
			else:
				mas_horarios = list()
				
				for horario in entity['horario']:
					dia  = horario['dia']
					hora = horario['hora']
					
					if "nota" in horario:
						nota = horario['nota']
					else:
						nota = ""

					mas_horarios.append(
						ENTITY_TEMPLATE_OPTIONAL_HORARIOS.replace(
							"[dia]",dia).replace("[hora]",hora).replace("[nota]",nota)
					   )
				
				new_entity['horarios'] = "".join(mas_horarios)
			
			if "precio" in entity:
				new_entity['precio'] = entity["precio"]
			
			if "nota" in entity:
				new_entity['nota'] = entity["nota"].replace("\\n","\n  ")
			
			if "url" in entity:
				new_entity['urls'] = ",".join(entity['url'])			
			
			if "telefono" in entities:
				new_entity['telefonos'] = ",".join(entity['telefono'])			
			
			if "email" in entity:
				new_entity['email'] = entity["email"]		
				
				
			final_file = ENTITY_TEMPLATE_BASE.format(**new_entity)
			
			print ("\n final file is as follows: ")
			print (final_file)
			answer = input(" continue? (y=save, n=exit): ")
			answer = answer.lower()
			if answer == "n" or answer == "exit" or answer == "no":
				exit()
				
			if answer == "y" or answer == "yes" or not answer:
				try:
					os.makedirs(final_path_folder, exist_ok=True) #if part of it exist, create anyways
				except OSError:
					print("can't create the following folder path. " + final_path_folder)
					exit()
				
				with open(final_path, 'w', encoding='utf-8-sig') as saveme:
					saveme.writelines(final_file)
				
print (" -------------------------- ")
print (" Total entities: {} - Converted: {}".format(TOTAL_ENTITIES,ENTITIES_CONVERTED))
print (" -------------------------- ")
print (" finished. Have a nice day. ")
