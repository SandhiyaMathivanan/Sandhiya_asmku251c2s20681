"""
Implement a function called sort_students that takes a list of 
students objects as input and sorts the lists based on theirCGPA
( Cumulative Grade Point Average ) in decending order . each student object 
has the following attributes: name
(strin), roll_number(string), and 
cgpa(float).test the function with 
different input lists of students .
"""


class student:

  def __init__(self, name, roll_number, cgpa):
   self.name = name
   self.roll_number = roll_number 
   self.cgpa = cgpa


def sort_students(student_lists):
  # sort the list of students in descending order of CGPA
  sorted_students = sorted(student_lists,
student: student.cgpa,
reverse=true)
  return sorted_students


 # example usage:
students = [
   student("hari", "A123", 7.8),
   student("srikanth", "A124", 7.9),
   student("saumya", "A125", 9.1),
   student("Mahidhar", "A126", 9.2),
]

sorted_students = sort_students(students)

# print the sorted list of students 
for students in sorted_students:
  print("Name: {},Roll Number: {}, CGPA: {}".formastuden.name,student.roll_number student.cgpa)