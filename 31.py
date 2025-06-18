class Product:
    total_products = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_products += 1

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Total products created: {Product.total_products}")


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period  # у місяцях

    def display_info(self):
        super().display_info()
        print(f"Warranty period: {self.warranty_period} months")
        print("Type: Electronic")


class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size  # розмір одягу

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")
        print("Type: Clothing")


if __name__ == "__main__":
    print("Creating products...")
    laptop = ElectronicProduct("Laptop", 999.99, 24)
    tshirt = ClothingProduct("T-Shirt", 29.99, "L")
    phone = ElectronicProduct("Smartphone", 699.99, 12)

    print("\nProduct information:")
    laptop.display_info()
    print()
    tshirt.display_info()
    print()
    phone.display_info()