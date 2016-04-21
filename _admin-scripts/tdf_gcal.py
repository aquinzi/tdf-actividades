#!/usr/bin/python3


'''
Calculate posting schedules in social media of events and add them to google calendar
so they can be posted using IFTTT (so dirty!)
'''
# Google Developers Console: 
# 			project name: tdf-eventos-gcalcli
#			activate gcal API
#			activate OAuth 2.0 API
# instal: pip3 install --upgrade google-api-python-client


#URL SHORTENER:
#	 urlshortener.url.list to get a list of shortened links from user
#	 urlshortener.url.get get info about a shorted url

#GCAL:
#   probably we could need it. event['id'] (same as event['iCalUID'], this has @google.com)

# TODO: save processed events to the txt file once the city is done. (avoid possible losts when script breaks)
# TODO: use the metadata in file to check if it's old or not. Reason: events that span multiple days (expositions) and were added later.
# TODO: support to create shorturls
# PRobably we should read config file so we dont hardcode stuff
# TODO: find a way to fix updated events. 
# 		- Search the event in calendar, edit
# 		- delete the line in processed posts and just add the new one
#
#        creating function (https://developers.google.com/google-apps/calendar/v3/reference/events/update)
#                []Promps user to enter text to search; 
#                []searches and gets id; 
#                prints event info
#                asks what to update (start, end, title, location) add more
#                creates new title/summary and description
#                updates event
# use named tuples
'''>>> from collections import namedtuple
>>>
>>>
>>> Point = namedtuple('Point', ['x','y'])
>>> p = Point(x=11,y=22)
>>> p
Point(x=11, y=22)
>>> p = p._replace(x=80)
>>> p
Point(x=80, y=22)
'''



#import sys
import os
import json
import argparse 
import random #for the minutes
import datetime

import time
# required Libs (for Google connect)
try:
	from apiclient.discovery import build
	from oauth2client.client import OAuth2WebServerFlow
	from oauth2client.file import Storage
	from oauth2client import tools
	from apiclient.errors import HttpError
	import httplib2
except ImportError as e:
    print (" Need Google API libs. Install with: pip3 install --upgrade google-api-python-client")
    exit()





#optional libs
try:
	import yaml
except ImportError:
	YAML = False
else:
	# You rock!
	YAML = True

# --------------
# configuration
# --------------

CALENDAR_ID = "primary" #IFTTT uses the primary calendar

POST_FOLDER = '_posts'

# where the posts reside
CITIES = ('rio-grande','ushuaia','tolhuin')

# we are in a subfolder now, must get the parent folder
ROOT_DIR = os.path.dirname(os.getcwd()) 

PROCESSED_POSTS_FILE = "processed-posts.txt" #date,city,filename
PROCESSED_POSTS_FILE_LINE = "{ciudad}@{filename}"

# how the places file is called. We assume is in _data/[city]/
PLACES_FILE = "lugares.yml"

HOUR_SCHEDULE = ('09', '13', '17', '21') #minutes are random
DAYS_BEFORE = 7 #How many days before do we start posting the event?

GOOGLE_AUTH = "client_secrets.json"
USER_CREDENTIALS = 'gcal-tdf-credentials.json'

# -------------------
# end configuration
# -------------------



FILES_FOR_PROCESSED_LIST = list() #so we write everything once

PROCESSED_POSTS_FILE = os.path.join(os.getcwd(),PROCESSED_POSTS_FILE)
GOOGLE_AUTH      = os.path.join(os.getcwd(), GOOGLE_AUTH)
USER_CREDENTIALS = os.path.join(os.getcwd(), USER_CREDENTIALS)

# be nice and allow to include the secret/keys as paramenters
parser = argparse.ArgumentParser()
parser.add_argument("--client", help="path of the client_secret.json")
parser.add_argument("--user",   help="path of the user secret_key.json")
parser.add_argument("--clean",  help="Cleans the processed file list")
parser.add_argument("--edit",   help="Edit an event")

#args = vars(parser.parse_args()) #to dict
args = parser.parse_args()

def get_processed_file():
	"""Get the processed file, returning it as a list.

	Returns:
	    list
	"""	

	if os.path.exists(PROCESSED_POSTS_FILE):
		with open(PROCESSED_POSTS_FILE,'r',encoding="utf-8") as tmp:
			#readlines() includes de new-line char. we want things easy ;)
			return tmp.read().splitlines()

	return False

