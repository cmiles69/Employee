#!/usr/bin/env python3
# coding = utf-8

# https://www.youtube.com/watch?v=1xGh0bmGOrw Captain D.J Oamen
#

import tkinter
from tkinter import font
from tkinter import ttk

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
                            borderwidth = 5,
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
                                   size = 15,
                                   weight = 'bold' )
        self.ent_font = font.Font( family = 'DejaVu Serif',
                                   size = 15,
                                   weight = 'bold' )
        self.btn_font = font.Font( family = 'Bitstream Charter',
                                   size = 16,
                                   weight = 'bold' )

#===========================Variables===================================

    def create_variables( self ):
        self.reference     = tkinter.StringVar()
        self.firstname     = tkinter.StringVar()
        self.surname       = tkinter.StringVar()
        self.address       = tkinter.StringVar()
        self.gender        = tkinter.StringVar()
        self.mobile        = tkinter.StringVar()
        self.city          = tkinter.StringVar()
        self.student_loan  = tkinter.StringVar()
        self.other_payment = tkinter.StringVar()
        self.NI_payment    = tkinter.StringVar()
        self.basic_salary  = tkinter.StringVar()
        self.pension       = tkinter.StringVar()
        self.over_time     = tkinter.StringVar()
        self.tax           = tkinter.StringVar()                                   

#===========================Create Widgets==============================

    def create_widgets( self ):
        self.create_widgets_left()
        self.create_widgets_left_inner()
 
    def create_widgets_left( self ):
        self.lbl_reference = tkinter.Label( self.frm_left,
                            font = self.lbl_font,
                            text = 'Reference :',
                            borderwidth = 3,
                            background = 'RoyalBlue4',
                            foreground = 'lavender',
                            relief = tkinter.FLAT )
        self.lbl_reference.place( relx = 0,
                                  rely = 0 )
        self.ent_reference = tkinter.Entry( self.frm_left,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.reference )
        self.ent_reference.place( relx = 0.23,
                                  rely = 0 )

        self.lbl_firstname = tkinter.Label( self.frm_left,
                            font = self.lbl_font,
                            text = 'Firstname :',
                            borderwidth = 3,
                            background = 'RoyalBlue4',
                            foreground = 'lavender',
                            relief = tkinter.FLAT )
        self.lbl_firstname.place( relx = 0,
                                  rely = 0.1 )
        self.ent_firstname = tkinter.Entry( self.frm_left,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.firstname )
        self.ent_firstname.place( relx = 0.23,
                                  rely = 0.1 )

        self.lbl_surname = tkinter.Label( self.frm_left,
                            font = self.lbl_font,
                            text = 'Surname :',
                            borderwidth = 3,
                            background = 'RoyalBlue4',
                            foreground = 'lavender',
                            relief = tkinter.FLAT )
        self.lbl_surname.place( relx = 0.017,
                                rely = 0.2 )
        self.ent_surname = tkinter.Entry( self.frm_left,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.surname )
        self.ent_surname.place( relx = 0.23,
                                rely = 0.2 )

        self.lbl_address = tkinter.Label( self.frm_left,
                            font = self.lbl_font,
                            text = 'Address :',
                            borderwidth = 3,
                            background = 'RoyalBlue4',
                            foreground = 'lavender',
                            relief = tkinter.FLAT )
        self.lbl_address.place( relx = 0.033,
                                rely = 0.3 )

        self.ent_address = tkinter.Entry( self.frm_left,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.address )
        self.ent_address.place( relx = 0.23,
                                rely = 0.3 )

        self.lbl_gender = tkinter.Label( self.frm_left,         
                            font = self.lbl_font,
                            text = 'Gender :',
                            borderwidth = 3,
                            background = 'RoyalBlue4',
                            foreground = 'lavender',
                            relief = tkinter.FLAT )
        self.lbl_gender.place( relx = 0.042,
                               rely = 0.4 )
        style = ttk.Style()
        style.map( 'TCombobox',
                    fieldbackground = [('readonly','green')])
        style.map( 'TCombobox',
                    selectbackground = [('readonly','green')])
        style.map( 'TCombobox',
                    selectforeground = [('readonly','black')])
                                                                        
        self.ent_gender = ttk.Combobox( self.frm_left,
                            font = self.ent_font,
                            background = 'green',                       
                            textvariable = self.gender )
        self.ent_gender['values'] = ( '',
                                      'Male',
                                      'Female',
                                      'Transsexual',
                                      'Trans Man',
                                      'Trans Women',
                                      'Transitioning',
                                      'Genderqueer',
                                      'Indeterminate Sex',
                                      'Not Stated',
                                      'Refused to answer',
                                      'Response Unidentifiable' )
        self.ent_gender['state'] = 'readonly'
        self.ent_gender.current( 0 )
        self.ent_gender.place( relx = 0.23,
                               rely = 0.4,
                               relwidth = 0.416,
                               relheight = 0.065 )
        
        self.lbl_mobile = tkinter.Label( self.frm_left,
                            font = self.lbl_font,
                            text = 'Mobile :',
                            borderwidth = 3,
                            background = 'RoyalBlue4',
                            foreground = 'lavender',
                            relief = tkinter.FLAT )
        self.lbl_mobile.place( relx = 0.048,
                               rely = 0.5 )
        self.ent_mobile = tkinter.Entry( self.frm_left,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.mobile )
        self.ent_mobile.place( relx = 0.23,
                               rely = 0.5 )

