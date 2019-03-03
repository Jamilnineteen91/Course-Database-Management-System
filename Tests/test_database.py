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

        self.studentB=[(7644042,'jamil','mbabaali','M','183 eastcote dr.','winnipeg','manitoba','canada','r2n4h4',2049791641)]



        self.assertEqual(self.db, self.studentA, type(self.studentB))





if __name__ == '__main__':
    unittest.main()


