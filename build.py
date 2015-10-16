#! python3
# -*- coding: utf-8 -*-

'''Parse the JSONs files from the "rg-actividades" to HTML. Activities AND places.
Outputs in current folder
'''

# TODO: activities: add keys not in properties list
# TODO: activities: add key overwritting
# TODO: simplify code so it's not that redundant and duplicated (lazyness & quickness won)
# TODO: place: can have also opening-times
<<<<<<< HEAD
 

=======
# TODO: Option to update index file to include latest changes
# TPL replacements:
# 		main tpl: 
# 			{body}
# 			{date-iso}  -> last updated
# 			{date-human}  -> last updated
# 			{header-secondheading}  -> <div class="my-content-sub-heading"> <h2>Actividades</h2> </div>
# 		TPL_ACTIVITIES_PAGE
# 			{toc_items}
# 			{sections} -> rest of the page
# 		TPL_PAGE_ACTIVITIES_SECTION
# 			{activity_name_id}
# 			{activity_name}
# 			{cards}
# 		TPL_PAGE_ACTIVITIES_CARD
# 			{price_bg}  --> my-card-green-bg (paid?), my-card-blue-bg (free?), empty (no price info)
# 			{name}
# 			{info}  --> the dts
# 		TPL_PAGE_ACTIVITIES_CARD_DT
# 			{dt_class}	
# 			{dt_text}
# 			{dd_class}
# 			{dd_text}
# 		TPL_PAGE_PLACES
# 			{cards}
# 		TPL_PAGE_PLACES
# 			{cards}
# 		TPL_PAGE_PLACES_CARD 
# 			{name}
# 			{img_front}  --> usually google street view image
#			{info}  --> the dts
#		TPL_PAGE_PLACES_IMG_STREET_VIEW
#			{lat}
#			{lon}
#			{angle}  -->  &heading
#			{zoom} --> fov
#		TPL_PAGE_PLACES_MAP_LIST
#			{map_link}  --> openstreetmaps or openlinkmaps
#			{map_streetview} --> Google Street View
#			{lat} --> geo:(Programa asociado) and data tags
#			{lon}  --> geo:(Programa asociado) and data tags
>>>>>>> 9adb490... sketch new template



	






 			
 			
import json
import os
import sys
import re

# =======================
# ==== configuration ====

SRC_FOLDER = "src" #where json and geojson live togheter
OUTPUT_FOLDER = "output" # can have the final html inside a git folder, switch branches and copy them

# under SRC_FOLDER we have:
ACTIVITY_FOLDER = "actividades" #activity's home
HTML_FOLDER = "html" 
PLACES_FILE = "lugares.geojson"
ACTIVITY_DUMMY_FILE = "actividad-tpl.json"
PAGE_TEMPLATE_FILE = "page_tpl.html"

PLACES_OUTPUT_FILE = "rg-lugares.html"
ACTIVITIES_OUTPUT_FILE = "rg-actividades.html"

#MAP_URL = "http://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=17/{lat}/{lon}"
MAP_URL = "http://www.openlinkmap.org/?lat={lat}&lon={lon}&zoom=17&id=1709214056&type=node&lang=es"

# pages that website holds besides activities & places. Hardcoded.
HTML_PAGES_KEYWORDS = ('index', 'colaboracion', 'preguntas-frecuentes')

# Let's put the poor japanese I know in use.
# people don't use Hepburn romanization (w/circumflex). Go with the flow.
REMOVE_CIRCUMFLEX = ( 
	('shôtôkan', 'shotokan') 
	, ('gôjû-ryû', 'goju-ryu') 
	, ('dôjô', 'dojo') 
	)

# ---------------
# HTML templates

TPL_ACTIVITIES_PAGE = '''
<p>Actividades encontradas en esta página, separada por categorías y por orden alfabético.</p>

<ol class="toc-columns">
{toc_items}
</ol>

{sections}
'''

TPL_PAGE_ACTIVITIES_SECTION = '''
	<section aria-labelledby="{activity_name_id}">
		<h3 id="{activity_name_id}">{activity_name}</h3>

		{cards}
	</section>
'''

TPL_PAGE_ACTIVITIES_CARD = '''
				<div class="my-card h-card {price_bg}">
					<h4 class="p-name">{name}</h4>
					<dl>
						{info}
					</dl>
				</div>
'''