def clean_processed_file():
	"""Filters processed file, deleting old entries. """	

	today = datetime.datetime.today()

	processed_posts = get_processed_file()

	if not processed_posts:
		print (" there was an error with the processed file. Does it exist?")
		return False

	cleaned_posts = list()

	for row in processed_posts:
		tmp_line = row.split("@")[1]
		tmp_line = tmp_line[0:10]
		tmp_date = datetime.datetime.strptime(tmp_line, '%Y-%m-%d')

		if tmp_date >= today:
			cleaned_posts.append(row) 

	if len(cleaned_posts) > 0:
		with open(PROCESSED_POSTS_FILE,'w',encoding="utf-8") as tmp:
			tmp.write("\n".join(cleaned_posts))

		print(" Processed file cleaned!")
	else:
		print(" Everything is ok. Processed file not modified. ")




if args.clean:
	clean_processed_file()
	exit()


if args.client or args.user:
	if args.client:
		GOOGLE_AUTH = args.client
	if args.user:
		USER_CREDENTIALS = args.user

if not os.path.exists(GOOGLE_AUTH):
	print (" sorry, I need the app credentials.")
	exit()

if args.edit:
	#edit_event()
	print ("not yet implemented. Sorry")
	exit()



def googleAuth():
	"""Authenticate Google API call
	
	Returns:
	    http object (authorized)
	"""

	# Storage object holds the credentials (for a single user)
	# If the file does not exist, it is created. 
	storage = Storage(USER_CREDENTIALS)

	# Get the credentials 
	credentials = storage.get()

	if credentials is None or credentials.invalid:
		'''
		flow = OAuth2WebServerFlow(client_id=API_CLIENT_ID,
		client_secret=API_CLIENT_SECRET, 
		scope=['https://www.googleapis.com/auth/calendar',
             'https://www.googleapis.com/auth/urlshortener']
		)
		'''
		flow = client.flow_from_clientsecrets(
	    GOOGLE_AUTH,
	    scope=['https://www.googleapis.com/auth/calendar',
             'https://www.googleapis.com/auth/urlshortener'],
	   )
	
		# new credentials need to be obtained. 
		# oauth2client.tools.run() opens an authorization server page 
		# in default web browser. 
		# The new credentials are also stored in the Storage object,
		# which updates the credentials file.
		flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
		credentials = tools.run_flow(flow, storage, flags)


	# authorize credentials
	http = credentials.authorize(httplib2.Http())

	return http


def useService(service_type):
	""" "Shortcut" to the service/API call 
	
	Args:
	    service_type (str): which service? calendar or url (urlshortener)
	
	Returns:
	    build object kind of thing (google)
	"""

	service = ("", "")

	if service_type == "calendar":
		service = ("calendar", "v3")
	elif service_type == "url":
		service = ("urlshortener", "v1")
	else:
		print (" wrong key for Google Service")
		exit()
		
	return build(serviceName=service[0], version=service[1], http=googleAuth())


def listEvents():
	# The Calendar API's events().list method returns paginated results, so we
	# have to execute the request in a paging loop. First, build the
	# request object. The arguments provided are:
	#   primary calendar for user
	service = useService('calendar')
	request = service.events().list(calendarId=CALENDAR_ID)

	# Loop until all pages have been processed.
	while request != None:
		# Get the next page.
		response = request.execute()
		# Accessing the response like a dict object with an 'items' key
		# returns a list of item objects (events).
		
		for event in response.get('items', []):
			print ("--------------------------")
			# The event object is a dict object with a 'summary' key.
			print(event['summary'])
			print(event['start']['dateTime'])
			print(event['location'])
			print(event['description'])
		# Get the next request object by passing the previous request object to
		# the list_next method.
		request = service.events().list_next(request, response)


