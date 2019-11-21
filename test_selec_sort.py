import unittest
import selection_sort
import bubble_sort
import insertion_sort
import quick_sort

class SelectionSortTestCase(unittest.TestCase):
	def test_selection_sort(self):
                self.assertEqual(selection_sort.selection_sort([-2, -66, -9, -22, -66, -90]), [-90, -66, -66, -22, -9, -2])
	def test_bubble_sort(self):
                self.assertEqual(bubble_sort.bubble_sort([-2, -66, -9, -22, -66, -90]), [-90, -66, -66, -22, -9, -2])
	def test_insertion_sort(self):
                self.assertEqual(insertion_sort.insertion_sort([-2, -66, -9, -22, -66, -90]), [-90, -66, -66, -22, -9, -2])
	def test_quick_sort(self):
                self.assertEqual(quick_sort.quick_sort([-2, -66, -9, -22, -66, -90]), [-90, -66, -66, -22, -9, -2])


if __name__ == "__main__":
	unittest.main()
