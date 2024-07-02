class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)
        print(f"Product '{name}' added.")

    def view_products(self):
        if not self.products:
            print("No products available.")
            return
        print("Products available:")
        for product in self.products:
            print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    def update_product(self, name, new_price, new_quantity):
        for product in self.products:
            if product.name == name:
                product.price = new_price
                product.quantity = new_quantity
                print(f"Product '{name}' updated.")
                return
        print(f"Product '{name}' not found.")

    def delete_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Product '{name}' deleted.")
                return
        print(f"Product '{name}' not found.")

def main():
    manager = ProductManager()

    while True:
        print("\n-- Product Management System Menu --")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            manager.add_product(name, price, quantity)
        elif choice == "2":
            manager.view_products()
        elif choice == "3":
            name = input("Enter product name to update: ")
            new_price = float(input("Enter new price: "))
            new_quantity = int(input("Enter new quantity: "))
            manager.update_product(name, new_price, new_quantity)
        elif choice == "4":
            name = input("Enter product name to delete: ")
            manager.delete_product(name)
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
    