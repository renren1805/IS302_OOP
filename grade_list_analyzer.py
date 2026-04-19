# Create an empty list
grades_kdm = []

# Ask the user to input 5 grades
for i in range(5):
    grade_kdm = float(input(f"Enter grade {i+1}: "))
    grades_kdm.append(grade_kdm)

# Compute values
average_kdm = sum(grades_kdm) / len(grades_kdm)
highest_kdm = max(grades_kdm)
lowest_kdm = min(grades_kdm)

# Display results
print("\nAverage Grade:", average_kdm)
print("Highest Grade:", highest_kdm)
print("Lowest Grade:", lowest_kdm)

# Montes, Karen