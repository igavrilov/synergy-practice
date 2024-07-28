CREATE TABLE Services (
    service_id INT PRIMARY KEY,
    service_name VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2)
);

CREATE TABLE Tours (
    tour_id INT PRIMARY KEY,
    tour_name VARCHAR(255),
    description TEXT,
    duration_days INT
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    position VARCHAR(255),
    hire_date DATE
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    tour_id INT,
    service_id INT,
    employee_id INT,
    order_date DATE,
    total_price DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (tour_id) REFERENCES Tours(tour_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);
