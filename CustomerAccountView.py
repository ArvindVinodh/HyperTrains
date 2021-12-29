import mysql.connector
from tabulate import tabulate
def View_AccountDetails(IDno):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="EmiratesA380AR",database="HyperTrains")
    mycursor=mydb.cursor()
    mycursor.execute("select Idno,Name,Pwd from Customer where Idno='{}'".format(IDno))
    result=mycursor.fetchall()
    print(tabulate(result,headers=["HyperTrains ID","Name","Password"],tablefmt="fancy_grid"))
    K=input("press any key...")
    return

    