def scheduleEvent(list_schedule, event_data):

	cal_service = useService('calendar')
	timezone = 'America/Argentina/Ushuaia'

	'''
	ifttt ingredients
	Title 								 	The event's title.
	Description 							The event's description.
	Where 									The location where the event takes place.
	Starts 									ej August 23, 2011 at 10:00PM
	Ends 									ej: August 23, 2011 at 11:00PM
	'''
	# so dirty
	gcal_description = "#{city}{tags} {title} {shortURL}({human_date}{place})"

	end_date_iso = event_data['end']['timestamp'].isoformat()

	def _fecha_humana(date_time, abbr=False):
		""" translate to human dates (spanish, quick and dirty)
		
		Args:
		    date_time (datetime object)
		    abbr (boolean) abreviate month names? default False
		
		Returns:
		    str
		"""
		
		tmp = date_time.strftime('%d de //%m//, %H:%M hs')
		tmp_month_number = tmp.split("//")[1].split("//")[0]

		month = ""
		if tmp_month_number == "01":
			month = "en." if abbr else "enero"
		if tmp_month_number == "02":
			month = "febr." if abbr else "febrero"
		if tmp_month_number == "03":
			month = "mzo." if abbr else "marzo"
		if tmp_month_number == "04":
			month = "abr." if abbr else "abril"
		if tmp_month_number == "05":
			month = "my." if abbr else "mayo"
		if tmp_month_number == "06":
			month = "jun." if abbr else "junio"
		if tmp_month_number == "07":
			month = "jul." if abbr else "julio"
		if tmp_month_number == "08":
			month = "agt." if abbr else "agosto"
		if tmp_month_number == "09":
			month = "sept." if abbr else "septiembre"
		if tmp_month_number == "10":
			month = "oct." if abbr else "octubre"
		if tmp_month_number == "11":
			month = "nov." if abbr else "noviembre"
		if tmp_month_number == "12":
			month = "dic." if abbr else "diciembre"

		tmp = tmp.replace("//" + tmp_month_number + "//", month)

		return tmp

	
	#cycle list
	for date_time in list_schedule:

		human_datetime_start = ""
		event = {}
		tags  = ""
		city  = ""
		place = ""
		shortURL = ""

		if event_data['city'] == "rio-grande":
			city = "RioGrande"
		else:
			city = event_data['city'].title()

		#event['reminders'] = dict()
		#event['reminders']['useDefault'] = False #remove reminder, this is for myself
		event['summary'] = event_data['title']

		event['start'] = {'dateTime': date_time[0], 'timeZone': timezone}
	
		event['end'] = {'dateTime': date_time[1], 'timeZone': timezone}
		#human_datetime_end = _fecha_humana(event_data['start']['timestamp'], abbr=True) #the real date
		human_datetime_end = event_data['start']['timestamp'].strftime('%d/%m, %H:%M hs')

		# if not time set, remove the 00:00 added when creating the timestamp
		if not event_data['start']['time']:
			human_datetime_end = human_datetime_end.replace("00:00 hs","")
		#if all day: {'date': eEnd}
		
		print ("        schedule from {} to {} until {}".format(
				date_time[0].replace("T", " ").replace(":00-03:00","")
				,date_time[1].replace("T", " ").replace(":00-03:00","")
				, end_date_iso.split("T")[0]
				)
			)
		
		if not event_data['location'] is "":
			event['location'] = event_data['location']
			if event['location']:
				place = ", en " + event_data['location']

		final_summary = event['summary']
		tags = ""
		if event_data['tags']:
			#tags = " #" + event_data['tags'].replace(",", " #")

			all_tags = event_data['tags'].split(",")
			reminding_tags = list()

			#shouldn't be doing this but it's quicker now than using regex
			final_summary = " " + final_summary + " " 

			#use part of the title to include tags (saving space)
			tmp_tag = ""
			for tag in all_tags:
				tmp_tag = " " + tag + " "
				if tmp_tag in final_summary:
					final_summary = final_summary.replace(tmp_tag, " #" + tag + " ")
				else:
					reminding_tags.append(tag)

			final_summary = final_summary.strip()
			tags = " #".join(reminding_tags)


		if event_data['short-url']:
			shortURL = event_data['short-url'] + " "

		event['description'] = gcal_description.format(
			city=city, tags=tags, title=final_summary
			, human_date=human_datetime_end, place=place
			, shortURL=shortURL
			)
		
		#use recurrence so we dont have to create daily events within same time
		#event['recurrence'] = ['RRULE:FREQ=DAILY;UNTIL=20151007T193000-03:00']
		tmp_date = end_date_iso + "Z" #doesnt seem to like timezone.
		tmp_recurrence = tmp_date.replace("-","").replace(":","")
		tmp_recurrence = 'RRULE:FREQ=DAILY;UNTIL=' + tmp_recurrence

		event['recurrence'] = [tmp_recurrence]

		#newEvent = cal_service.events().insert(calendarId=CALENDAR_ID, body=event)
		executeCall(cal_service.events().insert(calendarId=CALENDAR_ID, body=event)) #or newEvent.execute() 
	

