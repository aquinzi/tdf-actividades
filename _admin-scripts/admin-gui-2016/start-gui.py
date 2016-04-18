# -*- coding: utf-8 -*- 

from __future__ import unicode_literals

# GUI stuff
import wx  # gui framework
import gui_formbuilder # where the our gui it's declared

# Other libs 
import os
import datetime
import string  #to clean filename
import codecs #allow python 2.7 to save with UTF

import ConfigParser #read config.ini


# ===========================
# ====== configuration ======

# load from config file
CONFIG = ConfigParser.ConfigParser()
CONFIG.read('config.ini')

	# create a dictionary from it (easier to manage)
	# although we can avoid it and just use: config.get('paths', 'post_folder')
	# 
	# use the proper method.
'''
CONFIG = dict()
for section in config_file.sections():
	CONFIG[section] = dict()

	for key, value in config_file.items(section):
		CONFIG[section][key] = value

if "," in CONFIG['paths']['allowed_extensions']:
	tmp = CONFIG['paths']['allowed_extensions'].split(",")
	CONFIG['paths']['allowed_extensions'] = tuple(tmp)
'''

# 	minor refinements for the settings
if "," in CONFIG.get('paths', 'allowed_extensions'):
	tmp = CONFIG.get('paths', 'allowed_extensions').split(",")
	CONFIG.set('paths', 'allowed_extensions',tuple(tmp))

tmp = CONFIG.get('paths', 'event_save_path')
tmp = tmp.replace("$filename$",CONFIG.get('paths', 'event_save_filename'))
CONFIG.set('paths', 'event_save_path', tmp)

tmp = CONFIG.get('paths', 'tag_save_path')
tmp = tmp.replace("$filename$",CONFIG.get('paths', 'tag_filename'))
CONFIG.set('paths', 'tag_save_path', tmp)


EVENT_FILE_TMP = ""
tmp = CONFIG.get('paths', 'event_tpl')
tmp = tmp.replace("$admin_folder$", os.getcwd())
if os.path.exists(tmp):
	with open(tmp) as f:
		EVENT_FILE_TMP = f.read()
else: 
	print(" Event template file doesnt exist. Exiting. ")
	exit()


TAG_FILE_TMP = ""
tmp = CONFIG.get('paths', 'tag_tpl')
tmp = tmp.replace("$admin_folder$", os.getcwd())
if os.path.exists(tmp):
	with open(tmp) as f:
		TAG_FILE_TMP = f.read()
else: 
	print(" Tag template file doesn't exist. Exiting. ")
	exit()




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

				if filePath.endswith(CONFIG.get('paths', 'allowed_extensions')) and not filename.startswith(CONFIG.get('paths', 'exclude_files_begin_with')):
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


ROOT_FOLDER = os.path.split(os.getcwd())[0] #We're now in a subfolder 
POST_FOLDER = os.path.join(ROOT_FOLDER, CONFIG.get('paths', 'post_folder'))
TAGS_FOLDER = os.path.join(ROOT_FOLDER, CONFIG.get('paths', 'tags_folder'))

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




#inherit from the MainFrame in gui_formbuilder and create EventFrame
#class IndexFrame(gui_formbuilder.index_frame):
class EventFrame(gui_formbuilder.index_frame):

	def __init__(self,parent=None):
		#constructor
		
		#initialize parent class
		gui_formbuilder.index_frame.__init__(self,parent)
		self.Show()

	# Virtual event handlers, overide them in your derived class
	def show_eventAdd( self, event ):
		window = eventoAdd_frame(self)
		window.Show()

	def show_datesAvanced( self, event ):
		show_window(self, "fechas_avanzado")

	def show_placeSelect( self, event ):
		show_window(self, "lugar_seleccion")
	
	def show_tagsSelect( self, event ):
		show_window(self, "tags_seleccion")
	
	def show_peopleSelect( self, event ):
		show_window(self, "personas_seleccion")

	def show_generateShortURL( self, event ):
		show_window(self, "generar_shorturl")

	def show_lugarAdd( self, event ):
		window = lugarAdd_frame(self)
		window.Show()

