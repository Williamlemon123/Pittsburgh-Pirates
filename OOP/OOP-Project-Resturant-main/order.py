class Order:
    def __init__(self, customer) -> None:
        self.customer = customer
        self.items = []
        self.bill = 0.0

    def add_item(self, item):
        if hasattr(item, 'price'):  # Check if the item has a price attribute
            self.items.append(item)
            self.bill += item.price
        else:
            raise ValueError("The provided item does not have a price attribute.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.bill -= item.price

    def display_order(self):
        print(f"Order for {self.customer}:")
        for item in self.items:
            print(f" - {item.name}: ${item.price:.2f}")
        print(f"Total Bill: ${self.bill:.2f}")

    def apply_discount(self, percentage):
        self.bill -= self.bill * (percentage / 100)

    def apply_tax(self, percentage):
        self.bill += self.bill * (percentage / 100)