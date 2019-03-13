import sys
sys.path.append('../')
import unittest
from unittest.mock import patch
from back_end import newDatabase

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = newDatabase()

    def tearDown(self):
        self.db.cursor.execute("DROP DATABASE IF EXISTS courseDB;")
        print('tearDown\n')

#<----------------------------------------------- Init Test ----------------------------------------------------------->

#     def test_newDatabase(self):
#         self.assertIsInstance(self.db,newDatabase)
#
# #<----------------------------------------------- Add f(x) Tests ------------------------------------------------------>
#     def test_add_student(self):
#
#         self.db.add_student(7644042,'jamil','mbabaali','M','183 eastcote dr.','winnipeg','manitoba','canada','r2n4h4',2049791641)
#         self.db.cursor.execute("SELECT * FROM student WHERE student_id=7644042")
#         self.studentA=self.db.cursor.fetchall()
#         print(self.studentA)
#
#         self.db.use()
#         self.db.cursor.execute("SELECT * FROM student;")
#         self.studentB=self.db.cursor.fetchall()
#         print(self.studentB)
#
#         self.assertEqual(self.studentA,self.studentB)
#         print('Add student')
#
#     def test_add_teacher(self):
#         self.db.add_teacher(8644042,'elon','musk','M','360 wakopa st.','cape town','western cape','south africa','abc123',1234567890)
#         self.db.cursor.execute("SELECT * FROM teacher WHERE teacher_id=8644042")
#         self.teacherA = self.db.cursor.fetchall()
#         print(self.teacherA)
#
#         self.db.use()
#         self.db.cursor.execute("SELECT * FROM teacher;")
#         self.teacherB = self.db.cursor.fetchall()
#         print(self.teacherB)
#
#         self.assertEqual(self.teacherA, self.teacherB)
#         print('Add teacher')
#
#     def test_add_course(self):
#         self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa','abc123', 1234567890)
#         self.db.add_course('Quantum physics','describes nature at the smallest scales of energy levels of atoms and subatomic particles','phys400',8644042)
#         self.db.cursor.execute("SELECT * FROM course WHERE course_id='phys400'")
#         self.courseA = self.db.cursor.fetchall()
#         print(self.courseA)
#
#         self.db.use()
#         self.db.cursor.execute("SELECT * FROM course;")
#         self.courseB = self.db.cursor.fetchall()
#         print(self.courseB)
#
#         self.assertEqual(self.courseA, self.courseB)
#         print('Add course')
#
#     def test_enroll(self):
#         self.db
#         self.db.add_student(1234567, 'lebron', 'james', 'M', '122 nash ave.', 'new york', 'new york', 'USA', 't3e6y5',1234567890)
#         self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa','abc123', 1234567890)
#         self.db.add_course('Quantum physics','describes nature at the smallest scales of energy levels of atoms and subatomic particles','phys400', 8644042)
#         self.db.enroll(1234567, 'phys400', 'A+')
#
#         self.db.use()
#         self.db.cursor.execute("SELECT * FROM enrollment WHERE student_id=1234567")
#         self.A = self.db.cursor.fetchall()
#         print(self.A)
#
#         self.db.use()
#         self.db.cursor.execute("SELECT * FROM enrollment WHERE student_id=1234567;")
#         self.B = self.db.cursor.fetchall()
#         print(self.B)
#
#         self.assertEqual(self.A, self.B)
#         print('Enroll')
#
#     # <----------------------------------------------- Delete f(x) Tests ---------------------------------------------->
#
    # def test_delete_student(self):
    #     self.db.add_student(7644042, 'jamil', 'mbabaali', 'M', '183 eastcote dr.', 'winnipeg', 'manitoba', 'canada',
    #                         'r2n4h4', 2049791641)
    #     self.db.delete_student(7644042)
    #
    #     self.db.use()
    #     self.db.cursor.execute("SELECT * FROM student;")
    #     self.student = self.db.cursor.fetchall()
    #     print(self.student)
    #
    #     self.empty=[]
    #
    #     self.assertEqual(self.student,self.empty)
    #     print('Delete student')
