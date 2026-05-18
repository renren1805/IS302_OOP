class Student:
    def __init__(self, student_id, name, course):
        self.student_id_kdm = student_id
        self.name_kdm = name
        self.course_kdm = course

    def display_info(self):
        print(self.student_id_kdm, self.name_kdm, self.course_kdm)

        # Montes,Karen D.