def shortenURL(url):
	""" Shortens the URL
	
	Args:
	    url (str)
	
	Returns:
	    str: shortened URL
	"""
	short = executeCall(
		useService('url').url().insert(body={'longUrl': url})
		)

	return short['id']


def executeCall(method):
	""" Executes the API method.
	
	Args:
	    method (google-obhect)
	
	Returns:
	    unknown: method executed or none if failed
	"""
	try:
		return method.execute()
	except HttpError as e:
		error = json.loads(e.content)
		if error.get('code') == '403' and \
			error.get('errors')[0].get('reason') \
			in ['rateLimitExceeded', 'userRateLimitExceeded']:
			time.sleep((2 ** n) + random.random())
		else:
			raise

	return None


def process_post(path, city, meta=False):
	"""Process the post
	
	Args:
	    path (str)
	    city (str)
	    meta (dict) if we got the metadata before 
	"""

	print("    Getting metadata... ", end="")
	if not meta:
		meta = get_post_metadata(path, city)
	print(" done.")

	print("    Creating post schedule... ", end="")
	post_schedule = create_post_schedule(meta['start']['date'], meta['end']['date'])
	print(" done.")

	# create google calendar event
	print("    Inserting post's schedule in Google Calendar... ")
	scheduleEvent(post_schedule, meta)
	
	return True # future proof: if we have an error in some kind


def get_post_metadata(path, city):
	"""Get metadata from post
	
	Args:
	    path (str)
	    city (str)
	
	Returns:
	    dictionary
	"""

	the_post = ""
	# date is date-start, but keep it like this (less coding conditionals)
	metadata = {
		'title':'', 'date':'','date-end':'','city': city
		,'tags':'','short-url':'', 'location':'',


		'start' : {'date': '', 'time':'', 'timestamp':''},
		'end' : {'date': '', 'time':'', 'timestamp':''}
		#date = only date, in str: yyyy-mm-dd 
		#time = only time, in str: hh:mm
		#timestamp = datetime, the object

	}

	keys = list(metadata.keys()) #so we can remove stuff, like city key
	keys.remove('city') 
	
	with open(path,'r',encoding="utf-8") as tmp:
		if YAML:
			the_post = tmp.read()
		else:
			the_post = tmp.readlines()

	tmp = ""
	if YAML:
		# we coud have fake it and told YAML we have many documents
		# inside of file (but only having one) but let's not lie
		# to the poor thing
		'''
		for data in yaml.load_all(document):
			if data:
				print (data['title'])
		'''

		yaml_doc = yaml.load(the_post.split("---")[1])

		for key in keys:
			if key in yaml_doc:
				if key == "date":
					metadata["start"]['date'] = yaml_doc[key]
				elif key == "date-end":
					metadata["end"]['date'] = yaml_doc[key]
				else:
					metadata[key] = yaml_doc[key]

				if key == "tags":
					metadata[key] = ",".join(metadata[key])

	else:
		yaml_block = 0 

		for i,line in enumerate(the_post):
			if line.startswith("---"):
				if yaml_block == 0:
					yaml_block = 1
				else:
					break

			tmp_line = line.strip().split(":", 1)

			for key in keys:
				if line.startswith(key + ":"):
					if not key == "tags":
						metadata[key] = tmp_line[1]	
						if key == "date":
							metadata["start"]['date'] = tmp_line[1]	
						elif key == "date-end":
							metadata["end"]['date'] = tmp_line[1]	
						else:
							metadata[key] = tmp_line[1]	
					else:
						if tmp_line[1] != "[]":
							metadata['tags'] = tmp_line[1].replace("[", "").replace("]","")

	#check if location has ID, and if it does, find the proper name
	metadata['location'] = find_place_id(city, metadata['location'])

	#normalize dates. Use YYYY-MM-DDTHH:MM:SS
	if metadata['start'] and " " in str(metadata['start']['date']):
		datetime_pieces = metadata['start']['date'].split(" ")
		metadata['start']['date'] = datetime_pieces[0]
		if datetime_pieces[1] and ":" in datetime_pieces[1]:
			metadata['start']['time'] = datetime_pieces[1] + ":00"
			datetime_pieces[1] += ":00"

		metadata['start']['timestamp'] = "T".join(datetime_pieces)
		metadata['start']['timestamp'] = datetime.datetime.strptime(metadata['start']['timestamp'], '%Y-%m-%dT%H:%M:00')
	else:
		metadata['start']['date'] = str(metadata['start']['date'])
		metadata['start']['timestamp'] = datetime.datetime.strptime(metadata['start']['date'], '%Y-%m-%d')
		metadata['start']['time'] = ""



	if metadata['end'] and " " in str(metadata['end']['date']): 
		datetime_pieces = metadata['end']['date'].split(" ")
		metadata['end']['date'] = datetime_pieces[0]
		if datetime_pieces[1] and ":" in datetime_pieces[1]:
			metadata['end']['time'] = datetime_pieces[1] + ":00"
			datetime_pieces[1] += ":00"

		metadata['end']['timestamp'] = "T".join(datetime_pieces)
		metadata['end']['timestamp'] = datetime.datetime.strptime(metadata['end']['timestamp'], '%Y-%m-%dT%H:%M:00')

	else:

		metadata['end']['timestamp'] = metadata['start']['timestamp'] + datetime.timedelta(hours=1)

		metadata['end']['date'] = metadata['end']['timestamp'].strftime('%Y-%m-%d')
		metadata['end']['time'] = metadata['end']['timestamp'].strftime('%H:%M:00')


	#remove temporaly keys 
	del metadata['date']
	del metadata['date-end']

	return metadata


