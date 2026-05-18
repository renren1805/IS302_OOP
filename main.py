from student import Student
from file_handler import save_student, view_students

def add_student():
    student_id_kdm = input("Enter Student ID: ")
    name_kdm = input("Enter Name: ")
    course_kdm = input("Enter Course: ")
    student = Student(student_id_kdm, name_kdm, course_kdm)
    save_student(student)
    print("Student added successfully")

def search_student():
    search_id = input("Enter Student ID to search: ")
    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_id_kdm, name_kdm, course_kdm = line.strip().split(",")
                if student_id_kdm == search_id:
                    print("Student Found:")
                    print(student_id_kdm, name_kdm, course_kdm)
                    return
        print("Student not found")
    except FileNotFoundError:
        print("No records available")

while True:
    print("\nSTUDENT INFORMATION SYSTEM")
    print("1 Add Student")
    print("2 View Students")
    print("3 Search Student")
    print("4 Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")

        # Montes, Karen D.