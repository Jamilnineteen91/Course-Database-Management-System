from PyQt5 import QtCore, QtGui, QtWidgets
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
        return [self.id, self.first_name, self.last_name, self.gender_comboBox, self.address,
        self.city, self.region, self.country, self.zip, self.telephone]

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

    def clear(self,fcn):
        alist=fcn
        i=0
        while i<len(alist):
            alist[i]=""
            i+=1

    # <------------------------------------------ Add functions ---------------------------------------------------->
    def add_button(self):
        if self.stdnt_radioButton.isChecked()==True:
            self.stdnt_info=self.persons_vals()
            for val in self.stdnt_info:
                print(val)
            self.db.add_student(self.db,self.stdnt_info[0],self.stdnt_info[1],self.stdnt_info[2],self.stdnt_info[3],self.stdnt_info[4],self.stdnt_info[5],self.stdnt_info[6],self.stdnt_info[7],self.stdnt_info[8],self.stdnt_info[9])
            self.clear(self.persons_vals())

        elif self.tchr_radioButton.isChecked()==True:
            self.tchr_info=self.persons_vals()
            self.db.add_teacher(self,self.tchr_info[0],self.tchr_info[1],self.tchr_info[2],self.tchr_info[3],
            self.tchr_info[4],self.tchr_info[5],self.tchr_info[6],self.tchr_info[7],self.tchr_info[8],self.tchr_info[9])
            self.clear(self.persons_vals())

        elif self.crs_radioButton.isChecked()==True:
            self.crs_info=self.course_vals()
            self.db.add_course(self,self.crs_info[0],self.crs_info[1],self.crs_info[2],self.crs_info[3])
            self.clear(self.course_vals())

        elif self.enroll_radioButton.isChecked()==True:
            self.enroll_info=self.self.enroll_vals()
            self.db.enroll(self,self.enroll_info[0],self.enroll_info[1],self.enroll_info[2])
            self.clear(self.enroll_vals())
        print('Worked!')

    # <------------------------------------- Deletion functions ------------------------------------------------------->
    def delete_button(self):
        if self.stdnt_radioButton.isChecked() == True:
            self.db.delete_student(self,int(self.stdnt_tchr_ID_lineEdit.text()))
            self.clear(self.persons_vals())
            print('worked!')

        elif self.tchr_radioButton.isChecked() == True:
            self.db.delete_teacher(self,int(self.stdnt_tchr_ID_lineEdit.text()))
            self.clear(self.persons_vals())

        elif self.crs_radioButton.isChecked() == True:
            self.db.delete_course(self,str(self.course_id_lineEdit.text()))
            self.clear(self.course_vals())





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller=controller()
    controller.show()
    sys.exit(app.exec_())