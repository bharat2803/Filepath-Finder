from filepath import fetchpath
import os
from getfileslist import getlist
from database_generator import generate
from time import sleep

if __name__ == "__main__":

    os.system("cls")
    print("Loading... Creating list of Documents present in your system")
    print("This may take a while... Please wait.")
    generate()      #To create database which contains list of all the files and their path presnt in the system.
    clr = os.system("cls")
    sleep(0.75)
    print("\t \t \t \t\t\tDOCUMENTS LISTER AND PATH FINDER \n \n \n\n\n\n")
    print("\tWelcome to the Documents lister and path finder. falana dhamkana. \n \n\n")
    print("Kindly choose one of the options below:\n\n")
    print("""1. View list of all PDFs present in your system.
2. View list of all Word Documents present in your system.
3. View list of all Excel files present in your system.
4. View list of other miscellaneous files present in your system.
5. View path of a file.
6. Exit\n \n""")

while True:

    choice = input("\nEnter your choice=")
    try:
        if int(choice) not in [1, 2, 3, 4, 5, 6]:
            print("Please enter a valid choice.")
            continue
        else:
            choice = int(choice)
    except ValueError:
        print("Please Enter a Number.")
        continue
    if choice in [1,2,3,4]:

        getlist(choice) #To get the list of all the corresponding files presnt in the system.

    elif choice == 5:

        while True:
            filename = input("\nEnter the name of the file(along with its extension): ")
            filepath = fetchpath(filename)
            if filepath == None:
                continue
            else:
                break

    elif choice == 6:

        print("\n\tThank you for using this software. Wish you a great day ahead!")
        sleep(10)
        exit()

    cont=input("\n \nDo you want to continue?(y/n) ")
    while True:
        if cont == 'n':
            print("\n\tThank you for using this software. Wish you a great day ahead!")
            sleep(5000)
            exit()
        elif cont == 'y':
            break
        else:
            cont = input("\n Please enter either y or n: ")
            continue
