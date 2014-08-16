class Node:
  def __init__(self, _value = None, _next = None):
    self.value = _value
    self.next = _next
    
  def __str__(self):
    return str(self.value)    
    
class LinkedList:
  def __init__(self, value):
    """Takes a number and sets it as the value at the head of the List"""
    self.head = Node(value) 							# create the first node and call it head
    self.length = 1										# initial length 
  	
  def length(self):
    """Returns the length of the list"""				# Complexity class of operation length: O(1)
    return self.length									# the length will be updated by add/remove
  
  def addNode(self, new_value):                       	# Complexity class of storing: O(1)
    """Takes a number and adds it to the end of the list"""
    new_node = Node(new_value)							# A new node to add to linked list
    current = self.head									# current node to reach value and next
    while current.next:                                 # the node to look into
	  current = current.next                            # move onto next node and make prev its value
    current.next = new_node								# new nodes value is prev next
    self.length += 1                                    # added a new node

  def addNodeAfter(self, new_value, after_node):        # Complexity class of operations: O(N)
    """Takes a number and adds it after the after_node"""
    new_node = Node(new_value)
    current = self.head
    if after_node > self.length: 						# if the index is out of scope
      return "Intended new node is out of scope"
    else:        										# to add value after a node in scope
      index = 2  										# doesn't work if we start from 1
      while index <= after_node:						
        current = current.next							
        index += 1  									# to go through all indices	
      current.next = Node(new_value, current.next)      # assignments for moving prev next new value
      self.length += 1									# added a new node
      return self.__str__()
      
  def addNodeBefore(self, new_value, before_node):		# Complexity class of operations: O(N)
    """Takes a value and adds before the before_node"""
    current = self.head
    if before_node > self.length: 						# if the index is out of scope
      return "Intended new node is out of scope" 
    elif before_node == 1:                              # if we intend to assign a new head
      new_node = Node(new_value)
      new_node.next = self.head
      self.head = new_node
      self.length += 1									# added a new node
    else:												# for adding before any other node
      index = 2
      while index <= (before_node -1):
        current = current.next
        index += 1
      current.next = Node(new_value, current.next)
      self.length += 1									# added a new node
    return self.__str__()     
      
  def removeNode(self, node_to_remove):					# Complexity class of operations: O(N)
    """Removes a node from the list"""
    current = self.head
    if node_to_remove > self.length:					# if the index is out of scope
      return "Intended removal is out of scope"
    elif node_to_remove == 1:						    # if the node we wanna remove is the head
      self.head = self.head.next
      self.length -= 1									# removed a node
    elif node_to_remove == self.length:					# if the node we wanna remove is the tail
      index = 2
      while index <= (node_to_remove - 1):
        current = current.next
        index += 1
      current.next = None
      self.length -=1									# removed a node
    else: 												# for removing any other node
      index = 2
      while index <= node_to_remove:
        current = current.next
        index += 1
      current.value = current.next
      current.next = current.next.next
      self.length -= 1									# removed a node
    return self.__str__()
    
  def removeNodesByValue(self, value):					# Complexity class of operations: O(N)
    """Takes a value, removes all nodes with that value"""
    current = self.head
    while current.next:  								# node to be examined
      if value == current.next.value: break				# if we get the value we are looking for
      current = current.next 							# move until we get to the node with given value
    else: 
      return "Value is not present"
    current.next = current.next.next					# make the assignments
    if current.next == None: 							# if tail
      self.value = current
    self.length -= 1									# removed a node
    return self.__str__()  
  
  def reverse(self):									# Complexity class of operations: O(N)
    """Reverses the order of the linked list"""	
    current = self.head									
    prev = None
    while current: 										# node to be examined
      next = current.next								# make the assignments
      current.next = prev
      prev = current
      current = next
    if self.head:										# assign the head
      self.next = self.head
    self.head = prev
    return self.__str__()  
  
  def __str__(self):									# Display function
    """Displays the list in some reasonable way"""
    current = self.head
    out = 'LinkedList: [' + str(current.value)
    while current.next:
      current = current.next
      out += '->' + str(current.value) 
    return out + ']'
    

# BONUS:
#   def hasCycle(self):
#     """Returns true if this linked list has a cycle."""
  
