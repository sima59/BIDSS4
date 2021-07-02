
##import mysql.connector

#mydb=mysql.connector.connect(
#host="localhost",
#user="taxoffice",
#password="7vGnSPoxPK4PbhLx",
#database="TaxOffice"
#)

#mycursor = mydb.cursor()

#sql = "INSERT INTO Accountdata (PARCEL CODE,RESIDENCE,CITY,Value,COUNTY PROPERTY TAX-Due,SOLID WASTE CHARGE,STATE PROPERTY TAX,TOTAL,TOTAL CREDITS, TOTAL-DUE) VALUES (%s, %s)"
#val = (23456, "RESIDENCE","Mansfield",325000,0,0,8000,8500,0,0)
#mycursor.execute(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record(s) inserted.")