#===========================Left Inner==================================

    def create_widgets_left_inner( self ):
        self.lbl_city = tkinter.Label( self.frm_left_inner,
                            font = self.lbl_font,
                            text = 'City Weighting :',
                            borderwidth = 3,
                            background = 'pale green',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_city.place( relx = 0,
                             rely = 0 )
        self.ent_city = tkinter.Entry( self.frm_left_inner,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.city )
        self.ent_city.place( relx = 0.29,
                             rely = 0,
                             relwidth = 0.22 )

        self.lbl_student_loan = tkinter.Label( self.frm_left_inner,
                            font = self.lbl_font,
                            text = 'Student Loan :',
                            borderwidth = 3,
                            background = 'pale green',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_student_loan.place( relx = 0.52,
                                     rely = 0 )
        self.ent_student_loan = tkinter.Entry( self.frm_left_inner,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.student_loan )
        self.ent_student_loan.place( relx = 0.78,
                                     rely = 0,
                                     relwidth = 0.22 )

        self.lbl_other_payment = tkinter.Label( self.frm_left_inner,
                            font = self.lbl_font,
                            text = 'Other Payment :',
                            borderwidth = 3,
                            background = 'pale green',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_other_payment.place( relx = 0,
                                      rely = 0.25 )
        self.ent_other_payment = tkinter.Entry( self.frm_left_inner,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.other_payment )
        self.ent_other_payment.place( relx = 0.29,
                                      rely = 0.25,
                                      relwidth = 0.22 )

        self.lbl_NI_payment = tkinter.Label( self.frm_left_inner,
                            font = self.lbl_font,
                            text = 'NI Payment :',
                            borderwidth = 3,
                            background = 'pale green',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_NI_payment.place( relx = 0.547,
                                   rely = 0.25 )
        self.ent_NI_payment = tkinter.Entry( self.frm_left_inner,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.NI_payment )
        self.ent_NI_payment.place( relx = 0.78,
                                   rely = 0.25,
                                   relwidth = 0.22 )

        self.lbl_basic_salary = tkinter.Label( self.frm_left_inner,
                            font = self.lbl_font,
                            text = 'Basic Salary :',
                            borderwidth = 3,
                            background = 'pale green',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_basic_salary.place( relx = 0.044,
                                     rely = 0.50 )
        self.ent_basic_salary = tkinter.Entry( self.frm_left_inner,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.basic_salary )
        self.ent_basic_salary.place( relx = 0.29,
                                     rely = 0.50,
                                     relwidth = 0.22 )

        self.lbl_pension = tkinter.Label( self.frm_left_inner,
                            font = self.lbl_font,
                            text = 'Pension :',
                            borderwidth = 3,
                            background = 'pale green',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_pension.place( relx = 0.606,
                                rely = 0.50 )
        self.ent_pension = tkinter.Entry( self.frm_left_inner,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.pension )
        self.ent_pension.place( relx = 0.78,
                                rely = 0.50,
                                relwidth = 0.22 )

        self.lbl_over_time = tkinter.Label( self.frm_left_inner,
                            font = self.lbl_font,
                            text = 'Over Time :',
                            borderwidth = 3,
                            background = 'pale green',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_over_time.place( relx = 0.076,
                                  rely = 0.75 )
        self.ent_over_time = tkinter.Entry( self.frm_left_inner,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.over_time )
        self.ent_over_time.place( relx = 0.29,
                                  rely = 0.75,
                                  relwidth = 0.22 )

        self.lbl_tax = tkinter.Label( self.frm_left_inner,
                            font = self.lbl_font,
                            text = 'Tax :',
                            borderwidth = 3,
                            background = 'pale green',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_tax.place( relx = 0.677,
                            rely = 0.75 )
        self.ent_tax = tkinter.Entry( self.frm_left_inner,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.tax )
        self.ent_tax.place( relx = 0.78,
                            rely = 0.75,
                            relwidth = 0.22 )
if __name__ == '__main__':
    root = tkinter.Tk()
    application = Employee( root )
    root.mainloop()