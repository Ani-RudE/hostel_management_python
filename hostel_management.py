##Header
import random
import datetime
import os
from time import sleep
# from tabulate import tabulate

global a

os.system('cls')

##List Declaration


##Variable Declaration


##Functions
#Home Function
def home():
    os.system('cls')
    print("\t\t\t\t\tWELCOME TO HOSTEL PORTAL\n")
    os.system('cls')
    print("\t\t\t1 -> Hostel Registration\n")
    print("\t\t\t2 -> Room Details\n")
    print("\t\t\t3 -> Hostel Info\n")
    print("\t\t\t4 -> Payment\n")
    print("\t\t\t5 -> Change Login Credentials\n")
    print("\t\t\t6 -> Log Out\n")
    a=int(input("\n\nYour Input: "))
    if (a==1):
        os.system('cls')
        hostelRegn()
    # if (a==2):
    #     x
    # if (a==3):
    #     x
    # if (a==4):
    #     x
    # if (a==5):
    #     x
    # if (a==6):
    #     x

#HostelRegn Function
def hostelRegn():
    os.system('cls')
    print("2A\t->\t2-Sharing AC\n")
    print("2NA\t->\t2-Sharing Non-AC\n")
    print("3A\t->\t3-Sharing AC\n")
    print("3NA\t->\t3-Sharing Non-AC\n")
    print("4A\t->\t4-Sharing AC\n")
    print("4NA\t->\t4-Sharing Non-AC\n")
    print("5A\t->\t5-Sharing AC\n")
    print("5NA\t->\t5-Sharing AC\n")

#Login Function
def login():
    os.system('cls')
    print("\tSRM UNIVERSITY AP")
    print("Enter Your Login Credentials")
    userN=int(input("Username : "))
    pwd=input("Password : ")
    captcha_query=random.randint(0,9)
    print("Captcha :",captcha_query)
    captcha_input=int(input("Enter Captcha : "))

    if (userN==9 and pwd=='9x'):
        if (captcha_input!=captcha_query):
            print("\n\nWrong Captcha Input!\nReloading page...")
            sleep(3)
            os.system('cls')
            login()
        elif (captcha_input==captcha_query):
            os.system('cls')
            os.system('cls')
            home()
    elif (userN!=9999 or pwd!=9999):
        print("\n\nWrong Username or Password\nReloading page...")
        sleep(3)
        os.system('cls')
        login()

##Driver Function
login()