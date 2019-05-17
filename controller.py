from PyQt5 import QtWidgets
from gui import Ui_MainWindow
from database import newDatabase

class controller(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        self.db=newDatabase()
        super(controller, self).__init__()

        # User interface setup from the designer.
        self.setupUi(self)

        # Button connections.
        self.add_pushButton.clicked.connect(self.add_button)
        self.delete_pushButton.clicked.connect(self.delete_button)
        self.search_pushButton.clicked.connect(self.search_button)
        self.update_pushButton.clicked.connect(self.update_button)


    # <------------------------------------------- GUI Tools ------------------------------------------------------>
    def persons_vals(self):
        self.id=int(self.stdnt_tchr_ID_lineEdit.text())
        self.first_name=str(self.first_name_lineEdit.text())
        self.last_name=str(self.last_name_lineEdit.text())
        self.gender_comboBox=self.comboBox.currentText()
        self.address=str(self.address_lineEdit.text())
        self.city=str(self.city_lineEdit.text())
        self.region=str(self.region_lineEdit.text())
        self.country=str(self.country_lineEdit.text())
        self.zip=str(self.zip_lineEdit.text())
        self.telephone=int(self.telephone_lineEdit.text())
        return [self.id, self.first_name, self.last_name, self.gender_comboBox, self.address,self.city, self.region, self.country, self.zip, self.telephone]

    def course_vals(self):
        self.crs_id=str(self.course_id_lineEdit.text())
        self.crs_name=str(self.crs_name_lineEdit.text())
        self.crs_desc=str(self.crs_desc_lineEdit.text())
        self.crs_teacherID=int(self.crs_teacherID_lineEdit.text())
        return [self.crs_id, self.crs_name, self.crs_desc, self.crs_teacherID]

    def enroll_vals(self):
        self.enroll_stdntID=int(self.enroll_stdntID_lineEdit.text())
        self.enroll_crsID=str(self.enroll_crsID_lineEdit.text())
        self.enroll_grade=str(self.enroll_grade_lineEdit.text())
        return [self.enroll_stdntID, self.enroll_crsID, self.enroll_grade]

    def empty_vals(self,array):
        for val in array:
            if len(val.text())>0:
                return False
            else:
                return True

    def clearFields(self):
        self.stdnt_tchr_ID_lineEdit.clear()
        self.first_name_lineEdit.clear()
        self.last_name_lineEdit.clear()
        self.address_lineEdit.clear()
        self.city_lineEdit.clear()
        self.region_lineEdit.clear()
        self.country_lineEdit.clear()
        self.zip_lineEdit.clear()
        self.telephone_lineEdit.clear()

        self.course_id_lineEdit.clear()
        self.crs_name_lineEdit.clear()
        self.crs_desc_lineEdit.clear()
        self.crs_teacherID_lineEdit.clear()

        self.enroll_stdntID_lineEdit.clear()
        self.enroll_crsID_lineEdit.clear()
        self.enroll_grade_lineEdit.clear()


    # <------------------------------------------ Add functions ---------------------------------------------------->
    def add_button(self):
        if self.stdnt_radioButton.isChecked():
            self.stdnt_info=self.persons_vals()
            self.db.add_student(self.stdnt_info[0],self.stdnt_info[1],self.stdnt_info[2],self.stdnt_info[3],self.stdnt_info[4],self.stdnt_info[5],self.stdnt_info[6],self.stdnt_info[7],self.stdnt_info[8],self.stdnt_info[9])


        elif self.tchr_radioButton.isChecked():
            self.tchr_info=self.persons_vals()
            self.db.add_teacher(self.tchr_info[0],self.tchr_info[1],self.tchr_info[2],self.tchr_info[3],self.tchr_info[4],self.tchr_info[5],self.tchr_info[6],self.tchr_info[7],self.tchr_info[8],self.tchr_info[9])


        elif self.crs_radioButton.isChecked():
            self.crs_info=self.course_vals()
            self.db.add_course(self.crs_info[0],self.crs_info[1],self.crs_info[2],self.crs_info[3])


        elif self.enroll_radioButton.isChecked():
            self.enroll_info=self.enroll_vals()
            self.db.enroll(self.enroll_info[0],self.enroll_info[1],self.enroll_info[2])

        self.clearFields()

    # <------------------------------------- Deletion functions ------------------------------------------------------->
    def delete_button(self):
        if self.stdnt_radioButton.isChecked() == True:
            self.db.delete_student(int(self.stdnt_tchr_ID_lineEdit.text()))

        elif self.tchr_radioButton.isChecked() == True:
            self.db.delete_teacher(int(self.stdnt_tchr_ID_lineEdit.text()))

        elif self.crs_radioButton.isChecked() == True:
            self.db.delete_course(str(self.course_id_lineEdit.text()))

    # <---------------------------------- Search/Look-up functions ---------------------------------------------------->

    def search_button(self):
        # Clear table
        self.tableWidget.clear()

        if self.stdnt_radioButton.isChecked():
            # Retrieve data
            self.stdnt_data=self.db.search_student(int(self.stdnt_tchr_ID_lineEdit.text())) # Returns 2 lists, [0] is desired data

            if len(self.stdnt_data)!=0:
                # Set up tableWidget rows and columns
                self.tableWidget.setColumnCount(len(self.stdnt_data[0][0]))
                self.tableWidget.insertRow(0)

                # Display data
                self.column=0
                for data in self.stdnt_data[0][0]:
                    self.tableWidget.setItem(0, self.column, QtWidgets.QTableWidgetItem(str(data)))
                    self.column+=1

                if len(self.stdnt_data)>1:
                    self.row=1
                    for course in self.stdnt_data[self.row]:
                        self.tableWidget.setItem(self.row, 0, QtWidgets.QTableWidgetItem(str(course[1])))
                        self.row+=1


        elif self.tchr_radioButton.isChecked():
            # Retrieve data
            self.tchr_data = self.db.search_teacher(int(self.stdnt_tchr_ID_lineEdit.text()))  # Returns 2 lists, [0] is desired data

            if self.tchr_data!=0:
                # Set up tableWidget rows and columns
                self.tableWidget.setColumnCount(len(self.tchr_data[0][0]))
                self.tableWidget.insertRow(0)

                # Display data
                self.column = 0
                for data in self.tchr_data[0][0]:
                    self.tableWidget.setItem(0, self.column, QtWidgets.QTableWidgetItem(str(data)))
                    self.column += 1

                if len(self.tchr_data)>1:
                    self.row = 1
                    for course in self.tchr_data[self.row]:
                        self.tableWidget.setItem(self.row, 0, QtWidgets.QTableWidgetItem(str(course[1])))
                        self.row += 1


        elif self.crs_radioButton.isChecked():
            # Retrieve data
            self.crs_data = self.db.search_course(str(self.course_id_lineEdit.text()))  # Returns 2 lists, [0] is desired data

            if len(self.crs_data)>0:
                # Set up tableWidget rows and columns
                self.tableWidget.setColumnCount(len(self.crs_data[0][0]))
                self.tableWidget.insertRow(0)

                # Display data
                self.column = 0
                for data in self.crs_data[0][0]:
                    self.tableWidget.setItem(0, self.column, QtWidgets.QTableWidgetItem(str(data)))
                    self.column += 1

            if len(self.crs_data)>0:
                self.row = 1
                for student in self.crs_data[self.row]:
                    self.tableWidget.setItem(self.row, 0, QtWidgets.QTableWidgetItem(str(student[1])))
                    self.row += 1

    def update_button(self):
        if self.stdnt_radioButton.isChecked():
            attr={
                0:'student_id',
                1:'first_name',
                2:'last_name',
                3:'gender',
                4:'address',
                5:'city',
                6:'region',
                7:'country',
                8:'zip',
                9:'phone_number'
                }
            self.vals=self.persons_vals()
            print(self.vals)
            for i in self.vals:
                if i != None:
                    print(i,self.vals[0],attr[i],self.vals[i])
                    self.update_student(self.vals[0],attr[i],self.vals[i])

        elif self.tchr_radioButton.isChecked():
            attr={
                0:'teacher_id',
                1:'first_name',
                2:'last_name',
                3:'gender',
                4:'address',
                5:'city',
                6:'region',
                7:'country',
                8:'zip',
                9:'phone_number'
            }
            self.vals=self.persons_vals()
            for i in self.vals:
                if i != None:
                    self.update_teacher(self.vals[0],attr[i],self.vals[i])

        elif self.crs_radioButton.isChecked():
            attr={
                0:'course_id',
                1:'course_name',
                2:'description',
                3:'teacher_id'
            }
            self.vals=self.persons_vals()
            for i in self.vals:
                if i != None:
                    self.update_course(self.vals[0],attr[i],self.vals[i])

        elif self.enroll_radioButton.isChecked():
            attr={
                0:'student_id',
                1:'course_id',
                2:'grade'
            }
            self.vals=self.persons_vals()
            for i in self.vals:
                if i != None:
                    self.update_enrollment(self.vals[0],attr[i],self.vals[i])



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller=controller()
    controller.show()
    sys.exit(app.exec_())