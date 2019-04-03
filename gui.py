# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt5.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from database import newDatabase

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.stdnt_teacher_title_label = QtWidgets.QLabel(self.centralwidget)
        self.stdnt_teacher_title_label.setObjectName("stdnt_teacher_title_label")
        self.gridLayout.addWidget(self.stdnt_teacher_title_label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.stdnt_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.stdnt_radioButton.setObjectName("stdnt_radioButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.stdnt_radioButton)
        self.tchr_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.tchr_radioButton.setObjectName("tchr_radioButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tchr_radioButton)
        self.first_name_label = QtWidgets.QLabel(self.centralwidget)
        self.first_name_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.first_name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.first_name_label.setObjectName("first_name_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.first_name_label)
        self.first_name_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.first_name_lineEdit.setObjectName("first_name_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.first_name_lineEdit)
        self.last_name_label = QtWidgets.QLabel(self.centralwidget)
        self.last_name_label.setObjectName("last_name_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.last_name_label)
        self.last_name_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.last_name_lineEdit.setObjectName("last_name_lineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.last_name_lineEdit)
        self.gender_label = QtWidgets.QLabel(self.centralwidget)
        self.gender_label.setObjectName("gender_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.gender_label)
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setObjectName("address_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.address_label)
        self.address_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.address_lineEdit.setObjectName("address_lineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.address_lineEdit)
        self.city_label = QtWidgets.QLabel(self.centralwidget)
        self.city_label.setObjectName("city_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.city_label)
        self.city_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.city_lineEdit.setObjectName("city_lineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.city_lineEdit)
        self.region_label = QtWidgets.QLabel(self.centralwidget)
        self.region_label.setObjectName("region_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.region_label)
        self.region_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.region_lineEdit.setObjectName("region_lineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.region_lineEdit)
        self.country_label = QtWidgets.QLabel(self.centralwidget)
        self.country_label.setObjectName("country_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.country_label)
        self.country_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.country_lineEdit.setObjectName("country_lineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.country_lineEdit)
        self.zip_label = QtWidgets.QLabel(self.centralwidget)
        self.zip_label.setObjectName("zip_label")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.zip_label)
        self.zip_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.zip_lineEdit.setObjectName("zip_lineEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.zip_lineEdit)
        self.telephone_label = QtWidgets.QLabel(self.centralwidget)
        self.telephone_label.setObjectName("telephone_label")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.telephone_label)
        self.telephone_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.telephone_lineEdit.setObjectName("telephone_lineEdit")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.telephone_lineEdit)
        self.stdnt_tchr_ID_label = QtWidgets.QLabel(self.centralwidget)
        self.stdnt_tchr_ID_label.setObjectName("stdnt_tchr_ID_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.stdnt_tchr_ID_label)
        self.stdnt_tchr_ID_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.stdnt_tchr_ID_lineEdit.setObjectName("stdnt_tchr_ID_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.stdnt_tchr_ID_lineEdit)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.course_title_label = QtWidgets.QLabel(self.centralwidget)
        self.course_title_label.setObjectName("course_title_label")
        self.verticalLayout_2.addWidget(self.course_title_label, 0, QtCore.Qt.AlignHCenter)
        self.crs_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.crs_radioButton.setObjectName("crs_radioButton")
        self.verticalLayout_2.addWidget(self.crs_radioButton, 0, QtCore.Qt.AlignHCenter)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.course_id_label = QtWidgets.QLabel(self.centralwidget)
        self.course_id_label.setObjectName("course_id_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.course_id_label)
        self.course_id_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.course_id_lineEdit.setObjectName("course_id_lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.course_id_lineEdit)
        self.crs_name_label = QtWidgets.QLabel(self.centralwidget)
        self.crs_name_label.setObjectName("crs_name_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.crs_name_label)
        self.crs_name_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.crs_name_lineEdit.setObjectName("crs_name_lineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.crs_name_lineEdit)
        self.desc_label = QtWidgets.QLabel(self.centralwidget)
        self.desc_label.setObjectName("desc_label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.desc_label)
        self.crs_teacherID_label = QtWidgets.QLabel(self.centralwidget)
        self.crs_teacherID_label.setObjectName("crs_teacherID_label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.crs_teacherID_label)
        self.crs_teacherID_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.crs_teacherID_lineEdit.setObjectName("crs_teacherID_lineEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.crs_teacherID_lineEdit)
        self.crs_desc_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.crs_desc_lineEdit.setObjectName("crs_desc_lineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.crs_desc_lineEdit)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.enroll_title_label = QtWidgets.QLabel(self.centralwidget)
        self.enroll_title_label.setObjectName("enroll_title_label")
        self.verticalLayout_2.addWidget(self.enroll_title_label, 0, QtCore.Qt.AlignHCenter)
        self.enroll_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.enroll_radioButton.setObjectName("enroll_radioButton")
        self.verticalLayout_2.addWidget(self.enroll_radioButton, 0, QtCore.Qt.AlignHCenter)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        self.enroll_stdntID_label = QtWidgets.QLabel(self.centralwidget)
        self.enroll_stdntID_label.setObjectName("enroll_stdntID_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.enroll_stdntID_label)
        self.enroll_crsID_label = QtWidgets.QLabel(self.centralwidget)
        self.enroll_crsID_label.setObjectName("enroll_crsID_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.enroll_crsID_label)
        self.enroll_stdntID_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.enroll_stdntID_lineEdit.setObjectName("enroll_stdntID_lineEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.enroll_stdntID_lineEdit)
        self.enroll_crsID_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.enroll_crsID_lineEdit.setObjectName("enroll_crsID_lineEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.enroll_crsID_lineEdit)
        self.enroll_grade_label = QtWidgets.QLabel(self.centralwidget)
        self.enroll_grade_label.setObjectName("enroll_grade_label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.enroll_grade_label)
        self.enroll_grade_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.enroll_grade_lineEdit.setObjectName("enroll_grade_lineEdit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.enroll_grade_lineEdit)
        self.verticalLayout_2.addLayout(self.formLayout_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_pushButton.setObjectName("add_pushButton")
        self.horizontalLayout_2.addWidget(self.add_pushButton)

        self.update_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.update_pushButton.setObjectName("update_pushButton")
        self.horizontalLayout_2.addWidget(self.update_pushButton)
        self.search_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.search_pushButton.setObjectName("search_pushButton")
        self.horizontalLayout_2.addWidget(self.search_pushButton)
        self.delete_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.horizontalLayout_2.addWidget(self.delete_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 919, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.db=newDatabase()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stdnt_teacher_title_label.setText(_translate("MainWindow", "Student/Teacher"))
        self.stdnt_radioButton.setText(_translate("MainWindow", "Student"))
        self.tchr_radioButton.setText(_translate("MainWindow", "Teacher"))
        self.first_name_label.setText(_translate("MainWindow", "First name"))
        self.last_name_label.setText(_translate("MainWindow", "Last name"))
        self.gender_label.setText(_translate("MainWindow", "Gender"))
        self.address_label.setText(_translate("MainWindow", "Address"))
        self.city_label.setText(_translate("MainWindow", "City"))
        self.region_label.setText(_translate("MainWindow", "Region"))
        self.country_label.setText(_translate("MainWindow", "Country"))
        self.zip_label.setText(_translate("MainWindow", "Zip"))
        self.telephone_label.setText(_translate("MainWindow", "Telephone number"))
        self.stdnt_tchr_ID_label.setText(_translate("MainWindow", "Student/Teacher ID"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Other"))
        self.course_title_label.setText(_translate("MainWindow", "Course"))
        self.crs_radioButton.setText(_translate("MainWindow", "Course"))
        self.course_id_label.setText(_translate("MainWindow", "Course ID"))
        self.crs_name_label.setText(_translate("MainWindow", "Course name"))
        self.desc_label.setText(_translate("MainWindow", "Description"))
        self.crs_teacherID_label.setText(_translate("MainWindow", "Teacher ID"))
        self.enroll_title_label.setText(_translate("MainWindow", "Enrollment"))
        self.enroll_radioButton.setText(_translate("MainWindow", "Enrollment"))
        self.enroll_stdntID_label.setText(_translate("MainWindow", "Student ID"))
        self.enroll_crsID_label.setText(_translate("MainWindow", "Course ID"))
        self.enroll_grade_label.setText(_translate("MainWindow", "Grade"))
        self.add_pushButton.setText(_translate("MainWindow", "Add"))
        self.update_pushButton.setText(_translate("MainWindow", "Update"))
        self.search_pushButton.setText(_translate("MainWindow", "Search"))
        self.delete_pushButton.setText(_translate("MainWindow", "Delete"))

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
        for val in alist:
            val=""


    def add_button(self):
        if self.stdnt_radioButton.isChecked()==True and self.empty_vals(self.persons_vals())==False:
            self.stdnt_info=self.persons_vals()
            self.db.add_student(self.stdnt_info[0],self.stdnt_info[1],self.stdnt_info[2],self.stdnt_info[3],
            self.stdnt_info[4],self.stdnt_info[5],self.stdnt_info[6],self.stdnt_info[7],self.stdnt_info[8],self.stdnt_info[9])

        elif self.tchr_radioButton.isChecked()==True and self.empty_vals(self.persons_vals())==False:
            self.tchr_info=self.persons_vals()
            self.db.add_teacher(self.tchr_info[0],self.tchr_info[1],self.tchr_info[2],self.tchr_info[3],
            self.tchr_info[4],self.tchr_info[5],self.tchr_info[6],self.tchr_info[7],self.tchr_info[8],self.tchr_info[9])

        elif self.crs_radioButton.isChecked()==True and self.empty_vals(self.course_vals())==False:
            self.crs_info=self.course_vals()
            self.db.add_course(self.crs_info[0],self.crs_info[1],self.crs_info[2],self.crs_info[3])

        elif self.enroll_radioButton.isChecked()==True and self.empty_vals(self.enroll_vals())==False:
            self.enroll_info=self.self.enroll_vals()
            self.db.enroll(self.enroll_info[0],self.enroll_info[1],self.enroll_info[2])

        self.add_pushButton.clicked().connect(self.add_button())

    def delete_button(self):
        if self.stdnt_radioButton.isChecked() == True:
            self.db.delete_student(int(self.stdnt_tchr_ID_lineEdit.text()))

        elif self.tchr_radioButton.isChecked() == True:
            self.db.delete_teacher(int(self.stdnt_tchr_ID_lineEdit.text()))

        elif self.crs_radioButton.isChecked() == True:
            self.db.delete_course(str(self.course_id_lineEdit.text()))

        self.delete_pushButton.clicked().connect(self.delete_button())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

