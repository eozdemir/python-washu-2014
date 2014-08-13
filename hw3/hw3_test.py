import unittest
from hw3 import *

class SortTest(unittest.TestCase):
  def setUp(self):
    self.alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    self.sortedAlist = [17, 20, 26, 31, 44, 54, 55, 77, 93]

  def test_bubble_sort(self):
    self.assertEqual(self.sortedAlist, bubbleSort(self.alist))
    
  def test_merge_sort(self):
  	self.assertEqual(self.sortedAlist, mergeSort(self.alist))
  
if __name__ == '__main__':
  unittest.main() 
