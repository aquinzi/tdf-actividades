'''GitHub Issues on the command line

toma user y repo de la configuracion de git

similar a: https://github.com/stephencelis/ghi

los que necesitamos basicos:

[x] list
[x] show
[x] open -> as open title -d descripcion rapida -l labels,labels
	[] opcion para poner milestone number: -m [numero]
[x] close: se edita el issue y cambia el estado. 
	[] Opcional dejar comentario explicando
opcional: color 
[x]opcional: human dates en detalles issue
[x]mejorar login e informacion del repo (usar git)
[] mejor entrada de password? o por lo menos guardarla en un temp 


mas adelante:
dejar un comentario en issue (mas que nada para cuando se cierra)
editar
listar milestones con sus issues https://developer.github.com/v3/issues/milestones/
manejar labels? https://developer.github.com/v3/issues/labels/


crear comentario:  POST /repos/:owner/:repo/issues/:number/comments
	requiere body
'''




import requests
import json
import sys, os
#import argparse #less complicated than sys when opening an issue



COMMANDS_ACCEPTED = ("list", "show", "open", "close")


def pretty_date(date_time):
	"""
	Get a ISO date (string YYYY-MM-DDTHH:MM:SS) and return a
	pretty string like 'an hour ago', 'Yesterday', '3 months ago',
	'just now', etc

	modified from: http://stackoverflow.com/questions/1551382/user-friendly-time-format-in-python/
	"""

	if "Z" in date_time:
		date_time = date_time.replace("Z", "")

	#from datetime import datetime
	import datetime
	now = datetime.datetime.now()

	old_date = datetime.datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S")
	old_date = old_date + datetime.timedelta(hours=-3)

	diff = now - old_date

	second_diff = diff.seconds
	day_diff    = diff.days

	tpl_string = "hace {} {}" # num, unidad (ej: 2 horas)

	if day_diff <= 0:
		if second_diff < 10:
			return "recien"
		if second_diff < 60:
			return tpl_string.format(int(second_diff),"segundos")
		if second_diff < 120:
			return tpl_string.format("un","minuto")
		if second_diff < 3600:
			return tpl_string.format(int(second_diff / 60),"minutos")
		if second_diff < 7200:
			return tpl_string.format("una","hora")
		if second_diff < 86400:
			return tpl_string.format(int(second_diff / 3600),"horas")

	if day_diff == 1:
		return "ayer"
	if day_diff < 7:
			return tpl_string.format(int(day_diff),"dias")
	if day_diff < 31:
			return tpl_string.format(int(day_diff / 7),"semanas")
	if day_diff < 365:
			return tpl_string.format(int(day_diff / 30),"meses")
		
	#return str(day_diff / 365) + " years ago"
	# if it's more than 12 months, just return normal date cleaned
	return old_date.strftime("%Y-%m-%d %H:%M")


def get_git_config():

	import configparser

	config = configparser.ConfigParser()
	config.read(os.path.join(os.getcwd(),".git","config"))

	user  = config['user']['name']
	repo = config['remote "origin"']['url']
	repo = repo.replace(".git", "").replace("https://github.com/", "")

	return user, repo


def list_issues ():

	url = GH_BASE_URL + "/issues"

	r = requests.get(url)

	if(r.ok):
		repoItem = json.loads(r.text or r.content)

		for issue in repoItem:
			labels = ""
			for label in issue['labels']:
				labels += " #" + label['name']

			milestone = ""
			if issue['milestone']:
				milestone = " milestone: " + issue['milestone']['title']
		

			print ("  {number}: {title} {labels}{milestone} ({date})".format(
				number=issue['number']
				, labels=labels
				, title=issue['title']
				, milestone=milestone
				, date=pretty_date(issue['created_at'])
				)
			)