# DTs example. Activity
# <dt class="direccion">Dirección</dt><dd class="p-street-address h-card"><a href="rg-lugares.html#centrodeportivo">Centro Deportivo Municipal "Reverendo Padre José Forgacs"</a></dd>
# <dt class="precio">Precio</dt><dd>gratis</dd>
# <dt class="horarios">Horarios</dt><dd><ul><li><time>lunes, miercoles, viernes. 18:30-19:30</time>. <i>menores</i></li><li><time>lunes, miercoles, viernes. 19:30-20:30</time>. <i>menores</i></li><li><time>lunes, miercoles, viernes. 20:30-21:30</time>. <i>mayores</i></li></ul></dd>
# <dt class="web">Sitios</dt><dd><ul><li><a href="http://www.facebook.com/pages/Karate-Do-Shotokan-RG" class="u-url">http://www.facebook.com/pages/Karate-Do-Shotokan-RG</a></li></ul></dd>
# <dt class="email">email</dt><dd class="u-email"><a href="mailto:#">lalala@lalala.com</a></dd>
# <dt class="nota">Nota</dt><dd class="p-note">Municipio</dd>
# <dt class="ultima-actualizacion">Última actualización</dt><dd><time>2015-07-23</time></dd>

# DTs example. Place
# <dt class="direccion">Dirección</dt>
# <dd><span class="p-street-address">Avenida Belgrano 1130</span>
#	 <ul class="ver-mapa"  aria-label="Ver en mapa">
#	 <li><a href="http://www.openstreetmap.org/?mlat=-53.7895781&mlon=-67.7070647#map=17/-53.7895781/-67.7070647" rel="external">Mapa</a>
#	 <li><a href="#" rel="external">Google Street View</a>
#	 <li><a href="geo:-53.7895781,-67.7070647;u=35" rel="external">Programa asociado</a>
#	 <data class="p-latitude" value="-53.7895781"><data class="p-longitude" value="-67.7070647">
#	</ul>
# </dd>
# <dt class="horarios">Horarios</dt><dd><ul><li><time>lunes, miercoles, viernes. 18:30-19:30</time>. <i>menores</i></li><li><time>lunes, miercoles, viernes. 19:30-20:30</time>. <i>menores</i></li><li><time>lunes, miercoles, viernes. 20:30-21:30</time>. <i>mayores</i></li></ul></dd>
# <dt class="web">Sitios</dt><dd><ul><li><a href="http://www.facebook.com/sportivo.rg" class="u-url">http://www.facebook.com/sportivo.rg</a></li><li><a href="http://twitter.com/CLUBSPORTIVORG" class="u-url">http://twitter.com/CLUBSPORTIVORG</a></li></ul></dd>
# <dt class="email">email</dt><dd class="u-email"><a href="mailto:#">lalala@lalala.com</a></dd>
# <dt class="telefono">Telefono</dt><dd><span class="p-tel">421398</span></dd>
# <dt class="ultima-actualizacion">Última actualización</dt><dd><time>2015-07-23</time></dd>




TPL_PAGE_ACTIVITIES_CARD_DT = '''<dt{dt_class}>{dt_text}</dt><dd{dd_class}>{dd_text}</dd>'''


TPL_PAGE_PLACES = '''
{cards}
'''

TPL_PAGE_PLACES_CARD = '''
	<div class="my-card h-card">
		<div class="my-card-img">
			<h3 class="p-name">{name}</h3>
			<img alt="Frente de {name}" src="{img_front}">
		</div>

		<dl>
			{info}
		</dl>
'''

TPL_PAGE_PLACES_IMG_STREET_VIEW = '''http://maps.googleapis.com/maps/api/streetview?size=800x400&location={lat},{lon}&heading={angle}&fov={zoom}'''

TPL_PAGE_PLACES_MAP_LIST = '''
		<ul class="ver-mapa" aria-label="Ver en mapa">
			<li><a href="{map_link}" rel="external">Mapa</a>
			<li><a href="{map_streetview}" rel="external">Google Street View</a>
			<li><a href="geo:{lat},{lon};u=35" rel="external">Programa asociado</a>
			<data class="p-latitude" value="{lat}"><data class="p-longitude" value="{lon}">
		</ul>
'''







TPL_ITEM = '''
	<dl{dlatrr}>
		{defs}
	</dl>
'''

TPL_ITEM_DATA = '''<dt>{dt}</dt><dd{ddattr}>{dd}</dd>
'''
TPL_SECTION_ACTIVITY = '''
<section{sectionattr}>
	<h3{hatrrb}>{actividad}</h3>
	{lista}
</section>
'''

