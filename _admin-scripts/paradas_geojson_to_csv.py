import json
import os
import sys

if not sys.argv[1]:
   print("Feedme paradas.geojson")
   exit()

if not os.path.exists(sys.argv[1]):
   print("File doesn't exist")
   exit()

if not sys.argv[1].endswith(".geojson"):
   print("Wrong file format")
   exit()


pieces_path = os.path.split(sys.argv[1])
folder = pieces_path[0]
filename,_ = os.path.splitext(pieces_path[1])
final_path = os.path.join(folder,filename + ".csv")

with open(sys.argv[1],"r",encoding="utf-8") as tmp:
   bus_stops = json.loads(tmp.read())["features"]

final_file = list()
final_file.append("ID\tLíneas\tLugar\tGarita\tEstado\tExtra")
for item in bus_stops:
	row = list()
	current = item['properties']
	has_garita = "no"
	name = current['name']
	if " Garita" in name:
	   has_garita = "si"
	   name = name.replace(" Garita","")
	name = name.replace("P.","").strip()
	if not name:
		name = "s/id"
	tmp = current['description'].split("\n")
	tmp_lines = list()
	tmp_location = ""
	tmp_extra = list()
	for piece in tmp:
		if piece.startswith("Línea"):
		   tmp_lines.append(piece.replace("Línea ",""))
		elif piece.startswith("C:"):
			 tmp_location = piece
		else:
			 tmp_extra.append(piece)
	state = "no checkeado"
	if '_storage_options' in current and 'color' in current['_storage_options']:
		if "Green" in current['_storage_options']['color']:
			state = "checkeado"
		elif current['_storage_options']['color']   == "Gold":
			state = "deshuso?"
	row.append(name)
	row.append(", ".join(tmp_lines))
	row.append(tmp_location.replace("C: ",""))
	row.append(has_garita)
	row.append(state)
	tmp = "" if not tmp_extra else ",".join(tmp_extra)
	row.append(tmp)

	final_file.append("\t".join(row))

with open(final_path,"w",encoding="utf-8") as tmp:
	 tmp.write("\n".join(final_file))

print("file saved to " + final_path)