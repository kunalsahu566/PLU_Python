-- Question 5
-- Consider the following tables.
-- Employee
-- | EmployeeID | Name | DepartmentID |
-- | ---------- | ----- | ------------ |
-- | 1 | Rahul | 101 |
-- | 2 | Priya | 102 |
-- | 3 | Aman | 101 |
-- Department
-- | DepartmentID | DepartmentName |
-- | ------------ | -------------- |
-- | 101 | IT |
-- | 102 | HR |
-- Write an SQL query to display
-- * Employee Name
-- * Department Name
-- using an INNER JOIN

-- table creation for Employee
CREATE TABLE Employee (
    EmployeeID INT,
    Name VARCHAR(100),
    DepartmentID INT
);

-- table creation for Department
CREATE TABLE Department (
    DepartmentID INT,
    DepartmentName VARCHAR(100)
);

-- insert data into the Employee table
INSERT INTO Employee (EmployeeID, Name, DepartmentID) VALUES
(1, 'Rahul', 101),
(2, 'Priya', 102),
(3, 'Aman', 101);

-- insert data into the Department table
INSERT INTO Department (DepartmentID, DepartmentName) VALUES
(101, 'IT'),
(102, 'HR');

-- SQL query to display Employee Name and Department Name using INNER JOIN
SELECT Employee.Name AS EmployeeName, Department.DepartmentName
FROM Employee
INNER JOIN Department ON Employee.DepartmentID = Department.DepartmentID;



