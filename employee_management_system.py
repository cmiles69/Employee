#!/usr/bin/env python3
# coding = utf-8

# https://www.youtube.com/watch?v=1rzaEXL016g Captain D.J Oamen
# 25:10, 28:26, 38:23, 43:40, 48:00, 54:35, 57:55, 1:07:48

import tkinter
import tkinter.scrolledtext as tkst
import secrets
import names
import random
import employee_DB
import tkinter.messagebox
import os
import subprocess
import tempfile
from tkinter import font
from tkinter import ttk
from tkcalendar import DateEntry
from faker import Faker


class Employee( object ):

    def __init__( self, root ):
        self.root = root
        self.initUI()

    def initUI( self ):
        self.root.title( 'Employee Database Management System' )
        self.geometry = self.screen_size( size = 0.75 )
        # print( self.geometry )
        self.root.geometry( self.geometry )
        self.root.protocol( 'WM_DELETE_WINDOW', self.Ask_Quit )
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

        self.txt_font = font.Font( family = 'DejaVu Serif',
                                   size = 12,
                                   weight = 'bold' )        
        self.lbl_font = font.Font( family = 'DejaVu Serif',
                                   size = 15,
                                   weight = 'bold' )
        self.ent_font = font.Font( family = 'DejaVu Serif',
                                   size = 15,
                                   weight = 'bold' )
        self.btn_font = font.Font( family = 'Bitstream Charter',
                                   size = 16,
                                   weight = 'bold' )
        self.tree_font = font.Font( family = 'Suruma',
                                    size = 15,
                                    weight = 'bold' )

#===========================Variables===================================

    def create_variables( self ):
        self.reference       = tkinter.StringVar()
        self.firstname       = tkinter.StringVar()
        self.surname         = tkinter.StringVar()
        self.address         = tkinter.StringVar()
        self.gender          = tkinter.StringVar()
        self.mobile          = tkinter.StringVar()
        self.city            = tkinter.StringVar()
        self.student_loan    = tkinter.StringVar()
        self.other_payment   = tkinter.StringVar()
        self.NI_payment      = tkinter.StringVar()
        self.basic_salary    = tkinter.StringVar()
        self.pension         = tkinter.StringVar()
        self.over_time       = tkinter.StringVar()
        self.tax             = tkinter.StringVar()
        self.pensionable_pay = tkinter.StringVar()
        self.taxable_pay     = tkinter.StringVar()
        self.tax_period      = tkinter.StringVar()
        self.tax_code        = tkinter.StringVar()
        self.NI_number       = tkinter.StringVar()
        self.NI_code         = tkinter.StringVar()
        self.deductions      = tkinter.StringVar()
        self.gross_pay       = tkinter.StringVar()
        self.net_pay         = tkinter.StringVar()
        self.pay_day         = tkinter.StringVar()                                   

#===================Create Widgets Dispatch=============================

    def create_widgets( self ):
        self.create_widgets_left()
        self.create_widgets_left_inner()
        self.create_widgets_middle()
        self.create_widgets_right()
        self.create_widgets_bottom()
        self.create_widgets_button()

