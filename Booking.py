import mysql.connector
from tabulate import tabulate

def storing_return(fr,reach,FrDate,BackDate,TravelTime,Class_,AmountPaid,NumPeople,username):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="hypertrains")
    mycursor=mydb.cursor()
    print()
    query="update customer set fr=%s,reach=%s,FrDate=%s,FrTime=%s,BackDate=%s,R_FrTime=%s,TravelTime=%s,Class=%s,AmountPaid=%s,NumPeople=%s where Name=%s"
    record=(fr,reach,FrDate,"8:00am",BackDate,"8:00am",TravelTime,Class_,AmountPaid,NumPeople,username)
    mycursor.execute(query,record)
    mydb.commit()
    print()
    print("Booking succesfully done")
    print("Thank you")
    
def storing_out(fr,reach,FrDate,TravelTime,Class_,AmountPaid,NumPeople,username):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="hypertrains")
    mycursor=mydb.cursor()
    print()
    query="update customer set fr=%s,reach=%s,FrDate=%s,FrTime=%s,TravelTime=%s,Class=%s,AmountPaid=%s,NumPeople=%s where Name=%s"
    record=(fr,reach,FrDate,"8:00am",TravelTime,Class_,AmountPaid,NumPeople,username)
    mycursor.execute(query,record)
    mydb.commit()
    print()
    print("Booking succesfully done")
    print("Thank you")
    
def class_return(c3,FC,HP,S):
    print("Class")
    n_c3=int(c3)
    n_FC=int(FC)
    n_HP=int(HP)
    n_S=int(S)
    print("1:First Class(Out and Return) --> ",c3,"x",chr(163)+FC+" =",chr(163)+str(n_c3*n_FC))
    print("2:HyperTrains Premium(Out and Return) --> ",c3,"x",chr(163)+HP+" =",chr(163)+str(n_c3*n_HP))
    print("3:Standard(Out and Return) --> ",c3,"x",chr(163)+S+" =",chr(163)+str(n_c3*n_S))
    c6=input("Enter your choice: ")
    print()
    if c6=="1":
        Class_="First Class"
        AmountPaid=chr(163)+str(n_c3*n_FC)
    elif c6=="2":
        Class_="HyperTrains Premium"
        AmountPaid=chr(163)+str(n_c3*n_HP)
    elif c6=="3":
        Class_="Standard"
        AmountPaid=chr(163)+str(n_c3*n_S)
    return Class_,AmountPaid

def class_out(c3,FC,HP,S):
    print("Class")
    n_c3=int(c3)
    n_FC=int(FC)
    n_HP=int(HP)
    n_S=int(S)
    print("1:First Class --> ",c3,"x",chr(163)+FC+" =",chr(163)+str(n_c3*n_FC))
    print("2:HyperTrains Premium --> ",c3,"x",chr(163)+HP+" =",chr(163)+str(n_c3*n_HP))
    print("3:Standard --> ",c3,"x",chr(163)+S+" =",chr(163)+str(n_c3*n_S))
    c6=input("Enter your choice: ")
    print()
    if c6=="1":
        Class_="First Class"
        AmountPaid=chr(163)+str(n_c3*n_FC)
    elif c6=="2":
        Class_="HyperTrains Premium"
        AmountPaid=chr(163)+str(n_c3*n_HP)
    elif c6=="3":
        Class_="Standard"
        AmountPaid=chr(163)+str(n_c3*n_S)
    return Class_,AmountPaid

def View_Booking(username):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="hypertrains")
    mycursor=mydb.cursor()
    query="select fr,reach,FrDate,FrTime,BackDate,R_FrTime,TravelTime,Class,AmountPaid,NumPeople from customer where Name=%s"
    mycursor.execute(query,(username,))
    record=mycursor.fetchall()
    print(tabulate(record,headers=["From","To","Out Date","Out Time","Return Date","Return Out Time","Travel Time","Class","Amount Paid","Number of people"],tablefmt="fancy_grid"))
    K=input("Press any key...")
    
def Book(username):
    while True:
        print("\t\t==================================================")
        print("\t\t*****************Book a Train*********************")
        print("1:London")
        print("2:Paris")
        print("3:Amsterdam")
        print("4:Berlin")
        print("5:Lyon")
        c1=int(input("From: "))
        if c1==1:
            c1="London"
        elif c1==2:
            c1="Paris"
        elif c1==3:
            c1="Amsterdam"
        elif c1==4:
            c1="Berlin"
        elif c1==5:
            c1="Lyon"
        else:
            print("Invalid choice.....try again later")
            return
        c2=int(input("To: "))
        if c2==1:
            c2="London"
        elif c2==2:
            c2="Paris"
        elif c2==3:
            c2="Amsterdam"
        elif c2==4:
            c2="Berlin"
        elif c2==5:
            c2="Lyon"
        else:
            print("Invalid choice.....try again later")
            return
        print()

        c3=input("Enter number of people: ")
        NumPeople=c3
        print()
        print("Out Date: ")
        c4a=input("Input Year: ")
        c4b=input("Input Month: ")
        c4c=input("Input Date: ")
        FrDate=c4a+"-"+c4b+"-"+c4c
        print()
        c5=input("Do you want a return?(y or n): ")
        if c5 in "Yy":
            print("Return Date: ")
            c5a=input("Input Year: ")
            c5b=input("Input Month: ")
            c5c=input("Input Date: ")
            BackDate=c5a+"-"+c5b+"-"+c5c
        print()
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="hypertrains")
        mycursor=mydb.cursor()
        if c5 in "Yy":
            query="select TravelTime,R_First,R_Premium,R_Standard from locations where fr=%s and reach=%s"
            record=(c1,c2)
            mycursor.execute(query,record)
            result=mycursor.fetchall()
            TravelTime=result[0][0]
            R_First=result[0][1]
            R_Premium=result[0][2]
            R_Standard=result[0][3]
            Class_,AmountPaid=class_return(c3,R_First,R_Premium,R_Standard)
            storing_return(c1,c2,FrDate,BackDate,TravelTime,Class_,AmountPaid,NumPeople,username)
        else:
            query="select TravelTime,First,Premium,Standard from locations where fr=%s and reach=%s"
            record=(c1,c2)
            mycursor.execute(query,record)
            result=mycursor.fetchall()
            TravelTime=result[0][0]
            First=result[0][1]
            Premium=result[0][2]
            Standard=result[0][3]
            Class_,AmountPaid=class_return(c3,First,Premium,Standard)
            storing_out(c1,c2,FrDate,TravelTime,Class_,AmountPaid,NumPeople,username)
        View_Booking(username)
        c=input("Do you want to delete this booking and book another?(amount paid will be refunded)(y or n): ")
        if c in 'Nn':
            return
    
