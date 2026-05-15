try:
    number_kdm = int(input("Enter a number: "))
    result_kdm = 100 / number_kdm
    print("Result:", result_kdm)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

    # Montes, Karen D.