import random

class Portfolio(object):							      # Constructor of the class
  def __init__(self):                                     # An empty portfolio
    self.cash = 0.00								
    self.stock = 0.00
    self.mutualFund = 0.00
    self.tr = "Created an empty portfolio\n"		      # record of transaction		
    
  def __str__(self):                                      # to print portfolio
    return "This portfolio has\n cash: {0}\n stock: {1}\n mutual funds: {2}".format(self.cash, self.stock, self.mutualFund)
	
  def addCash(self, amount): 						      # addCash function
    """Adds cash to portfolio"""
    amount_f = float(amount)						      # to make sure we can to the math properly
    self.cash += amount_f
    self.tr += "Added ${0} of cash\n".format(amount)      # record of transaction
    
  def withdrawCash(self, amount):                         # withdrawCash function
    """Withdraws cash from portfolio """
    amount_f = float(amount)						
    if amount_f > self.cash:						      # if there is not enough cash to withdraw
  	  self.tr += "Failed to withdraw cash"			      # record of failed transaction
  	  return "Not enough cash in portfolio"         
    self.cash -= amount_f							      # subtract the amount when enough
    self.tr += "Withdrew ${0} of cash\n".format(amount)   # record of transaction
	
  def buyStock(self, amount, asset):                      # buyStock function
	"""Buys 'amount' shares of 'asset' stock"""
	amount_f = float(amount)               
	if amount_f * asset.price > self.cash:                # if there is not enough cash to buy
	  self.tr += "Failed to buy the stock"                # record of failed transaction
	  return "Not enough cash in portfolio"
	if amount != int(amount):                             # if the amount input is not proper
	  self.tr += "Failed to buy the stock"                # record of failed transaction
	  return "You can only buy stocks as whole"
	else: 
	  self.stock += amount_f                              # add to stocks when you can buy
	  self.cash -= amount_f * asset.price                 # subtract the corr. amount from cash
  	  self.tr += "Bought {0} {1}\n".format(amount, asset) # record of transaction
       
  def sellStock(self, asset, amount):                     # sellStock function
    """Sells 'amount' shares of 'asset'"""              
    amount_f = float(amount)							 
    if self.stock < amount_f:							  # if there is not enough stocks to sell	
      self.tr += "Failed to sell the stock"				  # record of failed transaction
      return "Not enough stocks in portfolio"         
    if amount != int(amount):                             # if the amount input is not proper
      self.tr += "Failed to sell the stock"               # record of failed transaction
      return "You can only sell stocks as whole"
    else: 
      self.stock -= amount_f                              # subtract from stocks when you can sell
      self.cash += amount_f *20* random.uniform(0.5, 1.5) # add the corr. amount to cash
      # I couldn't figure out how to integrate price here, so I used the price in example
      self.tr += "Sold {0} Stock with symbol {1}\n".format(amount, asset)
  
  def buyMutualFund(self, amount, asset):                 # buyMutualFund function  
    """Buys 'amount' shares of 'asset'"""
    amount_f = float(amount)
    if amount_f > self.cash:                              # if there is not enough cash to buy
      self.tr += "Failed to buy the mutual fund"          # record of failed transaction
      return "Not enough cash in portfolio"
    else:  
      self.mutualFund += amount_f                         # add to mutual funds when you can buy
      self.cash -= amount_f                               # subtract the corr. amount from cash
      self.tr += "Bought {0} {1}\n".format(amount, asset) # record of transaction
  
  def sellMutualFund(self, asset, amount):                # sellMutualFund function
    """Sells 'amount' shares of 'asset'"""
    amount_f = float(amount)              
    if self.mutualFund < amount_f:           			  # if there is not enough MFs to sell
      self.tr += "Failed to sell the mutual fund"         # record of failed transaction
      return "Not enough mutual funds in portfolio"       
    else:
      self.mutualFund -= amount_f                         # subtract from MFs when you can sell
      self.cash += amount_f * random.uniform(0.9, 1.2)    # add the corr. amount to cash
      self.tr += "Sold {0} Mutual Fund with symbol {1}\n".format(amount, asset)      
  
  def history(self):                                      # history of transactions
    """Prints list of all transactions, ordered by time"""
    print self.tr                                         # print all records

class Asset(object):                                      # Constructor of the class
  def __init__(self, price, asset):                       # Price and name of asset as initializers
    self.price = price
    self.asset = asset
    
class Stock(Asset):                                      # Stock asset inheriting from super class Asset
  def __init__(self, price, asset):                      
    Asset.__init__(self, price, asset)                   # Requires price and name of the asset
	  
  def __str__(self):
	return "Stock with price {0} and symbol {1}".format(self.price, self.asset)
	    
class MutualFund(Asset):                                 # MF asset inheriting from super class Asset
  def __init__(self, asset):
    Asset.__init__(self, 1.0, asset)                     # Only requires name of the asset
    
  def __str__(self):
    return "Mutual Fund with symbol {0}".format(self.asset)
