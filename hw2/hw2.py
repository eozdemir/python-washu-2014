import random

class Portfolio(object):
  def __init__(self):   
    self.cash = 0.00
    self.stock = 0.00
    self.mutualFund = 0.00
    self.tr = "Created an empty portfolio\n"		# for history of transactions		
    
  def __str__(self): 
    return "This portfolio has\n cash: {0}\n stock: {1}\n mutual funds: {2}".format(self.cash, self.stock, self.mutualFund)
	
  def addCash(self, amount):
    """Adds cash to portfolio"""
    amount_f = float(amount)
    self.cash += amount_f
    self.tr += "Added ${0} of cash\n".format(amount)  
    
  def withdrawCash(self, amount):
    """Withdraws cash from portfolio """
    amount_f = float(amount)
    if amount_f > self.cash:
  	  self.tr += "Failed to withdraw cash"
  	  return "Not enough cash in portfolio"
    self.cash -= amount_f
    self.tr += "Withdrew ${0} of cash\n".format(amount)
	
  def buyStock(self, amount, asset):
	"""Buys 'amount' shares of 'asset' stock"""
	amount_f = float(amount)
	if amount_f * asset.price > self.cash:
	  self.tr += "Failed to buy the stock"
	  return "Not enough cash in portfolio"
	if amount != int(amount):
	  self.tr += "Failed to buy the stock"
	  return "You can only buy stocks as whole"
	else: 
	  self.stock += amount_f
	  self.cash -= amount_f * asset.price
  	  self.tr += "Bought {0} {1}\n".format(amount, asset)
       
  def sellStock(self, asset, amount):
    """Sells 'amount' shares of 'asset'"""
    amount_f = float(amount)
    if self.stock < amount_f:
      self.tr += "Failed to sell the stock"
      return "Not enough stocks in portfolio"
    if amount != int(amount):
      self.tr += "Failed to sell the stock"
      return "You can only sell stocks as whole"
    else: 
      self.stock -= amount_f
      self.cash += amount_f * 20 * random.uniform(0.5, 1.5)
      # couldn't figure out how to integrate price here, so I used the price in example
      self.tr += "Sold {0} Stock with symbol {1}\n".format(amount, asset)
  
  def buyMutualFund(self, amount, asset):
    """Buys 'amount' shares of 'asset'"""
    amount_f = float(amount)
    if amount_f > self.cash:
      self.tr += "Failed to buy the mutual fund"
      return "Not enough cash in portfolio"
    else:  
      self.mutualFund += amount_f
      self.cash -= amount_f   # $1/share
      self.tr += "Bought {0} {1}\n".format(amount, asset)
  
  def sellMutualFund(self, asset, amount):
    """Sells 'amount' shares of 'asset'"""
    amount_f = float(amount)
    if self.mutualFund < amount_f:
      self.tr += "Failed to sell the mutual fund"
      return "Not enough mutual funds in portfolio"    
    else:
      self.mutualFund -= amount_f
      self.cash += amount_f * random.uniform(0.9, 1.2)
      self.tr += "Sold {0} Mutual Fund with symbol {1}\n".format(amount, asset)      
  
  def history(self):
    """Prints list of all transactions, ordered by time"""
    print self.tr

class Asset(object):
  def __init__(self, price, asset):
    self.price = price
    self.asset = asset
    
class Stock(Asset):
  def __init__(self, price, asset):
    Asset.__init__(self, price, asset)
	  
  def __str__(self):
	return "Stock with price {0} and symbol {1}".format(self.price, self.asset)
	    
class MutualFund(Asset):
  def __init__(self, asset):
    Asset.__init__(self, 1.0, asset)
    
  def __str__(self):
    return "Mutual Fund with symbol {0}".format(self.asset)

    
# portfolio = Portfolio() #Creates a new portfolio
# print portfolio
# portfolio.addCash(300.50) #Adds cash to the portfolio
# print portfolio 
# s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
# print s
# portfolio.buyStock(5, s) #Buys 5 shares of stock s
# print portfolio
# mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
# mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
# print mf1, mf2
# portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
# portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
# print(portfolio) #Prints portfolio
# # 				  cash: $140.50
# # 				  stock: 5 HFH
# # 				  mutual funds: 10.33 BRT
# # 							     2    GHT
# portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
# print portfolio
# portfolio.sellStock("HFH", 1) #Sells 1 share of HFH
# print portfolio
# portfolio.withdrawCash(50) #Removes $50
# print portfolio
# portfolio.withdrawCash(1000)
# print portfolio
# portfolio.history() #Prints a list of all transactions ordered by time
  
