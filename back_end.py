
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

		except mysql.connector.Error as e:
			print(e)

		self.cursor = self.database.cursor()

		# Creates database
		self.cursor.execute("CREATE DATABASE IF NOT EXISTS courseDB")

		# Creates database tables
		use = self.cursor.execute("USE courseDB")
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

		self.cursor.execute("""CREATE TABLE IF NOT EXISTS course(
							course_name VARCHAR(20) NOT NULL,
							description VARCHAR(60) NOT NULL,
							course_id INT(7) UNSIGNED NOT NULL PRIMARY KEY,
							teacher_id INT(7) UNSIGNED NOT NULL,
							FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id))""")



	def ShowTables(self):
		self.cursor.execute("USE courseDB")
		print(self.cursor.execute("SHOW TABLES"))




	def add_student(self):
		self.cursor.execute("USE courseDB")
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
	db.ShowTables()

if __name__ == '__main__':
	main()


