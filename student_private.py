class Student:
    def __init__(self_kdm, name, student_id, gpa):
        self_kdm.__name_kdm = name
        self_kdm.__student_id_kdm = student_id
        self_kdm.__gpa_kdm = gpa

    def get_student_info(self_kdm):
        print("Name:", self_kdm.__name_kdm)
        print("Student ID:", self_kdm.__student_id_kdm)
        print("GPA:", self_kdm.__gpa_kdm)

student1 = Student("Juan", "2023-001", 1.75)

student1.get_student_info()

# Montes, Karen