#class EventFrame(gui_formbuilder.eventoAdd_frame):
class eventoAdd_frame ( gui_formbuilder.eventoAdd_frame ):
	def __init__(self,parent=None):
		gui_formbuilder.eventoAdd_frame.__init__(self,parent)
		self.Show()

	def clean_form( self, event ):

		data_entered = False

		if self.txtTitle.GetValue().strip():
			data_entered = True
		elif self.lstSchedule.GetCount() > 0:
			data_entered = True
		elif self.lblLocationSelected.GetValue():
			data_entered = True
		elif self.txtPostID.GetValue().strip():
			data_entered = True

		if data_entered:
			answer = showMessage(self,"warning", "Hay datos escritos. ¿Quiere borrar?", buttons="yesno_n")
			if answer == wx.ID_YES:
				form_default_values(self, "add_event")


	def dismiss_form( self, event ):
		self.Destroy()
	
	def show_placeSelect( self, event ):
		show_window(self, "lugar_seleccion")
	
	def show_tagsSelect( self, event ):
		show_window(self, "tags_seleccion")
	
	def show_peopleSelect( self, event ):
		show_window(self, "personas_seleccion")



	def date_deleteselected( self, event ):
		itemsSelected = self.lstSchedule.GetSelections()
		if (itemsSelected):
			for item in itemsSelected:
				self.lstSchedule.Delete(item)






class seleccionLugar_dialog ( gui_formbuilder.seleccionLugar_dialog ):
	def __init__(self,parent=None):
		gui_formbuilder.seleccionLugar_dialog.__init__(self,parent)
		self.Show()

class seleccionTags_dialog ( gui_formbuilder.seleccionTags_dialog ):
	def __init__(self,parent=None):
		gui_formbuilder.seleccionTags_dialog.__init__(self,parent)
		self.Show()

class seleccionPersonas_dialog ( gui_formbuilder.seleccionPersonas_dialog ):
	def __init__(self,parent=None):
		gui_formbuilder.seleccionPersonas_dialog.__init__(self,parent)
		self.Show()

class generarURLcorta_dialog ( gui_formbuilder.generarURLcorta_dialog  ):
	def __init__(self,parent=None):
		gui_formbuilder.generarURLcorta_dialog.__init__(self,parent)
		self.Show()



def show_window(the_instance, which_window):
	'''easy way to duplicate the call to show the windows/dialogs from multiple places'''

	if which_window == "fechas_avanzado":
		window = fechasAvanzado_dialog(the_instance)
	elif which_window == "lugar_seleccion":
		window = seleccionLugar_dialog(the_instance)
	elif which_window == "tags_seleccion":
		window = seleccionTags_dialog(the_instance)
	elif which_window == "personas_seleccion":
		window = seleccionPersonas_dialog(the_instance)
	elif which_window == "generar_shorturl":
		window = generarURLcorta_dialog(the_instance)
	else:
		return

	window.ShowModal()
	window.Destroy() 	

def form_default_values(the_instance, which_window):
	'''Default values of controls'''



	if which_window == "add_event":
		the_instance.txtTitle.SetValue('')
		the_instance.lstSchedule.Clear()
		#the_instance.datepickerEvent.SetValue(wx.DefaultDateTime)
		the_instance.txtTimeStart.SetValue('hh.mm')
		the_instance.txtTimeEnd.SetValue('hh.mm')
		the_instance.cboCity.SetSelection(0)
		the_instance.lblLocationSelected.SetLabel('')
		the_instance.txtPostID.SetValue('')
		the_instance.lblURLfinal.SetLabel('')
		the_instance.lblTagsSelected.SetLabel('')
		the_instance.lblPeopleSelected.SetLabel('')
		the_instance.txtSource.SetValue('')
		the_instance.txtDescription.SetValue('')


		the_instance.txtTitle.SetFocus()

	else: return

def showMessage(the_instance, type_msg, msg, title="", buttons=""):
	
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
	
	if type_msg == "error":
		style = style | wx.ICON_ERROR
	if type_msg == "info":
		style = style | wx.ICON_ASTERISK
	if type_msg == "warning":
		style = style | wx.ICON_WARNING

	dlg = wx.MessageDialog(parent=None, message=msg, 
		caption=title, style=style)

	return dlg.ShowModal()


if __name__ == '__main__':
	#create an app. False = no stdin/stdout
	app = wx.App(False)

	#frame = EventFrame()
	frame = eventoAdd_frame()
	app.MainLoop()
