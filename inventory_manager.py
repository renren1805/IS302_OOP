def add_product(product):
    with open("products.txt", "a") as file_kdm:
        file_kdm.write(product.get_product_info_kdm() + "\n")

def view_products():
    try:
        with open("products.txt", "r") as file_kdm:
            for line in file_kdm:
                print(line.strip())
    except FileNotFoundError:
        print("No products found.")

        # MOntes,Karen D.