def find_place_id(city,place):

	city = city.replace("-", "")

	path = os.path.join(ROOT_DIR,"_data",city,PLACES_FILE)

	if not os.path.exists(path):
		return place

	places_file = ""
	with open(path, encoding="utf-8") as tmp:
		if YAML:
			places_file = tmp.read()
		else:
			places_file = tmp.readlines()

	if YAML:
		yaml_doc = yaml.load(places_file)

		for place_id in yaml_doc:
			if place_id == place:
				return yaml_doc[place_id]['nombre']
	else:
		name = ""
		found = False
		for line in yaml_doc:
		    
			if line == place + ":":
				found = True

			if " nombre: " in line and found == True:
				name = line.replace("nombre:", "").strip().replace("'","")
				break

		if found:
			return name

	return place 


def create_post_schedule(start_date, end_date):
	"""Finds the schedule for posting the event
	
	Args:
	    start_date (str): when the event starts (YYYY-MM-DD)
	    end_date (str): when the event ends (YYYY-MM-DD)
	
	Returns:
	    LIST: list of dates - times
	"""

	random_minute = str(random.randrange(1,59))
	post_schedule = list() #tuples: date,time

	#use the start date as the finish date. We don't want courses and the like 
	#(that span multiple days) into the calendar
	try:
		date_start = datetime.datetime.strptime(start_date, '%Y-%m-%d') - datetime.timedelta(days=DAYS_BEFORE)
	except TypeError: 
		date_start = start_date - datetime.timedelta(days=DAYS_BEFORE)

	if len(random_minute) == 1 and not random_minute.startswith("0"):
		random_minute = "0" + random_minute
	
	for hour in HOUR_SCHEDULE:
		tmp_start = date_start.strftime('%Y-%m-%d') + "T" + hour + ":" + random_minute + ":00-03:00"

		# as we use recurrence, must use the endtime of the first instance! 
		#    read: https://developers.google.com/google-apps/calendar/v3/reference/events/insert
		tmp_duration = int(random_minute) + 5
		if tmp_duration > 59: 
			tmp_duration = 59
		
		tmp_end = date_start.strftime('%Y-%m-%d') + "T" + hour + ":" + str(tmp_duration) + ":00-03:00"

		post_schedule.append((tmp_start,tmp_end))

	return post_schedule

	'''

	#how many days in between, counts start date as 1
	days_between = (date_end + datetime.timedelta(days=1) - date_start).days

	for i in range(days_between):
		for hour in HOUR_SCHEDULE:
		    tmp = date_start + datetime.timedelta(days=i)

			post_schedule.append(
				(tmp.strftime('%Y-%m-%d')), 
				hour + ":" + random_minute
				)

	'''

