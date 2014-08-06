class Clock():
	def __init__(self, hours, minutes=0):
		self.hours = hours
		self.minutes = minutes
	    	
	def __str__(self):
		if self.hours<10 and self.minutes<10:
			return "0%d:0%d" % (self.hours, self.minutes)
		elif self.hours<10:
			return "0%d:%d" % (self.hours, self.minutes)
		elif self.minutes<10:
			return "%d:0%d" % (self.hours, self.minutes)
		else:
			return "%d:%d" % (self.hours, self.minutes)	
			
	@classmethod
	def at(cls, hours, minutes=0):
		return cls(hours, minutes)
		
	def __add__(self, other):
	  self.minutes=self.minutes + other
	  if self.minutes>=60:
		add_hour=self.minutes/60
		self.hours += add_hour
		self.minutes=self.minutes%60
	  if self.hours>=24:
	  	self.hours-=24
	  return self
		
	def __sub__(self, other):
	  if self.hours ==0:
	    self.hours = 24
	  if other>=60:
	    self.hours -= other/60
	    self.minutes -= other%60
	  if self.minutes < 0:   
	    self.hours -=1
	    self.minutes += 60
	  if self.hours>=24:
	  	 self.hours-=24
	  return self
	  	
	def __eq__(self, other):
		return(self.hours==other.hours and self.minutes==other.minutes)
		
	def __ne__(self, other):
		return(self.hours!=other.hours or self.minutes!=other.minutes)
	  
	  
clock = Clock(2)
print clock

print Clock.at(2,8)
print Clock.at(2,8) + 70