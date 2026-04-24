# school_system.py

class Person:
    def __init__(self_kdm, name, age):
        self_kdm.name = name
        self_kdm.age = age

    def display_info(self_kdm):
        print(f"Name: {self_kdm.name}")
        print(f"Age: {self_kdm.age}")

class Student(Person):
    def __init__(self_kdm, name, age, course):
        super().__init__(name, age)
        self_kdm.course = course

    def display_info(self_kdm):
        print(f"Name: {self_kdm.name}")
        print(f"Age: {self_kdm.age}")
        print(f"Course: {self_kdm.course}")

class Teacher(Person):
    def __init__(self_kdm, name, age, subject):
        super().__init__(name, age)
        self_kdm.subject = subject

    def display_info(self_kdm):
        print(f"Name: {self_kdm.name}")
        print(f"Age: {self_kdm.age}")
        print(f"Subject: {self_kdm.subject}")

# Test the classes
student1 = Student("Maria", 16, "Computer Science")
teacher1 = Teacher("Mr. Reyes", 35, "Math")

print("Student Info:")
student1.display_info()
print("\nTeacher Info:")
teacher1.display_info()

# Montes,Karen