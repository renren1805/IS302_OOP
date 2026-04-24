class Employee:
    def __init__(self_kdm, name):
        self_kdm.__name_kdm = name
        self_kdm.__salary_kdm = 0

    def set_salary(self_kdm, salary):
        if salary > 0:
            self_kdm.__salary_kdm = salary

    def get_salary(self_kdm):
        return self_kdm.__salary_kdm

emp = Employee("Ana")
emp.set_salary(30000)
print("Salary:", emp.get_salary())