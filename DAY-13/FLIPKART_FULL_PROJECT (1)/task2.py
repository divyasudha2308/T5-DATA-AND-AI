import json
from datetime import datetime

# ---------------- DECORATOR FOR LOGGING ----------------
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Action: {func.__name__} executed at {datetime.now()}")
        return func(*args, **kwargs)
    return wrapper


# ---------------- BASE CLASS ----------------
class Product:
    def __init__(self, pid, name, price, stock):
        self.__pid = pid
        self.__name = name
        self.__price = price
        self.__stock = stock

    # -------- GETTERS --------
    def get_pid(self):
        return self.__pid

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # -------- SETTERS --------
    def set_stock(self, stock):
        if stock < 0:
            raise ValueError("Stock cannot be negative!")
        self.__stock = stock

    # -------- POLYMORPHISM METHOD --------
    def product_type(self):
        return "General Product"

    def to_dict(self):
        return {
            "pid": self.__pid,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "type": self.product_type()
        }


# ---------------- SUBCLASS: Electronics ----------------
class Electronics(Product):
    def __init__(self, pid, name, price, stock, warranty):
        super().__init__(pid, name, price, stock)
        self.warranty = warranty

    def product_type(self):
        return "Electronics"


# ---------------- SUBCLASS: Grocery ----------------
class Grocery(Product):
    def __init__(self, pid, name, price, stock, expiry_date):
        super().__init__(pid, name, price, stock)
        self.expiry_date = expiry_date

    def product_type(self):
        return "Grocery"


# ---------------- CUSTOM ITERATOR ----------------
class InventoryIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            item = self.products[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


# ---------------- INVENTORY CLASS ----------------
class Inventory:
    def __init__(self):
        self.products = []

    # -------- ADD PRODUCT --------
    @log_action
    def add_product(self, product):
        self.products.append(product)
        print("✅ Product Added Successfully!")

    # -------- REMOVE PRODUCT --------
    @log_action
    def remove_product(self, pid):
        for p in self.products:
            if p.get_pid() == pid:
                self.products.remove(p)
                print("✅ Product Removed Successfully!")
                return
        print("❌ Product Not Found!")

    # -------- UPDATE STOCK --------
    @log_action
    def update_stock(self, pid, stock):
        for p in self.products:
            if p.get_pid() == pid:
                p.set_stock(stock)
                print("✅ Stock Updated!")
                return
        print("❌ Product Not Found!")

    # -------- SEARCH PRODUCT --------
    @log_action
    def search_product(self, name):
        for p in self.products:
            if p.get_name().lower() == name.lower():
                print("✅ Product Found:", p.to_dict())
                return
        print("❌ Product Not Found!")

    # -------- DISPLAY PRODUCTS --------
    def list_products(self):
        print("\n📌 Inventory Products:")
        iterator = InventoryIterator(self.products)
        for product in iterator:
            print(product.to_dict())

    # -------- SAVE TO FILE --------
    @log_action
    def save_inventory(self):
        with open("inventory.json", "w") as file:
            json.dump([p.to_dict() for p in self.products], file, indent=4)
        print("✅ Inventory Saved to File!")

    # -------- LOAD FROM FILE --------
    @log_action
    def load_inventory(self):
        try:
            with open("inventory.json", "r") as file:
                data = json.load(file)

            self.products.clear()
            for item in data:
                if item["type"] == "Electronics":
                    self.products.append(
                        Electronics(item["pid"], item["name"], item["price"], item["stock"], "1 Year")
                    )
                elif item["type"] == "Grocery":
                    self.products.append(
                        Grocery(item["pid"], item["name"], item["price"], item["stock"], "2026")
                    )
                else:
                    self.products.append(
                        Product(item["pid"], item["name"], item["price"], item["stock"])
                    )

            print("✅ Inventory Loaded Successfully!")

        except FileNotFoundError:
            print("❌ No Inventory File Found!")


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    inv = Inventory()

    while True:
        print("\n====== INVENTORY MANAGEMENT SYSTEM ======")
        print("1. Add Electronics")
        print("2. Add Grocery")
        print("3. Remove Product")
        print("4. Update Stock")
        print("5. Search Product")
        print("6. List Products")
        print("7. Save Inventory")
        print("8. Load Inventory")
        print("9. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                pid = input("Enter ID: ")
                name = input("Enter Name: ")
                price = float(input("Enter Price: "))
                stock = int(input("Enter Stock: "))
                warranty = input("Enter Warranty: ")

                inv.add_product(Electronics(pid, name, price, stock, warranty))

            elif choice == "2":
                pid = input("Enter ID: ")
                name = input("Enter Name: ")
                price = float(input("Enter Price: "))
                stock = int(input("Enter Stock: "))
                expiry = input("Enter Expiry Date: ")

                inv.add_product(Grocery(pid, name, price, stock, expiry))

            elif choice == "3":
                pid = input("Enter Product ID to Remove: ")
                inv.remove_product(pid)

            elif choice == "4":
                pid = input("Enter Product ID: ")
                stock = int(input("Enter New Stock: "))
                inv.update_stock(pid, stock)

            elif choice == "5":
                name = input("Enter Product Name: ")
                inv.search_product(name)

            elif choice == "6":
                inv.list_products()

            elif choice == "7":
                inv.save_inventory()

            elif choice == "8":
                inv.load_inventory()

            elif choice == "9":
                print("👋 Exiting Program...")
                break

            else:
                print("❌ Invalid Choice!")

        except Exception as e:
            print("⚠ Error:", e)