"""
1. Create a "Student" class containing:
   - Student ID
   - Name
   - Age
   - Marks
2. Implement methods to display student information and update marks.
3. Create a "StudentManager" class that uses a Python list or dictionary to store multiple students.
4. Implement functionality to:
   - Add a student.
   - Display all students.
   - Search for a student by ID.
   - Remove a student.
5. Create at least three student objects and demonstrate that all functionalities work correctly.
"""
class Student:
    def __init__(self, studentID, name, age, marks):
        self.studentID = studentID
        self.name = name
        self.age = age
        self.marks = marks
        
    def display_info(self):
        print(f"{self.studentID}, {self.name}, {self.age}, {self.marks}")

class StudentManager:
        def __init__(self):
            self.manage = {
                "ID101" : {"name": "Rayyan", "age": 22, "marks": 95},
                "ID102" : {"name": "John", "age": 20, "marks": 70},
                "ID103" : {"name": "Joe", "age": 21, "marks": 85}
            }

s1 = Student(101, "Rayyan", 22, 90)
s2 = Student(102, "John", 20, 70)
s3 = Student(103, "Joe", 21, 85)

#updating student marks
s1.marks = 95

#display all students
s1.display_info()
s2.display_info()
s3.display_info()


#searching student by ID
manager = StudentManager()
print(manager.manage.get("ID103"))

#add student
manager.manage["ID104"] = {"name: Nolan", "age: 24", "marks: 70"}
manager.manage["ID105"] = {"name: Morgan", "age: 21", "marks: 80"}

#delete student 
manager.manage.pop("ID101")
print(manager.manage)
