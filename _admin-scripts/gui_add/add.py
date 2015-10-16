# -*- coding: utf-8 -*- 

from __future__ import unicode_literals

# GUI stuff
import wx  # gui framework
import gui # where the our gui it's declared

# Other libs 
import os
import datetime
import string  #to clean filename
import codecs #allow python 2.7 to save with UTF


# ===========================
# ====== configuration ======

POST_FOLDER = "_posts"
TAGS_FOLDER = 'tag'

EVENT_FILE_TMP_NO_TIME = "\nno-time-{type}: True"

EVENT_FILE_TMP = '''---
layout: event 
title: {title}
date: {date}{notime_start}
date-end: {date_end}{notime_end}
category: {category}
location: {location}
tags: [{tags}]
source: {source}
---

{description}
'''

# As of 27/08/2015 remember to save it as /tag/{tag}.html
TAG_FILE_TMP = '''---
tag: {tag}
---
'''

# ==== end configuration ====
# ===========================


def files_get(path, folders=False, only_filename=False):
	''' Get a list of files in dir. Returns list

	:param:folders to get folders names. Default: false
	:return:list list of files
	'''
	
	theFiles = list()
	for root, subFolders, files in os.walk(path):
		if folders:
			for subfolder in subFolders:
				theFiles.append(subfolder)
		else:
			for filename in files:
				filePath = os.path.join(root, filename)

				if filePath.endswith(("md", "html")) and not filename.startswith("_"):
					if only_filename:
						theFiles.append(filename.split(".")[0])
					else:
						theFiles.append(filePath)

	return theFiles

	
def clean_filename(s):
	'''Removes invalid chars from the string, making it 
	safe for a filename

	:param:s string the string to clean 
	'''
	# from: http://stackoverflow.com/a/295146
	 
	valid_chars = "- _%s%s" % (string.ascii_letters,string.digits)

	return "".join(char for char in s if char in valid_chars)

	
def remove_accentedLetters(s):
	'''Converts accented letters to proper ascii 
	:return: string 
	'''

	return s.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')


def save_file(path, filename, text):
	'''Saves the text to path

	:param:path string the path to save to 
	:param:filename string the filename (with extension)
	:param:text string the content
	'''

	if not os.path.exists(path):
		path_mkdir(path)

	path = os.path.join(path, filename)

	with codecs.open(path, 'w', encoding="utf-8-sig") as output_file:
			output_file.write(text)	
	
	
def path_mkdir(path):
	""" make tree dirs from path """

	try:
		os.makedirs(path)
	except OSError:
		pass
		
		
#ROOT_FOLDER = os.getcwd()
ROOT_FOLDER = os.path.split(os.getcwd())[0] #We're now in a subfolder 
POST_FOLDER = os.path.join(ROOT_FOLDER, POST_FOLDER)
TAGS_FOLDER = os.path.join(ROOT_FOLDER, TAGS_FOLDER)

TAGS = list()
TAGS = files_get(TAGS_FOLDER, only_filename=True)	

'''
https://github.com/wxWidgets/wxPython/blob/master/demo/TimeCtrl.py
add checkboxes with code: http://userpages.umbc.edu/~dhood2/courses/cmsc433/spring2007/?section=Notes&topic=Python&notes=13
http://www.python-izm.com/contents/gui/radiobox.shtml (japones)
'''

# converting dates python <-> wxdate 
# from http://www.blog.pythonlibrary.org/2014/08/27/wxpython-converting-wx-datetime-python-datetime/
def pydate2wxdate(date):
     assert isinstance(date, (datetime.datetime, datetime.date))
     tt = date.timetuple()
     dmy = (tt[2], tt[1]-1, tt[0])
     return wx.DateTimeFromDMY(*dmy)
 
def wxdate2pydate(date):
	'''Converts wxdate to python date (YYYY-MM-DD)'''
	
	assert isinstance(date, wx.DateTime)
	if date.IsValid():
		ymd = map(int, date.FormatISODate().split('-'))
		return datetime.date(*ymd)
	else:
		return None


