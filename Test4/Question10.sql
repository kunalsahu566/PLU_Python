-- Question 10
-- Consider the following tables.
-- Student
-- | StudentID | Name | CourseID |
-- | --------- | ----- | -------- |
-- | 1 | Rahul | 101 |
-- | 2 | Neha | 102 |
-- | 3 | Aman | 101 |
-- Course
-- | CourseID | CourseName |
-- | -------- | ---------- |
-- | 101 | Python |
-- | 102 | Java |
-- Write SQL queries to:
-- 1. Display Student Name and Course Name using an INNER JOIN.
-- 2. Display only students enrolled in the Python course using the WHERE
-- clause.
-- 3. Create a view named 'PythonStudents' for students enrolled in the Python
-- course

CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50)
);

CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    CourseID INT,
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

INSERT INTO Course (CourseID, CourseName) VALUES
(101, 'Python'),
(102, 'Java');

INSERT INTO Student (StudentID, Name, CourseID) VALUES
(1, 'Rahul', 101),
(2, 'Neha', 102),
(3, 'Aman', 101);

-- 1. Display Student Name and Course Name using an INNER JOIN
SELECT s.Name AS StudentName, c.CourseName
FROM Student s
INNER JOIN Course c ON s.CourseID = c.CourseID;

-- 2. Display only students enrolled in the Python course using the WHERE clause
SELECT s.StudentID, s.Name, s.CourseID
FROM Student s
WHERE s.CourseID = 101;

-- 3. Create a view named PythonStudents for students enrolled in the Python course
CREATE VIEW PythonStudents AS
SELECT s.StudentID, s.Name, s.CourseID
FROM Student s
WHERE s.CourseID = 101;