# -*- coding: utf-8 -*- 

from __future__ import unicode_literals

# GUI stuff
import wx  # gui framework
import gui_formbuilder # where the our gui it's declared


#inherit from the MainFrame in gui and create EventFrame
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

	def show_lugarAdd( self, event ):
		window = lugarAdd_frame(self)
		window.Show()


class eventoAdd_frame ( gui_formbuilder.eventoAdd_frame ):
	def __init__(self,parent=None):
		gui_formbuilder.eventoAdd_frame.__init__(self,parent)
		self.Show()

	# Virtual event handlers, overide them in your derived class
	def show_datesAvanced( self, event ):
		show_window(self, "fechas_avanzado")
	
	def show_placeSelect( self, event ):
		show_window(self, "lugar_seleccion")
	
	def show_tagsSelect( self, event ):
		show_window(self, "tags_seleccion")
	
	def show_peopleSelect( self, event ):
		show_window(self, "personas_seleccion")


class lugarAdd_frame ( gui_formbuilder.lugarAdd_frame ):
	def __init__(self,parent=None):
		gui_formbuilder.lugarAdd_frame.__init__(self,parent)
		self.Show()



class fechasAvanzado_dialog ( gui_formbuilder.fechasAvanzado_dialog ):
	def __init__(self,parent=None):
		gui_formbuilder.fechasAvanzado_dialog.__init__(self,parent)
		self.Show()

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
	else:
		return

	window.ShowModal()
	window.Destroy() 	



if __name__ == '__main__':
	#create an app. False = not deteriction stdin/stdout
	app = wx.App(False)

	frame = EventFrame()
	app.MainLoop()
