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


    def test_newDatabase(self):
        self.assertIsInstance(self.db,newDatabase)

    def test_add_student(self):

        self.db.add_student(7644042,'jamil','mbabaali','M','183 eastcote dr.','winnipeg','manitoba','canada','r2n4h4',2049791641)
        self.db.cursor.execute("SELECT * FROM student WHERE student_id=7644042")
        self.studentA=self.db.cursor.fetchall()
        print(self.studentA)

        self.db.use()
        self.db.cursor.execute("SELECT * FROM student;")
        self.studentB=self.db.cursor.fetchall()
        print(self.studentB)


        self.assertEqual(self.studentA,self.studentB)

    def test_add_teacher(self):
        self.db
        self.db.add_teacher(8644042,'elon','musk','M','360 wakopa st.','cape town','western cape','south africa','abc123',1234567890)
        self.db.cursor.execute("SELECT * FROM teacher WHERE teacher_id=8644042")
        self.teacherA = self.db.cursor.fetchall()
        print(self.teacherA)

        self.db.use()
        self.db.cursor.execute("SELECT * FROM teacher;")
        self.teacherB = self.db.cursor.fetchall()
        print(self.teacherB)

        self.assertEqual(self.teacherA, self.teacherB)

    def test_add_course(self):
        self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa','abc123', 1234567890)
        self.db.add_course('Quantum physics','describes nature at the smallest scales of energy levels of atoms and subatomic particles','phys400',8644042)
        self.db.cursor.execute("SELECT * FROM course WHERE course_id='phys400'")
        self.courseA = self.db.cursor.fetchall()
        print(self.courseA)

        self.db.use()
        self.db.cursor.execute("SELECT * FROM course;")
        self.courseB = self.db.cursor.fetchall()
        print(self.courseB)

        self.assertEqual(self.courseA, self.courseB)

    def test_enroll(self):
        self.db
        self.db.add_student(1234567, 'lebron', 'james', 'M', '122 nash ave.', 'new york', 'new york', 'USA', 't3e6y5',1234567890)
        self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa','abc123', 1234567890)
        self.db.add_course('Quantum physics','describes nature at the smallest scales of energy levels of atoms and subatomic particles','phys400', 8644042)
        self.db.enroll(1234567, 'phys400', 'A+')

        self.db.use()
        self.db.cursor.execute("SELECT * FROM enrollment WHERE student_id=1234567")
        self.A = self.db.cursor.fetchall()
        print(self.A)


        self.db.use()
        self.db.cursor.execute("SELECT * FROM enrollment WHERE student_id=1234567;")
        self.B = self.db.cursor.fetchall()
        print(self.B)

        self.assertEqual(self.A, self.B)



if __name__ == '__main__':
    unittest.main()


