import mysql.connector
from Booking import *
from CustomerAccountView import *
from CustomerUpdate import *
from tabulate import tabulate
def menu_customer(username):
    while True:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="EmiratesA380AR",database="HyperTrains")
        mycursor=mydb.cursor()
        mycursor.execute("select Idno from customer where Name='{}'".format(username))
        result=mycursor.fetchall()
        IDno=result[0][0]
        print("\t\t==================================================")
        print("\t\t**************** Hi",username,"!!**********************")
        print(username,"your HyperTrains ID is",IDno) 
        print("1:Book a Train")
        print("2:View Booking")
        print("3:View Account Details")
        print("4:Modify Bookings")
        print("5:Delete Account")
        print("6:Log Out")
        print("\t\t==================================================")
        choice=int(input("enter your choice:"))
        if choice==1:
            Book(username)
        elif choice==2:
            View_Booking(username)
        elif choice==3:
            View_AccountDetails(IDno)
        elif choice==4:
            ModifyBooking(IDno)
        elif choice==5:
            DeleteAccount(IDno)
            break
        elif choice==6:
            return
        
