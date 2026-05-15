try:
    with open("data.txt", "r") as file:
        content_kdm = file.read()
    print(content_kdm)
except FileNotFoundError:
    print("File does not exist")

# Montes, Karen D.