#-------------IMPORTS--------------------------------
import sys
import os
import logging
logging.basicConfig(filename='logs.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s -  %(levelname)s -  %(message)s')
try:
    from functions import dataDirect, sqlQuery, dothething
    logging.debug("Functions imported successfully!")
except:
    logging.critical("functions.py file not found!")
    print("functions.py file not found!")
    sys.exit
#----------------------------------------------------
print("#" * 70)
print("Welcome to")
print("iMessage Exporter!")
print("#" * 70)
print("By using this program, you")
print("1: claim to have read and understand the instructions in the README.")
print("2: understand this program is under development, and is by no means perfect, therefore errors might occur.")
print("3: understand that Levi Eck (the developer) is not responsible for data loss or other issues that might occur.")
print()
agree = ('1')
disagree = ('2')
while True: 
    print("Type 1 to agree and continue.")
    print("Type 2 to exit the program.")
    print()
    acceptChoice = input(">: ")
    print()
    if acceptChoice in agree:
        while True:
            dataDirect()
            sqlQuery()
            dothething()
            repeatYes = ('y','Y')
            repeatNo = ('n','N')
            print()
            print("Would you like to try again? (y/n)")
            print()
            repeatChoice = input(">: ")
            if repeatChoice in repeatYes:
                continue
            elif repeatChoice in repeatNo:
                break
            else:
                continue
        print()
        print("Thanks for using this program!")
        print("Goodbye!")
        break
    elif acceptChoice in disagree:
        print("Goodbye!")
        print()
        break
    else:
        print("That is not a valid option.")
        print()
print("#" * 70)       
sys.exit