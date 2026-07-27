-- Question 3
-- Consider the following table.
-- Product
-- | ProductID | ProductName | Category | Price |
-- | --------- | ----------- | ----------- | ----- |
-- | 1 | Mouse | Electronics | 800 |
-- | 2 | Laptop | Electronics | 65000 |
-- | 3 | Chair | Furniture | 4500 |
-- | 4 | Keyboard | Electronics | 1200 |
-- Write SQL queries to:
-- 1. Display products costing more than ₹1000.
-- 2. Display all Electronics products.
-- 3. Display the Laptop record

-- table creation
CREATE TABLE Product (
    ProductID INT,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price INT
);

-- insert data into the Product table
INSERT INTO Product (ProductID, ProductName, Category, Price) VALUES
(1, 'Mouse', 'Electronics', 800),
(2, 'Laptop', 'Electronics', 65000),
(3, 'Chair', 'Furniture', 4500),
(4, 'Keyboard', 'Electronics', 1200);


-- 1. Display products costing more than ₹1000
SELECT *
FROM Product
WHERE Price > 1000;

-- 2. Display all Electronics products
SELECT *
FROM Product
WHERE Category = 'Electronics';

-- 3. Display the Laptop record
SELECT *
FROM Product
WHERE ProductName = 'Laptop';
