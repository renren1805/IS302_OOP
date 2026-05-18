class Product:
    def __init__(self, product_id, name, price, quantity):
        self.__product_id_kdm = product_id
        self.__name_kdm = name
        self.__price_kdm = price
        self.__quantity_kdm = quantity

    def get_product_info(self):
        return f"{self.__product_id_kdm}, {self.__name_kdm}, {self.__price_kdm}, {self.__quantity_kdm}"

    def get_id(self):
        return self.__product_id_kdm

    def update_quantity(self, quantity):
        self.__quantity_kdm = quantity

        # Montes,Karen D.