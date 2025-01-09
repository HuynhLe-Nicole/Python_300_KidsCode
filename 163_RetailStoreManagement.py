# Writing a retail store management program using object oriented programming(OOP). It will provide basic functionslities such as adding product, creating orders, calculatinh total order amounts, and displaying list of products and orders.
# Algorithm: 1_Create a Product class with properties like name, price, and stock quantity. 2_Create an Order class with properties for the list of products and the total amount. 3_Create a StoreManagement class to manage the lists of products and orders.
# Main Methods: Add new products to the store. Create new orders. Calculate the total amount of an order. Display the list of products. Display the list of orders. Provide a user interface to input commands and manage the store.


class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Stock: {self.stock_quantity}"


class Order:
    def __init__(self):
        self.product_list = []
        self.total_amount = 0

    def add_product(self, product, quantity):
        if product.stock_quantity >= quantity:
            self.product_list.append((product, quantity))
            product.stock_quantity -= quantity
            self.total_amount += product.price * quantity
            return True
        return False
    
    def __str__(self):
        items = ", ".join(f"{product.name} (x{quantity})" for product, quantity in self.product_list)
        return f"Order: {items}, Total Amount: {self.total_amount}"
    

class StoreManager:
    def __init__(self):
        self.product_list = []
        self.order_list = []

    def add_product(self, product):
        self.product_list.append(product)

    def create_order(self, purchase_list):
        order = Order()
        for product_name, quantity in purchase_list.item():
            product = self.find_product(product_name)
            if product:
                if not order.add_product(product, quantity):
                    print(f"Insufficient quantity for product: {product_name}")
                    return None
        self.order_list.append(order)
        return order
    
    def display_product_list(self):
        for product in self.product_list:
            print(product)

    def display_order_list(self):
        for order in self.order_list:
            print(order)

    def find_product(self, name):
        for product in self.product_list:
            if product.name == name:
                return product
        return None
    
def menu():
    store_manager = StoreManager()
    while True:
        print("\n1. Add Product")
        print("2. Create Order")
        print("3. Display Product List")
        print("4. Display Order List")
        print("5. Exit") 
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter stock quantity: "))
            product = Product(name, price, quantity)
            store_manager.add_product(product)
            print("Product added.")

        elif choice == '2':
            purchase_list = {}
            while True:
                name = input("Enter the product name to buy (or 'done' to finish): ")
                if name == 'done':
                    break
                quantity = int(input("Enter quantity: "))
                purchase_list[name] = quantity
            order = store_manager.create_order(purchase_list)
            if order:
                print("Order created.")
            else:
                print("Cannot create order.")

        elif choice == '3':
            store_manager.display_product_list()

        elif choice == '4':
            store_manager.display_order_list()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, Please select again.")

if __name__=="__main__":
    menu()