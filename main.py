#-------------IMPORTS--------------------------------
import sys
import logging
logging.basicConfig(filename='logs.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s -  %(levelname)s -  %(message)s')
try:
    from functions import dataDirect, sqlQuery, dothething, deleteData
    logging.debug("Functions imported successfully!")
except:
    logging.critical("functions.py file not found!")
    print("functions.py file not found!")
    sys.exit
#----------------------------------------------------
print("#" * 70)
print("Welcome to")
print("iMessage Exporter")
print("#" * 70)
print("By continuing, you claim to have read and understand the instructions in the README.")
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
        deleteData()
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