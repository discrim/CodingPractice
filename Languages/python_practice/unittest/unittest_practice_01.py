import unittest

# Write test case
class CustomTests(unittest.TestCase):
    def test_runs(self):
        """ Check whether it can be run """
        custom_function()

def custom_function():
    pass

if __name__ == "__main__":
    unittest.main()