# Import necessary classes from modules
from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from Userss import Chef, Customer, Server, Manager
from order import Order

def main():
    # Initializing a new menu
    menu = Menu()

    # Creating pizzas, burgers, and drinks and adding them to the menu
    pizza_1 = Pizza('Shutki pizz', 600, 'large', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('alor bortar pizz', 400, 'large', ['potato', 'onion'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('dal pizza', 500, 'large', ['dal', 'piyazo'])
    menu.add_menu_item('pizza', pizza_3)

    burger_1 = Burger('naga burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('beef burger', 2000, 'beef', ['goru', 'haddi'])
    menu.add_menu_item('burger', burger_2)

    coke = Drinks('coke', 50, True)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('Mocha coffee', 300, False)
    menu.add_menu_item('drinks', coffee)

    # Displaying the complete menu to the console
    menu.show_menu()

    # Initializing a restaurant and adding employees
    restaurant = Restaurant("Sai Baba Restaurant", 2000, menu)

    manager = Manager('Mashudul hoque', 18, 'mashud@mail.com', 'ctg', 30000, 'Jan 01 2022', "core")
    restaurant.add_employee('manager', manager)  # specify the type 'manager'

    chef = Chef('Siddik baburchi', 82, 'siddik@maill.com', 'baskali', 2000, 'Feb 02 2022', 'chef', 'everything')
    restaurant.add_employee('chef', chef)  # specify the type 'chef'

    server = Server('alam bodda', 19, 'bodda@mail.com', 'baskali', 5000, 'jan 2, 2022', 'staff')
    restaurant.add_employee('server', server)  # specify the type 'server'

    # Displaying the list of employees
    restaurant.Show_employees()
    print('-----------------------------------')

    # Simulating the process of a customer placing an order
    customer_1 = Customer('opi', 12, 'opi@com', 'ctg', 10000)
    order_1 = Order(customer_1)
    order_1.add_item(pizza_3)
    order_1.add_item(coffee)

    # Apply a 10% discount and a 5% tax to order_1
    order_1.apply_discount(10)
    order_1.apply_tax(5)

    order_1.display_order()  # Shows the updated bill after discount and tax

    customer_1.pay_for_order(order_1,manager)
    restaurant.add_order(order_1)
    restaurant.recive_payment(order_1, 2000, customer_1)
    print(f'revenue and balance after first customer: ', restaurant.revenue, restaurant.balance)

    customer_2 = Customer('rafi', 12, 'opi@com', 'ctg', 50000)
    order_2 = Order(customer_2)
    order_2.add_item(pizza_2)
    order_2.add_item(burger_2)
    order_2.add_item(coke)
    order_2.add_item(coffee)

    # Apply a 10% discount and a 5% tax to order_2
    order_2.apply_discount(10)
    order_2.apply_tax(5)

    order_2.display_order()  # Shows the updated bill after discount and tax

    customer_2.pay_for_order(order_2,manager)
    restaurant.add_order(order_2)
    restaurant.recive_payment(order_2, 4000, customer_2)
    print(f'revenue and balance after 2nd customer: ', restaurant.revenue, restaurant.balance)
    print('-------------------------------------------------')
    # Paying expenses and salaries
    restaurant.pay_expense(restaurant.rent, 'Rent')
    print(f'After paying rent: ', restaurant.revenue, restaurant.expense)
    restaurant.pay_salary(chef)
    print(f'After paying chef\'s salary: ', restaurant.revenue, restaurant.balance, restaurant.expense)

# Entry point of the script
if __name__ == '__main__':
    main()
