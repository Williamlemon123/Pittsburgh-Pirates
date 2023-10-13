class Restaurant:
    def __init__(self, name, rent, menu = []) -> None:
        self.name = name
        self.orders = []
        self.chef = None
        self.server = None
        self.manager = None
        self.rent = rent
        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.balance = 0
        self.profit = 0

    def add_employee(self, employee_type, empployee):
        if employee_type == "chef":
            self.chef = empployee
        elif employee_type == 'server':
            self.server = empployee
        elif employee_type == 'manager':
            self.manager = empployee

    def add_order(self, order):
        self.orders.append(order)
  
    def recive_payment(self, order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print('Not enough Money pay more')
        
    def pay_expense(self, amount, description):
        if amount <self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expense {amount} for {description}')
        else:
            print(f'not enough money to pay {amount}')

    
    def pay_salary(self, employee):
        print(f'Paying salary for {employee.name} salary : {employee.salary}')
        if employee.salary < self.balance:
            self.balance -= employee.salary
            self.expense += employee.salary
            employee.receive_salary()

    def Show_employees(self):
        print(f'\n-----------Show Employees-----------')
        if self.chef is not None:
            print(f'Chef: {self.chef.name} with salary: {self.chef.salary}')
        if self.server is not None:
            print(f'Server: {self.server.name} with salary: {self.server.salary}')
        if self.manager is not None:
            print(f'Manager: {self.manager.name} with salary: {self.manager.salary}')

        


