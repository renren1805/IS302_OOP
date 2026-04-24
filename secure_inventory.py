# secure_inventory.py

class Product:
    def __init__(self_kdm, name, price, quantity):
        """Constructor to initialize private attributes"""
        self_kdm.__name = name          # Private attribute
        self_kdm.__price = price        # Private attribute
        self_kdm.__quantity = quantity  # Private attribute
    
    def get_product_info(self_kdm):
        """Returns product information as a formatted string"""
        return f"Product: {self_kdm.__name}\nPrice: {self_kdm.__price}\nQuantity: {self_kdm.__quantity}"
    
    def update_quantity(self_kdm, new_quantity):
        """Updates the product quantity"""
        if new_quantity >= 0:
            self_kdm.__quantity = new_quantity
            print(f"Quantity updated to {self_kdm.__quantity}")
        else:
            print("Error: Quantity cannot be negative")
    
    def update_price(self_kdm, new_price):
        """Updates the product price"""
        if new_price >= 0:
            self_kdm.__price = new_price
            print(f"Price updated to {self_kdm.__price}")
        else:
            print("Error: Price cannot be negative")
    
    # Optional: Getter methods for individual attributes if needed
    def get_name(self_kdm):
        return self_kdm.__name
    
    def get_price(self_kdm):
        return self_kdm.__price
    
    def get_quantity(self_kdm):
        return self_kdm.__quantity


# Demonstration of the Inventory System
if __name__ == "__main__":
    # Create a product instance
    product = Product("Laptop", 45000, 10)
    
    # Display product information
    print(product.get_product_info())
    print("-" * 30)
    
    # Update quantity
    product.update_quantity(15)
    print(product.get_product_info())
    print("-" * 30)
    
    # Update price
    product.update_price(50000)
    print(product.get_product_info())
    print("-" * 30)
    
    # Test error handling
    product.update_quantity(-5)   # Should show error
    product.update_price(-1000)   # Should show error

# Montes, Karen