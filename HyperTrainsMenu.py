from signin import *
from login import *
from CustomerAccountView import *
from CustomerUpdate import *
def Main_menu():
    while True:
        print("\t\t==================================================")
        print("\t\t*************Welcome to Hyper Trains**************")
        print("\t\t==================================================")
        print("\t\t******************MAIN MENU***********************")
        print("1:Sign In")
        print("2:Log In ")
        print("3:Exit")
        print("\t\t==================================================")

        choice=int(input("enter your choice:"))
        if choice==1:
            SignIn()
        elif choice==2:
            LogIn()
        elif choice==3:
            print("Thank you for using Hyper Trains")
            print("Goodbye")
            K=input("Press any key...")
            return
        else:
            print("Error:invalid choice try again")
            K=input("Press any key...")
Main_menu()
