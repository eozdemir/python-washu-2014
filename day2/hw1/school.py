class School():
  def __init__(self, school):        # initialize the class
    self.school = school 	         # only argument to generate an incidence of School class is school name
    self.db = {}			         # create an empty dictionary to add students and grades
	
  def add(self, student, grade):     # function to add students and grades to dictionary
    if type(grade) != int:           # in case user might enter invalid grade type
      self.db = "Try to use integers for grade levels!" # also added a test for that
    else:						     # function works with a proper grade type
      if grade in self.db:		     # if the grade already exists in dictionary
        self.db[grade].add(student)  # add the student name using given key for grade level
      else: 						 # if the grade is not there 
        self.db[grade] = {student}   # add a new key and assign a name for corresponding value 
      
  def sort(self):					 # function to sort the students in a grade
    sorted_students = {}			 # a new/empty dictionary to add sorted students
    for i in self.db.keys():		 # loop goes through the keys of dic.
      sorted_students[i] = sorted(self.db[i]) # assigns sorted names into grade keys 
      sorted_students[i] = tuple(sorted_students[i]) # since 'sorted' forced them into list
    return sorted_students           # returns the new dictionary with sorted students
      
  def grade(self, student_grade):    # function to get students in a grade
  	if student_grade not in self.db: # if no such grade exists 
  	  return None					 # returns None according to test
  	else:							 # if such grade exists
  	  return self.db[student_grade]  # uses the grade key to reach out to student names
  	  
    