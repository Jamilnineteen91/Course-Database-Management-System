import sys
sys.path.append('../')
import unittest
from unittest.mock import patch
from back_end import newDatabase

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = newDatabase()

    def tearDown(self):
        pass


    def test_newDatabase(self):
        self.assertIsInstance(self.db,newDatabase)





if __name__ == '__main__':
    unittest.main()


