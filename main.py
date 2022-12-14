##Header
import random
import datetime
import os
from time import sleep
# from tabulate import tabulate


os.system('cls')


##Variable Declaration
global a
global i
global key
global roomCode
global cost


##List Declaration
roll=["21001",	"21002",	"21003",	"21004",	"21005",	"21006",	"21007",	"21008",	"21009",	"21010",	
      "21011",	"21012",	"21013",	"21014",	"21015",	"21016",	"21017",	"21018",	"21019",	"21020",	
      "21021",	"21022",	"21023",	"21024",	"21025",	"21026",	"21027",	"21028",	"21029",	"21030",	
      "21031",	"21032",	"21033",	"21034",	"21035",	"21036",	"21037",	"21038",	"21039",	"21040",	
      "21041",	"21042",	"21043",	"21044",	"21045",	"21046",	"21047",	"21048",	"21049",	"21050"]

password=["pass@21001",	"pass@21002",	"pass@21003",	"pass@21004",	"pass@21005",	"pass@21006",	"pass@21007",	"pass@21008",	"pass@21009",	"pass@21010",	
          "pass@21011",	"pass@21012",	"pass@21013",	"pass@21014",	"pass@21015",	"pass@21016",	"pass@21017",	"pass@21018",	"pass@21019",	"pass@21020",	
          "pass@21021",	"pass@21022",	"pass@21023",	"pass@21024",	"pass@21025",	"pass@21026",	"pass@21027",	"pass@21028",	"pass@21029",	"pass@21030",	
          "pass@21031",	"pass@21032",	"pass@21033",	"pass@21034",	"pass@21035",	"pass@21036",	"pass@21037",	"pass@21038",	"pass@21039",	"pass@21040",	
          "pass@21041",	"pass@21042",	"pass@21043",	"pass@21044",	"pass@21045",	"pass@21046",	"pass@21047",	"pass@21048",	"pass@21049",	"pass@21050"]

roomBooked=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
        
bedBooked=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

roomAvailable=[20,40,15,25,10,10,5,5]


##Functions
#Receipt Function
def receipt(key, roomCode, roomBooked, cost):
    os.system('cls')
    print("\n******************** SRM UNIVERSITY *************************\n")
    print("--------------------- Booking Receipt -----------------------\n\n")
    print("\t\tRoll Number: {}".format(roll[key]))
    print("\t\tRoom Type: {}".format(roomCode))
    print("\t\tBed Number: {}".format(roomBooked[key-1]))
    print("\t\tAmount Paid: {}".format(cost))

    f = open("receipt.txt", "w+")

    f.write("\n******************** SRM UNIVERSITY *************************\n")
    f.write("--------------------- Booking Receipt --------------------------\n\n")
    f.write("Roll Number: {}\nRoom Type: {}\nBed Number: {}\nAmount Paid: {}\n\nThank you for the payment...\n\n------------------------------------------".format(key, roomCode, roomBooked[key-1], cost))
    
    f.close()

    print("\n\n\nPess 'any key' to return to home page.")
    ns=input()
    os.system('cls')
    home(key)


#ChangeLogin Function
def changeLogin(key):
    os.system('cls')
    print("Enter your current password:")
    currPass=input()
    print("Enter your new password:")
    newPass=input()
    print("Confirm your new password:")
    confirmPass=input()
    if (currPass==password[key-1]):
        if (newPass==confirmPass):
            password[key-1]=newPass
            print("\n...")
            sleep(1)
            print("\n...")
            sleep(1)
            print("\n...")
            sleep(1)
            os.system('cls')
            print("\n\nPassword changed succesfully!\n")
            print("Redirecting to home page...")
            sleep(3)
            os.system('cls')
            home(key)
        else:
            print("\n\nCheck your new password!\nReloading Page...")
            sleep(3)
            os.system('cls')
            changeLogin(key)
    else:
        print("\n\nWrong password entered!\nReloading Page...")
        sleep(3)
        os.system('cls')
        changeLogin(key)


