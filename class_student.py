class Student:
    def __init__(self_kdm, name, student_id, course):
        self_kdm.name_kdm = name
        self_kdm.student_id_kdm = student_id
        self_kdm.course_kdm = course

    def display_student(self_kdm):
        print("Name:", self_kdm.name_kdm)
        print("Student ID:", self_kdm.student_id_kdm)
        print("Course:", self_kdm.course_kdm)

student1 = Student("Maria", "2023-001", "BSIS")
student1.display_student()

# Montes, Karen
