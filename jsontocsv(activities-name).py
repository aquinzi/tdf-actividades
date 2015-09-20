'''
run where the files are
'''

import json
import os

final_file = "tipo,nombre,nombre_alt\n"

for root, subFolders, files in os.walk(os.getcwd()):
	for filename in files:
		filePath = os.path.join(root, filename)
		
		if not filePath.endswith(".json") or filename.startswith("_"): 
			continue
			
		print (" processing " + filePath)
		
		current_text = ""
		with open(filePath, 'r', encoding='utf-8-sig') as readme:
			current_text = readme.read()
		
		
		tmp_file = json.loads(current_text)
		
		nombre_alt = "\"\""
		if "nombre_alt" in tmp_file:
			nombre_alt = tmp_file["nombre_alt"]
		
		final_file += tmp_file["tipo"] + "," + tmp_file["nombre"] + "," + nombre_alt + "\n"
		

with open(os.path.join(os.getcwd(),"actividades_merged.csv"), 'w', encoding='utf-8-sig') as saveme:
	saveme.writelines(final_file)