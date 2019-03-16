import sys
sys.path.append('../../')
import unittest
from unittest.mock import patch
from database import newDatabase

# ******************** This test file tests the mysql error catching functions in the new Database class ***************
# *************************(These tests ensured all mysql mistakes caught & printed) ***********************************

class TestDatabase(unittest.TestCase):

    def setUp(self):# Initializes the database during each test automatically.
        self.db = newDatabase()

    def tearDown(self):# Drops schema from the database server at the end of each test automatically.
        self.db.cursor.execute("DROP DATABASE IF EXISTS courseDB;")
        print('tearDown\n')

#<----------------------------------------------- Add f(x) Tests ------------------------------------------------------>


    def test_add_student(self):
        self.db.add_student(7644042,'jamil','mbabaali','M','183 eastcote dr.','winnipeg','manitoba','canada','r2n4h4',2049791641)
        self.db.add_student(7644042, 'jamil', 'mbabaali', 'M', '183 eastcote dr.', 'winnipeg', 'manitoba', 'canada','r2n4h4', 2049791641)
        print('ID Test: Add student')


    def test_add_teacher(self):
        self.db.add_teacher(8644042,'elon','musk','M','360 wakopa st.','cape town','western cape','south africa','abc123',1234567890)
        self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa','abc123', 1234567890)
        print('ID Test: Add teacher')


    def test_add_course(self):
        self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa','abc123', 1234567890)
        self.db.add_course('phys400','Quantum Physics','describes nature at the smallest scales of energy levels of atoms and subatomic particles',8644042)
        self.db.add_course('phys400', 'Quantum Physics','describes nature at the smallest scales of energy levels of atoms and subatomic particles',8644042)
        print('ID Test: Add course')


    def test_enroll(self):
        self.db.enroll(7644042, 'phys400', 'A+')
        print('ID Test: Enroll')

# <----------------------------------------------- Delete f(x) Tests -------------------------------------------------->


    def test_delete_student(self):
        self.db.add_student(7644042, 'jamil', 'mbabaali', 'M', '183 eastcote dr.', 'winnipeg', 'manitoba', 'canada',
                                'r2n4h4', 2049791641)
        self.db.delete_student(7644042)
        print('ID Test: Delete student')


    def test_delete_teacher(self):
        self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa','abc123', 1234567890)
        self.db.delete_teacher(8644042)
        print('ID Test: Delete teacher')


    def test_delete_course(self):
        self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa','abc123', 1234567890)
        self.db.add_course('phys400','Quantum physics','describes nature at the smallest scales of energy levels of atoms and subatomic particles', 8644042)
        self.db.delete_course('phys400')
        print('ID Test: Delete course')

# <----------------------------------------------- Search f(x) Tests -------------------------------------------------->

    def test_search_student(self):
        self.db.add_student(7644042, 'jamil', 'mbabaali', 'M', '183 eastcote dr.', 'winnipeg', 'manitoba', 'canada',
                            'r2n4h4', 2049791641)
        self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa',
                            'abc123', 1234567890)
        self.db.add_course('phys400','Quantum physics','describes nature at the smallest scales of energy levels of atoms and subatomic particles',8644042)
        self.db.enroll(7644042, 'phys400', 'A+')


        self.db.search_student(7644042)
        print('ID Test: Search student')


    def test_search_teacher(self):
        self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa',
                            'abc123', 1234567890)
        self.db.add_course('phys400','Quantum physics','describes nature at the smallest scales of energy levels of atoms and subatomic particles', 8644042)
        self.db.add_course('phys100','Classical mechanics','the study of the motion of bodies in accordance with the general principles first enunciated by Sir Isaac Newton',8644042)
        self.db.search_teacher(8644042)
        print('ID Test: Search teacher')


    def test_search_course(self):
        self.db.add_student(7644042, 'jamil', 'mbabaali', 'M', '183 eastcote dr.', 'winnipeg', 'manitoba', 'canada',
                            'r2n4h4', 2049791641)
        self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa',
                            'abc123', 1234567890)
        self.db.add_course('phys400', 'Quantum physics',
                           'describes nature at the smallest scales of energy levels of atoms and subatomic particles',
                           8644042)
        self.db.enroll(7644042, 'phys400', 'A+')
        self.db.search_course('phys400')
        print('ID Test: Search course')


# #<----------------------------------------------- Up-date f(x) Tests -------------------------------------------------->

    def test_update_student(self):
        self.db.add_student(1234567, 'lebron', 'james', 'M', '122 nash ave.', 'new york', 'new york', 'USA', 't3e6y5',
                            1234567890)
        self.db.update_student(1234567,'last_name','Durant')
        print('Test: Update student')

    def test_update_teacher(self):
        self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa',
                            'abc123', 1234567890)
        self.db.update_teacher(8644042,'phone_number',1316233777)
        print('Test: Update teacher')

    def test_update_course(self):
        self.db.add_teacher(9644042, 'Bill', 'Gates', 'M', '560 state st.', 'New York', 'New York', 'USA',
                            'abc123', 987654321)
        self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa',
                            'abc123', 1234567890)
        self.db.add_course('phys400','Quantum physics','describes nature at the smallest scales of energy levels of atoms and subatomic particles',
                            8644042)
        self.db.update_course('phys400','teacher_id',9644042)
        print('Test: Update course')

    def test_update_enrollment(self):
        self.db.add_student(1234567, 'lebron', 'james', 'M', '122 nash ave.', 'new york', 'new york', 'USA', 't3e6y5',1234567890)
        self.db.add_teacher(8644042, 'elon', 'musk', 'M', '360 wakopa st.', 'cape town', 'western cape', 'south africa','abc123', 1234567890)
        self.db.add_course('phys400','Quantum physics','describes nature at the smallest scales of energy levels of atoms and subatomic particles', 8644042)
        self.db.enroll(1234567,'phys400', 'A+')
        self.db.update_enrollment(1234567,'phys400','B-','grade')
        print('ID Test: Update enroll')


if __name__ == '__main__':
    unittest.main()