#Payment Function
def payment(key, roomCode):
    os.system('cls')
    print("{}, Enter your card details below to process your payment".format(roll[key-1]))
    cardNum=input("Card Number: ")
    expDate=input("Expiry Date: ")
    cvv=input("CVV: ")
    if (len(cardNum)!=16 or len(cvv)!=3):
        print("\nInvalid Card!")
        print("\nRedirecting back to Payments.\nPlease wait...")
        sleep(5)
        os.system('cls')
        payment(key, roomCode)
    else:
        if (roomCode=='2A'):
            cost='Rs.1,80,000'
            roomAvailable[0]-=1
            roomBooked[key-1]=random.randint(501,520)
            bedBooked[key-1]=random.randint(1,2)
        if (roomCode=='2NA'):
            cost='Rs.1,55,000'
            roomAvailable[1]-=1
            roomBooked[key-1]=random.randint(401,440)
            bedBooked[key-1]=random.randint(1,2)
        if (roomCode=='3A'):
            cost='Rs.1,60,000'
            roomAvailable[2]-=1
            roomBooked[key-1]=random.randint(301,315)
            bedBooked[key-1]=random.randint(1,3)
        if (roomCode=='3NA'):
            cost='Rs.1,25,000'
            roomAvailable[3]-=1
            roomBooked[key-1]=random.randint(101,125)
            bedBooked[3]=random.randint(1,3)
        if (roomCode=='4A'):
            cost='Rs.1,30,000'
            roomAvailable[4]-=1
            roomBooked[key-1]=random.randint(901,910)
            bedBooked[key-1]=random.randint(1,4)
        if (roomCode=='4NA'):
            cost='Rs.95,000'
            roomAvailable[5]-=1
            roomBooked[key-1]=random.randint(801,810)
            bedBooked[key-1]=random.randint(1,4)
        if (roomCode=='5A'):
            cost='Rs.1,00,000'
            roomAvailable[6]-=1
            roomBooked[key-1]=random.randint(701,705)
            bedBooked[key-1]=random.randint(1,5)
        if (roomCode=='5NA'):
            cost='Rs.80,000'
            roomAvailable[7]-=1
            roomBooked[key-1]=random.randint(601,605)
            bedBooked[key-1]=random.randint(1,5)
        print("Room booked successfully!\n")
        print("Press '1' if you wish to check your room details.")
        print("Press '2' to print the payment receipt.")
        print("Press 'any other key' to return to home page.")
        wp=input(("\n\nYour Input: "))
        if (wp=='1'):
            roomDetail(key)
        elif (wp=='2'):
            receipt(key,roomCode,roomBooked,cost)
        else:
            home(key)

#RoomDetail Function
def roomDetail(key):
    os.system('cls')
    print("Room details for:",roll[key-1],"\n\n")
    if (roomBooked[key-1]==0):
        print("No room is booked\n\n")
        print("Press any key to return to home page.")
        x=input()
        os.system('cls')
        home(key)
    else:
        print("Room Number :", roomBooked[key-1])
        print("Bed Number :", bedBooked[key-1])
        print("\n\nPress any key to return to home page.")
        x=input()
        os.system('cls')
        home(key)

# HostelInfo Function
def hostelInfo(key):
    os.system('cls')
    print("-------------------------------- HOSTEL ROOMS INFO -----------------------------------\n\n")
    print("2-Sharing AC\t\t\t\t\t->\t\t\tRs.1,80,000\n\n")
    print("2-Sharing Non-AC\t\t\t\t->\t\t\tRs.1,55,000\n\n")
    print("3-Sharing A\t\t\t\t\t->\t\t\tRs.1,60,000\n\n")
    print("3-Sharing Non-AC\t\t\t\t->\t\t\tRs.1,25,000\n\n")
    print("4-Sharing AC\t\t\t\t\t->\t\t\tRs.1,30,000\n\n")
    print("4-Sharing Non-AC\t\t\t\t->\t\t\tRs.95,000\n\n")
    print("5-Sharing AC\t\t\t\t\t->\t\t\tRs.1,00,000\n\n")
    print("5-Sharing Non-AC\t\t\t\t->\t\t\tRs.80,000\n\n")
    print("\n\n")
    print("Press any key to return to home page.")
    gg=input()
    os.system('cls')
    home(key)
    # print(tabulate([['2-Sharing AC', 'Rs.1,80,000'],
    #                 ['2-Sharing AC', 'Rs.1,80,000'],
    #                 ['2-Sharing Non-AC', 'Rs.1,55,000'],
    #                 ['2-Sharing AC', 'Rs.1,80,000'],
    #                 ['2-Sharing AC', 'Rs.1,80,000'],
    #                 ['2-Sharing AC', 'Rs.1,80,000'],
    #                 ['2-Sharing AC', 'Rs.1,80,000'],
    #                 ['2-Sharing AC', 'Rs.1,80,000']],
    #                 headers=['Room Type', 'Price\n']))