TPL_ACTIVITY_PAGE = '''
<h2>Actividades en Río Grande</h2>
{sections}
'''
TPL_PLACES_PAGE = '''
<h2>Lugares en Río Grande</h2>
{sections}
'''

'''

  <dt>horarios</dt><dd><span class="openinghours">martes, jueves 17:00-19:00</span> comment":"mayores"; <span class="operating-hours">sábado 16:30-19:30</span>"comment":"Clase general"

'''


# ==== end configuration ====
# ===========================

# =======================
# ==== global vars ====

HTML_PAGE_TEMPLATE = ""

# make it less anoying to call it
SRC_FOLDER    = os.path.join(os.getcwd(), SRC_FOLDER)
OUTPUT_FOLDER = os.path.join(os.getcwd(), OUTPUT_FOLDER)
HTML_FOLDER   = os.path.join(SRC_FOLDER, HTML_FOLDER)

DO_PLACES     = True
DO_ACTIVITIES = True
DO_PAGES 	  = True
DO_PAGE 	     = ""

# ==== end global vars ====
# ===========================

def files_get(path):
	''' Get a list of files in dir. Returns list
	:return:list list of files
	'''

	theFiles = list()
	for root, subFolders, files in os.walk(path):
		for filename in files:
			filePath = os.path.join(root, filename)

			if os.path.exists(filePath) and filePath.endswith("json") and not filename.startswith("_"):
				theFiles.append(filePath)

	return theFiles


def open_file(path):
	''' Opens file and returns text
	:return:text
	'''

	with open(path, 'r', encoding='utf-8-sig') as readme:
		return readme.read()

def save_file(path, text):
	''' Saves the file to path '''

	with open(path, 'w', encoding='utf-8-sig') as saveme:
		saveme.writelines(text)

def process_places(places):
	'''Process the places file. 

	:param:places Must be a "json object" (already read and converted)
	'''

	#get keys/properties from dummy item in the begining of the file
	properties = list()
	properties_with_list = ('telefono', 'url')

	for key,v in places['features'][0]['properties'].items():
		properties.append(key)

	properties.remove("marker-symbol") # only for display in geojson, we don't need it in html
	properties.remove("id")

	#have some ordering
	a, b = properties.index('nombre'), 0
	properties[b], properties[a] = properties[a], properties[b]
	a, b = properties.index('direccion'), 1
	properties[b], properties[a] = properties[a], properties[b]
	a, b = properties.index('last-update'), len(properties) -1
	properties[b], properties[a] = properties[a], properties[b]
	a, b = properties.index('nota'), len(properties) -2
	properties[b], properties[a] = properties[a], properties[b]

	properties = tuple(properties)

	final_item = ""
	final_places_page = ""
	tmp_item = ""
	tmp_property = ""

	for place in places['features'][1:]:
		prop = place['properties']
		geo = place['geometry']['coordinates'] #lon, lat
		tmp_item = ""
		final_item = ""

		for propkey in properties:
			tmp_property = ""
			if propkey in prop:
				if propkey == "url":
					for url in prop[propkey]:
						tmp_property += '<li><a href="' + url + '" class="u-url">' + url + '</a></li>'

					tmp_property = "<ul>" + tmp_property + "</ul>"
					tmp_property = TPL_ITEM_DATA.format(dt="Sitios",ddattr='', dd=tmp_property)

				elif propkey == "telefono":
					for phone in prop[propkey]:
						tmp_property += '<span class="p-tel">' + phone + '</span>, '

					tmp_property = tmp_property[:len(tmp_property)-2] #remove last ", "
					tmp_property = TPL_ITEM_DATA.format(dt="Telefono",ddattr='', dd=tmp_property)

				elif propkey == "email":
					tmp_property = '<a class="u-email" href="mailto:' + prop[propkey] + '">' + prop[propkey] + '</a>'
					tmp_property = TPL_ITEM_DATA.format(dt="email",ddattr='',dd=tmp_property)

				elif propkey == "nota":
					tmp_property = TPL_ITEM_DATA.format(dt="Nota",ddattr=' class="p-note"', dd=prop[propkey])

				elif propkey == "direccion":
					geo[1] = str(geo[1])
					geo[0] = str(geo[0])

					tmp_property = '<span class="p-street-address">' + prop[propkey] + '</span>'
					tmp_property += '<a href="' + MAP_URL.format(lat=geo[1], lon=geo[0]) + '">Ver en mapa</a>'
					tmp_property += '<a href="geo:' + geo[1] + ',' + geo[0] + ';u=35">Ver en programa asociado</a>'
					tmp_property += '<data class="p-latitude" value="' + geo[1] + '">'
					tmp_property += '<data class="p-longitude" value="' + geo[0] + '">'

					tmp_property = TPL_ITEM_DATA.format(dt="Dirección", ddattr='', dd=tmp_property)

			tmp_item += tmp_property

		final_item = tmp_item

		if 'last-update' in prop and prop['last-update']:
			final_item += TPL_ITEM_DATA.format(dt="Última actualización", ddattr='', dd="<time>" + prop['last-update'] + "</time>")

		tmp = TPL_ITEM.format(dlatrr='', defs=final_item)
		tmp = TPL_SECTION_ACTIVITY.format(sectionattr=' class="h-card"'
			,hatrrb=' id="' + prop['id'] + '" class="p-name"',actividad=prop['nombre'],lista=tmp)
		final_places_page += tmp

	final_places_page = TPL_PLACES_PAGE.format(sections=final_places_page)

	# add missing html (headers, div, etc)
	final_places_page = HTML_PAGE_TEMPLATE.replace("{body}", final_places_page)

	save_file(os.path.join(OUTPUT_FOLDER, PLACES_OUTPUT_FILE), final_places_page)

