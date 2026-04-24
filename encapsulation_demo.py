class Person:

    def __init__(self_kdm, name, age):
        self_kdm.__name_kdm = name
        self_kdm.__age_kdm = age

def get_name(self_kdm):
    return self_kdm.__name_kdm

def get_age(self_kdm):
    return self_kdm.__age_kdm

p1 = Person("Maria", 20)
print("Name:", p1.get_name_kdm())
print("Age:", p1.get_age_kdm())

# Montes, Karen