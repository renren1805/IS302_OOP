def save_student(student):
    with open("students.txt", "a") as file:
        file.write(student.student_id_kdm + "," + student.name_kdm + "," + student.course_kdm + "\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_id_kdm, name_kdm, course_kdm = line.strip().split(",")
                print(student_id_kdm, name_kdm, course_kdm)
    except FileNotFoundError:
        print("No records found.")

        # Montes,Karen D.