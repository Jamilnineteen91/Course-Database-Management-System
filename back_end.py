
import mysql.connector
from mysql.connector import errorcode

# mydb = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	password="password",
# 	database="testdb"
# 	)
#
# cur = mydb.cursor()
#
#
# cur.execute("""CREATE TABLE students(
# 			first_name VARCHAR(30),
# 			last_name VARCHAR(30),
# 			age INT(10)
# 			)
# 			""")
# cur.execute("""SHOW TABLES""")
#
# for tb in cur:
# 	print(tb)

class newDatabase:
	def __init__(self, database):
		self.database = mysql.connector.connect(
			host="localhost",
			user="root",
			password="password",
			database="testdb2"
		)
		self.cursor=self.database.cursor()
		self.ConnectionTest()


	def ConnectionTest(self):
		try:
			print(self.database)
		except Exception as e:
			print(e)



if __name__ == '__main__':
	db='test2DB'
	dbu=newDatabase(db)