def process_activities(file_list, places):
	'''Process activities
	
	:param:file_list a list with paths to files
	:param:places Must be a "json object" (already read and converted)
	'''

	# get basic keys to use
	#get keys/properties from dummy file (must open)
	#if not os.path.exists(os.path.join(SRC_FOLDER, ACTIVITY_DUMMY_FILE)):
	#	print("Need dummy file. Exiting")
	#	exit()

	#tmp = json.loads(open_file(os.path.join(SRC_FOLDER, ACTIVITY_DUMMY_FILE)))

	properties = ('nombre','direccion', 'precio', 'horario', 'url', 'nota', 'last-update')
	# other keys that are also in .geojson: telefono, geo, email

	properties_with_list = ('telefono', 'url', 'geo')

	#for key,v in tmp[0].items():
	#	properties.append(key)

	#have some ordering
	#a, b = properties.index('nombre'), 0
	#properties[b], properties[a] = properties[a], properties[b]
	#a, b = properties.index('direccion'), 1
	#properties[b], properties[a] = properties[a], properties[b]
	#a, b = properties.index('horario'), 2
	#properties[b], properties[a] = properties[a], properties[b]
	#a, b = properties.index('last-update'), len(properties) -1
	#properties[b], properties[a] = properties[a], properties[b]
	#a, b = properties.index('nota'), len(properties) -2
	#properties[b], properties[a] = properties[a], properties[b]

	#properties = tuple(properties)

	# go trough list of files, open them, create json, convert, add to final_doc
	final_item = ""
	tmp_final_activities = ""
	tmp_final_section = ""
	tmp_item = ""
	final_text = ""

	activities_all = dict()

	for f in file_list:
		activity = json.loads(open_file(f))
		activity_name = os.path.basename(f) #get filename
		print(" Processing: " + activity_name)
	
		activity_name = activity['nombre'].title()

		if not activity['tipo'] in activities_all:
			activities_all[activity['tipo']] = list()

		tmp_final_activities = ""

		for item in activity['lugares']:
			tmp_item = ""
			final_item = ""

			for propkey in properties:
				tmp_property = ""

				if propkey in item:

					if propkey == "precio":
						tmp_property = TPL_ITEM_DATA.format(dt="Precio",ddattr='',dd=item[propkey])

					if propkey == "nombre":
						if item[propkey]:
							tmp_property = TPL_ITEM_DATA.format(dt="Nombre",ddattr='',dd=item[propkey].title())

					elif propkey == "url":
						if propkey in item:
							for url in item[propkey]:
								tmp_property += '<li><a href="' + url + '" class="u-url">' + url + '</a></li>'

							tmp_property = "<ul>" + tmp_property + "</ul>"
							tmp_property = TPL_ITEM_DATA.format(dt="Sitios",ddattr='', dd=tmp_property)

					elif propkey == "telefono":
						if propkey in item:
							for phone in item[propkey]:
								tmp_property += '<span class="p-tel">' + phone + '</span>, '

							tmp_property = tmp_property[:len(tmp_property)-2] #remove last ", "
							tmp_property = TPL_ITEM_DATA.format(dt="Telefono",ddattr='', dd=tmp_property)

					elif propkey == "email":
						if propkey in item:
							tmp_property = '<a class="u-email" href="' + item[propkey] + '">' + item[propkey] + '</a>'
							tmp_property = TPL_ITEM_DATA.format(dt="email",ddattr='',dd=tmp_property)

					elif propkey == "nota":
						if propkey in item:
							tmp_property = TPL_ITEM_DATA.format(dt="Nota",ddattr=' class="p-note"', dd=item[propkey])
							tmp_property = tmp_property.replace("\\n","<br>")
					
					elif propkey == "horario":
						if propkey in item:
							for hora in item[propkey]:
								horario_dia = hora['dia']
								horario_hora = hora['hora']
								horario_nota = ""
								if 'nota' in hora:
									horario_nota = hora['nota']

								tmp_property += "<li><time>{}. {}</time>. <i>{}</i></li>".format(horario_dia, 
									horario_hora, horario_nota)
							tmp_property = '<ul>' + tmp_property + '</ul>'
							tmp_property = TPL_ITEM_DATA.format(dt="Horarios",ddattr='', dd=tmp_property)


					elif propkey == "direccion":
						address = ""
						address_href = "" #link or not to lugares.html

						#search in places file for key
						if propkey in item:
							for p in places['features'][1:]:
								if p['properties']["id"] == item[propkey]:
									address = p['properties']["nombre"]
									address_href = "rg-lugares.html#" + p['properties']["id"]
									break

							if not address:
								address = item[propkey]

						if address:
							if address_href:
								tmp_property = '<a href="' + address_href + '">' + address + '</a>'
							else:
								tmp_property = address

							tmp_property = TPL_ITEM_DATA.format(dt="Dirección", ddattr=' class="p-street-address"', dd=tmp_property)
				elif propkey == "direccion":
					tmp_property = '¡¿Donde se da!?'
					tmp_property = TPL_ITEM_DATA.format(dt="Dirección", ddattr='', dd=tmp_property)				

				for circumflex in REMOVE_CIRCUMFLEX:
					tmp_property = re.sub(circumflex[0], circumflex[0] + " (" + circumflex[1] + ") ", tmp_property, flags=re.IGNORECASE)
					
				if propkey == "nombre":
					tmp_property = tmp_property.title() #gets overwritten from above

				tmp_item += tmp_property

			final_item = tmp_item

			if 'last-update' in item and item['last-update']:
				final_item += TPL_ITEM_DATA.format(dt="Última actualización", ddattr='', dd="<time>" + item['last-update'] + "</time>")

			tmp_final_activities += TPL_ITEM.format(dlatrr=' class="h-card"',defs=final_item)

		activity_name_heading = activity_name
		if activity['nombre_alt']:
			activity_name_heading += "/" + activity['nombre_alt']

		tmp_final_section = TPL_SECTION_ACTIVITY.format(sectionattr="",
			hatrrb=' id="' + activity_name.lower() + '"',actividad=activity_name_heading
			,lista=tmp_final_activities)

		activities_all[activity['tipo']].append('<a href="#' + activity_name.lower() + '">' + activity_name + '</a>')


		final_text += tmp_final_section

	#proper index
	tmp = "<ul>"
	for key in activities_all:
		tmp += "<li>" + key + ": " + ", ".join(activities_all[key]) + "</li>"
	tmp += "</ul>"

	# add missing html (headers, div, etc)
	final_text = HTML_PAGE_TEMPLATE.replace("{body}", tmp + final_text)

	save_file(os.path.join(OUTPUT_FOLDER, ACTIVITIES_OUTPUT_FILE), final_text)

