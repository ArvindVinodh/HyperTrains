import mysql.connector
from tabulate import tabulate
#function to delete a customer account
def DeleteAccount(IDno):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="EmiratesA380AR",database="hyperTrains")
    mycursor=mydb.cursor()
    com="select Idno,Name,Pwd from customer where Idno={}".format(IDno)
    mycursor.execute(com)
    result=mycursor.fetchall()
    print(tabulate(result,headers=["ID no","Name","Password"],tablefmt="fancy_grid"))
    choice=input("Are you sure you want to delete this account as it will also cancel bookings you have already made?(Y or N): ")
    if choice in "Yy":
        com="delete from customer where Idno={}".format(IDno)
        mycursor.execute(com)
        mydb.commit()
    else:
        print("Try again later")
        return
#function to delete a booking
def DeleteBooking(IDno):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="EmiratesA380AR",database="hyperTrains")
    mycursor=mydb.cursor()
    
    com="select Name,Pwd from customer where Idno={}".format(IDno)
    mycursor.execute(com)
    result=mycursor.fetchall()
    username=result[0][0]
    Pwd=result[0][1]
    
    com="select fr,reach,FrDate,FrTime,BackDate,R_FrTime,TravelTime,Class,AmountPaid,NumPeople from customer where Idno={}".format(IDno)
    mycursor.execute(com)
    result=mycursor.fetchall()
    print(tabulate(result,headers=["From","To","Out Date","Out Time","Return Date","Return Out Time","Travel Time","Class","Amount Paid","Number of People"],tablefmt="fancy_grid"))
    choice=input("Are you sure you want to delete this booking?(Y or N): ")
    if choice in "Yy":
        com="delete from customer where Idno={}".format(IDno)
        mycursor.execute(com)
        mydb.commit()
        
        query="insert into customer(Idno,Name,Pwd) values(%s,%s,%s)"
        record=(IDno,username,Pwd)
        mycursor.execute(query,record)
        mydb.commit()
        
    else:
        print("Try again later")
        return


#function to modify the departure location of customer
def Modify_FromLocation(IDno):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="EmiratesA380AR",database="hypertrains")
    mycursor=mydb.cursor()
    print()
    print("Current Booking Details:")
    com="select fr,reach,FrDate,FrTime,BackDate,R_FrTime,TravelTime,Class,AmountPaid,NumPeople from customer where Idno={}".format(IDno)
    mycursor.execute(com)
    result=mycursor.fetchall()
    print(tabulate(result,headers=["From","To","Out Date","Out Time","Return Date","Return Out Time","Travel Time","Class","Amount Paid","Number of People"],tablefmt="fancy_grid"))

    print("1:London")
    print("2:Paris")
    print("3:Amsterdam")
    print("4:Berlin")
    print("5:Lyon")

    n=result[0][9]
    amt=int(n)*1000
    s_amt=chr(163)+str(amt)
    
    com="select reach from customer where Idno={}".format(IDno)
    mycursor.execute(com)
    result=mycursor.fetchall()
    c2=result[0][0]

    
    c=int(input("Choose your new Departure Location: "))
    if c==1:
        c1="London"
    elif c==2:
        c1="Paris"
    elif c==3:
        c1="Amsterdam"
    elif c==4:
        c1="Berlin"
    elif c==5:
        c1="Lyon"
    else:
        print("Invalid choice.....try again later")
        return

    query="select TravelTime from locations where fr=%s and reach=%s"
    record=(c1,c2)
    mycursor.execute(query,record)
    result=mycursor.fetchall()
    TravelTime=result[0][0]
    
    com="Update customer Set fr=%s,TravelTime=%s,AmountPaid=%s where Idno=%s"
    record=(c1,TravelTime,s_amt,IDno)
    mycursor.execute(com,record)
    mydb.commit()

    #Display modified ticket details
    print()
    print("Updated Booking Details:")
    com="select fr,reach,FrDate,FrTime,BackDate,R_FrTime,TravelTime,Class,AmountPaid,NumPeople from customer where Idno={}".format(IDno)
    mycursor.execute(com)
    result=mycursor.fetchall()
    print(tabulate(result,headers=["From","To","Out Date","Out Time","Return Date","Return Out Time","Travel Time","Class","Amount Paid","Number of People"],tablefmt="fancy_grid"))

    

        
