class Car:
    def __init__(self_kdm, brand, model, year):
        self_kdm.brand_kdm = brand
        self_kdm.model_kdm = model
        self_kdm.year_kdm = year

    def display_car(self_kdm):
        print(self_kdm.brand_kdm, self_kdm.model_kdm, self_kdm.year_kdm)

car1 = Car("Toyota", "Corolla", 2020)
car1.display_car()

# Montes, Karen