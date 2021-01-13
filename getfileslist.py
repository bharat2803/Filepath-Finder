import sqlite3
import os
from pathlib import Path

def getlist(choice):

    dbconnect = sqlite3.connect("pdfdatabase.sqlite")
    dbcursor = dbconnect.cursor()
    if choice == 1:
        print("\n\n  These are all the PDF files present in your system: \n\n")
        dbcursor.execute("SELECT DISTINCT pdf_files FROM PDFs ORDER BY pdf_files")
        pdfs_list = dbcursor.fetchall()
        for i in range(len(pdfs_list)):
            print(str(i+1)+') '+pdfs_list[i][0])

    elif choice == 2:
        print("\n\n  These are all the Word files present in your system: \n\n")
        dbcursor.execute("SELECT DISTINCT doc_files FROM docs ORDER BY doc_files")
        docs_list = dbcursor.fetchall()
        for i in range(len(docs_list)):
            print(str(i+1)+') '+docs_list[i][0])

    elif choice == 3:
        print("\n\n  These are all the Excel files present in your system: \n\n")
        dbcursor.execute("SELECT DISTINCT excel_files FROM excels ORDER BY excel_files")
        excel_list = dbcursor.fetchall()
        for i in range(len(excel_list)):
            print(str(i+1)+') '+excel_list[i][0])

    elif choice == 4:
        extn = input("Enter the extension of the type of files you want to find(eg-'.docx' for word document): ")
        print(f"\n\n  These are all the {extn} files present in your system: \n\n")
        dbcursor.execute("SELECT DISTINCT misc_files FROM misc ORDER BY misc_files")
        misc_list = dbcursor.fetchall()
        flag = 0
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
