import sys
sys.path.append('../')
import unittest
from unittest.mock import patch
from database import newDatabase

class TestDatabase(unittest.TestCase):


#<----------------------------------------------- Init Test ----------------------------------------------------------->

    @unittest.expectedFailure
    def test_newDatabase(self):
        self.db = newDatabase()
        self.assertIsInstance(self.d,newDatabase)
        print('ID Test: Database init')
        self.db.cursor().execute("DROP DATABASE IF EXISTS courseDB;")

if __name__ == '__main__':
    unittest.main()