#inherit from the MainFrame in gui and create EventFrame
class EventFrame(gui.MainFrame):

	previous_event = dict()

	def __init__(self,parent=None):
		#constructor
		
		#initialize parent class
		gui.MainFrame.__init__(self,parent, title="Añadir evento")
		self.reloadTags(self)

		self.Show()

	# event handlers
	def clean_form(self,event):
		self.default_values()

		self.title.SetFocus()
			
	def save_form( self, event ):

		form_data = {
			'title': self.title.GetValue().strip()
			, 'datetime': (
				wxdate2pydate(self.dateStart.GetValue()).isoformat()
				, self.timeStart.GetValue()
				)
			, 'datetime_end': (
				wxdate2pydate(self.dateEnd.GetValue()).isoformat()
				, self.timeEnd.GetValue()
				)
			, 'category': self.city.GetStringSelection()
			, 'tags': self.tags.GetValue().strip()
			, 'location': self.location.GetValue().strip()
			, 'source': self.source.GetValue().strip()
			, 'description': self.description.GetValue().strip()
		}

		form_data = self._check_form_data(form_data)

		if not form_data:
			return




		# ---- Data preparation
		
		# Convert event/post dates
		
		tmp = [form_data['datetime'][0] + " " + form_data['datetime'][1] , ""]

		if self.timeStart_dontinclude.GetValue():
			tmp[0] = form_data['datetime'][0]
			tmp[1] = EVENT_FILE_TMP_NO_TIME.format(type='start')

		form_data['date'] = tmp[0] 
		form_data['notime_start'] = tmp[1]
		
		tmp = [form_data['datetime_end'][0] + " " + form_data['datetime_end'][1] , ""]

		if self.timeEnd_dontinclude.GetValue():
			tmp[0] = form_data['datetime_end'][0]
			tmp[1] = EVENT_FILE_TMP_NO_TIME.format(type='end')

		form_data['date_end'] = tmp[0]
		form_data['notime_end'] = tmp[1]
		
		if form_data['tags']:
			form_data['tags'] = ",".join(form_data['tags'].split())
		
		# convert to proper city/category name
		tmp = ""

		if form_data['category'] == "Río Grande":
			tmp = "rio-grande"
		else:
			tmp = form_data['category'].lower()
			
		form_data['category'] = tmp 
		

		# ---- Ready to save 
		
		final_event_filename = ""
		final_event          = ""
		
		final_event_filename = form_data['datetime'][0] + "-" + form_data["title"]
		final_event_filename = clean_filename(final_event_filename)  + ".md"
	

		# check file existance
		write_file = True 
		path       = os.path.join(POST_FOLDER,form_data['category'])
		path_file  = os.path.join(path, final_event_filename)

		if os.path.exists(path_file):
			answer = self.showMessage("error"
				, "Archivo ({}) ya existe. ¿Desea sobreescribir?".format(path_file)
				, buttons="yesno_y")

			if answer == wx.ID_NO:
				write_file = False 

		if not write_file:
			return

		final_event = EVENT_FILE_TMP.format(**form_data)
		save_file(path, final_event_filename, final_event)

		# save previous event, delete date mess
		del form_data['date']
		del form_data['date_end']	

		# to avoid using copy.deepcopy()
		self.previous_event = {}

		for k,v in form_data.items():
			self.previous_event[k] = v

		self.showMessage("info", "Evento guardado")
		
		# ---- save new tags
		if form_data["tags"]:
			global TAGS 

			global_tags = set(TAGS)
			event_tags = form_data["tags"].split(",")
			event_tags = set([remove_accentedLetters(x) for x in event_tags])

			tmp = event_tags - global_tags  # in new tag string but not in old list
			tmp = list(tmp)
			modify_this_tags = self.selectTagsModify(tmp)

			for index, tag in enumerate(tmp):
				tag_slug = tag 
				tag_name = tag 

				if index in modify_this_tags:
					tag_name = self.modifyTag(tag)

				tmp_tag_filename = tag_slug + ".html"
				tmp_tag_file = TAG_FILE_TMP.format(tag=tag_name)
				#path_mkdir(os.path.join(TAGS_FOLDER, event_tag))
				#save_file(os.path.join(TAGS_FOLDER,event_tag), tmp_tag_filename, tmp_tag_file)
				save_file(TAGS_FOLDER, tmp_tag_filename, tmp_tag_file)

			if tmp:
				self.showMessage("info", "Nuevas etiquetas añadidas/guardadas:\n" + "\n".join(tmp))
				
				TAGS.extend(tmp)
				self.reloadTags(self)
				
		self.clean_form(self)
		self.toolbar.EnableTool(self.TOOLBAR_ITEMS['previous'].id, True)
		
	def load_previous(self,event):
		''' Load previous event information'''
		
		if self.previous_event:
			self.set_form_data(self.previous_event)
			self.showMessage("info", "Evento anterior cargado")

	def load_scriptInfo(self,event):
		'''Load some script variables and stuff. For fun '''

		final_str = """
		Running on: 
		       {getcwd}
		Post folder: 
		       {post_folder}
		Tag folder:  
		       {tag_folder}

		Tags:
		{tags}

		Event template: 
		{event_tpl}
		""".format(
			getcwd = os.getcwd(), tags=",".join(TAGS)
			, post_folder=POST_FOLDER , tag_folder=TAGS_FOLDER
			, event_tpl=EVENT_FILE_TMP 
			)

		#self.showMessage("info",final_str)
		info = wx.AboutDialogInfo()
		info.SetName('TdF actividades')
		info.SetVersion('0.1')
		info.SetDescription(final_str)
		#info.SetWebSite('http://www.zetcode.com')
		#info.SetIcon(wx.Icon('hunter.png', wx.BITMAP_TYPE_PNG))
		#info.SetCopyright('(C) 2007 - 2014 Jan Bodnar')
		#info.SetLicence(licence_str)
		#info.AddDeveloper('Jan Bodnar')
		#info.AddDocWriter('Jan Bodnar')
		#info.AddArtist('The Tango crew')
		#info.AddTranslator('Jan Bodnar')
		
		wx.AboutBox(info)



	# other functions

	def reloadTags(self, event):
		'''Reload the tags from main list in the autocomplete box'''

		self.tags.all_candidates = TAGS
		self.Layout()

	def _check_form_data (self, form_data):
		# Check empty fields
		error_data = ""

		if not form_data['title']:
			error_data += "\nTítulo"
		
		if not form_data['location']:
			error_data += "\nLugar"
			
		if error_data:
			error_data = "Hay información requerida en blanco:\n" + error_data

		# Check dates and times 
		tmp = False 
		if form_data['datetime'][0] > form_data['datetime_end'][0]:
			tmp = True 
			
		if (form_data['datetime'][0] == form_data['datetime_end'][0]) and (
			form_data['datetime'][1] > form_data['datetime_end'][1] ):
				tmp = True 
		
		if tmp:
			error_data += "\n\nHay fechas/horas incompatibles"
		
		if error_data:
			self.showMessage("warning", error_data)
			return False
		
		return form_data 
	
	def showMessage(self, type_msg, msg, title="", buttons=""):
		
		style = wx.OK

		if not title:
			if type_msg == "error":   title = "Error"
			if type_msg == "info":    title = "Información"
			if type_msg == "warning": title = "Atención"
	
		if buttons == "yesno_y":
			style = wx.YES_NO|wx.YES_DEFAULT
		elif buttons == "yesno_n":
			style = wx.YES_NO|wx.NO_DEFAULT
		elif buttons == "okcancel":
			style = wx.OK|wx.CANCEL

		#other buttons: wx.HELP wx.CANCEL_DEFAULT  wx.OK_DEFAULT
		
		if type == "error":
			style = style | wx.ICON_ERROR
		if type == "info":
			style = style | wx.ICON_ASTERISK
		if type == "warning":
			style = style | wx.ICON_WARNING

		dlg = wx.MessageDialog(parent=None, message=msg, 
			caption=title, style=style)

		return dlg.ShowModal()
		
	def selectTagsModify(self, tags):
		'''Select the tags to modify.
		:return: list of original indexes
		'''


		dlg = wx.MultiChoiceDialog( self, 
		                          "Seleccionar tags a editar",
		                          "Nuevos tags", tags)
		selections = list()

		if (dlg.ShowModal() == wx.ID_OK):
		   selections = dlg.GetSelections()
		   #strings = [tags[x] for x in selections]
		
		dlg.Destroy()

		return selections

	def modifyTag(self, tag):
		'''modify the name of the tag 
		:return:string 
		'''

		dlg_change = wx.TextEntryDialog(
		       self, 'Cambiar el nombre de: ' + tag,
		       'Nuevo nombre', tag)

		new_name = ""

		if dlg_change.ShowModal() == wx.ID_OK:
			if dlg_change.GetValue():
				new_name = dlg_change.GetValue()
			else:
				new_name = tag
			
		dlg_change.Destroy()

		return new_name



		
if __name__ == '__main__':
	#create an app. False = not deteriction stdin/stdout
	app = wx.App(False)

	frame = EventFrame()
	app.MainLoop()
