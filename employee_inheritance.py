class Employee:
    def __init__(self_kdm, name, salary):
        self_kdm.name = name
        self_kdm.salary = salary

class Manager(Employee):
    def __init__(self_kdm, name, salary, department):
        super().__init__(name, salary)
        self_kdm.department = department

    def display_manager(self_kdm):
        print("Name:", self_kdm.name)
        print("Salary:", self_kdm.salary)
        print("Department:", self_kdm.department)

manager1 = Manager("John", 50000, "IT")
manager1.display_manager()

# montes,karen