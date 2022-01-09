import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
mycursor = mydb.cursor()
mycursor.execute(''' create database if not exists hypertrains ''')
mydb.close()

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="hypertrains")
mycursor = mydb.cursor()

mycursor.execute("create table customer (Idno varchar(5) PRIMARY KEY,"
                     "Name varchar(20),Pwd varchar(20),fr varchar(20),reach varchar(20),frDate date,FrTime varchar(20),BackDate date,R_FrTime varchar(20),"
                 "TravelTime varchar(20),Class varchar(20),AmountPaid varchar(5),NumPeople varchar(4))")
mydb.close()
print("Done Customers")
