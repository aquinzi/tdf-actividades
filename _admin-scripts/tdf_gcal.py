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


''' if we dont feel like using google API libs.: 

	#code from https://gist.github.com/ymotongpoo/1907281 (and some transltions in: https://gist.github.com/joemontibello/1a17e3d27955897d53b2
		)
	import requests, json, webbrowser
	import urllib.parse #in python2: from urllib import urlencode

	#set variables needed for API access:
	client_id = "CLIENT_ID"
	client_secret = "CLIENT_SECRET"
	redirect_uri = "urn:ietf:wg:oauth:2.0:oob" #https%3A%2F%2Foauth2-login-demo.appspot.com%2Fcode&
	#redirect_uri = "http://localhost/" # redirects to http://localhost/?code=4/E6MdDZWeEFcCubmzI63ip5d_iX8XUzmaBopDcs18Pko#
	base_url = "https://accounts.google.com/o/oauth2/" 
	authorization_code = ""
	access_token = ""

	google_auth_url = "https://accounts.google.com/o/oauth2/auth"

	authorization_code_req = {
		"response_type": "code",
		"client_id": client_id,
		"redirect_uri": redirect_uri,
		"scope": "https://www.googleapis.com/auth/calendar"
	}

	r = requests.get(google_auth_url, params=authorization_code_req, allow_redirects=False)

	url = r.url #user must enter this url to accept auth

	print ("Opening the following URL in default browser. Copy the auth code. " + url)

	# Open URL in a new tab, if a browser window is already open.
	webbrowser.open_new_tab(url)

	authorization_code = input("\nAuthorization Code >>> ")


	# Retrieving authorization_code from authorization API.

	def retrieve_authorization_code():
		authorization_code_req = {
			"response_type": "code",
			"client_id": client_id,
			"redirect_uri": redirect_uri,
			"scope": ("https://www.googleapis.com/auth/calendar")
		}
		data = urllib.parse.urlencode(authorization_code_req)
		#data = data.encode('utf-8') # data should be bytes

		r = requests.get(base_url + "auth?" + data, allow_redirects=False)

		print ("Open the following URL, please enter the string that is displayed in the access after approval.")
		url = r.headers.get('location')
		Popen(["open", url])

		authorization_code = input("\nAuthorization Code >>> ")
		return authorization_code


	#Retrieving access_token and refresh_token from Token API.

	def retrieve_tokens(authorization_code):
		access_token_req = {
			"code" : authorization_code,
			"client_id" : client_id,
			"client_secret" : client_secret,
			"redirect_uri" : redirect_uri,
			"grant_type": "authorization_code",
		}
		data = urllib.parse.urlencode(access_token_req)
		#data = data.encode('utf-8') # data should be bytes
		content_length=len(data)
		access_token_req['content-length'] = str(content_length)

		r = requests.post(base_url + "token", data=access_token_req)
		data = json.loads(r.text)
		return data


	def get_calendar_list():
		global authorization_code
		global access_token

		authorization_code = retrieve_authorization_code()
		tokens = retrieve_tokens(authorization_code)
		access_token = tokens['access_token']
		authorization_header = {"Authorization": "OAuth " + access_token}

		r = requests.get("https://www.googleapis.com/calendar/v3/users/me/calendarList",
		               headers=authorization_header)
		return r.text


	def get_events_list():
		global authorization_code
		global access_token

		data = json.loads(get_calendar_list())

		for calendar in data['items']:
			calendar_id = calendar['id']
			print (calendar['summary'])

			if authorization_code == "" or access_token == "":
				authorization_code = retrieve_authorization_code()
				tokens = retrieve_tokens(authorization_code)
				access_token = tokens['access_token']

			authorization_header = {"Authorization": "OAuth " + access_token}
			tmp1 = urllib.parse.quote_plus(calendar_id)
			tmp2 = urllib.parse.quote_plus(api_key)

			url = "https://www.googleapis.com/calendar/v3/calendars/" + tmp1 + "/events?key=" + tmp2
			r = requests.get(url, headers=authorization_header)

			events = json.loads(r.text)
			for event in events['items']:
				print (event.get('summary', '(Event title not set)'))
			
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
DAYS_BEFORE = 3 #How many days before do we start posting the event?

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

	'''mockup of tweet
	#RioGrande #{tag} {titulo lindo} ({dia} de {mes-abbr}, {horas} hs; {lugar}). 

	ifttt ingredients
	Title 								 	The event's title.
	Description 							The event's description.
	Where 									The location where the event takes place.
	Starts 									ej August 23, 2011 at 10:00PM
	Ends 									ej: August 23, 2011 at 11:00PM
	'''
	# so dirty
	gcal_description = "#{city}{tags} {title} ({human_date}{place})"

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

		event = {}
		human_datetime_start = ""
		tags = ""
		city = ""
		place = ""

		if event_data['city'] == "rio-grande":
			city = "RioGrande"
		else:
			city = event_data['city'].title()

		#event['reminders'] = dict()
		#event['reminders']['useDefault'] = False #remove reminder, this is for myself
		event['summary'] = event_data['title']

		event['start'] = {'dateTime': date_time[0], 'timeZone': timezone}

		tmp = datetime.datetime.strptime(date_time[1], '%Y-%m-%dT%H:%M:00-0300')
		event['end'] = {'dateTime': date_time[1], 'timeZone': timezone}
		human_datetime_end = _fecha_humana(tmp) #the real date
		#if all day: {'date': eEnd}
		
		print ("        schedule from {} to daily-until {} ".format(
				date_time[0].replace("T", " ").replace(":00","")
				,date_time[1].replace("T", " ").replace(":00","").replace("-0300", "")
				)
			)
		
		if event_data['location']:
			event['location'] = event_data['location']
			place = ", en " + event_data['location']

		if event_data['tags']:
			tags = " #" + event_data['tags'].replace(",", "#")

		event['description'] = gcal_description.format(
			city=city, tags=tags, title=event['summary']
			, human_date=human_datetime_end, place=place
			)
		
		#use recurrence so we dont have to create daily events within same time
		#event['recurrence'] = ['RRULE:FREQ=DAILY;UNTIL=20151007T193000-03:00']
		tmp_recurrence = date_time[1].replace("-","").replace(":","").replace("0300","-03:00")
		event['recurrence'] = 'RRULE:FREQ=DAILY;UNTIL=' + tmp_recurrence

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


def process_post(path, city):
	"""Process the post
	
	Args:
	    path (str)
	    city (str)
	"""

	print("    Getting metadata... ", end="")
	post_metadata = get_post_metadata(path, city)
	print(" done.")

	#normalize dates. Use YYYY-MM-DDTHH:MM:SS
	try:
		post_metadata['date'] = post_metadata['date'].replace(" ", "T")
	except TypeError:
		pass
	else:
		post_metadata['date'] = post_metadata['date'].replace(" ", "T")

	try:
		if ":" in post_metadata['date']:
			pass
	except TypeError:
		pass
	else:
		post_metadata['date'] += ":00"


	if post_metadata['date-end']:
		try:
			if ":" in post_metadata['date-end']:
				pass
		except TypeError:
			pass
		else:
			post_metadata['date-end'] = post_metadata['date-end'].replace(" ", "T") + ":00"

	else:
		tmp = datetime.datetime.strptime(post_metadata['date'], '%Y-%m-%dT%H:%M:00')
		post_metadata['date-end'] = (tmp + datetime.timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:00')



	print("    Creating post schedule... ", end="")
	post_schedule = create_post_schedule(str(post_metadata['date']), str(post_metadata['date-end']))
	print(" done.")

	# create google calendar event
	print("    Inserting post's schedule in Google Calendar... ")
	scheduleEvent(post_schedule, post_metadata)
	
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
		,'tags':'','shortURL':'', 'location':''
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
					else:
						if tmp_line[1] != "[]":
							metadata['tags'] = tmp_line[1].replace("[", "").replace("]","")

	#check if location has ID, and if it does, find the proper name
	metadata['location'] = find_place_id(city, metadata['location'])

	return metadata


def find_place_id(city,place):

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
	    start_date (str): when the event starts
	    end_date (str): when the event ends
	
	Returns:
	    LIST: list of dates - times
	"""

	random_minute = random.randrange(1,59)
	post_schedule = list() #tuples: date,time

	# find when do we have to start the event publication and
	# when it ends
	
	try:
		date_start = datetime.datetime.strptime(start_date, '%Y-%m-%dT%H:%M:00')
	except ValueError:
		date_start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
	'''
	try:
		date_end   = datetime.datetime.strptime(end_date, '%Y-%m-%dT%H:%M:00')
	except ValueError:
		date_end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
	'''

	#use the start date as the finish date. We don't want courses and the like 
	#(that span multiple days) into the calendar
	date_end = date_start

	date_start = date_start - datetime.timedelta(days=DAYS_BEFORE)

	random_minute = str(random_minute)
	if len(random_minute) == 1 and not random_minute.startswith("0"):
		random_minute = "0" + random_minute
	
	for hour in HOUR_SCHEDULE:
		tmp_start = date_start.strftime('%Y-%m-%d') + "T" + hour + ":" + random_minute + ":00"
		tmp_end = date_end.strftime('%Y-%m-%d') + "T23:59:00-0300"

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
    	tmp.write("\n".join(list_files))


def clean_processed_file():
	"""Filters processed file, deleting old entries. """	

	today = datetime.date.today()

	processed_posts = get_processed_file()

	if not processed_posts:
		print (" there was an error with the processed file. Does it exist?")
		return False

	cleaned_posts = list()

	for row in processed_posts:
		tmp_date = datetime.datetime.strptime(row.split(";")[0], '%Y-%m-%d')

		if tmp_date >= today:
			cleaned_posts.append(row) 

	if len(cleaned_posts) > 0:
		with open(PROCESSED_POSTS_FILE,'w',encoding="utf-8") as tmp:
			tmp.write("\n".join(cleaned_posts))

		print(" Processed file cleaned!")
	else:
		print(" Everything is ok. Processed file not modified. ")


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
	#today_date = datetime.date.today() 
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
				file_line_processed = PROCESSED_POSTS_FILE_LINE.format(ciudad=ciudad,filename=archivo)

				file_date = datetime.datetime.strptime(file_date, '%Y-%m-%d')

				if file_date < today_date:
					print (" ... old. skip", end="")
					continue
			
				if file_line_processed in processed_posts:
					print (" ... already proccesed. skip", end="")
					continue

				print() #print so we can use newlines for next messages

				result = process_post(file_path,ciudad)

				# add file to processed file-list
				FILES_FOR_PROCESSED_LIST.append(file_line_processed)

		print ("\n\n -------------------------------")

	print (" updating proccesed file list...")
	if len(FILES_FOR_PROCESSED_LIST) > 0:
		update_processed_file(FILES_FOR_PROCESSED_LIST)


	print ( "\n finished! ")


#listEvents()

