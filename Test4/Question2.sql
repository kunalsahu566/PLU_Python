-- Question 2
-- Consider the following table.
-- Student
-- | StudentID | Name | Course | Marks |
-- | --------- | ----- | ------ | ----- |
-- | 101 | Rahul | Python | 80 |
-- | 102 | Priya | Java | 75 |
-- | 103 | Aman | Python | 90 |
-- | 104 | Neha | SQL | 70 |
-- Write SQL queries to:
-- 1. Display all student records.
-- 2. Display only Name and Marks.
-- 3. Display only the Course column.

-- table creation
CREATE TABLE Student (
    StudentID INT,
    Name VARCHAR(100),
    Course VARCHAR(50),
    Marks INT
);

-- insert data into the Student table
INSERT INTO Student (StudentID, Name, Course, Marks) VALUES
(101, 'Rahul', 'Python', 80),
(102, 'Priya', 'Java', 75),
(103, 'Aman', 'Python', 90),
(104, 'Neha', 'SQL', 70);

-- 1. Display all student records
SELECT *
FROM Student;

-- 2. Display only Name and Marks
SELECT Name, Marks
FROM Student;

-- 3. Display only the Course column
SELECT Course
FROM Student;
