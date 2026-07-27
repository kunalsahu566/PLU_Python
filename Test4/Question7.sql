-- Question 7
-- Consider the following table.
-- Employee
-- | EmployeeID | Name | Department | Salary |
-- | ---------- | ----- | ---------- | ------ |
-- | 1 | Rahul | IT | 65000 |
-- | 2 | Priya | HR | 45000 |
-- | 3 | Aman | IT | 70000 |
-- Create a view named HighSalaryEmployees that displays employees earning more than ₹60,000



CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100),
    Department VARCHAR(50),
    Salary INT
);



INSERT INTO Employee (EmployeeID, Name, Department, Salary) VALUES
(1, 'Rahul', 'IT', 65000),
(2, 'Priya', 'HR', 45000),
(3, 'Aman', 'IT', 70000);



CREATE VIEW HighSalaryEmployees AS
SELECT EmployeeID, Name, Department, Salary
FROM Employee
WHERE Salary > 60000;