'''
Create event files from a memory list (fake csv) with just the date", "title 
and city", "with a hardcoded template. Modify as needed.

TODO: create month folders if not found

'''
import sys, os 


args = sys.argv[1:]

if not args:
	print ("Provide root folder of the project")
	exit()

if not os.path.exists(args[0]):
	print ("Provide root folder of the project")
	exit()


PATH_TO_SAVE = args[0]

EVENT_TPL = '''---
layout: event 
title: Campeonato Apertura de Voleibol, {genre}, {teams}
date: 2016-{month_day}
no-time-start: true
date-end: 2016-{month_day}
no-time-end: true
location: 
category: {city}
tags: [deportes,voley]
source: http://www.surenio.com.ar/los-sesenta-ocho-partidos-del-campeonato-apertura-2016/
people: []
---
'''


COLUMN_DATE = 0
COLUMN_GENRE = 2
COLUMN_CITY = 1
COLUMN_TEAMS = 3

EVENTS = (
    ("09/04", "ushuaia", "mujeres", "CAEF-UOM")
    ,("10/04", "ushuaia", "mujeres", "AEP/Oshovia-Pingüino")
    ,("10/04", "ushuaia", "mujeres", "CAEF-QRU")
    ,("23/04", "ushuaia", "mujeres", "Campolter-CAEF")
    ,("30/04", "ushuaia", "mujeres", "Campolter-QRU")
    ,("01/05", "ushuaia", "mujeres", "AEP/Oshovia-QRU")
    ,("01/05", "ushuaia", "mujeres", "Campolter-UOM")
    ,("28/05", "ushuaia", "mujeres", "Campolter-AEP/Oshovia")
    ,("28/05", "ushuaia", "mujeres", "CAEF-Pingüino")
    ,("29/05", "ushuaia", "mujeres", "AEP/Oshovia-CAEF")
    ,("29/05", "ushuaia", "mujeres", "Campolter-Pingüino")
    ,("04/06", "ushuaia", "mujeres", "AEP/Oshovia-UOM")
    ,("05/06", "ushuaia", "mujeres", "CAEF-Campolter")
    ,("09/04", "rio-grande", "varones", "QRU-Universitario")
    ,("09/04", "rio-grande", "varones", "Pingüino A-Campolter")
    ,("09/04", "rio-grande", "varones", "Pingüino B-AEP/Oshovia")
    ,("10/04", "rio-grande", "varones", "Universitario-AEP/Oshovia")
    ,("10/04", "rio-grande", "varones", "QRU-Pingüino A")
    ,("10/04", "rio-grande", "varones", "Pingüino B-Campolter")
    ,("23/04", "ushuaia", "varones", "AEP/Oshovia-QRU")
    ,("23/04", "ushuaia", "varones", "Campolter-Universitario")
    ,("23/04", "rio-grande", "varones", "Pingüino A-Pingüino B")
    ,("30/04", "ushuaia", "varones", "Campolter-QRU")
    ,("30/04", "rio-grande", "varones", "Pingüino A-AEP/Oshovia")
    ,("30/04", "rio-grande", "varones", "Universitario-Pingüino B")
    ,("28/05", "rio-grande", "varones", "Pingüino A-Universitario")
    ,("28/05", "ushuaia", "varones", "Campolter-AEP/Oshovia")
    ,("28/05", "rio-grande", "varones", "Pingüino B-QRU")
    ,("29/05", "ushuaia", "varones", "AEP/Oshovia-Pingüino B")
    ,("29/05", "rio-grande", "varones", "Universitario-QRU")
    ,("29/05", "ushuaia", "varones", "Campolter-Pingüino A")
    ,("04/06", "ushuaia", "varones", "AEP/Oshovia-Universitario")
    ,("04/06", "rio-grande", "varones", "Pingüino-QRU")
    ,("04/06", "ushuaia", "varones", "Campolter-Pingüino B")
    ,("18/06", "rio-grande", "varones", "Universitario-Campolter")
    ,("18/06", "rio-grande", "varones", "QRU-AEP/Oshovia")
    ,("18/06", "rio-grande", "varones", "Pingüino B-Pingüino A")
    ,("19/06", "ushuaia", "varones", "AEP/Oshovia-Pingüino A")
    ,("19/06", "rio-grande", "varones", "QRU-Campolter")
    ,("19/06", "rio-grande", "varones", "Pingüino B-Universitario")
)


# cycle the list of tuples.

for event in EVENTS:
	print ("processing: " + ",".join(event))
	proper_date_day, proper_date_month = event[COLUMN_DATE].split("/")
	proper_date = proper_date_month + "-" + proper_date_day
	
	new_event = ""
	
	#put in tpl
	new_event = EVENT_TPL.format(genre=event[COLUMN_GENRE], teams=event[COLUMN_TEAMS], 
	                             month_day=proper_date, city=event[COLUMN_CITY])

	# create filename
	event_filename = ""
	
	tmp_teams = ""
	tmp_teams = event[COLUMN_TEAMS].lower().replace("/","-").replace("ü","u").replace(" ","-")
	tmp = "campeonato-apertura-voleibol-" + event[COLUMN_GENRE] + "-" + tmp_teams
	
	event_filename = "2016-" + proper_date + "-" + tmp + ".md"
	
	
	#find the path
	event_path = os.path.join(PATH_TO_SAVE,event[COLUMN_CITY],"_posts","2016", proper_date_month)
		
	#save 
	with open(os.path.join(event_path,event_filename),'w',encoding="utf-8") as tmp:
		tmp.writelines(new_event)
