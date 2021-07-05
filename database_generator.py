import sqlite3
from pathlib import Path
import os

#To create database which contains the list of all the files and their paths present in the system
def generate():
    dbconnect = sqlite3.connect("filepathdatabase.sqlite")

    dbcursor = dbconnect.cursor()

    dbcursor.executescript("""
    DROP TABLE IF EXISTS pdfs;
    DROP TABLE IF EXISTS docs;
    DROP TABLE IF EXISTS excels;
    DROP TABLE IF EXISTS misc;

    CREATE TABLE pdfs (filepath VARCHAR,
                    pdf_files VARCHAR);

    CREATE TABLE docs (filepath VARCHAR,
                    doc_files VARCHAR);

    CREATE TABLE excels (filepath VARCHAR,
                    excel_files VARCHAR);

    CREATE TABLE misc (filepath VARCHAR,
                    misc_files VARCHAR);""")

    #This function is used for recursion to create the path of every file present in the system.
    def creater(pathname):
        for x in os.scandir(pathname):
            try:
                if os.path.isdir(x):
                    nextpath= os.path.join(pathname,x.name+'\\')
                    creater(nextpath)

                if os.path.isfile(x):
                    if x.name.split('.')[-1] == "pdf":
                        filepath= os.path.join(pathname,x.name)
                        dbcursor.execute("INSERT INTO pdfs (filepath,pdf_files) VALUES (?,?)",(filepath,x.name,))

                    elif x.name.split('.')[-1] == "docx" or x.name.split('.')[-1] == "doc":
                        filepath= os.path.join(pathname,x.name)
                        dbcursor.execute("INSERT INTO docs (filepath,doc_files) VALUES (?,?)",(filepath,x.name,))

                    elif x.name.split('.')[-1] == "xls" or x.name.split('.')[-1] == "xlsx" or x.name.split('.')[-1] == 'csv':
                        filepath= os.path.join(pathname,x.name)
                        dbcursor.execute("INSERT INTO excels (filepath,excel_files) VALUES (?,?)",(filepath,x.name,))

                    else:
                        filepath= os.path.join(pathname,x.name)
                        dbcursor.execute("INSERT INTO misc (filepath,misc_files) VALUES (?,?)",(filepath,x.name,))

            except:
                pass

    creater("C:\\Users\\")
    dbconnect.commit()
    dbconnect.close()
