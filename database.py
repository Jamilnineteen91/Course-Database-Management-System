import mysql.connector
from PyQt5.QtWidgets import QMessageBox


class newDatabase():
	def displayMessageBox(self, message):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Warning)
		msgBox.setWindowTitle('Error')
		msgBox.setText(message)
		msgBox.setStandardButtons(QMessageBox.Ok)
		msgBox.exec_()

	def __init__(self):
		# Tests DB server connection
		try:
			self.database = mysql.connector.connect(
				host="localhost",
				user="root",
				password="alienworkshop",
			)

			self.cursor = self.database.cursor()
			# Creates database
			self.cursor.execute("CREATE DATABASE IF NOT EXISTS courseDB;")

			# Creates database tables
			self.cursor.execute("USE courseDB")
			self.cursor.execute("""CREATE TABLE IF NOT EXISTS student(
											student_id INT(7) UNSIGNED NOT NULL PRIMARY KEY,
											first_name VARCHAR(30) NOT NULL,
											last_name VARCHAR(30) NOT NULL,
											gender ENUM('Male','Female','Other'),
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

		except mysql.connector.Error as e:
			message="Database server connection failed\nError:{}".format(e)
			self.displayMessageBox(message)

		except Exception as e:
			message="Unable to initialize database.\nError:{}".format(e)
			self.displayMessageBox(message)

	# <------------------------------------------- Database Tools ----------------------------------------------------->
	def use(self):
		self.cursor.execute("USE courseDB;")

	def save(self):
		self.database.commit()

	def found(self,id,table):# This function aids with error correcting within numerous fuctions.
		self.use()
		self.cursor.execute("SELECT * FROM {}".format(table))
		theTable = self.cursor.fetchall()
		found = False
		if len(theTable)<0:
			found=False
		else:
			for data in theTable:
				if data[0] == id:
					found = True
		return found

	def found_enrollment(self,student_id,course_id):# This function aids with error correcting within the update_
													# enrollment function.
		self.use()
		self.cursor.execute("SELECT * FROM enrollment")
		theTable = self.cursor.fetchall()
		found = False
		if len(theTable)<0:
			found=False
		else:
			for data in theTable:
				if data[0] == student_id and data[1] == course_id:
					found = True
		return found

	# <-------------------------------------- Add/Inserting functions ------------------------------------------------->
	def add_student(self,id,first_name,last_name,gender,address,city,region,country,zip,phone_num):
		if 999999 < id <= 9999999:
			try:
				self.use()
				self.cursor.execute("""INSERT INTO student(student_id, first_name, last_name, gender, address, city, region, country, zip, phone_number)
										VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""", (id,first_name,last_name,gender,address,city,region,country,zip,phone_num),)
				self.save()

			except TypeError as T:
				message="Unable to create new student\nError: Missing required field/s\n{}".format(T)
				self.displayMessageBox(message)
			except Exception as e:
				message="Unable to create new student\nError:{}".format(e)
				self.displayMessageBox(message)
		else:
			message="Unable to create new student\nError: Student id must be 7 digits."
			self.displayMessageBox(message)

	def add_teacher(self,id,first_name,last_name,gender,address,city,region,country,zip,phone_num):
		if 999999 < id <= 9999999:
			try:
				self.use()
				self.cursor.execute("""INSERT INTO teacher(teacher_id, first_name, last_name, gender, address, city, region, country, zip, phone_number)
										VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""", (id,first_name,last_name,gender,address,city,region,country,zip,phone_num),)
				self.save()

			except TypeError:
				message="Unable to create new teacher\nError: missing required field/s"
				self.displayMessageBox(message)

			except Exception as e:
				message="Unable to create new teacher\nError:{}".format(e)
				self.displayMessageBox(message)

		else:
			message="Unable to create new teacher\nError: teacher id must be 7 digits."
			self.displayMessageBox(message)

	def add_course(self,course_id, course_name, description, teacher_id):
		Found=self.found(teacher_id,'teacher')
		if len(course_id) == 7 and Found:
			try:
				self.use()
				self.cursor.execute("""INSERT INTO course(course_id,course_name,description,teacher_id)
									VALUES (%s,%s,%s,%s);""", ( course_id,course_name, description, teacher_id), )
				self.save()

			except TypeError:
				message="Unable to create new course {} with {}\nError: missing required field/s".format(course_name,teacher_id)
				self.displayMessageBox(message)

			except Exception as e:
				message="Unable to create new course {} with {}\nError:{}".format(course_name,teacher_id,e)
				self.displayMessageBox(message)

		else:
			message="Unable to create new course {} with {}\nHint: Ensure course id is 7 characters long and/or teacher id is correct.".format(course_name, teacher_id)
			self.displayMessageBox(message)

	def enroll(self,student_id,course_id,grade):
		Found=self.found(student_id,'enrollment')
		if not Found:
			try:
				self.use()
				self.cursor.execute("""INSERT INTO enrollment(student_id,course_id,grade)
									VALUES (%s,%s,%s);""", (student_id,course_id,grade), )
				self.save()

			except TypeError:
				message="Unable to enroll student {} in {}\nError: missing required field/s".format(student_id,course_id)
				self.displayMessageBox(message)

			except Exception as e:
				message="Unable to enroll student {} in {}\nError:{}".format(student_id,course_id,e)
				self.displayMessageBox(message)
		else:
			message="Error: {} is already enrolled in {}".format(student_id,course_id)
			self.displayMessageBox(message)

	# <------------------------------------- Deletion functions ------------------------------------------------------->

	def delete_student(self,id):
		Found=self.found(id,'student')
		if Found:
			try:
				self.use()
				self.cursor.execute("DELETE FROM enrollment WHERE student_id = %s;", (id,))
				self.cursor.execute("DELETE FROM student WHERE student_id = %s;", (id,))
				self.save()
			except Exception as e:
				message="Unable to delete student {}\nError:{}".format(id,e)
				self.displayMessageBox(message)
		else:
			message="Unable to delete student {}\nError: Student {} DNE".format(id,id)
			self.displayMessageBox(message)

	def delete_teacher(self,id):
		Found=self.found(id,'teacher')
		if Found:
			try:
				self.use()
				self.cursor.execute("UPDATE course SET teacher_id = null WHERE teacher_id = %s;", (id,))
				self.cursor.execute("DELETE FROM teacher WHERE teacher_id= %s;", (id,))
				self.save()
			except Exception as e:
				message="Unable to delete teacher {}\nError:{}".format(id,e)
				self.displayMessageBox(message)
		else:
			message="Unable to delete teacher {}\nError: Teacher {} DNE".format(id,id)
			self.displayMessageBox(message)

	def delete_course(self,id):
		Found=self.found(id,'course')
		if Found:
			try:
				self.use()
				self.cursor.execute("DELETE FROM enrollment WHERE course_id = %s;", (id,))
				self.cursor.execute("DELETE FROM course WHERE course_id = %s;", (id,))
				self.save()
			except Exception as e:
				message="Unable to delete course {}\nError:{}".format(id,e)
				self.displayMessageBox(message)
		else:
			message="Unable to delete course {}\nError: Course {} DNE".format(id,id)
			self.displayMessageBox(message)

	#<---------------------------------------------- Search/Show functions ------------------------------------------>

	def search_student(self,id):
		Found=self.found(id,'student')
		if Found:
			try:
				self.use()
				self.cursor.execute("SELECT * FROM student WHERE student_id = %s;", (id,))
				student=self.cursor.fetchall()
				self.cursor.execute("SELECT * FROM enrollment WHERE student_id = %s ORDER BY course_id;", (id,))
				courses=self.cursor.fetchall()
				course_load=[]
				for classes in courses:
					course_load.append(classes)
				return student, course_load
			except Exception as e:
				message="Error:{}".format(e)
				self.displayMessageBox(message)
		else:
			message="Error: Student {} DNE".format(id)
			self.displayMessageBox(message)

	def search_teacher(self,id):
		Found=self.found(id,'teacher')
		if Found:
			try:
				self.use()
				self.cursor.execute("SELECT * FROM teacher WHERE teacher_id = %s;", (id,))
				teacher=self.cursor.fetchall()
				self.cursor.execute("SELECT * FROM course WHERE teacher_id = %s ORDER BY course_name;", (id,))
				courses=self.cursor.fetchall()
				course_load=[]
				for classes in courses:
					course_load.append(classes)
				return teacher, course_load
			except Exception as e:
				message="Error:{}".format(e)
				self.displayMessageBox(message)
		else:
			message="Error: Teacher {} DNE".format(id)
			self.displayMessageBox(message)

	def search_course(self,id):
		Found=self.found(id,'course')
		if Found:
			try:
				self.use()
				self.cursor.execute("SELECT * FROM course WHERE course_id = %s;",(id,))
				course=self.cursor.fetchall()
				self.cursor.execute("SELECT * FROM enrollment WHERE course_id = %s ORDER BY student_id;",(id,))
				classroom=self.cursor.fetchall()
				enrolled=[]
				for students in classroom:
					enrolled.append(students)
				return course, enrolled
			except Exception as e:
				message="Error:{}".format(e)
				self.displayMessageBox(message)
		else:
			message="Error: Course {} DNE".format(id)
			self.displayMessageBox(message)

# <---------------------------------------------- Up-date functions ------------------------------------------>

	def update_student(self,id,col,val):
		Found = self.found(id, 'student')
		if Found:
			try:
				self.use()
				# Format method is needed to add column names into database
				self.cursor.execute("""UPDATE student SET {} = %s WHERE student_id = %s;""".format(col),(val,id),)
				self.save()
			except Exception as e:
				message="Error:{}".format(e)
				self.displayMessageBox(message)
		else:
			message="Unable to update student {}\nError: Student {} DNE".format(id,id)
			self.displayMessageBox(message)

	def update_teacher(self,id,col,val):
		Found = self.found(id, 'teacher')
		if Found:
			try:
				self.use()
				# Format method is needed to add column names into database
				self.cursor.execute("""UPDATE teacher SET {} = %s WHERE teacher_id = %s;""".format(col), (val, id), )
				self.save()
			except Exception as e:
				message="Error:{}".format(e)
				self.displayMessageBox(message)
		else:
			message="Unable to update teacher {}\nError: Teacher {} DNE".format(id,id)
			self.displayMessageBox(message)


	def update_course(self,id,col,val):
		Found = self.found(id, 'course')
		if Found:
			try:
				self.use()
				# Format method is needed to add column names into database
				self.cursor.execute("""UPDATE course SET {} = %s WHERE course_id = %s;""".format(col), (val,id), )
				self.save()
			except Exception as e:
				message="Error:{}".format(e)
				self.displayMessageBox(message)
		else:
			message="Unable to update course {}\nError: Course {} DNE".format(id,id)
			self.displayMessageBox(message)

	def update_enrollment(self,student_id,course_id,val,col='grade'):
		Found = self.found_enrollment(student_id, course_id)
		if Found:
			try:
				self.use()
				# Format method is needed to add column names into database
				self.cursor.execute("""UPDATE enrollment SET {} = %s WHERE student_id = %s 
									AND course_id = %s""".format(col), (val, student_id, course_id),)
				self.save()
			except Exception as e:
				message="Error:{}".format(e)
				self.displayMessageBox(message)
		else:
			message="""Unable to update enrollment\nError: Unable to identify student {} in course {}""".format(student_id,course_id)
			self.displayMessageBox(message)
