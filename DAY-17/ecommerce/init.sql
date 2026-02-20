DROP DATABASE IF EXISTS ecommerce_db;
CREATE DATABASE ecommerce_db;
USE ecommerce_db;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT
);
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(150) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL,
    category_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    order_status VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50),
    amount DECIMAL(10,2),
    payment_status VARCHAR(50),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
INSERT INTO categories (category_name, description) VALUES
('Electronics', 'Electronic items'),
('Clothing', 'Apparel and garments'),
('Books', 'Educational and novels'),
('Home Appliances', 'Home products'),
('Sports', 'Sports equipment');
INSERT INTO users (name, email, password, phone, address) VALUES
('Ravi Kumar','ravi@gmail.com','pass123','9000000001','Hyderabad'),
('Anita Sharma','anita@gmail.com','pass123','9000000002','Delhi'),
('Rahul Verma','rahul@gmail.com','pass123','9000000003','Mumbai'),
('Sneha Reddy','sneha@gmail.com','pass123','9000000004','Chennai'),
('Arjun Rao','arjun@gmail.com','pass123','9000000005','Bangalore'),
('Pooja Singh','pooja@gmail.com','pass123','9000000006','Pune'),
('Kiran Das','kiran@gmail.com','pass123','9000000007','Kolkata'),
('Meena Iyer','meena@gmail.com','pass123','9000000008','Kerala'),
('Vikas Yadav','vikas@gmail.com','pass123','9000000009','Lucknow'),
('Divya Patel','divya@gmail.com','pass123','9000000010','Ahmedabad');
INSERT INTO products (product_name, description, price, stock_quantity, category_id) VALUES
('Laptop','Dell Laptop',60000,20,1),
('Mobile','Samsung Phone',20000,50,1),
('Headphones','Sony Headphones',3000,30,1),
('T-Shirt','Cotton T-shirt',800,100,2),
('Jeans','Blue Jeans',1500,60,2),
('Novel','Fiction Book',500,40,3),
('Textbook','Math Book',700,35,3),
('Microwave','LG Microwave',10000,15,4),
('Refrigerator','Whirlpool Fridge',25000,10,4),
('Washing Machine','IFB Washer',18000,12,4),
('Cricket Bat','SS Bat',2500,25,5),
('Football','Adidas Ball',1500,40,5),
('Tablet','Lenovo Tab',15000,18,1),
('Smart Watch','Apple Watch',30000,22,1),
('Jacket','Winter Jacket',2500,45,2),
('Shoes','Running Shoes',3000,50,2),
('Cooker','Pressure Cooker',2000,30,4),
('Yoga Mat','Fitness Mat',1200,55,5),
('Keyboard','Mechanical Keyboard',4000,28,1),
('Mouse','Wireless Mouse',1500,35,1);
INSERT INTO orders (user_id, total_amount, order_status) VALUES
(1,60000,'Completed'),
(2,20000,'Pending'),
(3,3000,'Completed'),
(4,1500,'Shipped'),
(5,25000,'Completed'),
(6,800,'Pending'),
(7,700,'Completed'),
(8,10000,'Shipped'),
(9,2500,'Completed'),
(10,1500,'Completed'),
(1,3000,'Completed'),
(2,15000,'Shipped'),
(3,1200,'Completed'),
(4,4000,'Pending'),
(5,2500,'Completed');
INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1,1,1,60000),(2,2,1,20000),(3,3,1,3000),(4,12,1,1500),
(5,9,1,25000),(6,4,1,800),(7,7,1,700),(8,8,1,10000),
(9,11,1,2500),(10,12,1,1500),
(11,16,1,3000),(12,13,1,15000),(13,18,1,1200),
(14,19,1,4000),(15,15,1,2500),
(1,20,1,1500),(2,14,1,30000),(3,5,1,1500),(4,6,1,500),
(5,10,1,18000),(6,17,1,2000),(7,18,1,1200),(8,19,1,4000),
(9,2,1,20000),(10,3,1,3000),
(11,4,1,800),(12,5,1,1500),(13,6,1,500),
(14,7,1,700),(15,8,1,10000);
INSERT INTO payments (order_id, payment_method, amount, payment_status) VALUES
(1,'Card',60000,'Paid'),
(2,'UPI',20000,'Pending'),
(3,'Card',3000,'Paid'),
(4,'Cash',1500,'Paid'),
(5,'Card',25000,'Paid'),
(6,'UPI',800,'Pending'),
(7,'Card',700,'Paid'),
(8,'Card',10000,'Paid'),
(9,'Cash',2500,'Paid'),
(10,'UPI',1500,'Paid'),
(11,'Card',3000,'Paid'),
(12,'UPI',15000,'Paid'),
(13,'Cash',1200,'Paid'),
(14,'Card',4000,'Pending'),
(15,'UPI',2500,'Paid');
SELECT * FROM users;
SELECT * FROM products
WHERE price > 1000;
SELECT * FROM products
WHERE stock_quantity < 10;
SELECT * FROM orders
WHERE user_id = 1;
UPDATE products
SET price = 65000
WHERE product_id = 1;
UPDATE products
SET stock_quantity = stock_quantity - 2
WHERE product_id = 1;
select * from products