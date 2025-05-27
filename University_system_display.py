class Person:
    def __init__(self, name, age, ID):
        self.name=name
        self.age=age
        self.ID=ID
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.ID}")
        
class Student(Person):
    def __init__(self, name, age, ID, major):
        super().__init__(name, age, ID)  
        self.major=major
        self.courses=[]
        
    def enroll_course(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")
        
    def display_info(self):
        super().display_info()       
        print(f"Major: {self.major}, courses: {', '.join(self.courses)}")      
        
        
class Lecturer(Person):
    def __init__(self, name, age, ID, department):
        super().__init__(name, age, ID)
        self.department=department
        self.courses_taught=[]
        
    def assign_course(self, course):
        self.courses_taught.append(course)
        print(f"{self.name} assigned to teach {course}")
        
    def display_info(self):
        super().display_info()  
        print(f"Department: {self.department}, Teaching: {', '.join(self.courses_taught)}")   
        
        
class Staff(Person):
    def __init__(self, name, age, ID, role):
        super().__init__(name, age, ID)
        self.role=role
        
    def display_info(self):
        super().display_info()     
        print(f"Role: {self.role}")
        
        

student=Student("Junior", 21, "BSSE01", "Software Enginnering")
lecturer=Lecturer("Nasser", 40, "LTE10", "Engineering")
staff=Staff("Peter", 50, "STAFF03", "Admin")

print("\n--STUDENT--")  
student.enroll_course("Data structures")
student.enroll_course("OOP")
student.display_info()          

print("\n--LECTURER--")  
lecturer.assign_course("Computer networks")
lecturer.display_info()

print("\n--STAFF--")    
staff.display_info()  
            