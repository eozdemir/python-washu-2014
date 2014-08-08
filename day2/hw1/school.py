class School():
  def __init__(self, school):
    self.school = school
    self.db = {}
	
  def add(self, student, grade):
    if type(grade) != int:
  	  self.db = "Try to use integers for grade levels!"
    else:
      if grade in self.db:
        self.db[grade].add(student)
      else: 
        self.db[grade] = {student}
      
  def sort(self):
    sorted_students = {}
    for i in self.db.keys():
      sorted_students[i] = sorted(self.db[i])
      # since sorted forced them into list
      sorted_students[i] = tuple(sorted_students[i])
    return sorted_students
      
  def grade(self, student_grade):
  	if student_grade not in self.db:
  	  return None
  	else:
  	  return self.db[student_grade]
  	  
    