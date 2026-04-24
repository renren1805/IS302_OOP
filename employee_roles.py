class Employee:
    def work(self_kdm):
        print("Employee performs tasks")

class Programmer(Employee):
    def work(self_kdm):
        print("Programmer writes code")

class Designer(Employee):
    def work(self_kdm):
        print("Designer creates UI designs")

employees_kdm = [Programmer(), Designer()]
for emp in employees_kdm:
    emp.work()

    # Montes, Karen