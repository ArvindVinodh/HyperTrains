import mysql.connector
from Customer import *
def LogIn():
    while True:
        print("\t\t==================================================")
        print("\t\t*************Hyper Trains Log In**************")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="EmiratesA380AR",database="hypertrains")
        mycursor=mydb.cursor()
        choice_=input("Do you wish to exit?(y or n): ")
        if choice_ in "Yy":
            return
        username=input("Enter your Username: ")
        pwd=input("Enter password: ")
                    
        if "@hypertrains.com" in username:
            query="select Pwd from employee where Name=%s"
            mycursor.execute(query,(username,))
            record=mycursor.fetchall()
        else:
            query="select * from customer where Name=%s"
            mycursor.execute(query,(username,))
            r=mycursor.fetchall()
            if r==[]:
                print("Wrong Username or Password")
                LogIn()
            query="select Pwd from customer where Name=%s"
            mycursor.execute(query,(username,))
            record=mycursor.fetchall()
            for k in record:
                c_pwd=k[0]
            if pwd==c_pwd:
                menu_customer(username)
            else:
                print("Wrong Username or Password")
            
        