#function to modify the arrival location of customer     
def Modify_ReachLocation(IDno):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="EmiratesA380AR",database="hypertrains")
    mycursor=mydb.cursor()
    print()
    print("Current Booking Details:")
    com="select fr,reach,FrDate,FrTime,BackDate,R_FrTime,TravelTime,Class,AmountPaid,NumPeople from customer where Idno={}".format(IDno)
    mycursor.execute(com)
    result=mycursor.fetchall()
    print(tabulate(result,headers=["From","To","Out Date","Out Time","Return Date","Return Out Time","Travel Time","Class","Amount Paid","Number of People"],tablefmt="fancy_grid"))
    print("1:London")
    print("2:Paris")
    print("3:Amsterdam")
    print("4:Berlin")
    print("5:Lyon")
    c=int(input("Choose your new Arrvial Location: "))

    n=result[0][9]
    amt=int(n)*1000
    s_amt=chr(163)+str(amt)
    
    com="select fr from customer where Idno={}".format(IDno)
    mycursor.execute(com)
    result=mycursor.fetchall()
    c1=result[0][0]

    if c==1:
        c2="London"
    elif c==2:
        c2="Paris"
    elif c==3:
        c2="Amsterdam"
    elif c==4:
        c2="Berlin"
    elif c==5:
        c2="Lyon"
    else:
        print("Invalid choice.....try again later")
        return

    query="select TravelTime from locations where fr=%s and reach=%s"
    record=(c1,c2)
    mycursor.execute(query,record)
    result=mycursor.fetchall()
    TravelTime=result[0][0]
    
    com="Update customer Set reach=%s,TravelTime=%s,AmountPaid=%s where Idno=%s"
    record=(c2,TravelTime,s_amt,IDno)
    mycursor.execute(com,record)
    mydb.commit()

     #Display modified ticket details
    print()
    print("Updated Booking Details:")
    com="select fr,reach,FrDate,FrTime,BackDate,R_FrTime,TravelTime,Class,AmountPaid,NumPeople from customer where Idno={}".format(IDno)
    mycursor.execute(com)
    result=mycursor.fetchall()
    print(tabulate(result,headers=["From","To","Out Date","Out Time","Return Date","Return Out Time","Travel Time","Class","Amount Paid","Number of People"],tablefmt="fancy_grid"))
    

#function to modify from date of customer
def Modify_FromDate(IDno):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="EmiratesA380AR",database="hypertrains")
    mycursor=mydb.cursor()
    print()
    print("Current Booking Details:")
    com="select fr,reach,FrDate,FrTime,BackDate,R_FrTime,TravelTime,Class,AmountPaid,NumPeople from customer where Idno={}".format(IDno)
    mycursor.execute(com)
    result=mycursor.fetchall()
    print(tabulate(result,headers=["From","To","Out Date","Out Time","Return Date","Return Out Time","Travel Time","Class","Amount Paid","Number of People"],tablefmt="fancy_grid"))


    Year=input("Input new Year: ")
    Month=input("Input new Month: ")
    Date=input("Input new Date: ")
    FromDate=Year+"-"+Month+"-"+Date

    query="Update customer set frDate='{}' where Idno={}".format(FromDate,IDno)
    mycursor.execute(query)
    mydb.commit()
    print()
    print("Updated Booking Details:")
    com="select fr,reach,FrDate,FrTime,BackDate,R_FrTime,TravelTime,Class,AmountPaid,NumPeople from customer where Idno={}".format(IDno)
    mycursor.execute(com)
    result=mycursor.fetchall()
    print(tabulate(result,headers=["From","To","Out Date","Out Time","Return Date","Return Out Time","Travel Time","Class","Amount Paid","Number of People"],tablefmt="fancy_grid"))

    
#function to modify return date of customer
def Modify_ReturnDate(IDno):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="EmiratesA380AR",database="hypertrains")
    mycursor=mydb.cursor()
    print()
    print("Current Booking Details:")
    com="select fr,reach,FrDate,FrTime,BackDate,R_FrTime,TravelTime,Class,AmountPaid,NumPeople from customer where Idno={}".format(IDno)
    mycursor.execute(com)
    result=mycursor.fetchall()
    print(tabulate(result,headers=["From","To","Out Date","Out Time","Return Date","Return Out Time","Travel Time","Class","Amount Paid","Number of People"],tablefmt="fancy_grid"))

    Year=input("Input new Year: ")
    Month=input("Input new Month: ")
    Date=input("Input new Date: ")
    BackDate=Year+"-"+Month+"-"+Date

    com="select AmountPaid from customer where Idno={}".format(IDno)
    mycursor.execute(com)
    result=mycursor.fetchall()
    amt=result[0][0]
    s_amt=amt[1:]
    n_amt=int(s_amt)
    n_amt+=50
    new_s_amt=str(n_amt)
    new_amt=chr(163)+new_s_amt
    

    query="Update customer set BackDate=%s,R_FrTime='8:00am',AmountPaid=%s where Idno=%s"
    record=(BackDate,new_amt,IDno)
    mycursor.execute(query,record)
    mydb.commit()
    print()
    print("Updated Booking Details:")
    com="select fr,reach,FrDate,FrTime,BackDate,R_FrTime,TravelTime,Class,AmountPaid,NumPeople from customer where Idno={}".format(IDno)
    mycursor.execute(com)
    result=mycursor.fetchall()
    print(tabulate(result,headers=["From","To","Out Date","Out Time","Return Date","Return Out Time","Travel Time","Class","Amount Paid","Number of People"],tablefmt="fancy_grid"))


#Submenu for update bookings
def ModifyBooking(IDno):
    while True:
        print("\t\t==================================================")
        print("\t\t**************** Modify Bookings **********************")
        print("1:Modify Departure Location")
        print("2:Modify Arrival Location")
        print("3:Modify Starting date")
        print("4:Modify Return Date")
        print("5:Delete Booking")
        print("6:Return to Homepage")
        print("\t\t==================================================")
        choice=int(input("Enter your choice:"))
        if choice==1:
            Modify_FromLocation(IDno)
        elif choice==2:
            Modify_ReachLocation(IDno)
        elif choice==3:
            Modify_FromDate(IDno)
        elif choice==4:
            Modify_ReturnDate(IDno)            
        elif choice==5:
            DeleteBooking(IDno)
        elif choice==6:
            return
        else:
            print("Invalid choice....try again later")
            conti=input("Press any key to continue")
         

