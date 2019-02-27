
import mysql.connector

class newDatabase:

	def __init__(self):
		# Tests DB server connection
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
		self.cursor.execute("CREATE DATABASE IF NOT EXISTS courseDB;")

		# Creates database tables
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
							zip VARCHAR(6) NOT NULL,
							phone_number INT(20) NOT NULL);""")

		self.cursor.execute("""CREATE TABLE IF NOT EXISTS teacher(
							teacher_id INT(7) UNSIGNED PRIMARY KEY,
							first_name VARCHAR(30) NOT NULL,
							last_name VARCHAR(30) NOT NULL,
							gender ENUM('M','F','Other'),
							address VARCHAR(50) NOT NULL,
							city VARCHAR(40) NOT NULL,
							region VARCHAR(30) NOT NULL,
							country VARCHAR(30) NOT NULL,
							zip VARCHAR(6) NOT NULL,
							phone_number INT(20) NOT NULL);""")

		self.cursor.execute("""CREATE TABLE IF NOT EXISTS course(
							course_name VARCHAR(20) NOT NULL,
							description VARCHAR(60) NOT NULL,
							course_id VARCHAR(7) NOT NULL PRIMARY KEY,
							teacher_id INT(7) UNSIGNED,
							FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id));""")



		self.cursor.execute("""CREATE TABLE IF NOT EXISTS enrollment(
									student_id INT(7) UNSIGNED NOT NULL,
    								course_id VARCHAR(7) NOT NULL,
    								grade VARCHAR(2),
    								FOREIGN KEY (student_id) REFERENCES student(student_id),
    								FOREIGN KEY (course_id) REFERENCES course(course_id));""")

	# <------------------------------------------- Database Tools ----------------------------------------------------->
	def use(self):
		self.cursor.execute("USE courseDB;")

	def save(self):
		self.database.commit()


	# <-------------------------------------- Add/Inserting functions ------------------------------------------------->
	def add_student(self,id,first_name,last_name,gender,address,city,region,country,zip,phone_num):
		self.use()
		self.cursor.execute("""INSERT INTO student(student_id, first_name, last_name, gender, address, city, region, country, zip, phone_number)
							VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""", (id,first_name,last_name,gender,address,city,region,country,zip,phone_num),)
		self.save()

	def add_teacher(self,id,first_name,last_name,gender,address,city,region,country,zip,phone_num):
		self.use()
		self.cursor.execute("""INSERT INTO teacher(teacher_id, first_name, last_name, gender, address, city, region, country, zip, phone_number)
							VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""", (id,first_name,last_name,gender,address,city,region,country,zip,phone_num),)
		self.save()

	def add_course(self, course_name, description, course_id, teacher_id):
		self.use()
		self.cursor.execute("""INSERT INTO course(course_name,description,course_id,teacher_id)
							VALUES (%s,%s,%s,%s);""", (course_name, description, course_id, teacher_id), )
		self.save()

	def enroll(self,student_id,course_id,grade):
		self.use()
		self.cursor.execute("""INSERT INTO enrollment(student_id,course_id,grade)
							VALUES (%s,%s,%s);""", (student_id,course_id,grade), )
		self.save()

	# <------------------------------------- Deletion functions ------------------------------------------------------->

	def delete_student(self,id):
		self.use()
		self.cursor.execute("DELETE FROM enrollment WHERE student_id = %s;", (id,))
		self.cursor.execute("DELETE FROM student WHERE student_id = %s;", (id,))
		self.save()

	def delete_teacher(self,id):
		self.use()
		self.cursor.execute("UPDATE course SET teacher_id = null WHERE teacher_id = %s;", (id,))
		self.cursor.execute("DELETE FROM teacher WHERE teacher_id= %s;", (id,))
		self.save()

	def delete_course(self,id):
		self.use()
		self.cursor.execute("DELETE FROM enrollment WHERE course_id = %s;", (id,))
		self.cursor.execute("DELETE FROM course WHERE course_id = %s;", (id,))
		self.save()






def main():
	db=newDatabase()
	# db.add_student(7644042,'jamil','mbabaali','M','183 eastcote dr.','winnipeg','manitoba','canada','r2n4h4',2049791641)
	# db.add_teacher(8644042,'elon','musk','M','360 wakopa st.','cape town','western cape','south africa','abc123',1234567890)
	# db.add_course('physics','classical mechanics','phys101',8644042)
	# db.enroll(7644042,'phys101','A+')
	# db.delete_course('phys101')
if __name__ == '__main__':
	main()


