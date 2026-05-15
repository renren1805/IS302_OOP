try:
    num1_kd = float(input("Enter first number: "))
    num2_kdm = float(input("Enter second number: "))
    result_kdm = num1_kd / num2_kdm
    print("Result:", result_kdm)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid numeric input")

    # Montes, Karen D.