#========================Left Frame Widgets=============================
 
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
        self.ent_reference.place( relx = 0.21,
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
        self.ent_firstname.place( relx = 0.21,
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
        self.ent_surname.place( relx = 0.21,
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
        self.ent_address.place( relx = 0.21,
                                rely = 0.3,
                                relwidth = 0.788 )

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
                    activebackground = [('readonly','green')])
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
        self.ent_gender.place( relx = 0.21,
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
        self.ent_mobile.place( relx = 0.21,
                               rely = 0.5 )

#===========================Left Inner Frame Widgets====================

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

#=========================Middle Frame Widgets==========================

    def create_widgets_middle( self ):
        self.lbl_pensionable_pay = tkinter.Label( self.frm_middle,
                            font = self.lbl_font,
                            text = 'Pensionable Pay :',
                            borderwidth = 3,
                            background = 'dark salmon',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_pensionable_pay.place( relx = 0,
                                        rely = 0 )
        self.ent_pensionable_pay = tkinter.Entry( self.frm_middle,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.pensionable_pay )
        self.ent_pensionable_pay.place( relx = 0.62,
                                        rely = 0,
                                        relwidth = 0.38 )

        self.lbl_taxable_pay = tkinter.Label( self.frm_middle,
                            font = self.lbl_font,
                            text = 'Taxable Pay :',
                            borderwidth = 3,
                            background = 'dark salmon',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_taxable_pay.place( relx = 0.145,
                                    rely = 0.1 )
        self.ent_taxable_pay = tkinter.Entry( self.frm_middle,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.taxable_pay )
        self.ent_taxable_pay.place( relx = 0.62,
                                    rely = 0.1,
                                    relwidth = 0.38 )

        self.lbl_tax_period = tkinter.Label( self.frm_middle,
                            font = self.lbl_font,
                            text = 'Tax Period :',
                            borderwidth = 3,
                            background = 'dark salmon',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_tax_period.place( relx = 0.185,
                                   rely = 0.2 )
        self.ent_tax_period = tkinter.Entry( self.frm_middle,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.tax_period )
        self.ent_tax_period.place( relx = 0.62,
                                   rely = 0.2,
                                   relwidth = 0.38 )

        self.lbl_tax_code = tkinter.Label( self.frm_middle,
                            font = self.lbl_font,
                            text = 'Tax Code :',
                            borderwidth = 3,
                            background = 'dark salmon',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_tax_code.place( relx = 0.235,
                                 rely = 0.3 )
        self.ent_tax_code = tkinter.Entry( self.frm_middle,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.tax_code )
        self.ent_tax_code.place( relx = 0.62,
                                 rely = 0.3,
                                 relwidth = 0.38 )

        self.lbl_NI_number = tkinter.Label( self.frm_middle,
                            font = self.lbl_font,
                            text = 'NI Number :',
                            borderwidth = 3,
                            background = 'dark salmon',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_NI_number.place( relx = 0.169,
                                  rely = 0.4 )
        self.ent_NI_number = tkinter.Entry( self.frm_middle,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.NI_number )
        self.ent_NI_number.place( relx = 0.62,
                                  rely = 0.4,
                                  relwidth = 0.38 )

        self.lbl_NI_code = tkinter.Label( self.frm_middle,
                            font = self.lbl_font,
                            text = 'NI Code :',
                            borderwidth = 3,
                            background = 'dark salmon',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_NI_code.place( relx = 0.276,
                                rely = 0.5 )
        self.ent_NI_code = tkinter.Entry( self.frm_middle,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.NI_code )
        self.ent_NI_code.place( relx = 0.62,
                                rely = 0.5,
                                relwidth = 0.38 )

        self.lbl_deductions = tkinter.Label( self.frm_middle,
                            font = self.lbl_font,
                            text = 'Deductions :',
                            borderwidth = 3,
                            background = 'dark salmon',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_deductions.place( relx = 0.167,
                                   rely = 0.6 )
        self.ent_deductions = tkinter.Entry( self.frm_middle,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.deductions )
        self.ent_deductions.place( relx = 0.62,
                                   rely = 0.6,
                                   relwidth = 0.38 )

        self.lbl_gross_pay = tkinter.Label( self.frm_middle,
                            font = self.lbl_font,
                            text = 'Gross Pay :',
                            borderwidth = 3,
                            background = 'dark salmon',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_gross_pay.place( relx = 0.217,
                                  rely = 0.7 )
        self.ent_gross_pay = tkinter.Entry( self.frm_middle,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.gross_pay )
        self.ent_gross_pay.place( relx = 0.62,
                                  rely = 0.7,
                                  relwidth = 0.38 )

        self.lbl_net_pay = tkinter.Label( self.frm_middle,
                            font = self.lbl_font,
                            text = 'Net Pay :',
                            borderwidth = 3,
                            background = 'dark salmon',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_net_pay.place( relx = 0.286,
                                rely = 0.8 )
        self.ent_net_pay = tkinter.Entry( self.frm_middle,
                            font = self.ent_font,
                            borderwidth = 3,
                            background = 'green',
                            textvariable = self.net_pay )
        self.ent_net_pay.place( relx = 0.62,
                                rely = 0.8,
                                relwidth = 0.38 )

        self.lbl_pay_day = tkinter.Label( self.frm_middle,
                            font = self.lbl_font,
                            text = 'Pay Day :',
                            borderwidth = 3,
                            background = 'dark salmon',
                            foreground = 'blue',
                            relief = tkinter.FLAT )
        self.lbl_pay_day.place( relx = 0.280,
                                rely = 0.9 )

        style = ttk.Style()
        style.configure('my.DateEntry',
                        fieldbackground='green',
                        background='dark green',
                        foreground='dark blue',
                        arrowcolor='white')

        self.ent_pay_day = DateEntry( self.frm_middle,
                            font = self.ent_font,
                            style = 'my.DateEntry',
                            borderwidth = 3,
                            bordercolor = 'green',
                            background = 'green',
                            foreground = 'blue',
                            date_pattern = 'dd-mm-y',
                            textvariable = self.pay_day )
        self.ent_pay_day.place( relx = 0.62,
                                rely = 0.9,
                                relwidth = 0.38 )

#=========================Right Frame Widgets===========================

    def create_widgets_right( self ):
        self.text_scroll_reciept = tkst.ScrolledText( self.frm_right,
                            font = self.txt_font,
                            borderwidth = 5,
                            background = 'LightPink4',
                            relief = tkinter.RIDGE )
        self.text_scroll_reciept.place( relx = 0,
                                        rely = 0,
                                        relwidth = 1,
                                        relheight = 1 )

#=======================Bottom Frame widgets============================

    def create_widgets_bottom( self ):
        style = ttk.Style()
        style.configure( 'Treeview.Heading', font = self.tree_font )
        #style.configure( 'Treeview.Tag', tag = self.tree_font )
        style.configure( 'Treeview', background = 'gold',
                                     foreground = 'blue',
                                     font = self.lbl_font )

        self.tree_view = ttk.Treeview( self.frm_bottom,
            column = ( 'column1',
                       'column2',
                       'column3',
                       'column4',
                       'column5' ), show = 'headings' )
        self.tree_view.column( 'column1', width = 15 )
        self.tree_view.column( 'column2', width = 15 )
        self.tree_view.column( 'column3', width = 15 )
        self.tree_view.column( 'column4', width = 15 )
        self.tree_view.heading( '#1', text = 'Reference :' )
        self.tree_view.heading( '#2', text = 'First Name :' )
        self.tree_view.heading( '#3', text = 'Surname :' )
        self.tree_view.heading( '#4', text = 'Mobile :' )
        self.tree_view.heading( '#5', text = 'Address :' )
        self.tree_view.bind( '<<TreeviewSelect>>',
                             self.On_Tree_Select )
        self.tree_view.place( relx = 0,
                              rely = 0,
                              relwidth = 1,
                              relheight = 1 )

#=======================Button Callbacks================================

    def Ask_Quit( self ):
        exit_program = tkinter.messagebox.askyesno(
            title = 'Employee Database System',
            message = 'Confirm if you want to exit program?' )
        if exit_program > 0:
            self.root.destroy()
        else:
            return( None )

    def Display( self ):
        ''' Recieving all the records, but only showing selected'''
        for idx in self.tree_view.get_children():
            self.tree_view.delete( idx )
        for row in employee_DB.view_employee_record():
            self.tree_view.insert( '', tkinter.END,
                                    values = ( row[r'Reference'],
                                               row[r'Firstname'],
                                               row[r'Surname'],
                                               row[r'Mobile'],
                                               row[r'Address'] ))

    def Add_New( self ):
        self.employee_record = [( self.reference.get(),      
                                  self.firstname.get(),      
                                  self.surname.get(),        
                                  self.address.get(),        
                                  self.gender.get(),         
                                  self.mobile.get(),
                                  self.city.get(),
                                  self.other_payment.get(),
                                  self.basic_salary.get(),
                                  self.over_time.get(),
                                  self.student_loan.get(),
                                  self.NI_payment.get(),
                                  self.pension.get(),
                                  self.tax.get(),
                                  self.pensionable_pay.get(),
                                  self.taxable_pay.get(),
                                  self.tax_period.get(),
                                  self.tax_code.get(),
                                  self.NI_number.get(),
                                  self.NI_code.get(),      
                                  self.deductions.get(),
                                  self.gross_pay.get(),
                                  self.net_pay.get(),
                                  self.pay_day.get())]
        last_row_id = \
        employee_DB.add_employee_record( self.employee_record )
        print( 'Last Row ID is :', last_row_id )

    def Update( self ):
        EMP_REF = self.reference.get()
        self.employee_record =   [( self.reference.get(),      
                                    self.firstname.get(),      
                                    self.surname.get(),        
                                    self.address.get(),        
                                    self.gender.get(),         
                                    self.mobile.get(),
                                    self.city.get(),
                                    self.other_payment.get(),
                                    self.basic_salary.get(),
                                    self.over_time.get(),
                                    self.student_loan.get(),
                                    self.NI_payment.get(),
                                    self.pension.get(),
                                    self.tax.get(),
                                    self.pensionable_pay.get(),
                                    self.taxable_pay.get(),
                                    self.tax_period.get(),
                                    self.tax_code.get(),
                                    self.NI_number.get(),
                                    self.NI_code.get(),      
                                    self.deductions.get(),
                                    self.gross_pay.get(),
                                    self.net_pay.get(),
                                    self.pay_day.get(), EMP_REF )]

        employee_DB.update_employee_record( self.employee_record )

    def Search( self ):
        EMP_REF = self.On_Tree_Select( event = None )
        search_data = employee_DB.search_employee_record( EMP_REF )
        self.Reset()
        self.reference.set( search_data[r'Reference'])     
        self.firstname.set( search_data[r'Firstname'])     
        self.surname.set( search_data[r'Surname'])        
        self.address.set( search_data[r'Address'])        
        self.gender.set( search_data[r'Gender'])         
        self.mobile.set( search_data[r'Mobile'])
        self.city.set( search_data[r'City_Weighting'])
        self.other_payment.set( search_data[r'Other_Payment'])
        self.basic_salary.set( search_data[r'Basic_Salary'])
        self.over_time.set( search_data[r'Over_Time'])
        self.student_loan.set( search_data[r'Student_Loan'])
        self.NI_payment.set( search_data[r'NI_Payment'])
        self.pension.set( search_data[r'Pension'])
        self.tax.set( search_data[r'Tax'])
        self.pensionable_pay.set( search_data[r'Pensionable_Pay'])
        self.taxable_pay.set( search_data[r'Taxable_Pay'])
        self.tax_period.set( search_data[r'Tax_Period'])
        self.tax_code.set( search_data[r'Tax_Code'])
        self.NI_number.set( search_data[r'NI_Number'])
        self.NI_code.set( search_data[r'NI_Code'])
        self.deductions.set( search_data[r'Deductions'])
        self.gross_pay.set( search_data[r'Gross_pay'])
        self.net_pay.set( search_data[r'Net_pay'])
        self.pay_day.set( search_data[r'Pay_Day'])
        self.fill_text_reciept()


    def On_Tree_Select(self, event):
        item = self.tree_view.selection()[0]
        ''' Return Reference Number '''
        return( self.tree_view.item( item )['values'][0] )                            

    def Random( self ):
        self.create_random_employee_information()

    def Reset( self ):
        self.reference.set( '' )      
        self.firstname.set( '' )      
        self.surname.set( '' )        
        self.address.set( '' )        
        self.gender.set( '' )         
        self.mobile.set( '' )         
        self.city.set( '' )           
        self.student_loan.set( '' )   
        self.other_payment.set( '' )  
        self.NI_payment.set( '' )     
        self.basic_salary.set( '' )   
        self.pension.set( '' )        
        self.over_time.set( '' )      
        self.tax.set( '' )            
        self.pensionable_pay.set( '' )
        self.taxable_pay.set( '' )    
        self.tax_period.set( '' )     
        self.tax_code.set( '' )       
        self.NI_number.set( '' )      
        self.NI_code.set( '' )        
        self.deductions.set( '' )     
        self.gross_pay.set( '' )      
        self.net_pay.set( '' )        
        #self.pay_day.set( '' )
        self.text_scroll_reciept.delete( 1.0, tkinter.END )

    def Delete( self, message = True ):
        EMP_REF = self.On_Tree_Select( event = None )
        print( 'Delete EMP_REF', EMP_REF )
        if message == True:
            delete_booking = tkinter.messagebox.askyesno(
                title = 'Employee Management System',
                message = 'Confirm if you want to delete this employee?.' )
            if delete_booking > 0:
                self.Search()
                RV = employee_DB.delete_employee_record( EMP_REF )
                self.Display()
                print( 'Row Count Affected = ', RV )
            else:
                return

    def fill_text_reciept( self ):
        if len( self.text_scroll_reciept.get( 1.0, tkinter.END )) >= 1:
            self.text_scroll_reciept.delete( 1.0, tkinter.END )
        self.text_scroll_reciept.insert( 
                            tkinter.END, '\tMonthly Pay Slip'
                            + '\n\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'Reference:    '+
                            self.reference.get() + '\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'First Name:   '+
                            self.firstname.get() + '\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'Surname:      '+
                            self.surname.get() + '\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'Pay Date:      '+
                            self.pay_day.get() + '\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, '\n\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'Tax:                      '+
                            self.tax.get() + '\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'Pension:               '+
                            self.pension.get() + '\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'Student Loan:       '+
                            self.student_loan.get() + '\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'City Wheighting:   '+
                            self.city.get() + '\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'Deductions:          '+
                            self.deductions.get() + '\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'NI Payment:          '+
                            self.NI_payment.get() + '\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'NI Number:           '+
                            self.NI_number.get() + '\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, '\n\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'Over Time:         '+
                            self.over_time.get() + '\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'Tax Paid:            '+
                            self.taxable_pay.get() + '\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'Gross Pay:          '+
                            self.gross_pay.get() + '\n' )
        self.text_scroll_reciept.insert( 
                            tkinter.END, 'Net Pay:             '+
                            self.net_pay.get() + '\n' )
                         

    def Print_Reciept( self ):
        tmp = self.text_scroll_reciept.get( 1.0, 'tkinter.END - 1c' )
        tmp_file = tempfile.mktemp( '.txt' )
        open( tmp_file, 'w' ).write( tmp )
        os.startfile( tmp_file, 'print' )

        # lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
        # lpr.stdin.write(your_data_here) 
        


#=======================Button Frame Widgets============================

    def create_widgets_button( self ):
        self.btn_add_new = tkinter.Button( self.frm_buttons,
                            font = self.btn_font,
                            borderwidth = 4,
                            background = 'blue',
                            foreground = 'gold',
                            activeforeground = 'gold',
                            activebackground = 'green',
                            command = self.Add_New,
                            text = 'Add New' )
        self.btn_add_new.place( relx = 0.006,
                                rely = 0,
                                relheight = 1 )

        self.btn_print = tkinter.Button( self.frm_buttons,
                            font = self.btn_font,
                            borderwidth = 4,
                            background = 'CadetBlue3',
                            foreground = 'black',
                            activeforeground = 'gold',
                            activebackground = 'green',
                            #command = self.Print,
                            text = 'Print' )
        self.btn_print.place( relx = 0.101,
                              rely = 0,
                              relheight = 1 )

        self.btn_display = tkinter.Button( self.frm_buttons,
                            font = self.btn_font,
                            borderwidth = 4,
                            background = 'steel blue',
                            foreground = 'gold',
                            activeforeground = 'gold',
                            activebackground = 'green',
                            command = self.Display,
                            text = 'Display' )
        self.btn_display.place( relx = 0.167,
                                rely = 0,
                                relheight = 1 )

        self.btn_update = tkinter.Button( self.frm_buttons,
                            font = self.btn_font,
                            borderwidth = 4,
                            background = 'SlateGray4',
                            foreground = 'gold',
                            activeforeground = 'gold',
                            activebackground = 'green',
                            command = self.Update,
                            text = 'Update' )
        self.btn_update.place( relx = 0.250,
                               rely = 0,
                               relheight = 1 )

        self.btn_delete = tkinter.Button( self.frm_buttons,
                            font = self.btn_font,
                            borderwidth = 4,
                            background = 'red4',
                            foreground = 'gold',
                            activeforeground = 'gold',
                            activebackground = 'black',
                            command = self.Delete,
                            text = 'Delete' )
        self.btn_delete.place( relx = 0.332,
                               rely = 0,
                               relheight = 1 )

        self.btn_random = tkinter.Button( self.frm_buttons,
                            font = self.btn_font,
                            borderwidth = 4,
                            background = 'purple1',
                            foreground = 'gold',
                            activeforeground = 'gold',
                            activebackground = 'royal blue',
                            command = self.Random,
                            text = 'Random' )
        self.btn_random.place( relx = 0.407,
                               rely = 0,
                               relheight = 1 )

        self.btn_reset = tkinter.Button( self.frm_buttons,
                            font = self.btn_font,
                            borderwidth = 4,
                            background = 'gray26',
                            foreground = 'gold',
                            activeforeground = 'red',
                            activebackground = 'powder blue',
                            command = self.Reset,
                            text = 'Reset' )
        self.btn_reset.place( relx = 0.497,
                              rely = 0,
                              relheight = 1 )

        self.btn_search = tkinter.Button( self.frm_buttons,
                            font = self.btn_font,
                            borderwidth = 4,
                            background = 'AntiqueWhite4',
                            foreground = 'gold',
                            activeforeground = 'red',
                            activebackground = 'powder blue',
                            command = self.Search,
                            text = 'Search' )
        self.btn_search.place( relx = 0.567,
                               rely = 0,
                               relheight = 1 )

        self.btn_exit = tkinter.Button( self.frm_buttons,
                            font = self.btn_font,
                            borderwidth = 4,
                            background = 'orchid1',
                            foreground = 'gold',
                            activeforeground = 'cyan',
                            activebackground = 'gray8',
                            command = self.Ask_Quit,
                            text = 'Exit' )
        self.btn_exit.place( relx = 0.646,
                             rely = 0,
                             relheight = 1 )

#===================Random Employee Information=========================

    def generate_random_other_pay( self ):
        self.OPD = random.random()
        # print( OPD )
        string_other_pay = '$' + ( '%0.3f' % self.OPD )
        return( string_other_pay )

    def generate_random_over_time( self ):
        self.OT = float( random.randint( 2, 8215 ))
        string_overtime = '$' + str( '%2.f' % ( self.OT ))
        return( string_overtime )

    def generate_random_basic_salary( self ):
        self.BS = float( random.randint( 34051, 809123 ))
        string_basic_salary = '$' + str( '%2.f' % ( self.BS ))
        return( string_basic_salary )

    def generate_random_city_weighting( self ):
        self.CW = float( random.randint( 2456, 18593 ))
        string_city_weighting = '$' + str( '%2.f' % ( self.CW ))
        return( string_city_weighting )

    def generate_random_tax( self ):
        self._tax = (( self.BS + self.CW + self.OT ) * 0.3 )
        string_tax = '$' + str( '%.2f' % ( self._tax ))
        return( string_tax )

    def generate_random_pension( self ):
        self._pension = (( self.BS + self.CW + self.OT ) * 0.02 )
        string_pension = '$' + str( '%.2f' % ( self._pension ))
        return( string_pension )

    def generate_random_student_loan( self ):
        self._student_loan = (( self.BS + self.CW + self.OT ) * 0.012 )
        string_loan = '$' + str( '%.2f' % ( self._student_loan ))
        return( string_loan )

    def generate_random_NI_payment( self ):
        self._NI_payment = (( self.BS + self.CW + self.OT ) * 0.011 )
        string_ni = '$' + str( '%.2f' % ( self._NI_payment ))
        return( string_ni )

    def generate_random_gross_pay( self ):
        self._gross_pay = ( self.BS + self.CW + self.OT )
        string_gross = '$' + str( '%2.f' % ( self._gross_pay ))
        return( string_gross )

    def generate_random_net_pay( self ):
        self._net_pay = ( self.BS + self.CW + self.OT ) - self.DEDUCTIONS
        string_net_pay = '$' + str( '%.2f' % ( self._net_pay ))
        return( string_net_pay )

    def generate_random_deductions( self ):
        self.DEDUCTIONS = ( self._tax +
                       self._pension +
                       self._student_loan +
                       self._NI_payment )
        string_deduct = '$' + str( '%2.f' % ( self.DEDUCTIONS ))
        return( string_deduct )

    def generate_random_ni_code( self ):
        rand_ni_code = secrets.token_hex( 3 )
        string_nicode = ( str( 'NI-' + rand_ni_code ))
        return( string_nicode )

    def generate_random_ni_number( self ):
        ni_pay = random.randint( 34051, 409123 )
        _ni_number = ( 'NI-' + str( ni_pay ))
        return( _ni_number )

    def generate_random_tax_code( self ):
        taxcode = secrets.token_hex( 4 )
        #string_tax_code = ( str( 'TC-' + taxcode ))
        string_tax_code = ( str( taxcode ))
        return( string_tax_code )

    def generate_random_tax_period( self ):
        RTP = random.randint( 4, 13 )
        return( RTP )

    def generate_random_first_name( self ):
        return( names.get_first_name())

    def generate_random_surname( self ):
        return( names.get_last_name())

    def generate_random_address( self ):
        fake = Faker()
        return( fake.address())

    def generate_random_gender( self ):
        ''' Random Gender '''
        RG = random.randint( 1, len( self.ent_gender['values'][:-1] ))
        return( self.ent_gender['values'][RG] )

    def generate_random_mobile_number( self ):
        ''' Yes, well, cell phone number '''
        prefix = ['021', '022', '025', '027', '029']
        pre_cell = str( secrets.choice( prefix ))
        num_cell = str( secrets.randbits( 32 ))
        return( pre_cell + num_cell )

    def create_random_employee_information( self ): # 123
        self.reference.set( str( secrets.token_hex( 6 )))
        self.firstname.set( self.generate_random_first_name())
        self.surname.set( self.generate_random_surname())
        self.address.set( self.generate_random_address())
        self.gender.set( self.generate_random_gender())
        self.mobile.set( self.generate_random_mobile_number())
        self.city.set( self.generate_random_city_weighting())
        self.basic_salary.set( self.generate_random_basic_salary())
        self.over_time.set( self.generate_random_over_time())
        self.other_payment.set( self.generate_random_other_pay())
        self.tax.set( self.generate_random_tax())
        self.pension.set( self.generate_random_pension())
        self.student_loan.set( self.generate_random_student_loan())
        self.NI_payment.set( self.generate_random_NI_payment())
        self.deductions.set( self.generate_random_deductions())
        self.gross_pay.set( self.generate_random_gross_pay())
        self.net_pay.set( self.generate_random_net_pay())
        self.taxable_pay.set( self.tax.get())
        self.pensionable_pay.set( self.pension.get())
        self.NI_code.set( self.generate_random_ni_code())
        self.NI_number.set( self.generate_random_ni_number())
        self.tax_code.set( self.generate_random_tax_code())
        self.tax_period.set( self.generate_random_tax_period())



                              
if __name__ == '__main__':
    root = tkinter.Tk()
    application = Employee( root )
    root.mainloop()