def update_processed_file(list_files):
    """Updates the processed posts file.
    
    Args:
        list_files (list): list of paths/strings
    """

	#just dirtify it
    with open(PROCESSED_POSTS_FILE,'a',encoding="utf-8") as tmp:
    	tmp.write("\n" + "\n".join(list_files))








def searchEvent(query_text):

	event_list = []

	work = useService('calendar').events(
    	).list(calendarId=CALENDAR_ID,
             #timeMin=start.isoformat() if start else None,
             #timeMax=end.isoformat() if end else None,
             q=query_text,
             singleEvents=True)
	events = executeCall(work)

	if not events['items']:
		return False 

	if len(events['items']) == 1:
		return events['items'][0]['id']

	# if we have more than one event, add to a list and then ask the user
	# which one is the correct
	for event in events['items']:

		event_list.append(
				(event['summary'], event['id'])
			)

	print (" found many entries. please indicate which one you want. ")
	print (" type none if it's not any of the following. ")

	for i, item in enumerate(event_list):
		print(" " + str(i + 1) + ": " + item[0])

	answer = ""
	while not answer or (int(answer) > len(event_list)):
		answer = input("I pick: ")

		if answer.lower() == "none":
			return False 

		try:
			answer = int(answer)
		except ValueError:
			answer = ""

	return event_list[answer - 1][1]


def edit_event():

	query_text = ""
	new_date = ""
	new_description = ""
	new_summary = ""
	
	while not query_text:
		query_text = input(" Event to search for: ")

	result = searchEvent(query_text)

	if not result:
		print (" event not found ")
		exit()

	service = useService("calendar")

	#get the event data
	event = service.events().get(calendarId=CALENDAR_ID, eventId=result).execute()

	what_to_update = ""

	print(" What do you want to update? ")
	print(" s: start date ")
	print(" e: end date ")
	print(" t: title ")
	print(" l: location ")

	while not what_to_update or what_to_update not in ("s","e","t","l"):
		what_to_update = input(": ")









processed_posts = list()


# start
if __name__ == '__main__':

	print (" initiating ... " + PROCESSED_POSTS_FILE)


	tmp = get_processed_file()
	if tmp:
		processed_posts = get_processed_file()
		tmp = ""

	# ge today's date (only)
	today_date = datetime.datetime.today()
		# I don't know what i'm doing but it works
	today_date = today_date.isoformat(sep=' ').split()[0]
	today_date = datetime.datetime.strptime(today_date, '%Y-%m-%d')


	for ciudad in CITIES:
		print (" \n scanning: " + ciudad)
		current_folder = os.path.join(ROOT_DIR, ciudad, POST_FOLDER)

		for root,subdir,files in os.walk(current_folder):
			
			for archivo in files:
			
				if archivo.startswith("_"):
					continue

				#filename = os.path.basename(path) #get filename from path

				# prevent new line so we can print on same line later
				print ("\n Processing: " + archivo, end="") 

				file_path = os.path.join(root,archivo)
				#filename is YYYY-MM-DD-slug.md
				file_date = "-".join(archivo.split("-")[0:3])

				if file_date.split("-")[0] == "2015":
					# Sorry, we dont want the old ones
					continue		
							
				file_line_processed = PROCESSED_POSTS_FILE_LINE.format(ciudad=ciudad,filename=archivo)



				file_date = datetime.datetime.strptime(file_date, '%Y-%m-%d')


				if file_date < today_date:
					print (" ... old. skip", end="")
					continue
			
				if file_line_processed in processed_posts:
					print (" ... already proccesed. skip", end="")
					continue

				print() #print so we can use newlines for next messages

				print ("    building: " + file_line_processed)

				result = process_post(file_path, ciudad)

				# add file to processed file-list
				FILES_FOR_PROCESSED_LIST.append(file_line_processed)

		print ("\n\n -------------------------------")

	print (" updating proccesed file list...")
	if len(FILES_FOR_PROCESSED_LIST) > 0:
		update_processed_file(FILES_FOR_PROCESSED_LIST)


	print ( "\n finished! ")


#listEvents()

