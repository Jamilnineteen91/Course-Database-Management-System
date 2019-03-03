
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
			print("Database server connection failed\nError:{}".format(e))

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
							course_id VARCHAR(7) NOT NULL PRIMARY KEY,
							course_name VARCHAR(20) NOT NULL,
							description VARCHAR(200) NOT NULL,
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

	def found(self,id,table):
		self.use()
		self.cursor.execute("SELECT * FROM {}".format(table))
		theTable = self.cursor.fetchall()
		found = None
		if len(theTable)<0:
			found=None
		else:
			for data in theTable:
				if data[0] == id:
					found = True
		return found



	# <-------------------------------------- Add/Inserting functions ------------------------------------------------->
	def add_student(self,id,first_name,last_name,gender,address,city,region,country,zip,phone_num):
		ID = id
		if 999999 < ID <= 9999999:
			try:
				self.use()
				self.cursor.execute("""INSERT INTO student(student_id, first_name, last_name, gender, address, city, region, country, zip, phone_number)
										VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""", (ID,first_name,last_name,gender,address,city,region,country,zip,phone_num),)
				self.save()

			except TypeError:
				print("Unable to create new student\nError: Missing required field/s")

			except Exception as e:
				print("Unable to create new student\nError:{}".format(e))

		else:
			print("Unable to create new student\nError: Student id must be 7 digits.")

	def add_teacher(self,id,first_name,last_name,gender,address,city,region,country,zip,phone_num):
		ID = id
		if 999999 < ID <= 9999999:
			try:
				self.use()
				self.cursor.execute("""INSERT INTO teacher(teacher_id, first_name, last_name, gender, address, city, region, country, zip, phone_number)
										VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""", (ID,first_name,last_name,gender,address,city,region,country,zip,phone_num),)
				self.save()

			except TypeError:
				print("Unable to create new teacher\nError: missing required field/s")

			except Exception as e:
				print("Unable to create new teacher\nError:{}".format(e))

		else:
			print("Unable to create new student\nError: Student id must be 7 digits.")

	def add_course(self, course_name, description, course_id, teacher_id):
		ID=course_id
		if len(ID) == 7:
			try:
				self.use()
				self.cursor.execute("""INSERT INTO course(course_name,description,course_id,teacher_id)
									VALUES (%s,%s,%s,%s);""", (course_name, description, ID, teacher_id), )
				self.save()

			except TypeError:
				print("Unable to create new course {} with {}\nError: missing required field/s".format(course_name,teacher_id))

			except Exception as e:
				print("Unable to create new course {} with {}\nError:{}".format(course_name,teacher_id,e))

		else:
			print("Unable to create new course {} with {}\nError: Course id must be 7 digits.".format(course_name, teacher_id))

	def enroll(self,student_id,course_id,grade):
		Found=self.found(student_id,'enrollment')
		if not Found:
			try:
				self.use()
				self.cursor.execute("""INSERT INTO enrollment(student_id,course_id,grade)
									VALUES (%s,%s,%s);""", (student_id,course_id,grade), )
				self.save()

			except TypeError:
				print("Unable to enroll student {} in {}\nError: missing required field/s".format(student_id,course_id))

			except Exception as e:
				print("Unable to enroll student {} in {}\nError:{}".format(student_id,course_id,e))
		else:
			print("Error: {} is already enrolled in {}".format(student_id,course_id))

	# <------------------------------------- Deletion functions ------------------------------------------------------->

	def delete_student(self,id):
		Found=self.found(id,'student')
		if Found==True:
			try:
				self.use()
				self.cursor.execute("DELETE FROM enrollment WHERE student_id = %s;", (id,))
				self.cursor.execute("DELETE FROM student WHERE student_id = %s;", (id,))
				self.save()
			except Exception as e:
				print("Unable to delete student {}\nError:{}".format(id,e))
		else:
			print("Unable to delete student {}\nError: Student {} DNE".format(id,id))

	def delete_teacher(self,id):
		Found=self.found(id,'teacher')
		if Found==True:
			try:
				self.use()
				self.cursor.execute("UPDATE course SET teacher_id = null WHERE teacher_id = %s;", (id,))
				self.cursor.execute("DELETE FROM teacher WHERE teacher_id= %s;", (id,))
				self.save()
			except Exception as e:
				print("Unable to delete teacher {}\nError:{}".format(id,e))
		else:
			print("Unable to delete teacher {}\nError: Teacher {} DNE".format(id,id))

	def delete_course(self,id):
		Found=self.found(id,'course')
		if Found==True:
			try:
				self.use()
				self.cursor.execute("DELETE FROM enrollment WHERE course_id = %s;", (id,))
				self.cursor.execute("DELETE FROM course WHERE course_id = %s;", (id,))
				self.save()
			except Exception as e:
				print("Unable to delete course {}\nError:{}".format(id,e))
		else:
			print("Unable to delete course {}\nError: Course {} DNE".format(id,id))

	#<---------------------------------------------- Search/Show functions ------------------------------------------>

	def search_student(self,id):
		Found=self.found(id,'student')
		if Found==True:
			try:
				self.use()
				self.cursor.execute("SELECT * FROM student WHERE student_id = %s;", (id,))
				student=self.cursor.fetchall()
				self.cursor.execute("SELECT * FROM enrollment WHERE student_id = %s ORDER BY course_id;", (id,))
				course_load=self.cursor.fetchall()
				print(student)
				for classes in course_load:
					print(classes)
			except Exception as e:
				print("Error:{}".format(e))
		else:
			print("Error: Student {} DNE".format(id))

	def search_teacher(self,id):
		Found=self.found(id,'teacher')
		if Found==True:
			try:
				self.use()
				self.cursor.execute("SELECT * FROM teacher WHERE teacher_id = %s;", (id,))
				teacher=self.cursor.fetchall()
				self.cursor.execute("SELECT * FROM course WHERE teacher_id = %s ORDER BY course_name;", (id,))
				course_load=self.cursor.fetchall()
				print(teacher)
				for classes in course_load:
					print(classes)
			except Exception as e:
				print("Error:{}".format(e))
		else:
			print("Error: Teacher {} DNE".format(id))

	def search_course(self,id):
		Found=self.found(id,'course')
		if Found==True:
			try:
				self.use()
				self.cursor.execute("SELECT * FROM course WHERE course_id = %s;",(id,))
				course=self.cursor.fetchall()
				self.cursor.execute("SELECT * FROM enrollment WHERE course_id = %s ORDER BY student_id;",(id,))
				classroom=self.cursor.fetchall()
				print(course)
				for students in classroom:
					print(students)
			except Exception as e:
				print("Error:{}".format(e))
		else:
			print("Error: Course {} DNE".format(id))



def main():
	db=newDatabase()
	# db.add_student(7644042,'jamil','mbabaali','M','183 eastcote dr.','winnipeg','manitoba','canada','r2n4h4',2049791641)
	# db.add_teacher(8644042,'elon','musk','M','360 wakopa st.','cape town','western cape','south africa','abc123',1234567890)
	# db.add_course('Quantum physics','describes nature at the smallest scales of energy levels of atoms and subatomic particles','phys400',8644042)
	# db.enroll(1234567,'phys400','A+')
	# # db.add_student(1234567,'lebron','james','M','122 nash ave.','new york','new york','USA','t3e6y5',1234567890)
	# db.search_student(1234567)




if __name__ == '__main__':
	main()


