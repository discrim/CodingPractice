import unittest
import os

def custom_function(file_name):
    with open(file_name, 'rt') as infile:
        return sum(1 for _ in infile)

class CustomTests(unittest.TestCase):
    def setUp(self):
        """ Write a file before test """
        self.file_name = 'test_file.txt'
        with open(self.file_name, 'wt') as outfile:
            outfile.write("""
            Is it true that a unit test module is included in Python?
            Really? Good!
            I want to run unit tests well.
            """.strip())
    
    def tearDown(self):
        """ Delete file after test """
        try:
            os.remove(self.file_name)
        except:
            pass
    
    def test_runs(self):
        """ Test method for checking whether the code can be run or not """
        custom_function(self.file_name)
    
    def test_line_count(self):
        self.assertEqual(custom_function(self.file_name), 3)

if __name__ == '__main__':
    unittest.main()