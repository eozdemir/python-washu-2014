import unittest
from lab3 import *

class Lab3Test(unittest.TestCase):
  def test_shout(self):
  	self.assertEqual("MERHABA!", shout("merhaba"))	
  	self.assertEqual("MERHABA ELIF!", shout("merhaba elif")) 
  	self.assertEqual("MERHABA, ELIF!", shout("merhaba, elif"))

  def test_reverse(self):
  	self.assertEqual("abahrem", reverse("merhaba"))
  	
  def test_reverse2(self):	
  	self.assertEqual("luteb", reverse("betul"))
  	
  def test_reverse_number(self):
  	self.assertEqual("4102", reverse(2014))
  	
  def test_reversewords(self): 
  	self.assertEqual("elif merhaba. ", reversewords("merhaba elif"))
  	
  def test_reversesentence(self):
  	self.assertEqual("elif merhaba. betul merhaba. ", reversewords("merhaba elif! merhaba betul!"))
  	
  def test_reversewordletters(self):
  	self.assertEqual("abahrem file!", reversewordletters("merhaba elif!"))
  	
  def test_reverseletters_no_stop(self):
  	self.assertEqual("Punctuation missing!", reversewordletters("merhaba elif"))

if __name__ == '__main__':
  unittest.main() 