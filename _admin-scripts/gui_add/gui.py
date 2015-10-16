# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
###########################################################################

from __future__ import unicode_literals
import wx
import wx.xrc
import wx.lib.masked as masked

import datetime
from collections import namedtuple #just for fun

RED_COLOR = "pink" #or light red "#ec6a6a"
NULL_COLOR = wx.NullColour #wx.NullColor doesnt work
BACK_COLOR = wx.SYS_COLOUR_3DLIGHT #continue seting in class #wx.SYS_COLOUR_BTNFACE
LIMIT_TIME_CONTROL = False

TOOLBAR_ITEM = namedtuple('TOOLBAR_ITEM', 'id label tooltip icon')

# TODO: changes the font (yay!) but can seem to resize widget (bummer!)
#self.startTime.SetFont(font1)
# TODO: Must put cities somewhere else, call here (dynamic)


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame (wx.Frame):
	
	# So we can call and access it wherever we want. [key]:(id, label, tooltip, icon ID)
	# Could've used named tuples, but keep it simple 
	# 
	#  bitmap codes from: www.wxpython.org/Phoenix/docs/html/ArtProvider.html#phoenix-title-identifying-art-resources
	TOOLBAR_ITEMS = {
		'save'     : TOOLBAR_ITEM(wx.ID_SAVE, "Guardar", "Ctrl+S", wx.ART_FILE_SAVE_AS) 
		,'previous' : TOOLBAR_ITEM(wx.ID_BACKWARD, "Cargar evento previo", "Ctrl+R", wx.ART_REDO) 
		,'clean'    : TOOLBAR_ITEM(wx.ID_CLEAR, "Limpiar", "Ctrl+N", wx.ART_NEW)  
		,'info'     : TOOLBAR_ITEM(wx.ID_INFO, "Información", "F1", wx.ART_INFORMATION) 

	}
	# clean = new, but as we clear the form after we save it, let's call it like that	

	def __init__(self, parent, title):
		wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=title, 
			pos=wx.DefaultPosition, size=wx.Size( 500,500 ), 
			style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		global BACK_COLOR
		BACK_COLOR = wx.SystemSettings.GetColour(BACK_COLOR)
		
		self.initUI()
		self.SetTargetMinMax() 
		self.default_values() # also limit time controls
		self.bind_controls()

		# Color the controls that are required
		self.title.SetBackgroundColour(RED_COLOR)	
		self.location.SetBackgroundColour(RED_COLOR)
		
		self.panel_dateStart_color.SetBackgroundColour(RED_COLOR)
		self.panel_dateEnd_color.SetBackgroundColour(RED_COLOR)
		self.timeStart.SetBackgroundColour(RED_COLOR)
		self.timeEnd.SetBackgroundColour(RED_COLOR)

	def initUI(self):

		#font2 = wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
		#font1 = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

		# -------------------- 
		# Main "window"
		
		self.SetSizeHintsSz(wx.Size( 500,500 ), wx.DefaultSize ) #min size
		#self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.SetBackgroundColour( BACK_COLOR )
		
		sizer_frame = wx.BoxSizer( wx.VERTICAL )
		
		# to allow tabbing (and also correct way of doing it)
		self.paneltab = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.paneltab.SetBackgroundColour(BACK_COLOR)

		# Set a toolbar because Windows doesn't use icons for buttons and we want icons so bad. 
		# (punto para Linux) 
		
		toolbar_size = (24,24)

		self.toolbar = self.CreateToolBar(#managed by a frame
			wx.TB_HORIZONTAL 
			| wx.TB_HORZ_TEXT #combines wx.TB_TEXT | wx.TB_HORZ_LAYOUT
			#| wx.TB_NOICONS | wx.TB_FLAT
		) 
		
		self.toolbar.SetToolBitmapSize(toolbar_size)  # sets icon size

		toolbar_items_order = ('save', 'previous', 'clean', 'info')
		for key in toolbar_items_order:
			prop = self.TOOLBAR_ITEMS[key]

			#if we care about fatty icons, add the size
			icon = wx.ArtProvider.GetBitmap(prop.icon, wx.ART_TOOLBAR )

			#bind here so we dont "self." not necessary stuff
			if key == 'save': self.Bind(wx.EVT_MENU, self.save_form, id=prop.id)
			elif key == 'clean': self.Bind(wx.EVT_MENU, self.clean_form, id=prop.id)
			elif key == 'previous': 
				self.Bind(wx.EVT_MENU, self.load_previous, id=prop.id)
			elif key == 'info': 
				self.toolbar.AddSeparator()
				self.Bind(wx.EVT_MENU, self.load_scriptInfo, id=prop.id)

			# should be using AddTool in wxpython > 3.0 but can't find example
			self.toolbar.AddLabelTool(prop.id, prop.label, icon, shortHelp=prop.tooltip)
			if key == 'previous':
				self.toolbar.EnableTool(prop.id, False) #at first we dont have anything.


		# Show the toolbar 
		self.toolbar.Realize()

		# accelerators / keyboard shortcuts
		# AcceleratorTable = table of keyboard shortcuts for menu or button commands
		# Could use KEY_DOWN/UP if dind't want to bind to menu item
		self.accel_tbl = wx.AcceleratorTable([  
				(wx.ACCEL_CTRL, ord('S'), self.TOOLBAR_ITEMS['save'].id),
				(wx.ACCEL_CTRL, ord('R'), self.TOOLBAR_ITEMS['previous'].id),
				(wx.ACCEL_CTRL, ord('N'), self.TOOLBAR_ITEMS['clean'].id),
				(wx.ACCEL_NORMAL, wx.WXK_F1, self.TOOLBAR_ITEMS['info'].id),
					# special key code (as wxk_f1): http://www.wxpython.org/Phoenix/docs/html/KeyCode.enumeration.html#keycode
				#(wx.ACCEL_ALT, ord('X'), xit_id),
				#(wx.ACCEL_SHIFT|wx.ACCEL_ALT, ord('Y'), yit_id)
         ])
		self.SetAcceleratorTable(self.accel_tbl)
	
		sizer_main = wx.FlexGridSizer( 0, 2, 0, 0 ) #rows, cols, vgap, hgap
		sizer_main.AddGrowableCol( 1 ) #col where we have the controls
		sizer_main.AddGrowableRow( 6 ) #description row
		sizer_main.SetFlexibleDirection( wx.BOTH )
		sizer_main.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		# controls: title
		sizer_main.Add( 
			wx.StaticText( self.paneltab, label="Título")
			, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.title = wx.TextCtrl(self.paneltab, validator=TextObjectValidator())
		sizer_main.Add( self.title, 0, wx.ALL|wx.EXPAND, 5 )
		
		# controls: Start datetime
		sizer_main.Add( 
			wx.StaticText(self.paneltab, label="Inicio")
			, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		# 		control: date
		sizer_time_inicio = wx.BoxSizer( wx.HORIZONTAL ) #hold date, time, check

		# to change background color. Datepicker doesnt allow it
		self.panel_dateStart_color = wx.Panel(self.paneltab)
		self.panel_dateStart_color.SetBackgroundColour(BACK_COLOR)

		sizer_dates_color = wx.BoxSizer( wx.VERTICAL ) #hold "cell" date

		self.dateStart = wx.DatePickerCtrl(self.panel_dateStart_color, style=wx.DP_DEFAULT|wx.DP_SHOWCENTURY )
		sizer_dates_color.Add(self.dateStart, 1, wx.ALL, 5 )

		self.panel_dateStart_color.SetSizer( sizer_dates_color )
		self.panel_dateStart_color.Layout()
		sizer_dates_color.Fit( self.panel_dateStart_color )
		sizer_time_inicio.Add(self.panel_dateStart_color, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5)
		# 		end control: date

		# 		control: time
		sizer_dates_time = wx.BoxSizer(wx.HORIZONTAL)

		spin_btn = wx.SpinButton(self.paneltab, style=wx.SP_VERTICAL )
		self.timeStart = masked.TimeCtrl(self.paneltab, -1, format = '24HHMM', 
			spinButton=spin_btn, oob_color="Pink")

		sizer_dates_time.Add(self.timeStart, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		sizer_dates_time.Add(spin_btn, 0, wx.ALL, 5 )

		sizer_time_inicio.Add(sizer_dates_time, 0, wx.ALIGN_CENTER|wx.ALIGN_LEFT, 5 )
		
		self.timeStart_dontinclude = wx.CheckBox( self.paneltab, label="Sin hora")
		self.timeStart_dontinclude.SetToolTipString( "Cuando no se sabe la hora (eventos muy a futuro o no se consiguió)" )
		sizer_time_inicio.Add( self.timeStart_dontinclude, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		sizer_main.Add( sizer_time_inicio, 1, wx.EXPAND, 5 )
		# 		end control: time
		# end controls: Start datetime

		# controls: End datetime
		sizer_main.Add(
			wx.StaticText(self.paneltab, label="Fin")
			, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		# 		control: date
		sizer_time_fin = wx.BoxSizer( wx.HORIZONTAL )
		sizer_dates_tmp = wx.BoxSizer(wx.HORIZONTAL) #hold "cell" date
		
		# to change background color. Datepicker doesnt allow it
		self.panel_dateEnd_color = wx.Panel(self.paneltab)
		self.panel_dateEnd_color.SetBackgroundColour(BACK_COLOR)

		self.dateEnd = wx.DatePickerCtrl(self.panel_dateEnd_color, style=wx.DP_DEFAULT|wx.DP_SHOWCENTURY)
		sizer_dates_tmp.Add(self.dateEnd, 1, wx.ALL, 5 )

		self.panel_dateEnd_color.SetSizer( sizer_dates_tmp )
		self.panel_dateEnd_color.Layout()
		sizer_dates_tmp.Fit( self.panel_dateEnd_color )
		
		sizer_time_fin.Add(self.panel_dateEnd_color, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )
		
		# 		control: end date

		# 		control: time
		sizer_dates_tmp = wx.BoxSizer(wx.HORIZONTAL)
		
		spin_btn = wx.SpinButton(self.paneltab, style=wx.SP_VERTICAL )
		self.timeEnd = masked.TimeCtrl(self.paneltab, -1, format = '24HHMM', 
			spinButton=spin_btn, oob_color="Pink")

		sizer_dates_tmp.Add(self.timeEnd, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		sizer_dates_tmp.Add(spin_btn, 0, wx.ALL, 5 )

		sizer_time_fin.Add(sizer_dates_tmp, 0, wx.ALIGN_CENTER|wx.ALIGN_LEFT, 5 )

		self.timeEnd_dontinclude = wx.CheckBox(self.paneltab, label="Sin hora")
		self.timeEnd_dontinclude.SetToolTipString( "Cuando no se sabe la hora (eventos muy a futuro o no se consiguió)" )
		sizer_time_fin.Add( self.timeEnd_dontinclude, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		# 		end control: time
		
		sizer_main.Add( sizer_time_fin, 1, wx.EXPAND, 5 )
		# end controls: End datetime
		
		# controls: Location

		sizer_main.Add( 
			wx.StaticText( self.paneltab, label="Lugar")
			, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		sizer_lugar = wx.BoxSizer( wx.HORIZONTAL )
		
		self.location = wx.TextCtrl(self.paneltab, validator=TextObjectValidator())
		sizer_lugar.Add( self.location, 1, wx.ALL|wx.EXPAND, 5 )
		
		cities = ["Río Grande", "Ushuaia", "Tolhuin"]
		self.city = wx.Choice( self.paneltab, choices=cities, size=(90,-1))
		self.city.SetSelection(0)
		sizer_lugar.Add( self.city, 0, wx.ALL, 5 )
			
		sizer_main.Add( sizer_lugar, 1, wx.EXPAND, 5 )
		
		# controls: Tags
		sizer_main.Add( 
			wx.StaticText(self.paneltab, label="Tags \n(opcional)")
			, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.tags = self.tags = ACTextControl(self.paneltab, candidates=[''], 
			match_at_start=True, add_option=False, case_sensitive=True)
		self.tags.SetToolTipString( "Palabras separadas por guión. \nSeleccionar del autocompletado con Enter o Tab" )
		sizer_main.Add( self.tags, 0, wx.ALL|wx.EXPAND, 5 )
		
		# controls: Source
		sizer_main.Add(
			wx.StaticText( self.paneltab, label="Fuente \n(opcional)")
			, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.source = wx.TextCtrl(self.paneltab)
		sizer_main.Add( self.source, 0, wx.ALL|wx.EXPAND, 5 )
		
		# controls: Description
		sizer_main.Add(
			wx.StaticText( self.paneltab, label="Descripción \n(opcional)")
			, 0, wx.ALIGN_TOP|wx.ALL, 5 )
		
		self.description = wx.TextCtrl(self.paneltab, style=wx.TE_MULTILINE )
		sizer_main.Add( self.description, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		# Continue building main frame
		self.paneltab.SetSizer( sizer_main )
		self.paneltab.Layout()
		sizer_main.Fit( self.paneltab )
		sizer_frame.Add( self.paneltab, 1, wx.ALL|wx.EXPAND, 5 )
	
		
		# finish frame
		self.SetSizer( sizer_frame )
		self.Layout()
		
		self.Centre( wx.BOTH )

	def bind_controls(self):
		'''Bind everything in one place '''

		self.title.Bind( wx.EVT_TEXT, self._on_text )
		self.location.Bind( wx.EVT_TEXT, self._on_text )
		
		self.timeEnd_dontinclude.Bind(wx.EVT_CHECKBOX, self._check_box_disable_end)
		self.timeStart_dontinclude.Bind(wx.EVT_CHECKBOX, self._check_box_disable_start)

		#Color date and times
		self.Bind(wx.EVT_DATE_CHANGED, self._on_datetime_change, self.dateStart)
		self.Bind(wx.EVT_DATE_CHANGED, self._on_datetime_change, self.dateEnd)
		self.Bind(masked.EVT_TIMEUPDATE, self._on_datetime_change, self.timeStart)
		self.Bind(masked.EVT_TIMEUPDATE, self._on_datetime_change, self.timeEnd)

	def default_values(self):
		'''Default values of controls'''

		#now = wx.DateTime.Now()
		
		today = datetime.date.today().strftime("%Y-%m-%d")

		default = {
			'title': ''
			, 'datetime': (today , '10:00:00')
			, 'datetime_end': (today , '11:00:00')
			, 'category': 0
			, 'tags': ''
			, 'location': ''
			, 'source': ''
			, 'description': ''
		}

		self.set_form_data(default)

	def set_form_data(self,data={}):
		'''Set form data with dictionary data'''

		if not data:
			self.default_values()
		else:

			if 'title' in data:
				self.title.SetValue(data['title'])

			if 'location' in data:
				self.location.SetValue(data['location'])

			if 'tags' in data:
				self.tags.SetValue(data['tags'])

			if 'source' in data:
				self.source.SetValue(data['source'])

			if 'description' in data:
				self.description.SetValue(data['description'])
			
			if 'category' in data:
				#check it's a number 
				try:
					int(data['category'])
				except ValueError:
					self.city.SetSelection(0)
				else:
					self.city.SetSelection(int(data['category']))

			if 'datetime' in data:
				tt = datetime.datetime.strptime(
					data['datetime'][0]
					, "%Y-%m-%d").timetuple() 
					#timetuple breaks ISO date into a nice tuple, with numbers as int
				dmy = (tt[2], tt[1]-1, tt[0])
				tt = wx.DateTimeFromDMY(*dmy)


				#TODO: Should be checking
				self.dateStart.SetValue(tt)
				self.timeStart.SetValue(data['datetime'][1])

			if 'datetime_end' in data:
				tt = datetime.datetime.strptime(
					data['datetime_end'][0]
					, "%Y-%m-%d").timetuple() 
				dmy = (tt[2], tt[1]-1, tt[0])
				tt = wx.DateTimeFromDMY(*dmy)


				#TODO: Should be checking
				self.dateEnd.SetValue(tt)
				self.timeEnd.SetValue(data['datetime_end'][1])

		self._on_datetime_change()


	def __del__( self ):
		pass
	
	def _check_box_disable_start (self, event):
		if self.timeStart_dontinclude.GetValue():
			self.timeStart.Enable( False )
		else:
			self.timeStart.Enable(True)
		
	def _check_box_disable_end (self, event):
		if self.timeEnd_dontinclude.GetValue():
			self.timeEnd.Enable( False )
		else:
			self.timeEnd.Enable(True)
			
	def SetTargetMinMax( self, event=None ):
	
		#print "date start: " , self.dateStart.GetValue()
		#print "date start range: " , self.dateStart.GetValue().GetRange()
		#dt = self.dateStart.GetValue().FormatISODate() #force string 
		#year, month, day = dt.split("-")
		#wxdt = wx.DateTimeFromDMY(int(day), int(month), int(year))
		##self.dateEnd.SetRange(wxdt)
		#print "date end rage: " , self.dateEnd.GetRange()

		if not self.dateStart.GetValue() == self.dateEnd.GetValue():
			self.timeEnd.SetMin(None)
			return 
			
		min = self.timeStart.GetWxDateTime()
		
		#Always up to this when initialiting
		max = wx.DateTime()
		max.ParseTime("23:59:59") 

		cur_min, cur_max = self.timeEnd.GetBounds()

		if min and (min != cur_min): self.timeEnd.SetMin(min)
		if max and (max != cur_max): self.timeEnd.SetMax(max)

		self.timeEnd.SetLimited(LIMIT_TIME_CONTROL)
	
	def _on_text(self, event):
		# If we dont use a dialog, we must use the validator like this 
		# (http://stackoverflow.com/questions/24573892/validate-string-in-textctrl/24574992)
		
		self.title.GetValidator().Validate(self.title)
		self.location.GetValidator().Validate(self.location)
		
	def resetBackgroundColor(self,item, event=None):
		'''reset the color of textboxes'''
		item.SetBackgroundColour(NULL_COLOR)
		
	def redBackgroundColor(self, item, event=None):
		
		item.SetBackgroundColour(RED_COLOR)
	
	def _on_datetime_change (self, event=None):
		"""Color controls according to values """

		self.SetTargetMinMax(self)
		
		date_start = self.dateStart.GetValue()
		date_end   = self.dateEnd.GetValue()
		time_start = self.timeStart.GetValue()
		time_end   = self.timeEnd.GetValue()
		
		if date_start == date_end:
			self.resetBackgroundColor(self.panel_dateStart_color)
			self.resetBackgroundColor(self.panel_dateEnd_color)
			
			if time_start > time_end:
				self.redBackgroundColor(self.timeStart)
				self.resetBackgroundColor(self.timeEnd)
			elif time_start == time_end:
				self.redBackgroundColor(self.timeStart)
				self.redBackgroundColor(self.timeEnd)	
				
			else:
				self.resetBackgroundColor(self.timeStart)
				self.resetBackgroundColor(self.timeEnd)
		else:
			self.resetBackgroundColor(self.panel_dateStart_color)

			if date_start > date_end:
				self.redBackgroundColor(self.panel_dateEnd_color)
			else:
				self.resetBackgroundColor(self.panel_dateEnd_color)
			
			
		
		self.panel_dateStart_color.Refresh()
		self.panel_dateEnd_color.Refresh()
		self.timeStart.Refresh()
		self.timeEnd.Refresh()
		
	
	# Virtual event handlers, overide them in your derived class
	
	def save_form( self, event ):
		
		event.Skip()

	
	def clean_form( self, event ):
		event.Skip()

	def load_previous(self,event):
		event.Skip()

	def load_scriptInfo(self,event):
		event.Skip()




# ACTextControl: https://github.com/RajaS/ACTextCtrl  with some modifications by me
#    version 0.3 by https://github.com/Ezpy/ACTextCtrl
# 
# Written to satisfy my need for a text entry widget with autocomplete.
# Heavily borrowed ideas from http://wiki.wxpython.org/TextCtrlAutoComplete
# Raja Selvaraj <rajajs@gmail.com>
# 

# version 0.3
#  - Edited focus loss function to work properly.
#    (It could be only problem to me since I executed on Windows)
#  - After using tab to auto-complete, one more tab will move you to next ctrl.
#  - When used tab to auto-complete, highlight the auto-complete word to dropdown box.
#  - author: Changyun Lee <python.signal@gmail.com>. 
#  
# version 0.2
#  - Added option to use case sensitive matches, default is false
#
# version 0.1

#import wx

class ACTextControl(wx.TextCtrl):
    """
    A Textcontrol that accepts a list of choices at the beginning.
    Choices are presented to the user based on string being entered.
    If a string outside the choices list is entered, option may
    be given for user to add it to list of choices.
    match_at_start - Should only choices beginning with text be shown ?
    add_option - Should user be able to add new choices
    case_sensitive - Only case sensitive matches
    """
    def __init__(self, parent, candidates=[], match_at_start = False,
                 add_option=False, case_sensitive=False):
            
        wx.TextCtrl.__init__(self, parent, style=wx.TE_PROCESS_ENTER)

        self.all_candidates = candidates
        self.match_at_start = match_at_start
        self.add_option = add_option
        self.case_sensitive = case_sensitive
        self.max_candidates = 5   # maximum no. of candidates to show
        self.select_candidates = []
        self.popup = ACPopup(self)

        self._set_bindings()

        self._screenheight = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_Y)
        self._popdown = True # Does the popup go down from the textctrl ?

    def _set_bindings(self):
        """
        One place to setup all the bindings
        """
        # text entry triggers update of the popup window
        self.Bind(wx.EVT_TEXT, self._on_text, self)
        self.Bind(wx.EVT_KEY_DOWN, self._on_key_down, self)

        # loss of focus should hide the popup
        self.Bind(wx.EVT_KILL_FOCUS, self._on_focus_loss)
        self.Bind(wx.EVT_SET_FOCUS, self._on_focus)
        gp = self
        while gp != None :
            gp.Bind ( wx.EVT_MOVE , self._on_focus_loss, gp)
            gp.Bind ( wx.EVT_SIZE , self._on_focus_loss, gp)
            gp = gp.GetParent()       
        
        
        #Added by me
        self.Bind(wx.EVT_LISTBOX_DCLICK, self._list_double_click)
        
	  
    def SetValue(self, value):
        """
        Directly calling setvalue triggers textevent
        which results in popup appearing.
        To avoid this, call changevalue
        """
        super(ACTextControl, self).ChangeValue(value)


    # Added by me, only words without spaces
    def GetLastWord(self, text):
        whole_text = text

        last_piece = whole_text.rsplit(" ",1)
        print(last_piece)
        try:
            last_piece = last_piece[1]
        except IndexError:
            last_piece = last_piece[0]

        return last_piece



    def _on_text(self, event):
        """
        On text entry in the textctrl,
        Pop up the popup,
        or update candidates if its already visible
        """
        txt = self.GetValue()
        self.complete_text = txt
        
        txt = self.GetLastWord(txt)
        
        

        # if txt is empty (after backspace), hide popup
        if not txt:
            if self.popup.IsShown:
                self.popup.Show(False)
                event.Skip()
                return

        # select candidates
        if self.match_at_start and self.case_sensitive:
            self.select_candidates = [ch for ch in self.all_candidates
                              if ch.startswith(txt)]
        elif self.match_at_start and not self.case_sensitive:
            self.select_candidates = [ch for ch in self.all_candidates
                                      if ch.lower().startswith(txt.lower())]
        elif self.case_sensitive and not self.match_at_start:
            self.select_candidates = [ch for ch in self.all_candidates if txt in ch]
        else:
            self.select_candidates = [ch for ch in self.all_candidates if txt.lower() in ch.lower()]
            
        if len(self.select_candidates) == 0:
            if not self.add_option:
                if self.popup.IsShown():
                    self.popup.Show(False)

            else:
                display = ['Add ' + txt]
                self.popup._set_candidates(display, 'Add')
                self._resize_popup(display, txt)
                self._position_popup()
                if not self.popup.IsShown():
                    self.popup.Show()
                
        else:
            self._show_popup(self.select_candidates, txt)


    def _show_popup(self, candidates, txt):
		# set up the popup and bring it on
		self._resize_popup(candidates, txt)
		self._position_popup()

		candidates.sort()
		
		if self._popdown:
			 # TODO: Allow custom ordering
			 self.popup._set_candidates(candidates, txt)
			 self.popup.candidatebox.SetSelection(0)
			 
		else:
			 candidates.reverse()
			 self.popup._set_candidates(candidates, txt)
			 self.popup.candidatebox.SetSelection(len(candidates)-1)

		if not self.popup.IsShown():
			 self.popup.Show()
  

                
    def _on_focus_loss(self, event):
        """Close the popup when focus is lost"""
        if self.popup.IsShown():
            self.popup.Show(False)
        event.Skip()

            
    def _on_focus(self, event):
        """
        When focus is gained,
        if empty, show all candidates,
        else, show matches
        """
        txt =  self.GetValue()
        if txt == '':
            self.select_candidates = self.all_candidates
            self._show_popup(self.all_candidates, '')
        else:
            self._on_text(event)

            
    def _position_popup(self):
        """Calculate position for popup and
        display it"""
        left_x, upper_y = self.GetScreenPositionTuple()
        _, height = self.GetSizeTuple()
        popup_width, popup_height = self.popupsize
        
        if upper_y + height + popup_height > self._screenheight:
            self._popdown = False
            self.popup.SetPosition((left_x, upper_y - popup_height))
        else:
            self._popdown = True
            self.popup.SetPosition((left_x, upper_y + height))


    def _resize_popup(self, candidates, entered_txt):
        """Calculate the size for the popup to
        accomodate the selected candidates"""
        # Handle empty list (no matching candidates)
        if len(candidates) == 0:
            candidate_count = 3.5 # one line
            longest = len(entered_txt) + 4 + 4 #4 for 'Add '

        else:
            # additional 3 lines needed to show all candidates without scrollbar        
            candidate_count = min(self.max_candidates, len(candidates)) + 2.5
            longest = max([len(candidate) for candidate in candidates]) + 4

        
        charheight = self.popup.candidatebox.GetCharHeight()
        charwidth = self.popup.candidatebox.GetCharWidth()

        self.popupsize = wx.Size( charwidth*longest, charheight*candidate_count )

        self.popup.candidatebox.SetSize(self.popupsize)
        self.popup.SetClientSize(self.popupsize)
        

    # Added by me for those mouse-only days
    def _list_double_click	(self, event):
        """If double click list, add item to textbox"""    

        visible = self.popup.IsShown() 
        sel = self.popup.candidatebox.GetSelection()

        if not visible:
             #TODO: trigger event?
             pass
         # Add option is only displayed
        elif len(self.select_candidates) == 0:
             if self.popup.candidatebox.GetSelection() == 0:
                 self.all_candidates.append(self.GetValue())
             self.popup.Show(False)
             
        elif self.popup.candidatebox.GetSelection() == -1:
             self.popup.Show(False)

        elif self.popup.candidatebox.GetSelection() > -1:
             self.SetValue(self.select_candidates[self.popup.candidatebox.GetSelection()])
             self.SetInsertionPointEnd()
             self.popup.Show(False)
             
    def _on_key_down(self, event):
        """Handle key presses.
        Special keys are handled appropriately.
        For other keys, the event is skipped and allowed
        to be caught by ontext event"""
        skip = True
        visible = self.popup.IsShown() 
        sel = self.popup.candidatebox.GetSelection()
        
        # Escape key closes the popup if it is visible
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            if visible:
                self.popup.Show(False)

        # Down key for navigation in list of candidates
        elif event.GetKeyCode() == wx.WXK_DOWN:
            #skip = False #FIX: For all because it closes under Linux? (but not ander windows)
            if not visible:
                skip = False
                pass
            # 
            if sel + 1 < self.popup.candidatebox.GetItemCount():
                self.popup.candidatebox.SetSelection(sel + 1)
            else:
                skip = False

        # Up key for navigation in list of candidates
        elif event.GetKeyCode() == wx.WXK_UP:
            #skip = False #FIX: For all because it closes under Linux? (but not ander windows)
            if not visible:
                skip = False
                pass
            if sel > -1:
                self.popup.candidatebox.SetSelection(sel - 1)
            else:
                skip = False

        # Enter - use current selection for text
        elif event.GetKeyCode() == wx.WXK_RETURN:
            if not visible:
                #TODO: trigger event?
                pass
            # Add option is only displayed
            elif len(self.select_candidates) == 0:
                if self.popup.candidatebox.GetSelection() == 0:
                    self.all_candidates.append(self.GetValue())
                self.popup.Show(False)
                
            elif self.popup.candidatebox.GetSelection() == -1:
                self.popup.Show(False)

            elif self.popup.candidatebox.GetSelection() > -1:
                
                self.SetValue(self.select_candidates[self.popup.candidatebox.GetSelection()])
                self.SetInsertionPointEnd()
                self.popup.Show(False)

        # Tab  - set selected choice as text
        elif event.GetKeyCode() == wx.WXK_TAB:
            if visible:
                txt = self.GetValue()
                if txt == '' or txt == self.select_candidates[self.popup.candidatebox.GetSelection()]:
                    skip = True
                else:
                    self.SetValue(self.select_candidates[self.popup.candidatebox.GetSelection()])
                    # set cursor at end of text
                    self.SetInsertionPointEnd()
                    skip = False
                    self._on_focus(None)               
                
        if skip:
            event.Skip()
            

    def get_choices(self):
        """Return the current choices.
        Useful if choices have been added by the user"""
        return self.all_candidates        


class ACPopup(wx.PopupWindow):
    """
    The popup that displays the candidates for
    autocompleting the current text in the textctrl
    """
    def __init__(self, parent):
        wx.PopupWindow.__init__(self, parent)
        self.candidatebox = wx.SimpleHtmlListBox(self, -1, choices=[])
        self.SetSize((100, 100))
        self.displayed_candidates = []

    def _set_candidates(self, candidates, txt):
        """
        Clear existing candidates and use the supplied candidates
        Candidates is a list of strings.
        """
        # if there is no change, do not update
        if candidates == sorted(self.displayed_candidates):
            pass

        # Remove the current candidates
        self.candidatebox.Clear()
        
        for ch in candidates:
            self.candidatebox.Append(self._htmlformat(ch, txt))

        self.displayed_candidates = candidates


    def _htmlformat(self, text, substring):
        """
        For displaying in the popup, format the text
        to highlight the substring in html
        """
        # empty substring
        if len(substring) == 0:
            return text

        else:
            return text.replace(substring, '<b>' + substring + '</b>', 1)
        

# Demo of the Validators in the wxPython demo'''
class TextObjectValidator(wx.PyValidator):
    """ 
	 This validator is used to ensure that the user has entered something
    into the text object editor dialog's text field.
    """
    def __init__(self):
        """ Standard constructor."""
        wx.PyValidator.__init__(self)

    def Clone(self):
        """ Standard cloner. (every validator must implement the Clone() method.)"""
        return TextObjectValidator()

    def Validate(self, win):
        """ Validate the contents of the given text control."""
		  
        textCtrl = self.GetWindow()
        text     = textCtrl.GetValue()

        if len(text) == 0:
            #wx.MessageBox("A text object must contain some text!", "Error")
            #textCtrl.SetFocus() #comment to prevent jumping to next textfield
            textCtrl.SetBackgroundColour(RED_COLOR)
            textCtrl.Refresh()
            return False
        else:
            #textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
				textCtrl.SetBackgroundColour(NULL_COLOR)
				textCtrl.Refresh()
				return False

	''' Not necessary as we're not in a dialog
		 def TransferToWindow(self):
			  """ Transfer data from validator to window.
					The default implementation returns False, indicating that an error
					occurred.  We simply return True, as we don't do any data transfer.
			  """
			  return True # Prevent wxDialog from complaining.


		 def TransferFromWindow(self):
			  """ Transfer data from window to validator.
					The default implementation returns False, indicating that an error
					occurred.  We simply return True, as we don't do any data transfer.
			  """
			  return True # Prevent wxDialog from complaining.
	'''

	return True 
