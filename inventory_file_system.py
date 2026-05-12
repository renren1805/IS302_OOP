product_kdm = input("Enter product name: ")
price_kdm = input("Enter price: ")
with open("inventory.txt", "a") as file_kdm:
    file_kdm.write(product_kdm + "," + price_kdm + "\n")
print("Product saved successfully")

# Montes, Karen