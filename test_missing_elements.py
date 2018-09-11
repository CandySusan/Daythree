import unittest
from missing_elements import missing_numbers
class MissingElements(unittest.TestCase):
     """
        This tests methods in missing_elements file
     """
     def test_missing_elements(self):
         self.assertEqual((4,8),missing_elements.missing_elements([1,2,3,5,6,7,9]),msg='The output should be a missing_element')

if __name__ == "__main__":
    unittest.main()