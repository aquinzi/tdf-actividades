# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

ID_GUARDAR = 1000
ID_BORRAR = 1001
ID_REGENERAR_URL_CORTA = 1002
ID_CERRAR_VENTANA = 1003
ID_RG = 1004
ID_USH = 1005
ID_TOLHUIN = 1006
ID_LIMPIO = 1007

###########################################################################
## Class index_frame
###########################################################################

class index_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Admin ¿Qué hacer en Tierra del Fuego?", pos = wx.DefaultPosition, size = wx.Size( 482,521 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer_frame = wx.BoxSizer( wx.VERTICAL )
		
		self.m_paneltabme = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_paneltabme.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer_main = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText432 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Ventana principal del programa. Por ahora llamaría a ventanas principales por botones pero habría que buscar una forma para unificar todo mas bonito compartiendo un mismo menu (baja prioridad).\n\nNota: las ventanas importantes estan en frames. Si se sigue la modalidad de llamar por botón desde el index, podrían ser modals.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText432.Wrap( -1 )
		self.m_staticText432.SetMinSize( wx.Size( -1,85 ) )
		
		bSizer_main.Add( self.m_staticText432, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline32 = wx.StaticLine( self.m_paneltabme, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_main.Add( self.m_staticline32, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.m_button32 = wx.Button( self.m_paneltabme, wx.ID_ANY, u"Añadir evento", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_main.Add( self.m_button32, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_staticline321 = wx.StaticLine( self.m_paneltabme, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_main.Add( self.m_staticline321, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText429 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Ventanas para hacer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText429.Wrap( -1 )
		self.m_staticText429.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer_main.Add( self.m_staticText429, 0, wx.ALL, 5 )
		
		gSizer12 = wx.GridSizer( 0, 3, 0, 0 )
		
		bSizer238 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText430 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Ventanas importantes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText430.Wrap( -1 )
		bSizer238.Add( self.m_staticText430, 0, wx.ALL, 5 )
		
		self.m_staticText4301 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"sin código", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4301.Wrap( -1 )
		bSizer238.Add( self.m_staticText4301, 0, wx.ALL, 5 )
		
		self.m_button322 = wx.Button( self.m_paneltabme, wx.ID_ANY, u"Añadir/editar lugar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer238.Add( self.m_button322, 0, wx.ALL, 5 )
		
		self.m_staticText43011 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"faltan hacer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43011.Wrap( -1 )
		bSizer238.Add( self.m_staticText43011, 0, wx.ALL, 5 )
		
		self.m_button3221 = wx.Button( self.m_paneltabme, wx.ID_ANY, u"Añadir/editar entidad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3221.Enable( False )
		
		bSizer238.Add( self.m_button3221, 0, wx.ALL, 5 )
		
		self.m_button32211 = wx.Button( self.m_paneltabme, wx.ID_ANY, u"Añadir/editar actividad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button32211.Enable( False )
		
		bSizer238.Add( self.m_button32211, 0, wx.ALL, 5 )
		
		self.m_button322111 = wx.Button( self.m_paneltabme, wx.ID_ANY, u"Administración tags", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button322111.Enable( False )
		
		bSizer238.Add( self.m_button322111, 0, wx.ALL, 5 )
		
		self.m_button3221111 = wx.Button( self.m_paneltabme, wx.ID_ANY, u"Administración actividades", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3221111.Enable( False )
		
		bSizer238.Add( self.m_button3221111, 0, wx.ALL, 5 )
		
		self.m_button32211111 = wx.Button( self.m_paneltabme, wx.ID_ANY, u"Buscar (todo)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button32211111.Enable( False )
		
		bSizer238.Add( self.m_button32211111, 0, wx.ALL, 5 )
		
		self.m_button322111111 = wx.Button( self.m_paneltabme, wx.ID_ANY, u"Configuración programa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button322111111.Enable( False )
		
		bSizer238.Add( self.m_button322111111, 0, wx.ALL, 5 )
		
		
		gSizer12.Add( bSizer238, 1, wx.EXPAND, 5 )
		
		bSizer239 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText431 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Dialog/Modal (solo para listar,\n muchas sin codigo)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText431.Wrap( -1 )
		bSizer239.Add( self.m_staticText431, 0, wx.ALL, 5 )
		
		self.m_button321 = wx.Button( self.m_paneltabme, wx.ID_ANY, u"fechas avanzado", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer239.Add( self.m_button321, 0, wx.ALL, 5 )
		
		self.m_button3211 = wx.Button( self.m_paneltabme, wx.ID_ANY, u"seleccion lugar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer239.Add( self.m_button3211, 0, wx.ALL, 5 )
		
		self.m_button32111 = wx.Button( self.m_paneltabme, wx.ID_ANY, u"seleccion tags", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer239.Add( self.m_button32111, 0, wx.ALL, 5 )
		
		self.m_button321111 = wx.Button( self.m_paneltabme, wx.ID_ANY, u"seleccion personas", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer239.Add( self.m_button321111, 0, wx.ALL, 5 )
		
		self.m_button3211111 = wx.Button( self.m_paneltabme, wx.ID_ANY, u"generación short URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer239.Add( self.m_button3211111, 0, wx.ALL, 5 )
		
		
		gSizer12.Add( bSizer239, 1, wx.EXPAND, 5 )
		
		bSizer240 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText433 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Otras acciones con posible GUI:\n- check tags (los indices)\n- check personas (bien linkeo a posts)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText433.Wrap( -1 )
		bSizer240.Add( self.m_staticText433, 1, wx.ALL, 5 )
		
		self.m_staticText434 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"No sabemos si hacer GUI:\n- listar eventos, lugares, entidades, actividades por ciudad para buscar\n- configuracion jekyll", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText434.Wrap( -1 )
		bSizer240.Add( self.m_staticText434, 1, wx.ALL, 5 )
		
		
		gSizer12.Add( bSizer240, 1, wx.EXPAND, 5 )
		
		
		bSizer_main.Add( gSizer12, 1, wx.EXPAND, 5 )
		
		
		self.m_paneltabme.SetSizer( bSizer_main )
		self.m_paneltabme.Layout()
		bSizer_main.Fit( self.m_paneltabme )
		bSizer_frame.Add( self.m_paneltabme, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer_frame )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button32.Bind( wx.EVT_BUTTON, self.show_eventAdd )
		self.m_button322.Bind( wx.EVT_BUTTON, self.show_lugarAdd )
		self.m_button3221.Bind( wx.EVT_BUTTON, self.yes )
		self.m_button32211.Bind( wx.EVT_BUTTON, self.yes )
		self.m_button322111.Bind( wx.EVT_BUTTON, self.yes )
		self.m_button3221111.Bind( wx.EVT_BUTTON, self.yes )
		self.m_button32211111.Bind( wx.EVT_BUTTON, self.yes )
		self.m_button322111111.Bind( wx.EVT_BUTTON, self.yes )
		self.m_button321.Bind( wx.EVT_BUTTON, self.show_datesAvanced )
		self.m_button3211.Bind( wx.EVT_BUTTON, self.show_placeSelect )
		self.m_button32111.Bind( wx.EVT_BUTTON, self.show_tagsSelect )
		self.m_button321111.Bind( wx.EVT_BUTTON, self.show_peopleSelect )
		self.m_button3211111.Bind( wx.EVT_BUTTON, self.show_generateShortURL )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def show_eventAdd( self, event ):
		event.Skip()
	
	def show_lugarAdd( self, event ):
		event.Skip()
	
	def yes( self, event ):
		event.Skip()
	
	
	
	
	
	
	def show_datesAvanced( self, event ):
		event.Skip()
	
	def show_placeSelect( self, event ):
		event.Skip()
	
	def show_tagsSelect( self, event ):
		event.Skip()
	
	def show_peopleSelect( self, event ):
		event.Skip()
	
	def show_generateShortURL( self, event ):
		event.Skip()
	

###########################################################################
## Class eventoAdd_frame
###########################################################################

class eventoAdd_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Añadir evento", pos = wx.DefaultPosition, size = wx.Size( 446,463 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_archivo = wx.Menu()
		self.guardar = wx.MenuItem( self.m_archivo, ID_GUARDAR, u"Guardar", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_archivo.AppendItem( self.guardar )
		
		self.borrar = wx.MenuItem( self.m_archivo, ID_BORRAR, u"Borrar", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_archivo.AppendItem( self.borrar )
		
		self.regenerarUrlCorta = wx.MenuItem( self.m_archivo, ID_REGENERAR_URL_CORTA, u"Regenerar URL corta", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_archivo.AppendItem( self.regenerarUrlCorta )
		self.regenerarUrlCorta.Enable( False )
		
		self.cerrarVentana = wx.MenuItem( self.m_archivo, ID_CERRAR_VENTANA, u"Cerrar ventana", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_archivo.AppendItem( self.cerrarVentana )
		
		self.m_menubar1.Append( self.m_archivo, u"Archivo" ) 
		
		self.m_ciudad = wx.Menu()
		self.rg = wx.MenuItem( self.m_ciudad, ID_RG, u"RG", wx.EmptyString, wx.ITEM_RADIO )
		self.m_ciudad.AppendItem( self.rg )
		self.rg.Enable( False )
		
		self.ush = wx.MenuItem( self.m_ciudad, ID_USH, u"Ush", wx.EmptyString, wx.ITEM_RADIO )
		self.m_ciudad.AppendItem( self.ush )
		self.ush.Enable( False )
		
		self.tolhuin = wx.MenuItem( self.m_ciudad, ID_TOLHUIN, u"Tolhuin", wx.EmptyString, wx.ITEM_RADIO )
		self.m_ciudad.AppendItem( self.tolhuin )
		self.tolhuin.Enable( False )
		
		self.limpio = wx.MenuItem( self.m_ciudad, ID_LIMPIO, u"Nuevo cada vez", wx.EmptyString, wx.ITEM_RADIO )
		self.m_ciudad.AppendItem( self.limpio )
		self.limpio.Enable( False )
		
		self.m_menubar1.Append( self.m_ciudad, u"Basar en" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer_frame = wx.BoxSizer( wx.VERTICAL )
		
		self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_FLAT|wx.TB_HORZ_TEXT|wx.TB_NOICONS|wx.TB_TEXT ) 
		self.m_toolClean = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"Borrar", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolSave = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"Guardar", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Guardar evento", None ) 
		
		self.m_toolBar1.AddSeparator()
		
		self.m_toolBar1.Realize() 
		
		bSizer_frame.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )
		
		self.m_notebook3 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_paneltabme = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_paneltabme.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer_main1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer_title1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_label_title2 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Título:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_label_title2.Wrap( -1 )
		self.m_label_title2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer_title1.Add( self.m_label_title2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.txtTitle = wx.TextCtrl( self.m_paneltabme, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer_title1.Add( self.txtTitle, 1, wx.ALL, 5 )
		
		
		bSizer_main1.Add( bSizer_title1, 0, wx.EXPAND, 5 )
		
		sbSizer201 = wx.StaticBoxSizer( wx.StaticBox( self.m_paneltabme, wx.ID_ANY, u"Fecha/s" ), wx.VERTICAL )
		
		self.m_staticText351 = wx.StaticText( sbSizer201.GetStaticBox(), wx.ID_ANY, u"Si no se saben los horarios, poner \"-\" (guión).", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText351.Wrap( -1 )
		sbSizer201.Add( self.m_staticText351, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer_dates11 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer57 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer41 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer41.AddGrowableCol( 1 )
		fgSizer41.SetFlexibleDirection( wx.BOTH )
		fgSizer41.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText361 = wx.StaticText( sbSizer201.GetStaticBox(), wx.ID_ANY, u"Día:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText361.Wrap( -1 )
		fgSizer41.Add( self.m_staticText361, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.datepickerEvent = wx.DatePickerCtrl( sbSizer201.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		fgSizer41.Add( self.datepickerEvent, 0, wx.ALL, 5 )
		
		self.m_staticText371 = wx.StaticText( sbSizer201.GetStaticBox(), wx.ID_ANY, u"Hora inicio:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )
		fgSizer41.Add( self.m_staticText371, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txtTimeStart = wx.TextCtrl( sbSizer201.GetStaticBox(), wx.ID_ANY, u"hh.mm", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txtTimeStart.SetMaxLength( 5 ) 
		self.txtTimeStart.SetToolTipString( u"separar horas y minutos con : o ." )
		
		fgSizer41.Add( self.txtTimeStart, 0, wx.ALL, 5 )
		
		self.m_staticText381 = wx.StaticText( sbSizer201.GetStaticBox(), wx.ID_ANY, u"Hora fin:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText381.Wrap( -1 )
		fgSizer41.Add( self.m_staticText381, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txtTimeEnd = wx.TextCtrl( sbSizer201.GetStaticBox(), wx.ID_ANY, u"hh:mm", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txtTimeEnd.SetMaxLength( 5 ) 
		fgSizer41.Add( self.txtTimeEnd, 0, wx.ALL, 5 )
		
		
		bSizer57.Add( fgSizer41, 0, wx.EXPAND, 5 )
		
		bSizer56 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAddDate = wx.Button( sbSizer201.GetStaticBox(), wx.ID_ANY, u"Agregar fecha", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer56.Add( self.btnAddDate, 0, wx.ALL, 5 )
		
		self.m_button341 = wx.Button( sbSizer201.GetStaticBox(), wx.ID_ANY, u"Avanzado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button341.Enable( False )
		self.m_button341.SetToolTipString( u"Crear fechas con más horarios, rangos de fechas, etc" )
		
		bSizer56.Add( self.m_button341, 0, wx.ALL, 5 )
		
		
		bSizer57.Add( bSizer56, 1, wx.EXPAND, 5 )
		
		
		bSizer_dates11.Add( bSizer57, 1, wx.EXPAND, 5 )
		
		lstScheduleChoices = [ u"otra opcion es usar listbox", u"con botones para ", u"agregar y eliminar", u"yyyy-mm-dd, hh:mm, hh:mm" ]
		self.lstSchedule = wx.ListBox( sbSizer201.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), lstScheduleChoices, wx.LB_NEEDED_SB )
		bSizer_dates11.Add( self.lstSchedule, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnListScheduleDeleteItem = wx.Button( sbSizer201.GetStaticBox(), wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( -1,-1 ), wx.BU_EXACTFIT )
		self.btnListScheduleDeleteItem.SetToolTipString( u"Eliminar seleccionado" )
		
		bSizer_dates11.Add( self.btnListScheduleDeleteItem, 0, wx.ALL, 5 )
		
		
		sbSizer201.Add( bSizer_dates11, 0, wx.EXPAND, 5 )
		
		
		bSizer_main1.Add( sbSizer201, 0, wx.EXPAND, 5 )
		
		bSizer_location11 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer_main1.Add( bSizer_location11, 0, wx.EXPAND, 5 )
		
		fgSizer20 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer20.AddGrowableCol( 1 )
		fgSizer20.SetFlexibleDirection( wx.BOTH )
		fgSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_label_title111 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Ciudad:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_label_title111.Wrap( -1 )
		self.m_label_title111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer20.Add( self.m_label_title111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		cboCityChoices = [ u"Río Grande", u"Ushuaia", u"Tolhuin" ]
		self.cboCity = wx.ComboBox( self.m_paneltabme, wx.ID_ANY, u"Río Grande", wx.DefaultPosition, wx.Size( -1,-1 ), cboCityChoices, wx.CB_READONLY )
		self.cboCity.SetSelection( 0 )
		fgSizer20.Add( self.cboCity, 0, wx.ALL, 5 )
		
		self.m_labelLocation11 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Lugar:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_labelLocation11.Wrap( -1 )
		fgSizer20.Add( self.m_labelLocation11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer55 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lblLocationSelected = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Lugar super lindo!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLocationSelected.Wrap( -1 )
		bSizer55.Add( self.lblLocationSelected, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btnSelectLocation = wx.Button( self.m_paneltabme, wx.ID_ANY, u"Seleccionar lugar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer55.Add( self.btnSelectLocation, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer20.Add( bSizer55, 1, wx.EXPAND, 5 )
		
		
		bSizer_main1.Add( fgSizer20, 0, wx.EXPAND, 5 )
		
		self.m_staticline11 = wx.StaticLine( self.m_paneltabme, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_main1.Add( self.m_staticline11, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.AddGrowableCol( 1 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_label_title13211 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Post ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_label_title13211.Wrap( -1 )
		self.m_label_title13211.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer21.Add( self.m_label_title13211, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txtPostID = wx.TextCtrl( self.m_paneltabme, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.txtPostID.SetToolTipString( u"el ID (filename) sin extensión" )
		
		fgSizer21.Add( self.txtPostID, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_label_title122111 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"URL:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_label_title122111.Wrap( -1 )
		self.m_label_title122111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer21.Add( self.m_label_title122111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.lblURLfinal = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"tdf.aquinzi.com/ciudad/año/mes/id", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblURLfinal.Wrap( -1 )
		self.lblURLfinal.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer21.Add( self.lblURLfinal, 0, wx.ALL, 5 )
		
		
		bSizer_main1.Add( fgSizer21, 0, wx.EXPAND, 5 )
		
		
		self.m_paneltabme.SetSizer( bSizer_main1 )
		self.m_paneltabme.Layout()
		bSizer_main1.Fit( self.m_paneltabme )
		self.m_notebook3.AddPage( self.m_paneltabme, u"Importantes", True )
		self.m_paneltabme1 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_paneltabme1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer_main11 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer52 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer52.AddGrowableCol( 1 )
		fgSizer52.SetFlexibleDirection( wx.BOTH )
		fgSizer52.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText982 = wx.StaticText( self.m_paneltabme1, wx.ID_ANY, u"Tags:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText982.Wrap( -1 )
		fgSizer52.Add( self.m_staticText982, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer942 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lblTagsSelected = wx.StaticText( self.m_paneltabme1, wx.ID_ANY, u"tag1, tag2, tag3, tag1, tag2, tag3, ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTagsSelected.Wrap( -1 )
		bSizer942.Add( self.lblTagsSelected, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.btnSelectTags = wx.Button( self.m_paneltabme1, wx.ID_ANY, u"Seleccionar etiquetas", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer942.Add( self.btnSelectTags, 0, wx.ALL, 5 )
		
		
		fgSizer52.Add( bSizer942, 0, wx.EXPAND, 5 )
		
		self.m_labelSource11 = wx.StaticText( self.m_paneltabme1, wx.ID_ANY, u"Fuente:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_labelSource11.Wrap( -1 )
		fgSizer52.Add( self.m_labelSource11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txtSource = wx.TextCtrl( self.m_paneltabme1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtSource.SetToolTipString( u"¿De dónde se sacó?" )
		
		fgSizer52.Add( self.txtSource, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText9811 = wx.StaticText( self.m_paneltabme1, wx.ID_ANY, u"Personas:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9811.Wrap( -1 )
		fgSizer52.Add( self.m_staticText9811, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer9411 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lblPeopleSelected = wx.StaticText( self.m_paneltabme1, wx.ID_ANY, u"tag1, tag2, tag3, tag1, tag2, tag3, ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPeopleSelected.Wrap( -1 )
		bSizer9411.Add( self.lblPeopleSelected, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.btnSelectPeople = wx.Button( self.m_paneltabme1, wx.ID_ANY, u"Seleccionar entidades", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9411.Add( self.btnSelectPeople, 0, wx.ALL, 5 )
		
		
		fgSizer52.Add( bSizer9411, 0, wx.EXPAND, 5 )
		
		
		bSizer_main11.Add( fgSizer52, 0, wx.EXPAND, 5 )
		
		bSizer_description11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_labelDescription11 = wx.StaticText( self.m_paneltabme1, wx.ID_ANY, u"Descripción:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_labelDescription11.Wrap( -1 )
		bSizer_description11.Add( self.m_labelDescription11, 0, wx.ALL, 5 )
		
		self.txtDescription = wx.TextCtrl( self.m_paneltabme1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer_description11.Add( self.txtDescription, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer_main11.Add( bSizer_description11, 1, wx.EXPAND, 5 )
		
		
		self.m_paneltabme1.SetSizer( bSizer_main11 )
		self.m_paneltabme1.Layout()
		bSizer_main11.Fit( self.m_paneltabme1 )
		self.m_notebook3.AddPage( self.m_paneltabme1, u"Opcionales", False )
		
		bSizer_frame.Add( self.m_notebook3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer_frame )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.save_form, id = self.guardar.GetId() )
		self.Bind( wx.EVT_MENU, self.clean_form, id = self.borrar.GetId() )
		self.Bind( wx.EVT_MENU, self.dismiss_form, id = self.cerrarVentana.GetId() )
		self.Bind( wx.EVT_TOOL, self.clean_form, id = self.m_toolClean.GetId() )
		self.Bind( wx.EVT_TOOL, self.save_form, id = self.m_toolSave.GetId() )
		self.txtTitle.Bind( wx.EVT_TEXT, self.title_changed )
		self.btnAddDate.Bind( wx.EVT_BUTTON, self.date_added )
		self.m_button341.Bind( wx.EVT_BUTTON, self.show_datesAvanced )
		self.btnListScheduleDeleteItem.Bind( wx.EVT_BUTTON, self.date_deleteselected )
		self.cboCity.Bind( wx.EVT_COMBOBOX, self.city_changed )
		self.btnSelectLocation.Bind( wx.EVT_BUTTON, self.show_placeSelect )
		self.txtPostID.Bind( wx.EVT_TEXT, self.postID_changed )
		self.btnSelectTags.Bind( wx.EVT_BUTTON, self.show_tagsSelect )
		self.btnSelectPeople.Bind( wx.EVT_BUTTON, self.show_peopleSelect )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def save_form( self, event ):
		event.Skip()
	
	def clean_form( self, event ):
		event.Skip()
	
	def dismiss_form( self, event ):
		event.Skip()
	
	
	
	def title_changed( self, event ):
		event.Skip()
	
	def date_added( self, event ):
		event.Skip()
	
	def show_datesAvanced( self, event ):
		event.Skip()
	
	def date_deleteselected( self, event ):
		event.Skip()
	
	def city_changed( self, event ):
		event.Skip()
	
	def show_placeSelect( self, event ):
		event.Skip()
	
	def postID_changed( self, event ):
		event.Skip()
	
	def show_tagsSelect( self, event ):
		event.Skip()
	
	def show_peopleSelect( self, event ):
		event.Skip()
	

###########################################################################
## Class fechasAvanzado_dialog
###########################################################################

class fechasAvanzado_dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Agregar fechas (avanzado)", pos = wx.DefaultPosition, size = wx.Size( 690,435 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer173 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3DSASH )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )
		self.m_splitter1.SetMinimumPaneSize( 20 )
		
		self.m_panel18 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		columa1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer156 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText306 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"1. completar formularios\n2. agregar a la tabla\n3. opcional: editar \n4. aceptar cambios", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText306.Wrap( -1 )
		bSizer156.Add( self.m_staticText306, 0, wx.ALL, 5 )
		
		self.m_staticline13 = wx.StaticLine( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer156.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		columa1.Add( bSizer156, 0, wx.EXPAND, 5 )
		
		fgSizer34 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer34.AddGrowableCol( 1 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		self.m_staticText287 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"Inicia el", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText287.Wrap( -1 )
		fgSizer34.Add( self.m_staticText287, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_datePicker18 = wx.DatePickerCtrl( self.m_panel18, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer34.Add( self.m_datePicker18, 0, wx.ALL, 5 )
		
		self.m_staticText288 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"hasta el", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText288.Wrap( -1 )
		fgSizer34.Add( self.m_staticText288, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_datePicker19 = wx.DatePickerCtrl( self.m_panel18, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer34.Add( self.m_datePicker19, 0, wx.ALL, 5 )
		
		self.m_staticText2871 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"Empieza a las", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText2871.Wrap( -1 )
		fgSizer34.Add( self.m_staticText2871, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl116 = wx.TextCtrl( self.m_panel18, wx.ID_ANY, u"hh:mm", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_textCtrl116.SetMaxLength( 5 ) 
		fgSizer34.Add( self.m_textCtrl116, 0, wx.ALL, 5 )
		
		self.m_staticText2881 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"hasta las", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2881.Wrap( -1 )
		fgSizer34.Add( self.m_staticText2881, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl1161 = wx.TextCtrl( self.m_panel18, wx.ID_ANY, u"hh:mm", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_textCtrl1161.SetMaxLength( 5 ) 
		fgSizer34.Add( self.m_textCtrl1161, 0, wx.ALL, 5 )
		
		
		columa1.Add( fgSizer34, 0, 0, 5 )
		
		sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel18, wx.ID_ANY, u"Exceptuar dias de semana" ), wx.VERTICAL )
		
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer152 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button85 = wx.Button( sbSizer23.GetStaticBox(), wx.ID_ANY, u"solo lunes-viernes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer152.Add( self.m_button85, 0, wx.ALL, 5 )
		
		self.m_checkBox4 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"lunes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer152.Add( self.m_checkBox4, 0, wx.ALL, 5 )
		
		self.m_checkBox41 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"martes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer152.Add( self.m_checkBox41, 0, wx.ALL, 5 )
		
		self.m_checkBox42 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"miércoles", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer152.Add( self.m_checkBox42, 0, wx.ALL, 5 )
		
		self.m_checkBox43 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"jueves", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer152.Add( self.m_checkBox43, 0, wx.ALL, 5 )
		
		self.m_checkBox44 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"viernes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer152.Add( self.m_checkBox44, 0, wx.ALL, 5 )
		
		
		gSizer7.Add( bSizer152, 0, 0, 5 )
		
		bSizer155 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button851 = wx.Button( sbSizer23.GetStaticBox(), wx.ID_ANY, u"solo sábado y domingo", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer155.Add( self.m_button851, 0, wx.ALL, 5 )
		
		self.m_checkBox45 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"sábado", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer155.Add( self.m_checkBox45, 0, wx.ALL, 5 )
		
		self.m_checkBox46 = wx.CheckBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"domingo", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer155.Add( self.m_checkBox46, 0, wx.ALL, 5 )
		
		
		gSizer7.Add( bSizer155, 1, wx.EXPAND, 5 )
		
		
		sbSizer23.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		
		columa1.Add( sbSizer23, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.m_button83 = wx.Button( self.m_panel18, wx.ID_ANY, u"Agregar a listado", wx.DefaultPosition, wx.DefaultSize, 0 )
		columa1.Add( self.m_button83, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel18.SetSizer( columa1 )
		self.m_panel18.Layout()
		columa1.Fit( self.m_panel18 )
		self.m_panel19 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		columna2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid2 = wx.grid.Grid( self.m_panel19, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid2.CreateGrid( 5, 4 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid2.SetColSize( 0, 70 )
		self.m_grid2.SetColSize( 1, 94 )
		self.m_grid2.SetColSize( 2, 59 )
		self.m_grid2.SetColSize( 3, 80 )
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 20 )
		self.m_grid2.SetColLabelValue( 0, u"Fecha" )
		self.m_grid2.SetColLabelValue( 1, u"Día de semana" )
		self.m_grid2.SetColLabelValue( 2, u"Inicia" )
		self.m_grid2.SetColLabelValue( 3, u"Termina" )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid2.AutoSizeRows()
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 20 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTRE )
		columna2.Add( self.m_grid2, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button84 = wx.Button( self.m_panel19, wx.ID_ANY, u"Eliminar seleccionados", wx.DefaultPosition, wx.DefaultSize, 0 )
		columna2.Add( self.m_button84, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel19.SetSizer( columna2 )
		self.m_panel19.Layout()
		columna2.Fit( self.m_panel19 )
		self.m_splitter1.SplitVertically( self.m_panel18, self.m_panel19, 319 )
		bSizer173.Add( self.m_splitter1, 1, wx.EXPAND, 5 )
		
		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer173.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_button1091 = wx.Button( self, wx.ID_ANY, u"Agregar todos los horarios", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer173.Add( self.m_button1091, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer173 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 319 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class seleccionLugar_dialog
###########################################################################

class seleccionLugar_dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Selección lugar", pos = wx.DefaultPosition, size = wx.Size( 421,289 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer189 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer190 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText340 = wx.StaticText( self, wx.ID_ANY, u"Estando en", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText340.Wrap( -1 )
		bSizer190.Add( self.m_staticText340, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText341 = wx.StaticText( self, wx.ID_ANY, u"Río Grande", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText341.Wrap( -1 )
		self.m_staticText341.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer190.Add( self.m_staticText341, 0, wx.ALL, 5 )
		
		self.m_staticline24 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer190.Add( self.m_staticline24, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer189.Add( bSizer190, 0, wx.EXPAND, 5 )
		
		bSizer191 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText342 = wx.StaticText( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText342.Wrap( -1 )
		bSizer191.Add( self.m_staticText342, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl138 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer191.Add( self.m_textCtrl138, 1, wx.ALL, 5 )
		
		self.m_button113 = wx.Button( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer191.Add( self.m_button113, 0, wx.ALL, 5 )
		
		
		bSizer189.Add( bSizer191, 0, wx.EXPAND, 5 )
		
		m_listBox14Choices = [ u"Lugar lindo (dirección bonita y esos datos)", u"Lugar lindo (dirección bonita y esos datos)", u"Lugar lindo (dirección bonita y esos datos)", u"Lugar lindo (dirección bonita y esos datos)" ]
		self.m_listBox14 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox14Choices, wx.LB_NEEDED_SB|wx.LB_SINGLE )
		bSizer189.Add( self.m_listBox14, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer192 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button114 = wx.Button( self, wx.ID_ANY, u"Aceptar seleccionado", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer192.Add( self.m_button114, 0, wx.ALL, 5 )
		
		self.m_button115 = wx.Button( self, wx.ID_ANY, u"Usar ingresado", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer192.Add( self.m_button115, 0, wx.ALL, 5 )
		
		
		bSizer189.Add( bSizer192, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer189 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class seleccionTags_dialog
###########################################################################

class seleccionTags_dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Seleccionar etiquetas", pos = wx.DefaultPosition, size = wx.Size( 264,295 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer193 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText344 = wx.StaticText( self, wx.ID_ANY, u"Seleccionar (o no) una o mas etiquetas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText344.Wrap( -1 )
		bSizer193.Add( self.m_staticText344, 0, wx.ALL, 5 )
		
		m_checkList1Choices = [u"tag1", u"tag2", u"tag3", u"tag4"]
		self.m_checkList1 = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList1Choices, wx.LB_MULTIPLE|wx.LB_NEEDED_SB|wx.LB_SORT )
		bSizer193.Add( self.m_checkList1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText343 = wx.StaticText( self, wx.ID_ANY, u"tiene que ser un wx.MultiChoiceDialog pero no esta en formbuilder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText343.Wrap( 210 )
		bSizer193.Add( self.m_staticText343, 0, wx.ALL, 5 )
		
		self.m_staticline25 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer193.Add( self.m_staticline25, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer194 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button116 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer194.Add( self.m_button116, 0, wx.ALL, 5 )
		
		self.m_button117 = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer194.Add( self.m_button117, 0, wx.ALL, 5 )
		
		
		bSizer193.Add( bSizer194, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer193 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button117.Bind( wx.EVT_BUTTON, self.dismiss_form )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dismiss_form( self, event ):
		event.Skip()
	

###########################################################################
## Class seleccionPersonas_dialog
###########################################################################

class seleccionPersonas_dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Seleccionar personas", pos = wx.DefaultPosition, size = wx.Size( 529,358 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer193 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText344 = wx.StaticText( self, wx.ID_ANY, u"Seleccionar (o no) una o mas personas/entidades", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText344.Wrap( -1 )
		bSizer193.Add( self.m_staticText344, 0, wx.ALL, 5 )
		
		tabla = wx.BoxSizer( wx.HORIZONTAL )
		
		columnaIzq = wx.BoxSizer( wx.VERTICAL )
		
		bSizer202 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl139 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer202.Add( self.m_textCtrl139, 1, wx.ALL, 5 )
		
		self.m_button122 = wx.Button( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer202.Add( self.m_button122, 0, wx.ALL, 5 )
		
		
		columnaIzq.Add( bSizer202, 0, wx.EXPAND, 5 )
		
		m_listBox15Choices = [ u"nombre largo (id)", u"nombre largo (id)", u"nombre largo (id)", u"nombre largo (id)", u"nombre largo (id)" ]
		self.m_listBox15 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox15Choices, 0 )
		columnaIzq.Add( self.m_listBox15, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		tabla.Add( columnaIzq, 1, wx.EXPAND, 5 )
		
		columnaMed = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button123 = wx.Button( self, wx.ID_ANY, u"agregar ->", wx.DefaultPosition, wx.DefaultSize, 0 )
		columnaMed.Add( self.m_button123, 0, wx.ALL, 5 )
		
		self.m_button1231 = wx.Button( self, wx.ID_ANY, u"quitar <-", wx.DefaultPosition, wx.DefaultSize, 0 )
		columnaMed.Add( self.m_button1231, 0, wx.ALL, 5 )
		
		
		tabla.Add( columnaMed, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		columnaDer = wx.BoxSizer( wx.VERTICAL )
		
		m_listBox16Choices = [ u"nombre largo (id)", u"nombre largo (id)" ]
		self.m_listBox16 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox16Choices, 0 )
		columnaDer.Add( self.m_listBox16, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		tabla.Add( columnaDer, 1, wx.EXPAND, 5 )
		
		
		bSizer193.Add( tabla, 1, wx.EXPAND, 5 )
		
		self.m_staticline25 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer193.Add( self.m_staticline25, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer194 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button116 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer194.Add( self.m_button116, 0, wx.ALL, 5 )
		
		self.m_button117 = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer194.Add( self.m_button117, 0, wx.ALL, 5 )
		
		
		bSizer193.Add( bSizer194, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer193 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button117.Bind( wx.EVT_BUTTON, self.dismiss_form )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dismiss_form( self, event ):
		event.Skip()
	

###########################################################################
## Class lugarAdd_frame
###########################################################################

class lugarAdd_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Añadir lugar", pos = wx.DefaultPosition, size = wx.Size( 529,496 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.archivo = wx.Menu()
		self.guardar = wx.MenuItem( self.archivo, ID_GUARDAR, u"Guardar", wx.EmptyString, wx.ITEM_NORMAL )
		self.archivo.AppendItem( self.guardar )
		
		self.borrar = wx.MenuItem( self.archivo, ID_BORRAR, u"Borrar", wx.EmptyString, wx.ITEM_NORMAL )
		self.archivo.AppendItem( self.borrar )
		
		self.cerrarVentana = wx.MenuItem( self.archivo, ID_CERRAR_VENTANA, u"Cerrar ventana", wx.EmptyString, wx.ITEM_NORMAL )
		self.archivo.AppendItem( self.cerrarVentana )
		
		self.m_menubar1.Append( self.archivo, u"Archivo" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer_frame = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2591 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4681 = wx.StaticText( self, wx.ID_ANY, u"Agregar lugar en", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4681.Wrap( -1 )
		bSizer2591.Add( self.m_staticText4681, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText4691 = wx.StaticText( self, wx.ID_ANY, u"Rio Grande", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4691.Wrap( -1 )
		self.m_staticText4691.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer2591.Add( self.m_staticText4691, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer_frame.Add( bSizer2591, 0, wx.EXPAND, 5 )
		
		fgSizer66 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer66.AddGrowableCol( 1 )
		fgSizer66.SetFlexibleDirection( wx.BOTH )
		fgSizer66.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText471 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText471.Wrap( -1 )
		fgSizer66.Add( self.m_staticText471, 0, wx.ALL, 5 )
		
		self.m_textCtrl193 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer66.Add( self.m_textCtrl193, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText470 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText470.Wrap( -1 )
		fgSizer66.Add( self.m_staticText470, 0, wx.ALL, 5 )
		
		self.m_textCtrl192 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer66.Add( self.m_textCtrl192, 0, wx.ALL, 5 )
		
		self.m_staticText478 = wx.StaticText( self, wx.ID_ANY, u"Última actualización", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText478.Wrap( -1 )
		fgSizer66.Add( self.m_staticText478, 0, wx.ALL, 5 )
		
		self.m_textCtrl199 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer66.Add( self.m_textCtrl199, 0, wx.ALL, 5 )
		
		
		bSizer_frame.Add( fgSizer66, 0, wx.EXPAND, 5 )
		
		self.m_notebook6 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_paneltabme = wx.Panel( self.m_notebook6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_paneltabme.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer5921 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5921.AddGrowableCol( 1 )
		fgSizer5921.SetFlexibleDirection( wx.BOTH )
		fgSizer5921.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText472 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Dirección", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText472.Wrap( -1 )
		fgSizer5921.Add( self.m_staticText472, 0, wx.ALL, 5 )
		
		self.m_textCtrl19711 = wx.TextCtrl( self.m_paneltabme, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5921.Add( self.m_textCtrl19711, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText567 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Geo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText567.Wrap( -1 )
		fgSizer5921.Add( self.m_staticText567, 0, wx.ALL, 5 )
		
		fgSizer70 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer70.AddGrowableCol( 1 )
		fgSizer70.SetFlexibleDirection( wx.BOTH )
		fgSizer70.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText474 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Lat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText474.Wrap( -1 )
		fgSizer70.Add( self.m_staticText474, 0, wx.ALL, 5 )
		
		self.m_textCtrl195 = wx.TextCtrl( self.m_paneltabme, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer70.Add( self.m_textCtrl195, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText475 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Lon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText475.Wrap( -1 )
		fgSizer70.Add( self.m_staticText475, 0, wx.ALL, 5 )
		
		self.m_textCtrl196 = wx.TextCtrl( self.m_paneltabme, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer70.Add( self.m_textCtrl196, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer5921.Add( fgSizer70, 1, wx.EXPAND, 5 )
		
		self.m_staticText47611 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Google Street View", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47611.Wrap( -1 )
		fgSizer5921.Add( self.m_staticText47611, 0, wx.ALL, 5 )
		
		self.m_textCtrl19811 = wx.TextCtrl( self.m_paneltabme, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5921.Add( self.m_textCtrl19811, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText47711 = wx.StaticText( self.m_paneltabme, wx.ID_ANY, u"Imagen (URL)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47711.Wrap( -1 )
		fgSizer5921.Add( self.m_staticText47711, 0, wx.ALL, 5 )
		
		self.m_textCtrl194 = wx.TextCtrl( self.m_paneltabme, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5921.Add( self.m_textCtrl194, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_paneltabme.SetSizer( fgSizer5921 )
		self.m_paneltabme.Layout()
		fgSizer5921.Fit( self.m_paneltabme )
		self.m_notebook6.AddPage( self.m_paneltabme, u"Localizacion", True )
		self.m_paneltabme1 = wx.Panel( self.m_notebook6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_paneltabme1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer284 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer591 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer591.AddGrowableCol( 1 )
		fgSizer591.SetFlexibleDirection( wx.BOTH )
		fgSizer591.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4791 = wx.StaticText( self.m_paneltabme1, wx.ID_ANY, u"email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4791.Wrap( -1 )
		self.m_staticText4791.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		fgSizer591.Add( self.m_staticText4791, 0, wx.ALL, 5 )
		
		self.m_textCtrl2001 = wx.TextCtrl( self.m_paneltabme1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer591.Add( self.m_textCtrl2001, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText4811 = wx.StaticText( self.m_paneltabme1, wx.ID_ANY, u"URLs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4811.Wrap( -1 )
		fgSizer591.Add( self.m_staticText4811, 0, wx.ALL, 5 )
		
		self.m_textCtrl2021 = wx.TextCtrl( self.m_paneltabme1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		fgSizer591.Add( self.m_textCtrl2021, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText4831 = wx.StaticText( self.m_paneltabme1, wx.ID_ANY, u"Teléfono/s", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4831.Wrap( -1 )
		fgSizer591.Add( self.m_staticText4831, 0, wx.ALL, 5 )
		
		self.m_textCtrl2031 = wx.TextCtrl( self.m_paneltabme1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer591.Add( self.m_textCtrl2031, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText520 = wx.StaticText( self.m_paneltabme1, wx.ID_ANY, u"Horarios", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText520.Wrap( -1 )
		fgSizer591.Add( self.m_staticText520, 0, wx.ALL, 5 )
		
		bSizer286 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_grid7 = wx.grid.Grid( self.m_paneltabme1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid7.CreateGrid( 3, 3 )
		self.m_grid7.EnableEditing( True )
		self.m_grid7.EnableGridLines( True )
		self.m_grid7.EnableDragGridSize( False )
		self.m_grid7.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid7.EnableDragColMove( False )
		self.m_grid7.EnableDragColSize( True )
		self.m_grid7.SetColLabelSize( 20 )
		self.m_grid7.SetColLabelValue( 0, u"Día/s" )
		self.m_grid7.SetColLabelValue( 1, u"Hora" )
		self.m_grid7.SetColLabelValue( 2, u"Nota" )
		self.m_grid7.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid7.EnableDragRowSize( True )
		self.m_grid7.SetRowLabelSize( 13 )
		self.m_grid7.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid7.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer286.Add( self.m_grid7, 0, wx.ALL, 5 )
		
		self.m_button201 = wx.Button( self.m_paneltabme1, wx.ID_ANY, u"Borrar seleccionada", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer286.Add( self.m_button201, 0, wx.ALL, 5 )
		
		
		fgSizer591.Add( bSizer286, 1, wx.EXPAND, 5 )
		
		
		bSizer284.Add( fgSizer591, 1, wx.EXPAND, 5 )
		
		self.m_staticline35 = wx.StaticLine( self.m_paneltabme1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer284.Add( self.m_staticline35, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText568 = wx.StaticText( self.m_paneltabme1, wx.ID_ANY, u"Notas:\n- URLs: una url por línea\n- telefono: separar con \",\" (coma)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText568.Wrap( -1 )
		self.m_staticText568.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer284.Add( self.m_staticText568, 0, wx.ALL, 5 )
		
		
		self.m_paneltabme1.SetSizer( bSizer284 )
		self.m_paneltabme1.Layout()
		bSizer284.Fit( self.m_paneltabme1 )
		self.m_notebook6.AddPage( self.m_paneltabme1, u"Contacto", False )
		self.m_paneltabme3 = wx.Panel( self.m_notebook6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_paneltabme3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer593 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer593.AddGrowableCol( 1 )
		fgSizer593.AddGrowableRow( 1 )
		fgSizer593.SetFlexibleDirection( wx.BOTH )
		fgSizer593.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4841 = wx.StaticText( self.m_paneltabme3, wx.ID_ANY, u"Nota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4841.Wrap( -1 )
		fgSizer593.Add( self.m_staticText4841, 0, wx.ALL, 5 )
		
		self.m_textCtrl2041 = wx.TextCtrl( self.m_paneltabme3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl2041.SetMinSize( wx.Size( -1,100 ) )
		
		fgSizer593.Add( self.m_textCtrl2041, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText4851 = wx.StaticText( self.m_paneltabme3, wx.ID_ANY, u"Marker symbol", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4851.Wrap( -1 )
		fgSizer593.Add( self.m_staticText4851, 0, wx.ALL, 5 )
		
		m_choice11Choices = [ u"marker1", u"marker2" ]
		self.m_choice11 = wx.Choice( self.m_paneltabme3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11Choices, 0 )
		self.m_choice11.SetSelection( 0 )
		fgSizer593.Add( self.m_choice11, 0, wx.ALL, 5 )
		
		
		self.m_paneltabme3.SetSizer( fgSizer593 )
		self.m_paneltabme3.Layout()
		fgSizer593.Fit( self.m_paneltabme3 )
		self.m_notebook6.AddPage( self.m_paneltabme3, u"Opcional", False )
		
		bSizer_frame.Add( self.m_notebook6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer_frame )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class entidadAdd_frame
###########################################################################

class entidadAdd_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Añadir entidad", pos = wx.DefaultPosition, size = wx.Size( 529,496 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.archivo = wx.Menu()
		self.guardar = wx.MenuItem( self.archivo, ID_GUARDAR, u"Guardar", wx.EmptyString, wx.ITEM_NORMAL )
		self.archivo.AppendItem( self.guardar )
		
		self.borrar = wx.MenuItem( self.archivo, ID_BORRAR, u"Borrar", wx.EmptyString, wx.ITEM_NORMAL )
		self.archivo.AppendItem( self.borrar )
		
		self.cerrarVentana = wx.MenuItem( self.archivo, ID_CERRAR_VENTANA, u"Cerrar ventana", wx.EmptyString, wx.ITEM_NORMAL )
		self.archivo.AppendItem( self.cerrarVentana )
		
		self.m_menubar1.Append( self.archivo, u"Archivo" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer_frame = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2591 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4681 = wx.StaticText( self, wx.ID_ANY, u"Agregar entidad en", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4681.Wrap( -1 )
		bSizer2591.Add( self.m_staticText4681, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText4691 = wx.StaticText( self, wx.ID_ANY, u"Rio Grande", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4691.Wrap( -1 )
		self.m_staticText4691.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer2591.Add( self.m_staticText4691, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer_frame.Add( bSizer2591, 0, wx.EXPAND, 5 )
		
		fgSizer66 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer66.AddGrowableCol( 1 )
		fgSizer66.SetFlexibleDirection( wx.BOTH )
		fgSizer66.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText471 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText471.Wrap( -1 )
		fgSizer66.Add( self.m_staticText471, 0, wx.ALL, 5 )
		
		self.m_textCtrl193 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer66.Add( self.m_textCtrl193, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText470 = wx.StaticText( self, wx.ID_ANY, u"ID (nombre de archivo)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText470.Wrap( -1 )
		fgSizer66.Add( self.m_staticText470, 0, wx.ALL, 5 )
		
		self.m_textCtrl192 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer66.Add( self.m_textCtrl192, 0, wx.ALL, 5 )
		
		self.m_staticText478 = wx.StaticText( self, wx.ID_ANY, u"Última actualización", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText478.Wrap( -1 )
		fgSizer66.Add( self.m_staticText478, 0, wx.ALL, 5 )
		
		self.m_textCtrl199 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer66.Add( self.m_textCtrl199, 0, wx.ALL, 5 )
		
		self.m_staticText623 = wx.StaticText( self, wx.ID_ANY, u"Categoría", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText623.Wrap( -1 )
		fgSizer66.Add( self.m_staticText623, 0, wx.ALL, 5 )
		
		m_choice11Choices = []
		self.m_choice11 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11Choices, 0 )
		self.m_choice11.SetSelection( 0 )
		fgSizer66.Add( self.m_choice11, 0, wx.ALL, 5 )
		
		self.m_staticText624 = wx.StaticText( self, wx.ID_ANY, u"Lugar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText624.Wrap( -1 )
		fgSizer66.Add( self.m_staticText624, 0, wx.ALL, 5 )
		
		self.m_textCtrl307 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer66.Add( self.m_textCtrl307, 0, wx.ALL, 5 )
		
		self.m_staticText625 = wx.StaticText( self, wx.ID_ANY, u"geo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText625.Wrap( -1 )
		fgSizer66.Add( self.m_staticText625, 0, wx.ALL, 5 )
		
		self.m_textCtrl308 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer66.Add( self.m_textCtrl308, 0, wx.ALL, 5 )
		
		self.m_staticText626 = wx.StaticText( self, wx.ID_ANY, u"Horario", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText626.Wrap( -1 )
		fgSizer66.Add( self.m_staticText626, 0, wx.ALL, 5 )
		
		self.m_textCtrl309 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer66.Add( self.m_textCtrl309, 0, wx.ALL, 5 )
		
		self.m_staticText627 = wx.StaticText( self, wx.ID_ANY, u"Precio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText627.Wrap( -1 )
		fgSizer66.Add( self.m_staticText627, 0, wx.ALL, 5 )
		
		m_choice12Choices = []
		self.m_choice12 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice12Choices, 0 )
		self.m_choice12.SetSelection( 0 )
		fgSizer66.Add( self.m_choice12, 0, wx.ALL, 5 )
		
		self.m_staticText628 = wx.StaticText( self, wx.ID_ANY, u"Nota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText628.Wrap( -1 )
		fgSizer66.Add( self.m_staticText628, 0, wx.ALL, 5 )
		
		self.m_textCtrl310 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer66.Add( self.m_textCtrl310, 0, wx.ALL, 5 )
		
		self.m_staticText629 = wx.StaticText( self, wx.ID_ANY, u"URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText629.Wrap( -1 )
		fgSizer66.Add( self.m_staticText629, 0, wx.ALL, 5 )
		
		self.m_textCtrl311 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer66.Add( self.m_textCtrl311, 0, wx.ALL, 5 )
		
		self.m_staticText630 = wx.StaticText( self, wx.ID_ANY, u"Teléfono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText630.Wrap( -1 )
		fgSizer66.Add( self.m_staticText630, 0, wx.ALL, 5 )
		
		self.m_textCtrl312 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer66.Add( self.m_textCtrl312, 0, wx.ALL, 5 )
		
		self.m_staticText631 = wx.StaticText( self, wx.ID_ANY, u"email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText631.Wrap( -1 )
		fgSizer66.Add( self.m_staticText631, 0, wx.ALL, 5 )
		
		self.m_textCtrl313 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer66.Add( self.m_textCtrl313, 0, wx.ALL, 5 )
		
		self.m_staticText632 = wx.StaticText( self, wx.ID_ANY, u"Descripción", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText632.Wrap( -1 )
		fgSizer66.Add( self.m_staticText632, 0, wx.ALL, 5 )
		
		self.m_textCtrl314 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer66.Add( self.m_textCtrl314, 0, wx.ALL, 5 )
		
		
		bSizer_frame.Add( fgSizer66, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer_frame )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class generarURLcorta_dialog
###########################################################################

class generarURLcorta_dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generación URL corta", pos = wx.DefaultPosition, size = wx.Size( 222,140 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer58 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText129 = wx.StaticText( self, wx.ID_ANY, u"Generando URL corta...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText129.Wrap( -1 )
		bSizer58.Add( self.m_staticText129, 0, wx.ALL, 5 )
		
		self.m_staticText130 = wx.StaticText( self, wx.ID_ANY, u"URL: goo.gl/sfsdfsdf", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText130.Wrap( -1 )
		bSizer58.Add( self.m_staticText130, 0, wx.ALL, 5 )
		
		self.m_staticText131 = wx.StaticText( self, wx.ID_ANY, u"Evento \"titulo\" guardado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )
		bSizer58.Add( self.m_staticText131, 0, wx.ALL, 5 )
		
		self.m_button40 = wx.Button( self, wx.ID_ANY, u"Cargar otro", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer58.Add( self.m_button40, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer58 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button40.Bind( wx.EVT_BUTTON, self.dismiss_form )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dismiss_form( self, event ):
		event.Skip()
	

