import sqlite3
import os
from pathlib import Path

#To get the filepath of the file given.
def fetchpath(filename):
        try:
            dbconnect = sqlite3.connect("pdfdatabase.sqlite")
            dbcursor = dbconnect.cursor()
            extn = filename.rsplit('.',1)[1]
            if extn == 'pdf':
                dbcursor.execute("SELECT filepath FROM PDFs WHERE pdf_files = ?",(filename,))

            elif extn == 'doc' or extn == 'docx':
                dbcursor.execute("SELECT filepath FROM docs WHERE doc_files = ?",(filename,))

            elif extn == 'xls' or extn == 'xlsx' or extn == 'csv':
                dbcursor.execute("SELECT filepath FROM excels WHERE excel_files = ?",(filename,))

            else:
                dbcursor.execute("SELECT filepath FROM misc WHERE misc_files = ?",(filename,))

            filepaths = dbcursor.fetchall()
            l = len(filepaths)
            if l > 1:
                print(f"There are {l} {filename} files at different locations:\n")
                for i,filepath in enumerate(filepaths):
                    print(i+1,f") {filepath[0]}")
            else:
                print(f"\n\nThe path of the file, {filename}, is: {filepaths[0][0]}")
                return 1
        except:
            print("\n\nFile not found. Please check the name of the file and try again.\n \n")
            return None


if __name__ =="__main__":
    fetchpath("lib.py")
