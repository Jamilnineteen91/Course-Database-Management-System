
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

	def __init__(self):
		# This try and except function ensures a connection to the db server
		try:
			self.database = mysql.connector.connect(
				host="localhost",
				user="root",
				password="password",
			)

			self.cursor = self.database.cursor()
			self.CreateDatabase()
			self.CreateStudentTable()


		except mysql.connector.Error as e:
			print(e)


	def CreateDatabase(self):
		self.cursor.execute("CREATE DATABASE IF NOT EXISTS courseDB")

	def ShowTables(self):
		self.cursor.execute("SHOW TABLES")
		for tables in self.cursor:
			print(tables)

	def CreateStudentTable(self):
		self.cursor.execute("USE courseDB")
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS student(
							student_id INT(10) NOT NULL PRIMARY KEY,
							first_name VARCHAR(30) NOT NULL,
							last_name VARCHAR(30) NOT NULL,
							gender ENUM('M','F','Other'),
							address VARCHAR(50) NOT NULL,
							city VARCHAR(40) NOT NULL,
							region VARCHAR(30) NOT NULL,
							country VARCHAR(30) NOT NULL,
							zip MEDIUMINT UNSIGNED NOT NULL,
							phone_number VARCHAR(20) NOT NULL)""")

	def CreateTeacherTable(self):
		self.cursor.execute("USE courseDB")
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS teacher(
							teacher_id INT(10) NOT NULL PRIMARY KEY,
							first_name VARCHAR(30) NOT NULL,
							last_name VARCHAR(30) NOT NULL,
							gender ENUM('M','F','Other'),
							address VARCHAR(50) NOT NULL,
							city VARCHAR(40) NOT NULL,
							region VARCHAR(30) NOT NULL,
							country VARCHAR(30) NOT NULL,
							zip MEDIUMINT UNSIGNED NOT NULL,
							phone_number VARCHAR(20) NOT NULL)""")

	def CreateCourseTable(self):
		self.cursor.execute("USE courseDB")
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS course(
							course_name VARCHAR(20) NOT NULL,
							description VARCHAR(60) NOT NULL,
							course_id INT(10) PRIMARY KEY,
							teacher_id INT NOT NULL,
							FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)""")






def main():
	DB=newDatabase()
	DB.ShowTables()

if __name__ == '__main__':
	main()
