import unittest
from main import sort_list

class TestSortList(unittest.TestCase):

    def test_empty_list(self):
        """test to sort an empty list"""
        self.assertEqual(sort_list([]), [])

    def test_single_element_list(self):
        """test to sort single element list"""
        self.assertEqual(sort_list([5]), [5])

    def test_multiple_elements_list(self):
      """test to sort multiple elements list"""
      self.assertEqual(sort_list([6, 8, 10, 7, 9]), [6, 7, 8, 9, 10])

    def test_negative_elements_list(self):
        """test to sort negative elements list"""
        self.assertEqual(sort_list([-4, -5, -3, -1, -2, 0]), [-5, -4, -3, -2, -1, 0])

    def test_duplicate_elements_list(self):
        """test to sort duplicate elements list"""
        self.assertEqual(sort_list([3, 4, 3, 4, 5, 1, 2]), [1, 2, 3, 3, 4, 4, 5])

    def test_pre_sorted_list(self):
        """test to sort pre-sorted list"""
        self.assertEqual(sort_list([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
