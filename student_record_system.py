name_kdm = input("Enter student name: ")
course_kdm = input("Enter course: ")
with open("students.txt", "a") as file_kdm:
    file_kdm.write(name_kdm + "," + course_kdm + "\n")
print("\nStudent Records")
with open("students.txt", "r") as file_kdm:
    for line in file_kdm:
        print(line.strip())

        # Montes, Karen
        