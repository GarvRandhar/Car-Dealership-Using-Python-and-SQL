# Car Dealership Management System

This is a Python-based application to manage a car dealership's operations, including managing customers, cars, and sales. It uses MySQL as the database and provides a menu-driven interface for the user.

## Features

- **Add New Customers**: Save customer details including name, phone, and email.
- **Add New Cars**: Add details of cars available in the dealership such as make, model, year, price, and color.
- **Record Sales**: Record sales transactions by linking customers to cars and storing the purchase date.
- **View All Cars**: Display a list of all available cars.
- **View Customers**: Display a list of all customers.
- **View Sales**: Display all sales transactions.

## Prerequisites

- Python 3.7+
- MySQL Database
- Python Libraries:
  - `mysql-connector-python`
  - `tabulate`

## Install the required Python libraries:


pip install mysql-connector-python tabulate

# Create the database and tables:


CREATE DATABASE car_dealership;

USE car_dealership;

CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(255) NOT NULL
);

CREATE TABLE cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(255) NOT NULL,
    model VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    color VARCHAR(50) NOT NULL
);

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    car_id INT NOT NULL,
    purchase_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (car_id) REFERENCES cars(id)
);

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions
Contributions are welcome! Feel free to submit a pull request or report an issue.
