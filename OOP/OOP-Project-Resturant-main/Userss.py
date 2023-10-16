from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Order:  # Assuming a simple order class for the sake of demonstration
    def __init__(self, items, bill):
        self.items = items
        self.bill = bill

class Customer(User):
    def __init__(self, name, phone, email, address, money) -> None:
        self.wallet = money
        self.__order = None
        self.due_amount = 0
        super().__init__(name, phone, email, address)

    ##getting its value (getter)
    @property
    def order(self):
        return self.__order

    ##setting its value (setter)
    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        self.due_amount += order.bill
        print(f'{self.name} placed an order with bill {order.bill}')

    def eat_food(self, order):
        print(f'{self.name} ate food: {order.items}')

    def pay_for_order(self, order, manager):
        if order.bill <= self.wallet:  # Check if the customer has enough money in the wallet
            manager.collect_payment(order.bill)
            self.due_amount -= order.bill
            self.wallet -= order.bill
            print(f"{self.name} paid {order.bill} for the order.")
        else:
            print(f"{self.name} does not have enough money to pay for the order.")

    def give_tip(self, tips_amount):
        print(f"{self.name} gave a tip of {tips_amount}.")
        self.wallet -= tips_amount

    def write_review(self, stars):
        if 1 <= stars <= 5:
            print(f"{self.name} gave a {stars}-star review.")
        else:
            print("Invalid number of stars. Please provide a value between 1 and 5.")


class Employee(User):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.due = salary
        self.starting_date = starting_date
        self.department = department

    def receive_salary(self):
        self.due = 0
        print(f"{self.name} received their salary.")


class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department, cooking_item) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.cooking_item = cooking_item


class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        self.tips_earning = 0
        super().__init__(name, phone, email, address, salary, starting_date, department)

    def take_order(self, order):
        print(f"Server {self.name} has taken the order for {order.items}.")

    def transfer_order(self, order):
        print(f"Server {self.name} has transferred the order for {order.items} to the kitchen.")

    def serve_food(self, order):
        print(f"Server {self.name} has served the food for order {order.items}.")

    def receive_tips(self, amount):
        self.tips_earning += amount
        print(f"Server {self.name} received a tip of {amount}.")


class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.balance = 0

    def collect_payment(self, amount):
        self.balance += amount
        print(f"Manager {self.name} collected payment of {amount}. Current balance: {self.balance}")
