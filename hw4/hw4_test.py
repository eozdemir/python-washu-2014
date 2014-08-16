import unittest
from hw4 import *

class LinkTest(unittest.TestCase):
  def setUp(self):
    self.alist = LinkedList(5)

  def test_add_node(self):
    self.alist.addNode(12)
    self.alist.addNode(9)
    self.alist.addNode(2)
    self.assertEqual("LinkedList: [5->12->9->2]", self.alist.__str__())    

  def test_add_node_after(self):
    self.alist.addNode(12)
    self.alist.addNode(9)
    self.alist.addNode(2)
    self.assertEqual("Intended new node is out of scope", self.alist.addNodeAfter(7,5))
    self.assertEqual("LinkedList: [5->12->7->9->2]", self.alist.addNodeAfter(7, 2))

  def test_add_node_before(self):
    self.alist.addNode(12)
    self.alist.addNode(9)
    self.alist.addNode(2)
    self.assertEqual("Intended new node is out of scope", self.alist.addNodeBefore(7, 7))
    self.assertEqual("LinkedList: [5->8->12->9->2]", self.alist.addNodeBefore(8, 2))
        
  def test_remove_node(self):
    self.alist.addNode(12)
    self.alist.addNode(9)
    self.alist.addNode(2)
    self.assertEqual("Intended removal is out of scope", self.alist.removeNode(5))
    self.assertEqual("LinkedList: [5->12->9]", self.alist.removeNode(4))
   
  def test_remove_node_by_value(self):
    self.alist.addNode(12)
    self.alist.addNode(9)
    self.alist.addNode(2)  
    self.assertEqual("Value is not present", self.alist.removeNodesByValue(10))
    self.assertEqual("LinkedList: [5->9->2]", self.alist.removeNodesByValue(12))

  def test_reverse(self):
    self.alist.addNode(12)
    self.alist.addNode(9)
    self.alist.addNode(2)
    self.assertEqual("LinkedList: [2->9->12->5]", self.alist.reverse())


if __name__ == '__main__':
  unittest.main() 