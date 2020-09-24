import mysql.connector

print("hi.. py...")

mydb = mysql.connector.connect(host="localhost",user="root",passwd="root", database="hetal")

mycursor = mydb.cursor()

mycursor.execute("select * from std")



for i in mycursor:
	print(i)