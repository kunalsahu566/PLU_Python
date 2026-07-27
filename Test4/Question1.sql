-- A company wants to store employee information.
-- Create the following table.
-- Employee
-- | Column Name | Data Type |
-- | ------------ | ------------ |
-- | EmployeeID | INT |
-- | EmployeeName | VARCHAR(100) |
-- | Department | VARCHAR(50) |
-- | Salary | INT |
-- | JoiningDate | DATE |
-- Tasks
-- 1. Create the table.
-- 2. Make 'EmployeeID' the Primary Key.

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(100),
    Department VARCHAR(50),
    Salary INT,
    JoiningDate DATE
);