def get_issue(issue_id):

	url = GH_BASE_URL + "/issues/" + issue_id

	r = requests.get(url)

	if(r.ok):
		repoItem = json.loads(r.text or r.content)

		print("\n #{}: {}".format(repoItem['number'],repoItem['title']))

		labels = ""
		for label in repoItem['labels']:
			labels += " #" + label['name']

		print (" Abierto por @{} en {}. {}".format(
			repoItem['user']['login'], 
			pretty_date(repoItem['created_at']),
			labels
			)
		)

		if repoItem['milestone']:
			print (" Milestone: {} (number: {})".format(
				repoItem['milestone']['title'], 
				repoItem['milestone']['number']
				)
			)

		print (" " + repoItem['body'])


def get_password():
	
	login = input(" password (not stored): ")
	
	if not login:
		exit()

	return login.strip()


def open_issue(data):
	
	url = GH_BASE_URL + '/issues'

	original_command = "".join(data) #quick bugfix, shouldn't be doing this
	title = list()
	description = list()
	labels = list()

	# get title
	 
	if not " -d " and not " -l " in original_command:
		title = original_command
	else:
	 	# do you think you're cool for not using argsparse?
	 	# this could've been easier
	 	
		tmp = original_command.split()

		for piece in tmp:
			if piece not in ("-d", "-l"):
				title.append(piece)
			else:
				break

		title = "".join(title)

		# remove title (the most important)
		original_command = original_command.replace(title, "")

		#get the optional data 
		tmp = original_command.split()
		#labels are easier:
		try:
			labels = tmp[tmp.index("-l") + 1]
			original_command = original_command.replace("-l " + labels, "")
			labels = labels.split(",")
		except ValueError:
			pass

		try:
			tmp.index("-d")
		except ValueError:
			pass
		else:
			start_index = tmp.index("-d") + 1 
			for piece in tmp[start_index:len(tmp)]:
				description.append(piece)

	description = "".join(description)

	details = {'title': title}

	if len(labels) > 0:
		details['labels'] = labels

	if description:
		details['body'] = description
	
	password = get_password()

	r = requests.post(url, auth=(GH_USER, password), json=details)
	repoItem = json.loads(r.text or r.content)

	if(r.ok):
		print (" issue created!")
	else:
		print (repoItem)


def edit_issue(issue_id, title="", body="", state="", milestone=0, labels=[]):
	# unpack a dictionary which holds the data with edit_issue(**dictionary)
	
	url = GH_BASE_URL + '/issues/' + issue_id

	details = {
		'title': title, 
		'body': description,
		'labels': labels
		}

	password = get_password()

	r = requests.post(url, auth=(GH_USER, password), json=details)
	#repoItem = json.loads(r.text or r.content)

	if (r.ok):
		print (" issue edited!")


def close_issue(issue_id):

	# we could use edit_issue but keep it like this. 
	
	url = GH_BASE_URL + '/issues/' + issue_id

	details = {'state': "close"}

	password = get_password()

	r = requests.post(url, auth=(GH_USER, password), json=details)	 
	
	if (r.ok):
		print (" issue closed. ")
	else:
		print (" error ocurred trying to close issue")



GH_USER, GH_OWNER_REPO = get_git_config()
GH_BASE_URL = "https://api.github.com/repos/" + GH_OWNER_REPO

args = sys.argv[1:]

if not args:
	args.append("list")


if args[0]:
	args[0] = args[0].lower()

	if not args[0] in COMMANDS_ACCEPTED:
		print (" comando no aceptado. Los validos: " + " ".join(COMMANDS_ACCEPTED))
		exit()

	if args[0] in ("show", "close"):
		if len(args) < 2:
			print (" Se necesita un id")
			exit()

		try:
			int(args[1])
		except ValueError:
			print (" Se necesita un numero")
			exit()

	if args[0] == "open":
		if len(args) < 2:
			print (" Se necesita por lo menos un titulo")
			exit()




if args[0] == "list":
	list_issues()
elif args[0] == "show":
	get_issue(args[1])
elif args[0] == "open":
	open_issue(args[1:])
elif args[0] == "open":
	open_issue(args[1:])
elif args[0] == "close":
	close_issue(args[1])
