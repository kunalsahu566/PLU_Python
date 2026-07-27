-- Create the following table.
-- Customer
-- | Column | Data Type |
-- | ------------ | ------------ |
-- | CustomerID | INT |
-- | CustomerName | VARCHAR(100) |
-- | City | VARCHAR(50) |
-- | Mobile | VARCHAR(15) |
-- Tasks
-- 1. Create the table.
-- 2. Make CustomerID the Primary Key.
-- 3. Explain why Primary Keys are important.

-- 1. Create the table.

CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(50),
    Mobile VARCHAR(15)
)

-- 3. Explain why Primary Keys are important.
-- Primary Keys are important because they uniquely identify each record in a table,
-- ensuring that there are no duplicate entries.
--They also help establish relationships between tables in a database, allowing for efficient data retrieval


