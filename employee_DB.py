#!/usr/bin/env python3
# coding = utf-8
import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, r'employee.sqlite3' )


def get_conn():
    con = None
    #db_file = ( r'employee.sqlite3' )
    try:
        con = sqlite3.connect( db_path,
        detect_types = sqlite3.PARSE_COLNAMES | sqlite3.PARSE_DECLTYPES )
        # print( con )
        print( sqlite3.version )
        print( 'Successfull Connection!' )
        return con
    except sqlite3.Error as e:
        print( e )

def delete_employee_record( EMP_REF ):
    delete_employee_sql = '''DELETE FROM Employee
                             WHERE Reference = ?;'''
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute( delete_employee_sql, ( EMP_REF, ))
    conn.commit()

def view_employee_record():
    view_employee_sql = '''SELECT   Reference          ,
                                    Firstname          ,
                                    Surname            ,
                                    Address            ,
                                    Gender             ,
                                    Mobile             ,
                                    City_Weighting     ,
                                    Other_Payment      ,
                                    Basic_Salary       ,
                                    Over_Time          ,
                                    Student_Loan       ,
                                    NI_Payment         ,
                                    Pension            ,
                                    Tax                ,
                                    Pensionable_Pay    ,
                                    Taxable_Pay        ,
                                    Tax_Period         ,
                                    Tax_Code           ,
                                    NI_Number          ,
                                    NI_Code            ,
                                    Deductions         ,
                                    Gross_Pay          ,
                                    Net_Pay            ,
                                    Pay_Day            
                           FROM Employee;''' 
    conn = get_conn()
    conn.row_factory = sqlite3.Row  # table_data['Firstname']
    cursor = conn.cursor()
    cursor.execute( view_employee_sql )
    view_employee_data = cursor.fetchall()
    print( 'Employee Table Data Successfully Fetched!' )
    cursor.close()
    conn.close()
    return( view_employee_data )

def add_employee_record( employee_record ):
    add_employee_sql = '''INSERT OR REPLACE INTO Employee(
                                                 Reference          ,
                                                 Firstname          ,
                                                 Surname            ,
                                                 Address            ,
                                                 Gender             ,
                                                 Mobile             ,
                                                 City_Weighting     ,
                                                 Other_Payment      ,
                                                 Basic_Salary       ,
                                                 Over_Time          ,
                                                 Student_Loan       ,
                                                 NI_Payment         ,
                                                 Pension            ,
                                                 Tax                ,
                                                 Pensionable_Pay    ,
                                                 Taxable_Pay        ,
                                                 Tax_Period         ,
                                                 Tax_Code           ,
                                                 NI_Number          ,
                                                 NI_Code            ,
                                                 Deductions         ,
                                                 Gross_Pay          ,
                                                 Net_Pay            ,
                                                 Pay_Day )            
        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? );'''
    conn = get_conn()
    cursor = conn.cursor()
    cursor.executemany( add_employee_sql, employee_record )
    conn.commit()
    print( 'Inserted Employee Record Successfully!' )
    last_row_id = cursor.lastrowid
    cursor.close()
    conn.close()
    print( 'Database Employee Is Closed!' )
    return( last_row_id )

def update_employee_record( employee_record ):
    update_employee_sql = '''UPDATE Employee SET Reference          = ?, 
                                                 Firstname          = ?,
                                                 Surname            = ?,
                                                 Address            = ?,
                                                 Gender             = ?,
                                                 Mobile             = ?,
                                                 City_Weighting     = ?,
                                                 Other_Payment      = ?,
                                                 Basic_Salary       = ?,
                                                 Over_Time          = ?,
                                                 Student_Loan       = ?,
                                                 NI_Payment         = ?,
                                                 Pension            = ?,
                                                 Tax                = ?,
                                                 Pensionable_Pay    = ?,
                                                 Taxable_Pay        = ?,
                                                 Tax_Period         = ?,
                                                 Tax_Code           = ?,
                                                 NI_Number          = ?,
                                                 NI_Code            = ?,
                                                 Deductions         = ?,
                                                 Gross_Pay          = ?,
                                                 Net_Pay            = ?,
                                                 Pay_Day            = ?            
                             WHERE Reference = ?;'''
    conn = get_conn()
    cursor = conn.cursor()
    cursor.executemany( update_employee_sql, employee_record )
    conn.commit()
    print( 'Employee Record Updated Successfully!' )
    cursor.close()
    conn.close()
    
def search_employee_record( EMP_REF ):
    search_employee_sql = '''SELECT Reference          ,      
                                    Firstname          ,
                                    Surname            ,        
                                    Address            ,
                                    Gender             ,
                                    Mobile             ,
                                    City_Weighting     ,
                                    Other_Payment      ,
                                    Basic_Salary       ,
                                    Over_Time          ,
                                    Student_Loan       ,
                                    NI_Payment         ,
                                    Pension            ,
                                    Tax                ,
                                    Pensionable_Pay    ,
                                    Taxable_Pay        ,
                                    Tax_Period         ,
                                    Tax_Code           ,
                                    NI_Number          ,
                                    NI_Code            ,
                                    Deductions         ,
                                    Gross_Pay          ,
                                    Net_Pay            ,
                                    Pay_Day            
                             FROM Employee
                             WHERE Reference = ?;'''
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute( search_employee_sql, ( EMP_REF, ))
    search_employee_data = cursor.fetchone()
    cursor.close()
    conn.close()
    print( 'Search Employee Record Is Good!' )
    return( search_employee_data )

def delete_employee_record( EMP_REF ):
    delete_employee_sql = '''DELETE FROM Employee 
                             WHERE Reference = ?'''
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute( delete_employee_sql, ( EMP_REF, ))
    RC = cursor.rowcount
    conn.commit()
    print( 'Employee Record Deleted!' )
    return( RC )


def create_employee_table():
    employee_sql = '''CREATE TABLE IF NOT EXISTS Employee
                      ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Reference          TEXT,
                        Firstname          TEXT,
                        Surname            TEXT,
                        Address            TEXT,
                        Gender             TEXT,
                        Mobile             TEXT,
                        City_Weighting     TEXT,
                        Other_Payment      TEXT,
                        Basic_Salary       TEXT,
                        Over_Time          TEXT,
                        Student_Loan       TEXT,
                        NI_Payment         TEXT,
                        Pension            TEXT,
                        Tax                TEXT,
                        Pensionable_Pay    TEXT,
                        Taxable_Pay        TEXT,
                        Tax_Period         TEXT,
                        Tax_Code           TEXT,
                        NI_Number          TEXT,
                        NI_Code            TEXT, 
                        Deductions         TEXT,
                        Gross_Pay          TEXT,
                        Net_Pay            TEXT,
                        Pay_Day            TEXT
                         );'''
    conn = get_conn()
    cursor = conn.cursor()
    cursor.executescript( employee_sql )
    conn.commit()
    print( 'Created Employee Table Successfully!' )
    cursor.close()
    conn.close()
    print( 'Database Employee Is Closed!' )

'''Run this only once to create the database and employee table'''
#create_employee_table()

                          