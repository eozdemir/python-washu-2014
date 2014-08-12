import unittest
from hw2 import *

class PortfolioTest(unittest.TestCase):
  def setUp(self):
    self.portfolio = Portfolio()
    self.s = Stock(20, "HFH")
    self.mf1 = MutualFund("BRT")
    self.mf2 = MutualFund("GHT")
  
  def test_initial_portfolio(self):
  	self.assertEqual(0.0, self.portfolio.cash)	
  	self.assertEqual(0.0, self.portfolio.stock) 
  	self.assertEqual(0.0, self.portfolio.mutualFund)
  	self.assertTrue("Created an empty portfolio" in self.portfolio.tr)
  
  def test_stock(self):
    self.assertEqual(20, self.s.price)
    self.assertEqual("HFH", self.s.asset) 
 
  def test_mutualFund(self):
    self.assertEqual(1, self.mf1.price)
    self.assertEqual(1, self.mf2.price)
    self.assertEqual("BRT", self.mf1.asset)
    self.assertEqual("GHT", self.mf2.asset)
    
  def test_add_cash(self):
    self.portfolio.addCash(300.50)
    self.assertEqual(300.50, self.portfolio.cash)
    self.assertTrue("Added $300.5 of cash" in self.portfolio.tr)
    
  def test_withdraw_cash(self):
    self.portfolio.addCash(300.50)
    self.portfolio.withdrawCash(50)
    self.assertEqual(250.50, self.portfolio.cash)
    self.assertTrue("Withdrew $50 of cash" in self.portfolio.tr)
    self.assertTrue("Not enough cash in portfolio",self.portfolio.withdrawCash(300))
    
  def test_buy_stock(self):
    self.portfolio.addCash(300.50)
    self.portfolio.buyStock(5, self.s)
    self.assertEqual(200.50, self.portfolio.cash)
    self.assertEqual(5, self.portfolio.stock)
    self.assertTrue("Bought 5 Stock with price 20 and symbol HFH" in self.portfolio.tr)
    self.assertEqual("Not enough cash in portfolio", self.portfolio.buyStock(15, self.s))
    self.assertEqual("You can only buy stocks as whole", self.portfolio.buyStock(3.5, self.s))
    
  def test_buy_mutual_fund(self):
    self.portfolio.addCash(300.50)
    self.portfolio.buyMutualFund(100, self.mf1)
    self.assertEqual(200.50, self.portfolio.cash)
    self.assertEqual(100, self.portfolio.mutualFund)
    self.assertTrue("Bought 100 Mutual Fund with symbol BRT" in self.portfolio.tr)
    self.assertEqual(200.50, self.portfolio.cash)
    self.portfolio.buyMutualFund(5.50, self.mf2)
    self.assertEqual(195.0, self.portfolio.cash)
    self.assertEqual(105.5, self.portfolio.mutualFund) 
    self.assertTrue("Bought 5.5 Mutual Fund with symbol GHT" in self.portfolio.tr)
    self.assertEqual("Not enough cash in portfolio", self.portfolio.buyMutualFund(250, self.mf1))

  def test_sell_stock(self):
    self.portfolio.addCash(300.50)
    self.portfolio.buyStock(5, self.s)
    self.portfolio.sellStock("HFH", 1)
    self.assertEqual(4, self.portfolio.stock)
    self.assertTrue("Sold 1 Stock with symbol HFH" in self.portfolio.tr)
    self.assertEqual("Not enough stocks in portfolio", self.portfolio.sellStock("HFH", 5))
    self.assertEqual("You can only sell stocks as whole", self.portfolio.sellStock("HFH", 2.5))
    # Since the selling price is randomly distributed, 
    # I can't test the exact amount of cash remaining
    
  def test_sell_mutual_fund(self):
    self.portfolio.addCash(300.50)
    self.portfolio.buyMutualFund(10, self.mf1)
    self.portfolio.sellMutualFund("BRT", 3)
    self.assertEqual(7, self.portfolio.mutualFund)
    self.assertTrue("Sold 3 Mutual Fund with symbol BRT" in self.portfolio.tr)
    self.assertEqual("Not enough mutual funds in portfolio", self.portfolio.sellMutualFund("BRT", 10))
    # Since the selling price is randomly distributed, 
    # I can't test the exact amount of cash remaining
    
if __name__ == '__main__':
  unittest.main() 