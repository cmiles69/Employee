#!/usr/bin/env python3
# coding = utf-8

# https://www.youtube.com/watch?v=1xGh0bmGOrw Captain D.J Oamen
#

import tkinter

class Employee( object ):

    def __init__( self, root ):
        self.root = root
        self.initUI()

    def initUI( self ):
        self.root.title( 'Employee Database Management System' )
        self.geometry = self.screen_size( size = 0.75 )
        # print( self.geometry )
        self.root.geometry( self.geometry )
        self.center_root()
        self.root.configure( background = 'deep sky blue' )
        self.create_frames()
        self.create_fonts()
        self.create_variables()
        self.create_widgets()

    def screen_size( self, size ):
        # Obtain desired screen size
        width = self.root.winfo_screenwidth() * size
        height = self.root.winfo_screenheight() * size
        return( '{}x{}+{}+{}' 
        .format( int( width ), int( height ), 0, 0 ))

    def center_root( self ):
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        pos_right = \
        int( self.root.winfo_screenwidth() // 2 - window_width // 2 )
        pos_down = \
        int( self.root.winfo_screenheight() // 2 - window_height // 2 )
        self.root.geometry( '{}x{}+{}+{}'
        .format( window_width, window_height, pos_right, pos_down ))

#==========================Create Frames================================

    def create_frames( self ):
        self.frm_left = tkinter.Frame( self.root,
                            borderwidth = 10,
                            background = 'RoyalBlue4',
                            relief = tkinter.RIDGE )
        self.frm_left.place( relx = 0,
                             rely = 0,
                             relwidth = 0.5,
                             relheight = 0.65 )

        self.frm_left_inner = tkinter.Frame( self.frm_left,
                            borderwidth = 10,
                            background = 'pale green',
                            relief = tkinter.RIDGE )
        self.frm_left_inner.place( relx = 0,
                                   rely = 0.60,
                                   relwidth = 1,
                                   relheight = 0.4 )

        self.frm_middle = tkinter.Frame( self.root,
                            borderwidth = 10,
                            background = 'dark salmon',
                            relief = tkinter.RIDGE )
        self.frm_middle.place( relx = 0.5,
                               rely = 0,
                               relwidth = 0.25,
                               relheight = 0.65 )

        self.frm_right = tkinter.Frame( self.root,
                            borderwidth = 10,
                            background = 'LightPink4',
                            relief = tkinter.RIDGE )
        self.frm_right.place( relx = 0.75,
                              rely = 0,
                              relwidth = 0.25,
                              relheight = 0.65 )

        self.frm_bottom = tkinter.Frame( self.root,
                            borderwidth = 10,
                            background = 'orchid4',
                            relief = tkinter.RIDGE )
        self.frm_bottom.place( relx = 0,
                               rely = 0.65,
                               relwidth = 1,
                               relheight = 0.25 )

        self.frm_buttons = tkinter.Frame( self.root,
                            borderwidth = 10,
                            background = 'PaleGreen4',
                            relief = tkinter.RIDGE )
        self.frm_buttons.place( relx = 0,
                                rely = 0.903,
                                relwidth = 1,
                                relheight = 0.1 )

#===========================Fonts=======================================

    def create_fonts( self ):
        
        self.lbl_font = font.Font( family = 'DejaVu Serif',
                                   size = 12,
                                   weight = 'bold' )
        self.ent_font = font.Font( family = 'DejaVu Serif',
                                   size = 12,
                                   weight = 'bold' )
        self.btn_font = font.Font( family = 'Bitstream Charter',
                                   size = 16,
                                   weight = 'bold' )

#===========================Variables===================================

    def create_variables( self ):
        pass                                   

#===========================Create Widgets==============================
 
    def create_widgets( self ):
        pass                                
                                


if __name__ == '__main__':
    root = tkinter.Tk()
    application = Employee( root )
    root.mainloop()