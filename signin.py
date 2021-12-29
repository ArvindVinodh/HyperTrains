import mysql.connector
import random

from Customer import *

def SignIn():
    while True:
        print("\t\t==================================================")
        print("\t\t*************Hyper Trains Sign In**************")
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="EmiratesA380AR",database="hypertrains")
        mycursor=mydb.cursor()
        choice_=input("Do you wish to exit?(y or n): ")
        if choice_ in "Yy":
            return
        username=""
        pwd=""
        flag=0
        username=input("Enter a Username(max 20 characters): ")
        pwd=input("Enter a password: ")
        c_pwd=input("Re-enter password: ")
        mycursor.execute("select*from customer")
        result=mycursor.fetchall()
        #print(result)
        for k in result:
            if k[1]==username:
                #print(k[1])
                flag=1
        if flag==1:
            print("Username already exists")
            continue
        else:
            if pwd==c_pwd:
                l=[]
                for i in range(1):
                    r=random.randint(1,300)
                    if r not in l:
                        idno=r
                        l.append(r)
                query="insert into customer(Idno,Name,Pwd) values(%s,%s,%s)"
                record=(idno,username,pwd)
                mycursor.execute(query,record)
                mydb.commit()
                print("Account Succesfully created")
                K=input("Press any key..")
                menu_customer(username)
            else:
                print("Passwords do not match")
                print("Please try again")
            
       

