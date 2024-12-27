import mysql.connector
from tabulate import tabulate

db = mysql.connector.connect(host="localhost", user="root", password="your_passwd", database="car_dealership")
cursor = db.cursor()
def add_customer(name, phone, email):
    db = mysql.connector.connect (host="Localhost",user="root", password="your_passwd", database="car_dealership")
    cursor = db.cursor()
    cursor.execute("INSERT INTO customers (name,phone, email) VALUES( % s, %s, %s)", (name, phone,email) )
    db.commit()

def add_car(make, model, year, price, color):
    db = mysql.connector.connect(host="Localhost", user="root", password="your_passwd", database="car_dealership")
    cursor = db.cursor()
    cursor.execute("INSERT INTO cars (make, model,year, price, color) VALUES( % s, %s, %s, %S, %S)",(make, model, year, price, color))
    db.commit()

def make_sale(customer_id, car_id, purchase_date):
    db = mysql.connector.connect(host="Localhost", user="root", password="your_passwd", database="car_dealership")
    cursor = db.cursor()
    cursor.execute("INSERT INTO sales (customer_id,car_id, purchase_date) VALUES( % s, %s, %s)",(customer_id, car_id,purchase_date) )
    db.commit()

def get_all_cars():
    db = mysql.connector.connect(host="Localhost",user="root", password="your_passwd", database="car_dealership")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cars")
    rows = cursor.fetchall()
    column_names = ["Id", "Make", "Model", "Year", "Price", "Color"]
    print(tabulate(rows, headers=column_names, tablefmt="grid"))

def customers():
    db = mysql.connector.connect(host="Localhost",user="root", password="your_passwd", database="car_dealership")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM customers")
    # Fetch all the rows
    rows = cursor.fetchall()
    column_names = ["Id", "Name", "Phone", "Email"]
    print(tabulate(rows, headers=column_names,tablefmt="grid"))


def show_sales():
    db = mysql.connector.connect(host="Localhost", user="root", password="your_passwd", database="car_dealership")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM sales")
    rows = cursor. fetchall()
    column_names = ["Id", "Customer Id", "Car Id", "Date Of Purchasing" ]
    print(tabulate(rows, headers=column_names,tablefmt="grid") )
    cursor.close()
while True:
        print(
            '''
        
        |============================|
        |                            | 
        |       CAR DEALERSHIP       |
        |                            |
        |============================|
        
        
        ''')
        print(
            '''
        You Can Perform The Following Actions:
        1 - Add a new Customer
        2 - Add a New Car
        3 - Make a sale
        4 - Get all the cars in the dealership
        5 - Show Sales
        6 - Show Customers
        7 - Quit
        ''')

        action = int(input("Enter The Action You Need ToPerform: "))
        if action == 7:
            break
        elif action == 1:
            name = input('Name of customer: ')
            phone = int(input('Phone number: '))
            email = input('Email address: ')
            add_customer(name, phone, email)
        elif action == 2:

            make = input('Make of car: ')
            model = input('Model of car: ')
            year = int(input('Year of car: '))
            price = float(input('Price of car: '))
            color = input('Color of car: ')
            add_car(make, model, year, price, color)
        elif action == 3:
            custid = int(input('Customer ID to sell from'))
            carid = int(input('Car ID to sell: '))
            purchasedate = input("Enter Date Of Purchasing: ")
            make_sale(custid, carid, purchasedate)
        elif action == 4:
             get_all_cars()
        elif action == 5:
             show_sales()
        elif action == 6:
             customers()
        else:
            print("Invalid Input")