#HostelRegn Function
def hostelRegn(key):
    os.system('cls')
    print("\n\n2A\t->\t2-Sharing AC\t\t->\t\t", roomAvailable[0],"Rooms Available\n")
    print("2NA\t->\t2-Sharing Non-AC\t->\t\t", roomAvailable[1],"Rooms Available\n")
    print("3A\t->\t3-Sharing AC\t\t->\t\t", roomAvailable[2],"Rooms Available\n")
    print("3NA\t->\t3-Sharing Non-AC\t->\t\t", roomAvailable[3],"Rooms Available\n")
    print("4A\t->\t4-Sharing AC\t\t->\t\t", roomAvailable[4],"Rooms Available\n")
    print("4NA\t->\t4-Sharing Non-AC\t->\t\t", roomAvailable[5],"Rooms Available\n")
    print("5A\t->\t5-Sharing AC\t\t->\t\t", roomAvailable[6],"Rooms Available\n")
    print("5NA\t->\t5-Sharing AC\t\t->\t\t", roomAvailable[7],"Rooms Available\n\n")
    if (roomBooked[key-1]==0):
        print("Press '1' to book your room.")
        print("Press '2' to check room details.")
        print("Press '0' to go back to home page.\n\n")
        x=int(input("\n\nYour Input: "))
        if (x==1):
            print("\n\nEnter the room code that you wish to book:")
            roomCode=input()
            if (roomCode=='2A' or roomCode=='2NA' or roomCode=='3A' or roomCode=='3NA' or roomCode=='4A' or roomCode=='4NA' or roomCode=='5A' or roomCode=='5NA'):
                os.system('cls')
                payment(key, roomCode)
        elif (x==2):
            os.system('cls')
            hostelInfo(key)
        elif (x==0):
            os.system('cls')
            home(key)

    else:
        print("You cannot book another room.\n\n")
        print("Press 'any key' to go back to home page.")
        x=input()
        os.system('cls')
        home(key)


#Home Function
def home(key):
    os.system('cls')
    print("\t\t\tWELCOME TO HOSTEL PORTAL\n")
    print("\t\t\t1 -> Hostel Registration\n")
    print("\t\t\t2 -> Room Details\n")
    print("\t\t\t3 -> Hostel Info\n")
    print("\t\t\t4 -> Change Login Credentials\n")
    print("\t\t\t5 -> Log Out\n")
    a=int(input("\n\nYour Input: "))
    if (a==1):
        os.system('cls')
        hostelRegn(key)
    if (a==2):
        os.system('cls')
        roomDetail(key)
    if (a==3):
        os.system('cls')
        hostelInfo(key)
    if (a==4):
        os.system('cls')
        changeLogin(key)
    if (a==5):
        os.system('cls')
        login()

#Login Function
def login():
    os.system('cls')
    print("\tSRM UNIVERSITY")
    print("\n\nEnter Your Login Credentials...\n")
    userN=(input("Username : "))
    pwd=(input("Password : "))
    captcha_query=random.randint(100000,999999)
    print("\nCaptcha :",captcha_query)
    captcha_input=int(input("Enter Captcha : "))

    loginKey=0
    listlen=len(roll)

    for i in range (0,listlen+1):
        if (userN==roll[i-1] and pwd==password[i-1]):
            if (captcha_input!=captcha_query):
                loginKey=1
                print("\n\nWrong Captcha Input!\nReloading page...")
                sleep(3)
                os.system('cls')
                login()
            elif (captcha_input==captcha_query):
                loginKey=1
                key=i
                os.system('cls')
                os.system('cls')
                home(key)
    if (loginKey==0):
        print("\n\nWrong Username or Password\nReloading page...")
        sleep(3)
        os.system('cls')
        login()
    

##Driver Function
login()
