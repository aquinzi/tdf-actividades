#! python3
# -*- coding: utf-8 -*-

'''Parse the JSONs files from the "rg-actividades" to HTML. Activities AND places.
Outputs in current folder
'''

# TODO: activities: add keys not in properties list
# TODO: activities: add key overwritting
<<<<<<< HEAD
# TODO: simplify code so it's not that redundant and duplicated (lazyness & quickness won)
# TODO: place: can have also opening-times
<<<<<<< HEAD
<<<<<<< HEAD
 

=======
# TODO: Option to update index file to include latest changes
=======
=======
# TODO: activity can have it's own place
>>>>>>> 4c9bca0... finished updating to new layout
# 
>>>>>>> 2633dcc... add new template; clean main pages creation process
# TPL replacements:
# 		main tpl: 
# 			{body}
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
# 			
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
<<<<<<< HEAD
>>>>>>> 9adb490... sketch new template



	



=======
>>>>>>> 2633dcc... add new template; clean main pages creation process



 			
 			
import json
import os
import sys
import re
import datetime #to get today's date for footer("last built")
from collections import OrderedDict


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

PLACES_IMAGE_PLACEHOLDER = "images/lugar-marcador-posicion.jpg"

#MAP_URL = "http://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=17/{lat}/{lon}"
<<<<<<< HEAD
MAP_URL = "http://www.openlinkmap.org/?lat={lat}&lon={lon}&zoom=17&id=1709214056&type=node&lang=es"
=======
MAP_URL = "http://www.openlinkmap.org/?lat={lat}&lon={lon}&zoom=17&id=1709214056&type=node&lang=en"
>>>>>>> 2633dcc... add new template; clean main pages creation process

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

<<<<<<< HEAD
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



=======
TPL_INDEX_LATESTCHANGES = '''<li><time datetime="{date_iso}">{date_human}</time> {change}</li>'''
>>>>>>> 4c9bca0... finished updating to new layout

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


TPL_CARD_DT = '''<dt {dt_attr}>{dt_text}</dt><dd {dd_attr}>{dd_text}</dd>'''


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
	</div>
'''

TPL_PAGE_PLACES_IMG_STREET_VIEW = '''http://maps.googleapis.com/maps/api/streetview?size=800x400&location={lat},{lon}&heading={angle}&fov={zoom}'''

TPL_PAGE_PLACES_MAP_LIST = '''
		<ul class="ver-mapa" aria-label="Ver en mapa">
			<li><a href="{map_link}" rel="external">Mapa</a>
			<li><a href="{map_streetview}" rel="external">Google Street View</a>
			<!--<li><a href="geo:{lat},{lon};u=35" rel="external">Programa asociado</a>-->
			<data class="p-latitude" value="{lat}"><data class="p-longitude" value="{lon}">
		</ul>
'''



# end HTML templates
# --------------------

# ==== end configuration ====
# ===========================

# =======================
# ==== global vars ====

HTML_PAGE_TEMPLATE = ""
TODAY = datetime.datetime.now().strftime("%Y-%m-%d")

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

