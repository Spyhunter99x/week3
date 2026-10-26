class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=18):
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        subtotal = 0

        for product in self.products:
            subtotal += product.calculate_total()

        return subtotal

    def calculate_tax(self):
        subtotal = self.calculate_subtotal()
        tax = subtotal * self.tax_rate / 100

        return tax

    def calculate_grand_total(self):
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()

        return subtotal + tax

    def display_bill(self):
        print("\n")
        print("=" * 75)
        print("                         BILL")
        print("=" * 75)

        print(
            f"{'Product':<25}"
            f"{'Price':>12}"
            f"{'Quantity':>12}"
            f"{'Total':>15}"
        )

        print("-" * 75)

        for product in self.products:
            total = product.calculate_total()

            print(
                f"{product.name:<25}"
                f"₹{product.price:>10.2f}"
                f"{product.quantity:>12}"
                f"₹{total:>13.2f}"
            )

        print("-" * 75)

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        grand_total = self.calculate_grand_total()

        print(f"{'Subtotal':<50} ₹{subtotal:>13.2f}")
        print(f"{'Tax (' + str(self.tax_rate) + '%)':<50} ₹{tax:>13.2f}")
        print("=" * 75)
        print(f"{'Grand Total':<50} ₹{grand_total:>13.2f}")
        print("=" * 75)


# Creating products
product1 = Product("Laptop", 50000, 1)
product2 = Product("Mouse", 800, 2)
product3 = Product("Keyboard", 1500, 1)
product4 = Product("USB Cable", 300, 3)

# Creating bill
bill = Bill(18)

# Adding products to bill
bill.add_product(product1)
bill.add_product(product2)
bill.add_product(product3)
bill.add_product(product4)

# Display final bill
bill.display_bill()