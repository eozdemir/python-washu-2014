import unittest
from bob import *

class BobTest(unittest.TestCase):
  def test_answer(self):
  	self.assertEqual("Sure.", bob("What is wrong with you?"))
  def test_answer_shout(self):
  	self.assertEqual("Whoa, chill out!", bob("WHAT?"))
  def test_answer_whatever(self):
  	self.assertEqual("Whatever.", bob("Whatever"))
  def test_answer_Bob(self):
  	self.assertEqual("Fine. Be that way!", bob("Bob!!"))
  def test_answer_Bob2(self):
  	self.assertEqual("Fine. Be that way!", bob("Bob"))
  	
if __name__ == '__main__':
  unittest.main() 

