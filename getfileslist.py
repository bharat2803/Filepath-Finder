import sqlite3
import os
from pathlib import Path

def getlist(choice):

    dbconnect = sqlite3.connect("filepathdatabase.sqlite")
    dbcursor = dbconnect.cursor()
    
    def printlist(filetype):
        table=filetype.split('_')[0]+"s"
        dbcursor.execute(f"SELECT DISTINCT {filetype} FROM {table} ORDER BY {filetype}")
        file_list = dbcursor.fetchall()
        for i in range(len(file_list)):
            print(str(i+1)+')'+file_list[i][0])

    if choice == 1:
        print("\n\n  These are all the PDF files present in your system: \n\n")
        printlist("pdf_files")

    elif choice == 2:
        print("\n\n  These are all the Word files present in your system: \n\n")
        printlist("doc_files")

    elif choice == 3:
        print("\n\n  These are all the Excel files present in your system: \n\n")
        printlist("excel_files")

    elif choice == 4:
        extn = input("Enter the extension of the type of files you want to find(eg-'.docx' for word document): ")
        print(f"\n\n  These are all the {extn} files present in your system: \n\n")
        flag=0
        if extn == ".pdf":
            print("gg")
            printlist("pdf_files")
            flag=1
        elif extn == ".docx" or extn == ".doc":
            printlist("doc_files")
            flag=1
        elif extn == ".xls" or extn == ".xlsx":
            printlist("excel_files")
            flag=1
        else:
            dbcursor.execute("SELECT DISTINCT misc_files FROM misc ORDER BY misc_files")
            misc_list = dbcursor.fetchall()
            extn2 = extn[1:]
            j=1
            for i in range(len(misc_list)):
                if '.' in misc_list[i][0]:
                    if extn2 == misc_list[i][0].rsplit('.',1)[1]:
                        print(str(j)+') '+misc_list[i][0])
                        j=j+1
                        flag=1
        if flag == 0:
            print(f"\n\n There are no files with the extension of {extn} or {extn} does not exist")

if __name__ == "__main__":
    getlist(4)
