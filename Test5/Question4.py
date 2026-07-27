# 4. College Placement Portal
# ### Problem Statement
# A college stores student records in SQLite.
# Each student contains:
# * Roll Number
# * Name
# * CGPA
# * Skills
# * Placement Status
# ### Requirements
# 1. Retrieve all students.
# 2. Sort students by CGPA using **Heap Sort**.
# 3. Search students by Roll Number.
# 4. Display students eligible for placements (CGPA > 7.5).
# 5. Update placement status after selection.
# ### Concepts
# * Heap
# * Heap Sort
# * Binary Search
# * SQL UPDATE
# ---



import sqlite3


class Student:

    def __init__(self, roll_number, name, cgpa, skills, placement_status):
        self.roll_number = roll_number
        self.name = name
        self.cgpa = cgpa
        self.skills = skills
        self.placement_status = placement_status


def create_database():

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            roll_number INTEGER PRIMARY KEY,
            name TEXT,
            cgpa REAL,
            skills TEXT,
            placement_status TEXT
        )
    """)

    cursor.execute("DELETE FROM students")

    students = [
        (101, "Aarav", 8.9, "Python, SQL", "Not Placed"),
        (102, "Meera", 7.2, "Java, DBMS", "Not Placed"),
        (103, "Rohan", 9.1, "C++, AI", "Not Placed"),
        (104, "Nisha", 7.8, "Data Science, SQL", "Not Placed"),
        (105, "Kunal", 8.4, "Python, Django", "Not Placed")
    ]

    cursor.executemany(
        "INSERT INTO students VALUES (?,?,?,?,?)",
        students
    )

    conn.commit()
    conn.close()


def fetch_students():

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    student_list = []

    for row in rows:
        student = Student(row[0], row[1], row[2], row[3], row[4])
        student_list.append(student)

    conn.close()

    return student_list


def heap_sort(students):

    heap = []

    for student in students:

        heap.append(student)

        index = len(heap) - 1

        while index > 0:

            parent = (index - 1) // 2

            if heap[parent].cgpa <= heap[index].cgpa:
                break

            heap[parent], heap[index] = heap[index], heap[parent]

            index = parent

    sorted_students = []

    while len(heap) > 0:

        sorted_students.append(heap[0])

        last = heap.pop()

        if len(heap) == 0:
            break

        heap[0] = last

        index = 0

        while True:

            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < len(heap) and heap[left].cgpa < heap[smallest].cgpa:
                smallest = left

            if right < len(heap) and heap[right].cgpa < heap[smallest].cgpa:
                smallest = right

            if smallest == index:
                break

            heap[index], heap[smallest] = heap[smallest], heap[index]

            index = smallest

    sorted_students.reverse()

    return sorted_students


def binary_search(students, roll):

    low = 0
    high = len(students) - 1

    while low <= high:

        mid = (low + high) // 2

        if students[mid].roll_number == roll:
            return students[mid]

        elif students[mid].roll_number < roll:
            low = mid + 1

        else:
            high = mid - 1

    return None


def update_status(roll):

    conn = sqlite3.connect("placement.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET placement_status='Placed' WHERE roll_number=?",
        (roll,)
    )

    conn.commit()
    conn.close()


def display_student(student):

    print("----------------------------")
    print("Roll Number :", student.roll_number)
    print("Name        :", student.name)
    print("CGPA        :", student.cgpa)
    print("Skills      :", student.skills)
    print("Status      :", student.placement_status)


def display_all(students):

    for student in students:
        display_student(student)


def eligible_students(students):

    print("\nEligible Students (CGPA > 7.5)\n")

    found = False

    for student in students:

        if student.cgpa > 7.5:
            display_student(student)
            found = True

    if not found:
        print("No eligible students.")


def main():

    create_database()
    students = fetch_students()
    print("\nAll Students\n")

    display_all(students)
    sorted_students = heap_sort(students)
    print("\nStudents Sorted by CGPA\n")
    
    display_all(sorted_students)
    students_by_roll = sorted(students, key=lambda x: x.roll_number)
    roll = int(input("\nEnter Roll Number to Search: "))
    result = binary_search(students_by_roll, roll)

    if result:
        print("\nStudent Found\n")
        display_student(result)
    else:
        print("Student Not Found")

    eligible_students(students)
    roll = int(input("\nEnter Roll Number to Update Placement Status: "))
    update_status(roll)
    print("\nPlacement Status Updated Successfully")


if __name__ == "__main__":
    main()