class Vehicle:
    def __init__(self_kdm, brand, model):
        self_kdm.brand = brand
        self_kdm.model = model

class Car(Vehicle):



    def __init__(self_kdm, brand, model, year):
        super().__init__(brand, model)
        self_kdm.year = year

    def display_car(self_kdm):
        print(self_kdm.brand, self_kdm.model, self_kdm.year)

car1 = Car("Toyota", "Corolla", 2022)
car1.display_car()