import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="EmiratesA380AR")
mycursor=mydb.cursor()
mycursor.execute(''' create database if not exists hypertrains ''')
mydb.close()

mydb=mysql.connector.connect(host="localhost",user="root",passwd="EmiratesA380AR",database="hyperTrains")
mycursor=mydb.cursor()
mycursor.execute("create table locations (fr varchar(20),"
                     "reach varchar(20),TravelTime varchar(3),R_First varchar(5),R_Premium varchar(5),R_Standard varchar(5),First varchar(5),Premium varchar(5),Standard varchar(5))")
mydb.close()

mydb=mysql.connector.connect(host="localhost",user="root",passwd="EmiratesA380AR",database="hyperTrains")
mycursor=mydb.cursor()
com = """INSERT INTO locations (fr,reach,TravelTime,R_First,R_Premium,R_Standard,First,Premium,Standard)
                            VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s)"""

records = [("London","Paris","2h", "1050","650","250","1000","600","200"),
           ("London","Amsterdam","4h","1050","650","250","1000","600","200"),
           ("London","Berlin","9h", "1050","650","250","1000","600","200"),
           ("London","Lyon","7h","1050","650","250","1000","600","200"),
           ("Paris","London","2h","1000","550","150","950","500","100"),
           ("Paris","Amsterdam","3h","1000","550","150","950","500","100"),
           ("Paris","Berlin","8h","1000","550","150","950","500","100"),
           ("Paris","Lyon","2h","1000","550","150","950","500","100"),
           ("Amsterdam","London","4h","850","550","350","800","500","300"),
           ("Amsterdam","Paris","3h","850","550","350","800","500","300"),
           ("Amsterdam","Berlin","6h","850","550","350","800","500","300"),
           ("Amsterdam","Lyon","6h","850","550","350","800","500","300"),
           ("Berlin","London","9h","980","750","250","930","700","200"),
           ("Berlin","Paris","8h","980","750","250","930","700","200"),
           ("Berlin","Amsterdam","6h","980","750","250","930","700","200"),
           ("Berlin","Lyon","10h","980","750","250","930","700","200"),
           ("Lyon","London","7h","950","850","350","900","800","300"),
           ("Lyon","Paris","2h","950","850","350","900","800","300"),
           ("Lyon","Amsterdam","6h","950","850","350","900","800","300"),
           ("Lyon","Berlin","10h","950","850","350","900","800","300")]
mycursor.executemany(com,records)
mydb.commit()
mydb.close()

print("done locations")
