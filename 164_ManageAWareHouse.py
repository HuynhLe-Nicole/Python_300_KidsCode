# Writing a program to manage a warehouse using OOP. We will create basic objects such as products, stock in, stock out, and warehouse management. It provides basic functions like adding products, stocking in, stocking outm and displaying the list of products.
# Algorithm: 1_Create a Product class with properties such as: name, price, and stock quantity. 2_Create a WarehouseManager class to manage the list of products and stock-related operations. 3_Main method: Adding new products to the warehouse. Stocking in(increasing the stock quantity).
#Stocking out(decreasing the stock quantity). Display the list of products. 4_Provide a user interfaceto enter commands and manage the warehouse.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Stock: {self.quantity}"

class WarehouseManager:
    def __init__(self):
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)

    def stock_in(self, name, quantity):
        product = self.find_product(name)
        if product:
            product.quantity += quantity 
            return True 
        return False 
    
    def stock_out(self, name, quantity):
        product = self.find_product(name)
        if product and product.quantity >= quantity:
            product.quantity -= quantity
            return True 
        return False 
    
    def display_product_list(self):
        for product in self.product_list:
            print(product)

    def find_product(self, name):
        for product in self.product_list:
            if product.name == name:
                return product
        return None
    

def menu():
    wm = WarehouseManager()
    while True:
        print("\n1. Add Product")
        print("2. Stock In")
        print("3. Stock Out")
        print("4. Display Product List")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter stock quantity: "))
            product = Product(name, price, quantity)
            wm.add_product(product)
            print("Product added.")

        elif choice == '2':
            name = input("Enter product nane to stock in: ")
            quantity = int(input("Enter quantity to stock in: "))
            if wm.stock_in(name, quantity):
                print("Stock in successful.")
            else:
                print("Product not found.")

        elif choice == '3':
            name = input("Enter product nane to stock out: ")
            quantity = int(input("Enter quantity to stock out: "))
            if wm.stock_out(name, quantity):
                print("Stock out successful.")
            else:
                print("Cannot stock out (insufficient quantity or product not found).")

        elif choice == '4':
            wm.display_product_list()
        
        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid selection. Please choose again.")


if __name__=="__main__":
    menu()