def update_json(what="activities"):
	'''Regenerate json files to new structure

	:param:what   type of files to change. For now only activities 
	'''

	return

	if not what == "activities":
		print(" What are you trying to do?")
		exit()
	print(" Updating files to new structure")
	
	file_list = list()
	file_list = files_get(os.path.join(SRC_FOLDER, ACTIVITY_FOLDER))
	
	from collections import OrderedDict #order it as here
	new_json = OrderedDict()

	#now it's up to you!
	return

	new_json['nombre'] = ""
	new_json['nombre_alt'] = ""
	new_json['tipo'] = ""
	new_json['lugares'] = []

	for index, ffile in enumerate(file_list[11:]):
		print ("\n Reading: " + os.path.basename(ffile) + "  index: " + str(index + 11))

		tmp_name,_ = os.path.splitext(os.path.basename(ffile))
			
		answer = ""

		answer = input(" Name (heading, empty for '"+tmp_name+"'): ")
		if not answer:
			new_json['nombre'] = tmp_name
		else:
			new_json['nombre'] = answer
		
		answer = ""
		answer = input(" Name Alt: ")
		new_json['nombre_alt'] = answer

		answer = ""
		while (not answer): answer = input(" Tipo (ej. deporte): ")
		new_json['tipo'] = answer

		tmp_file = json.loads(open_file(ffile))
		new_json['lugares'] = tmp_file
		print (" Saving it! ")
		with open(ffile, 'w') as json_final:
			json.dump(new_json, json_final, ensure_ascii=False, indent=3)


