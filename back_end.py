
import mysql.connector
from mysql.connector import errorcode

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="yafvr8udisspac3exec"
	)

print(mydb)