def isoDateToHuman(date):
	'''Converts an ISO date (YYYY-MM-DD) to human (spanish).
	(simple way, without setting locale and calling datetime. 
		For now we don't need that)

	:param:date str the date 
	:return: str 
	'''
	
	year, month, day = date.split("-")

	

	month_list = ("desconocido", "enero", "febrero", "marzo", "abril", "mayo"
		, "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

	month = int(month) #also removes leading 0
	
	#ex: julio 27, 2015
	return "{} {}, {}".format(month_list[month], day, year)


def process_places(places):
	'''Process the places file. 

	:param:places Must be a "json object" (already read and converted)
	'''

	#get keys/properties from dummy item in the begining of the file
	main_properties = list()
	properties_with_list = ('telefono', 'url')

	for key,v in places['features'][0]['properties'].items():
		main_properties.append(key)

	main_properties.remove("marker-symbol") # only to display in geojson, not needed in html
	main_properties.remove("id")
	main_properties.remove("last-update") #always goes last
	
	main_properties = tuple(main_properties)

	final_item = ""
	final_places_page = ""
	tmp_item = ""
	tmp_property = ""

	for place in places['features'][1:]:
		properties = place['properties']
		geo  = place['geometry']['coordinates'] #lon, lat
		properties['geo'] = (str(geo[1]), str(geo[0]))

		tmp_item = ""
		final_item = ""

		for propkey in main_properties:
			tmp_item += create_property(propkey, properties, "places")

		final_item = tmp_item

		if 'last-update' in properties and properties['last-update']:
			final_item += TPL_CARD_DT.format(dt_text="Última actualización", 
				dt_attr=' class="ultima-actualizacion"', 
				dd_attr='', 
				dd_text='<time datetime="'+properties['last-update']+'">' + isoDateToHuman(properties['last-update']) + "</time>")

		
		tmp_name = properties['nombre'].replace('"', "'")

		tmp_img = ""
		if "imagen" in properties and properties['last-imagen']:
			tmp_img = properties['last-imagen']
		else:
			tmp_img = PLACES_IMAGE_PLACEHOLDER

		tmp = TPL_PAGE_PLACES_CARD.format(name=tmp_name, img_front=tmp_img, info=final_item)

		if tmp_img == PLACES_IMAGE_PLACEHOLDER:
			tmp = tmp.replace('<img alt="Frente de '+tmp_name+'"', '<img alt="Marcador de posición de imagen"')

		final_places_page += tmp

	final_places_page = TPL_PAGE_PLACES.format(cards=final_places_page)

	# add missing html (headers, div, etc)
	final_places_page = HTML_PAGE_TEMPLATE.replace("{body}", final_places_page)
	final_places_page = final_places_page.replace("{header-secondheading}", '<div class="my-content-sub-heading"><h2>Lugares</h2></div>')




	save_file(os.path.join(OUTPUT_FOLDER, PLACES_OUTPUT_FILE), final_places_page)

def process_activities(file_list, places):
	'''Process activities
	
	:param:file_list a list with paths to files
	:param:places Must be a "json object" (already read and converted)
	'''

	# get basic keys from template?
	#if not os.path.exists(os.path.join(SRC_FOLDER, ACTIVITY_DUMMY_FILE)):
	#	print("Need dummy file. Exiting")
	#	exit()

	#tmp = json.loads(open_file(os.path.join(SRC_FOLDER, ACTIVITY_DUMMY_FILE)))
	
	main_properties = ('nombre', 'direccion', 'precio', 'horario', 'url', 'email', 'telefono', 'geo', 'nota')
	
	properties_with_list = ('telefono', 'url', 'geo')

	# go trough files, open them, create json, convert, add to final_doc
	final_item = ""
	tmp_final_activities = ""
	tmp_final_section = ""
	tmp_item = ""
	final_text = ""

	activities_all = dict()

	for f in file_list:
		activity = json.loads(open_file(f), object_pairs_hook=OrderedDict)
		activity_name = os.path.basename(f) #get filename
		print(" Processing: " + activity_name)	

		activity_name = uppercase_first_letter(activity['nombre'])

		if not activity['tipo'] in activities_all:
			activities_all[activity['tipo']] = list()

		tmp_final_activities = ""

		for item in activity['lugares']:
			tmp_item = ""
			final_item = ""

			for propkey in main_properties:
				tmp_property = create_property(propkey, item, "activities")

				for circumflex in REMOVE_CIRCUMFLEX:
					tmp_property = re.sub(circumflex[0], circumflex[0] + " (" + circumflex[1] + ")", tmp_property, flags=re.IGNORECASE)

				tmp_item += tmp_property

			final_item = tmp_item

			if 'last-update' in item and item['last-update']:
				final_item += TPL_CARD_DT.format(dt_text="Última actualización", 
					dt_attr='class="ultima-actualizacion"',
					dd_attr='', 
					dd_text='<time datetime="'+item['last-update']+'">' + isoDateToHuman(item['last-update']) + "</time>")
		 	
			back_color = ""
			if 'precio' in item:
				if item['precio'].lower() == "gratis":
					back_color = "my-card-blue-bg"
				elif item['precio'].lower() == "pago":
					back_color = "my-card-green-bg"

			tmp_name = ""
			if 'nombre' in item and  item['nombre']:
				tmp_name = item['nombre']
			else:
				tmp_name = activity_name

			for circumflex in REMOVE_CIRCUMFLEX:
				tmp_name = re.sub(circumflex[0], circumflex[0] + " (" + circumflex[1] + ")", tmp_name, flags=re.IGNORECASE)
				tmp_name = uppercase_first_letter(tmp_name)


			tmp_final_activities += TPL_PAGE_ACTIVITIES_CARD.format(price_bg=back_color
				, name=tmp_name, info=final_item)


		activity_name_heading = activity_name
<<<<<<< HEAD
		if activity['nombre_alt']:
=======

		if 'nombre_alt' in activity and activity['nombre_alt']:
>>>>>>> 4c9bca0... finished updating to new layout
			activity_name_heading += "/" + activity['nombre_alt']


		tmp_final_section = TPL_PAGE_ACTIVITIES_SECTION.format(
			activity_name_id=activity_name.lower()
			, activity_name=activity_name_heading, cards=tmp_final_activities
			)

		final_text += tmp_final_section

		activities_all[activity['tipo']].append('<a href="#' + activity_name.lower() + '">' + activity_name + '</a>')

	#proper index
	tmp_toc = ""
	for key in activities_all:
		tmp_toc += "<li>" + key + "<ol>"

		for activity in activities_all[key]:
			tmp_toc += "<li>" + activity + "</li>"

		tmp_toc += "</ol></li>"


	#activity page
	final_text = TPL_ACTIVITIES_PAGE.format(toc_items=tmp_toc, sections=final_text)

	# add missing html (headers, div, etc)
	final_text = HTML_PAGE_TEMPLATE.replace("{body}", final_text).replace("{header-secondheading}", '<div class="my-content-sub-heading"><h2>Actividades</h2></div>')


	save_file(os.path.join(OUTPUT_FOLDER, ACTIVITIES_OUTPUT_FILE), final_text)

def uppercase_first_letter(s):
	'''Converts the first letter of the string to upper case, keeping the rest as is.
	:return: str 
	'''

	# if we wanted to capitalize the first and the rest in lower case: capitalize()
	return s[0].upper() + s[1:]


def create_property(key, properties_dict, isfrom):
	'''Creates the dt-dd pair from the key. 
	:param:key  the key (ex.: url, nombre, direccion)
	:param:properties_dict the dict with the data/properties 
	:param:isfrom str from where it's called: places or activities (for address)
	:return: str 
	'''

	if not key in properties_dict:
		return ""

	if key in ("nombre", "gstreetmap", "geo"):
		return ""

	tmp_property = ""
	tmp_format_dict = {'dt_attr': '', 'dt_text' : ''
		, 'dd_attr' : '', 'dd_text' : ''}


	if key == "telefono":
		for phone in properties_dict[key]:
			tmp_property += '<span class="p-tel">' + phone + '</span>, '

		tmp_property = tmp_property[:len(tmp_property)-2] #remove last ", "

		tmp_format_dict['dt_attr'] = 'class="telefono"'
		tmp_format_dict['dt_text'] = "Teléfono"
		tmp_format_dict['dd_text'] = tmp_property

	if key == "url":
		for url in properties_dict[key]:
			tmp_property += '<li><a href="' + url + '" class="u-url">' + url + '</a></li>'

		tmp_property = "<ul>" + tmp_property + "</ul>"

		tmp_format_dict['dt_attr'] = 'class="web"'
		tmp_format_dict['dt_text'] = "Sitios"
		tmp_format_dict['dd_text'] = tmp_property
		
	if key == "email":
		tmp_property = '<a class="u-email" href="mailto:' + properties_dict[key] + '">' + properties_dict[key] + '</a>'

		tmp_format_dict['dt_attr'] = 'class="email"'
		tmp_format_dict['dt_text'] = "email"
		tmp_format_dict['attr']    = 'class="u-email"'
		tmp_format_dict['dd_text'] = tmp_property	

	if key == "nota":
		tmp_format_dict['dt_attr'] = 'class="nota"'
		tmp_format_dict['dt_text'] = "Nota"
		tmp_format_dict['dd_attr'] = 'class="p-note"'
		tmp_format_dict['dd_text'] = properties_dict[key].replace("\\n","<br>")


	if key == "direccion":
		if isfrom == "places":
			geo_lat = properties_dict['geo'][0]
			geo_lon = properties_dict['geo'][1]

			tmp_property = '<span class="p-street-address">' + properties_dict[key] + '</span>'

		address = ""
		address_href = "" #link or not to lugares.html

		if isfrom == "activities":
			for p in places['features'][1:]:
				if p['properties']["id"] == properties_dict[key]:
					address = p['properties']["nombre"]
					address_href = "rg-lugares.html#" + p['properties']["id"]
					break
			if not address:
				address = properties_dict[key]
		
			if address:
				if address_href:
					tmp_property = '<a href="' + address_href + '" class="h-card">' + address + '</a>'
				else:
					tmp_property = address

			tmp_property = '<span class="p-street-address">' + tmp_property + '</span>'
		

		if isfrom == "places":
			tmp = TPL_PAGE_PLACES_MAP_LIST.format(
				map_link=MAP_URL.format(lat=geo_lat, lon=geo_lon), 
				#map_streetview=properties_dict['googlestreetview'],
				map_streetview='',
				lat=geo_lat, lon=geo_lon
				)
			
			tmp_property = tmp_property + tmp 

<<<<<<< HEAD
=======
		tmp_format_dict['dt_attr'] = 'class="direccion"'
		tmp_format_dict['dt_text'] = "Dirección"
		tmp_format_dict['dd_attr'] = ''
		tmp_format_dict['dd_text'] = tmp_property	

	if key == "precio":
		tmp_format_dict['dt_attr'] = 'class="precio"'
		tmp_format_dict['dt_text'] = "Precio"
		tmp_format_dict['dd_attr'] = ''
		tmp_format_dict['dd_text'] = properties_dict[key]	

	if key == "horario":
		tmp_property = ""

		for hora in properties_dict[key]:
			horario_dia  = ""
			horario_hora = ""
			horario_nota = ""

			if 'nota' in hora and hora['nota']:
				horario_nota = "<i>(" + hora['nota'] + ")</i>."

<<<<<<< HEAD
<<<<<<< HEAD
			tmp_property += '<li><span  class="openinghours"{}. {}.</span> {}</li>'.format(horario_dia, horario_hora, horario_nota)
>>>>>>> 4c9bca0... finished updating to new layout
=======
			if 'dia' in hora:
=======
			if 'dia' in hora and hora['dia']:
>>>>>>> 2a9378f... bug fixes; add placeholder image; fix css
				horario_dia = hora['dia'] + ". "

			if 'hora' in hora and hora['hora']:
				horario_hora = hora['hora'] + ". "

			if horario_dia or horario_hora:
				tmp_property = '<span class="openinghours">{} {}</span>'.format(horario_dia, horario_hora)

			tmp_property += '<li>{} {}</li>'.format(tmp_property, horario_nota)
>>>>>>> 8d7b3b7... fixed some html; fixed some wrong json keys

		tmp_property = '<ul>' + tmp_property + '</ul>'

		tmp_format_dict['dt_attr'] = 'class="horarios"'
		tmp_format_dict['dt_text'] = "Horarios"
		tmp_format_dict['dd_attr'] = ''
		tmp_format_dict['dd_text'] = tmp_property



	return TPL_CARD_DT.format(**tmp_format_dict)

# =======================
# ==== Program start ====
# =======================


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

if str(args).count("-") == 0:
	print(" Can't do anything. Exiting")
	exit()

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
HTML_PAGE_TEMPLATE = HTML_PAGE_TEMPLATE.replace("{date-iso}", TODAY).replace("{date-human}", isoDateToHuman(TODAY))


if DO_PAGES:

	if DO_PAGE and not DO_PAGE in HTML_PAGES_KEYWORDS:
		print(" Wrong page key. ")
		exit()

	# dirty way to avoid some code duplication
	must_do_page = ""
	if DO_PAGE:
		must_do_page = DO_PAGE

	for page in HTML_PAGES_KEYWORDS:
		tmp_page = ""
		tmp_subheading = ""

		if not must_do_page or must_do_page == page:
			tmp_page = open_file(os.path.join(HTML_FOLDER, page + ".html"))
<<<<<<< HEAD
			tmp_page = HTML_PAGE_TEMPLATE.replace("{body}", tmp_page)
			save_file(os.path.join(OUTPUT_FOLDER, page + ".html"), tmp_page)
	else:
		if not DO_PAGE in HTML_PAGES_KEYWORDS:
			print(" Wrong page key. ")
			exit()
=======
		else:
			continue

		if page == "colaboracion": tmp_subheading = "Colaboración"
		if page == "preguntas-frecuentes": tmp_subheading = "Preguntas frecuentes"

		if page == "index":
			today_date    = TODAY
			today_changes = ""
			final_str     = ""

			today_date = input(" Today is " + today_date + ". (Change it (ISO) or type x for not including update): ")
			
			if not today_date: today_date = TODAY 
			
			if not today_date.lower() == "x":
				while (not today_changes):
					today_changes = input(" Today changes: ")

				final_str = TPL_INDEX_LATESTCHANGES.format(date_iso=today_date, 
					date_human=isoDateToHuman(today_date), change=today_changes)
				

<<<<<<< HEAD
			tmp_page = tmp_page.replace("{latest-changes}", final_str)
>>>>>>> 2633dcc... add new template; clean main pages creation process
		
		tmp_page = HTML_PAGE_TEMPLATE.replace("{body}", tmp_page)
=======
			tmp_page = tmp_page.replace("{latest-changes}", "{latest-changes}\n" + final_str)

			#save latest changes to main index
			if not today_date.lower() == "x":
				save_file(os.path.join(HTML_FOLDER, page + ".html"), tmp_page)
			
			tmp_page = tmp_page.replace("{latest-changes}", "")
			
<<<<<<< HEAD
		tmp_page = HTML_PAGE_TEMPLATE.replace("{body}", tmp_page).replace("{header-secondheading}", tmp_subheading)
>>>>>>> a5dafb2... fixed stupid bugs
=======
		tmp_page = HTML_PAGE_TEMPLATE.replace("{body}", tmp_page).replace("{header-secondheading}", '<div class="my-content-sub-heading"><h2>'+tmp_subheading+'</h2></div>')



>>>>>>> 8d7b3b7... fixed some html; fixed some wrong json keys
		save_file(os.path.join(OUTPUT_FOLDER, page + ".html"), tmp_page)



if not DO_ACTIVITIES and not DO_PLACES:
	exit()


# load keys in order, as in the file
places = json.loads(open_file(os.path.join(SRC_FOLDER, PLACES_FILE)), object_pairs_hook=OrderedDict)

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