# =======================
# ==== Program start ====
# =======================

#future TODO: probably better to have a list 
if not os.path.exists(os.path.join(SRC_FOLDER, PLACES_FILE)):
	print("places file doesn't exist. Exiting")
	exit()

if not os.path.exists(os.path.join(SRC_FOLDER, PAGE_TEMPLATE_FILE)):
	print("template file doesn't exist. Exiting")
	exit()

if not os.path.exists(OUTPUT_FOLDER):
	print("output folder doesn't exist. Exiting")
	exit()

# 'Cause I'm cool I'm going to use the old sys.argv
args = sys.argv[1:]

if "-h" in args or "--help" in args:
	print(" Parsear archivos json/geojson o recrear HTMLs. Se indican con")
	print(" flags. Solo una opción.")
	print(" \n[script]    Regenera todo")
	print(" [script] -a    Regenera actividades")
	print(" [script] -l    Regenera lugares")
	print(" [script] -p    Regenera todas las páginas HTML")
	print(" [script] -p [keyword]   Regenera la página [keyword]. Opciones: " + str(HTML_PAGES_KEYWORDS))
	print(" [script] --update    Regenera todos los .JSON con la nueva estructura (desde codigo)")
	print("")
	print(" Las únicas opciones que se pueden poner juntas son -a y -l que se las une como -al o -la ")

	exit()

if args[0] == "--update":
	update_json()
	exit()


if str(args).count("-") > 1:
	print(" I'm not ready for that many flags. Exiting")
	exit()

if str(args).count("-") == 1:
	if not "-l" in args: DO_PLACES = False 
	if not "-a" in args: DO_ACTIVITIES = False 
	if not "-p" in args: DO_PAGES = False 

	if "-al" in args or "-la" in args: 
		DO_PLACES     = True 
		DO_ACTIVITIES = True 


if "-p" in args and len(args) > 1: 
	# "proper" way
	# DO_PAGE = args[args.index("-p") + 1]
	# But for quick & easyness let's hardcode it
	DO_PAGE = args[1]


if DO_ACTIVITIES:
	if not os.path.exists(os.path.join(SRC_FOLDER, ACTIVITY_FOLDER)):
		print("Activity folder doesn't exist. Exiting")
		exit()

HTML_PAGE_TEMPLATE = open_file(os.path.join(SRC_FOLDER, PAGE_TEMPLATE_FILE))


if DO_PAGES:
	if not DO_PAGE:
		#get keys & cycle through them
		for page in HTML_PAGES_KEYWORDS:
			tmp_page = open_file(os.path.join(HTML_FOLDER, page + ".html"))
			tmp_page = HTML_PAGE_TEMPLATE.replace("{body}", tmp_page)
			save_file(os.path.join(OUTPUT_FOLDER, page + ".html"), tmp_page)
	else:
		if not DO_PAGE in HTML_PAGES_KEYWORDS:
			print(" Wrong page key. ")
			exit()
		
		tmp_page = open_file(os.path.join(HTML_FOLDER, DO_PAGE + ".html"))
		tmp_page = HTML_PAGE_TEMPLATE.replace("{body}", tmp_page)
		save_file(os.path.join(OUTPUT_FOLDER, DO_PAGE + ".html"), tmp_page)
	
places = json.loads(open_file(os.path.join(SRC_FOLDER, PLACES_FILE)))

file_list = list()
if DO_ACTIVITIES:
	file_list = files_get(os.path.join(SRC_FOLDER, ACTIVITY_FOLDER))

# -----------------------
# generate places file

if not DO_PLACES:
	print(" Reading: geoplaces")
else:
	print(" Processing: geoplaces")
	process_places(places)


# -----------------------
# generate activities page

if DO_ACTIVITIES:
	process_activities(file_list, places)
