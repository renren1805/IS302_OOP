class Animal:
    def speak(self_kdm):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self_kdm):
        print("Dog barks")

class Cat(Animal):
    def speak(self_kdm):
        print("Cat meows")

animals_kdm = [Dog(), Cat()]
for animal_kdm in animals_kdm:
    animal_kdm.speak()

    # Montes,Karen