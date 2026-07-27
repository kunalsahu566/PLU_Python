-- Question 6
-- Consider the following tables.
-- Student
-- | StudentID | Name | CourseID |
-- | --------- | ----- | -------- |
-- | 1 | Rahul | 201 |
-- | 2 | Neha | 202 |
-- | 3 | Aman | NULL |
-- Course
-- | CourseID | CourseName |
-- | -------- | ---------- |
-- | 201 | Python |
-- | 202 | SQL |
-- Write an SQL query to display all students along with their course names
-- using a LEFT JOIN.



-- Create table
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

-- Insert Data into table

INSERT INTO Course (CourseID, CourseName) VALUES
(201, 'Python'),
(202, 'SQL');

INSERT INTO Student (StudentID, Name, CourseID) VALUES
(1, 'Rahul', 201),
(2, 'Neha', 202),
(3, 'Aman', NULL);


-- Left join


SELECT s.StudentID, s.Name, c.CourseName
FROM Student s
LEFT JOIN Course c ON s.CourseID = c.CourseID;
