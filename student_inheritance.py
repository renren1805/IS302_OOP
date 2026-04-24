class Person:
    def __init__(self_kdm, name, age):
        self_kdm.name_kdm = name
        self_kdm.age_kdm = age

class Student(Person):
    def __init__(self_kdm, name, age, course):
        super().__init__(name, age)
        self_kdm.course = course

    def display_student(self_kdm):
        print("Name:", self_kdm.name_kdm)
        print("Age:", self_kdm.age_kdm)
        print("Course:", self_kdm.course)

student1 = Student("Maria", 20, "BSIS")
student1.display_student()

# Montes,Karen
