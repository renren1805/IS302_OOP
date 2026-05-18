from product import Product
from inventory_manager import add_product, view_products

def search_product():
    product_id_kdm = input("Enter Product ID: ")
    try:
        with open("products.txt", "r") as file_kdm:
            for line in file_kdm:
                data = line.strip().split(",")
                if data[0] == product_id_kdm:
                    print("Product Found:", line.strip())
                    return
        print("Product not found")
    except FileNotFoundError:
        print("Inventory file not found")


def main():
    while True:
        print("\nINVENTORY MANAGEMENT SYSTEM")
        print("1 Add Product")
        print("2 View Products")
        print("3 Search Product")
        print("4 Exit")
        choice_kdm = input("Enter choice: ")
        if choice_kdm == "1":
            try:
                product_id_kdm = input("Enter Product ID: ")
                name_kdm = input("Enter Product Name: ")
                price_kdm = float(input("Enter Price: "))
                quantity_kdm = int(input("Enter Quantity: "))
                product_kdm = Product(product_id_kdm, name_kdm, price_kdm, quantity_kdm)
                add_product(product_kdm)
                print("Product added successfully")
            except ValueError:
                print("Invalid input")
        elif choice_kdm == "2":
            view_products()
        elif choice_kdm == "3":
            search_product()
        elif choice_kdm == "4":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()

    # Montes,Karen D.