#
#     def test_delete_teacher(self):
#         self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa','abc123', 1234567890)
#         self.db.delete_teacher(8644042)
#
#         self.db.use()
#         self.db.cursor.execute("SELECT * FROM teacher;")
#         self.teacher = self.db.cursor.fetchall()
#         print(self.teacher)
#
#         self.empty=[]
#
#         self.assertEqual(self.teacher,self.empty)
#         print('Delete teacher')
#
#     def test_delete_course(self):
#         self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa','abc123', 1234567890)
#         self.db.add_course('Quantum physics','describes nature at the smallest scales of energy levels of atoms and subatomic particles','phys400', 8644042)
#         self.db.delete_course('phys400')
#
#         self.db.use()
#         self.db.cursor.execute("SELECT * FROM course;")
#         self.course = self.db.cursor.fetchall()
#         print(self.course)
#
#         self.empty = []
#
#         self.assertEqual(self.course, self.empty)
#         print('Delete course')
#
# #<----------------------------------------------- Search f(x) Tests --------------------------------------------------->
#
#     def test_search_student(self):
#         self.db.add_student(7644042, 'jamil', 'mbabaali', 'M', '183 eastcote dr.', 'winnipeg', 'manitoba', 'canada',
#                             'r2n4h4', 2049791641)
#         self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa',
#                             'abc123', 1234567890)
#         self.db.add_course('Quantum physics',
#                            'describes nature at the smallest scales of energy levels of atoms and subatomic particles',
#                            'phys400', 8644042)
#         self.db.enroll(7644042, 'phys400', 'A+')
#
#
#         self.db.search_student(7644042)
#         print('Search course')
#
#     def test_search_teacher(self):
#         self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa',
#                             'abc123', 1234567890)
#         self.db.add_course('Quantum physics',
#                            'describes nature at the smallest scales of energy levels of atoms and subatomic particles',
#                            'phys400', 8644042)
#         self.db.add_course('Classical mechanics',
#                            'the study of the motion of bodies in accordance with the general principles first enunciated by Sir Isaac Newton',
#                            'phys100', 8644042)
#
#         self.db.search_teacher(8644042)
#         print('Search course')
#
#     def test_search_course(self):
#         self.db.add_student(1234567, 'lebron', 'james', 'M', '122 nash ave.', 'new york', 'new york', 'USA', 't3e6y5',
#                             1234567890)
#         self.db.add_student(7644042, 'jamil', 'mbabaali', 'M', '183 eastcote dr.', 'winnipeg', 'manitoba', 'canada',
#                             'r2n4h4', 2049791641)
#         self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa',
#                             'abc123', 1234567890)
#         self.db.add_course('Quantum physics',
#                            'describes nature at the smallest scales of energy levels of atoms and subatomic particles',
#                            'phys400', 8644042)
#         self.db.enroll(7644042, 'phys400', 'A+')
#         self.db.enroll(1234567, 'phys400', 'A+')
#
#         self.db.search_course('phys400')
#         print('Search course')

#<----------------------------------------------- Up-date f(x) Tests -------------------------------------------------->
    def test_update_student(self):
        self.db.add_student(1234567, 'lebron', 'james', 'M', '122 nash ave.', 'new york', 'new york', 'USA', 't3e6y5',
                            1234567890)
        self.db.cursor.execute("SELECT * FROM student WHERE student_id=1234567")
        self.studentA = self.db.cursor.fetchall()
        print(self.studentA)

        self.db.update_student(1234567,'last_name','Durant')
        self.db.cursor.execute("SELECT * FROM student WHERE student_id=1234567")
        self.studentB = self.db.cursor.fetchall()
        print(self.studentB)

        self.assertIsNot(self.studentA,self.studentB)

    def test_update_teacher(self):
        self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa',
                            'abc123', 1234567890)
        self.db.cursor.execute("SELECT * FROM teacher WHERE teacher_id=8644042")
        self.teacherA = self.db.cursor.fetchall()
        print(self.teacherA)

        self.db.update_teacher(8644042,'phone_number',1316233777)
        self.db.cursor.execute("SELECT * FROM teacher WHERE teacher_id=8644042")
        self.teacherB = self.db.cursor.fetchall()
        print(self.teacherB)

        self.assertIsNot(self.teacherA,self.teacherB)

    def test_update_course(self):
        self.db.add_teacher(9644042, 'Bill', 'Gates', 'M', '560 state st.', 'New York', 'New York', 'USA',
                            'abc123', 987654321)
        self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa',
                            'abc123', 1234567890)
        self.db.add_course('phys300','Quantum physics','describes nature at the smallest scales of energy levels of atoms and subatomic particles',
                            8644042)
        # self.db.cursor.execute("""SELECT * FROM course WHERE course_id = phys400""")
        # self.courseA = self.db.cursor.fetchall()
        # print(self.courseA)

        self.db.update_course('phys300','teacher_id',9644042)
        self.db.cursor.execute("SELECT * FROM course WHERE course_id= phys300")
        self.courseB = self.db.cursor.fetchall()
        print(self.courseB)

        # self.assertIsNot(self.courseA,self.courseB)




if __name__ == '__main__':
    unittest.main()
