-- Question 8
-- Consider the following table.
-- Orders
-- | OrderID | CustomerName | OrderDate | Amount |
-- | ------- | ------------ | --------- | ------ |
-- Tasks
-- 1. Create an index on OrderID.
-- 2. Explain one benefit of creating an index.

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    OrderDate DATE,
    Amount INT
);

INSERT INTO Orders (OrderID, CustomerName, OrderDate, Amount) VALUES
(101, 'Rahul', '2026-01-10', 500),
(102, 'Priya', '2026-01-11', 700);

CREATE INDEX idx_orders_orderid ON Orders(OrderID);

-- Benefit: An index speeds up data retrieval for queries that search or filter by OrderID.

