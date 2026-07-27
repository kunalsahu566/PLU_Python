# # 7. Employee Attendance Analytics
# ### Problem Statement
# A company records employee attendance.
# Each record contains:
# * Employee ID
# * Name
# * Check-in Time
# * Check-out Time
# ### Requirements
# 1. Retrieve attendance records.
# 2. Calculate total working hours.
# 3. Sort employees by total hours worked.
# 4. Search employees using Employee ID.
# 5. Display employees who worked more than 45 hours this week.
# ### Concepts
# * SQL
# * Sorting
# * Binary Search
# * DateTime
# ---




import sqlite3
from datetime import datetime


class Attendance:

    def __init__(self, employee_id, name, check_in, check_out):
        self.employee_id = employee_id
        self.name = name
        self.check_in = check_in
        self.check_out = check_out
        in_time = datetime.strptime(check_in, "%Y-%m-%d %H:%M")
        out_time = datetime.strptime(check_out, "%Y-%m-%d %H:%M")

        self.total_hours = round((out_time - in_time).total_seconds() / 3600, 2)


def create_database():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance(
            employee_id INTEGER PRIMARY KEY,
            name TEXT,
            check_in TEXT,
            check_out TEXT
        )
    """)

    cursor.execute("DELETE FROM attendance")

    records = [
        (101, "Asha", "2026-07-20 09:00", "2026-07-20 17:00"),
        (102, "Ravi", "2026-07-20 09:30", "2026-07-20 18:00"),
        (103, "Mina", "2026-07-20 08:30", "2026-07-20 20:00"),
        (104, "John", "2026-07-20 10:00", "2026-07-20 16:30"),
        (105, "Sara", "2026-07-20 08:00", "2026-07-20 19:00")
    ]

    cursor.executemany(
        "INSERT INTO attendance VALUES (?,?,?,?)",
        records
    )

    conn.commit()
    conn.close()


def fetch_records():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance")
    rows = cursor.fetchall()
    employee_list = []

    for row in rows:
        employee = Attendance(row[0], row[1], row[2], row[3])
        employee_list.append(employee)
    conn.close()
    return employee_list
def bubble_sort(records):
    n = len(records)
    for i in range(n):
        for j in range(n - i - 1):
            if records[j].total_hours < records[j + 1].total_hours:
                records[j], records[j + 1] = records[j + 1], records[j]
    return records


def binary_search(records, emp_id):
    low = 0
    high = len(records) - 1

    while low <= high:
        mid = (low + high) // 2
        if records[mid].employee_id == emp_id:
            return records[mid]
        elif records[mid].employee_id < emp_id:
            low = mid + 1
        else:
            high = mid - 1
    return None


def display_record(record):

    print("------------------------------")
    print("Employee ID :", record.employee_id)
    print("Name        :", record.name)
    print("Check In    :", record.check_in)
    print("Check Out   :", record.check_out)
    print("Total Hours :", record.total_hours)


def display_all(records):
    for record in records:
        display_record(record)


def overtime(records):
    print("\nEmployees Worked More Than 45 Hours\n")
    found = False
    for record in records:
        if record.total_hours > 45:
            display_record(record)
            found = True
    if not found:
        print("No employee worked more than 45 hours.")

def main():
    create_database()
    records = fetch_records()
    print("\nAttendance Records\n")
    display_all(records)
    sorted_records = bubble_sort(records.copy())
    print("\nEmployees Sorted by Working Hours\n")
    display_all(sorted_records)
    records_by_id = sorted(records, key=lambda x: x.employee_id)
    emp_id = int(input("\nEnter Employee ID to Search: "))
    result = binary_search(records_by_id, emp_id)
    if result:
        print("\nEmployee Found\n")
        display_record(result)
    else:
        print("Employee Not Found")
    overtime(records)


if __name__ == "__main__":
    main()