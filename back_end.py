
import mysql.connector

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
			self.CreateTeacherTable()
			self.CreateCourseTable()
			self.cursor.execute("USE courseDB")
			self.tables=self.cursor.fetchall()
			for i in range(len(self.tables)):
				print(self.tables[i])


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
							student_id INT(7) UNSIGNED NOT NULL PRIMARY KEY,
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
							teacher_id INT(7) UNSIGNED NOT NULL PRIMARY KEY,
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
							course_id INT(7) UNSIGNED NOT NULL PRIMARY KEY,
							teacher_id INT(7) UNSIGNED NOT NULL,
							FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id))""")

	def add_student(self):
		self.cursor.execute("""INSERT INTO student(student_id, first_name, last_name, gender, address, city, region, country, zip, phone_number)
							VALUES ({},{},{},{},{},{},{},{},{},{})""").format(self.studentTeacherIDLineEdit.text(),
                                       										  self.firstNameLineEdit.text(),
                                       										  self.lastNameLineEdit.text(),
                                       										  self.genderNameLineEdit.text(),
                                       										  self.addressLineEdit.text(),
                                       										  self.cityLineEdit.text(),
                                      	 									  self.regionLineEdit.text(),
                                       										  self.countryLineEdit.text(),
                                       										  self.zipLineEdit.text(),
                                       										  self.phoneNumberLineEdit.text())



print("Imported back_end file!")


def main():
	db=newDatabase()
	# db.cursor.execute("USE courseDB")
	# tables=db.cursor.fetchall()
	# for i in range(len(tables)):
	# 	print(tables[i])

if __name__ == '__main__':
	main()


