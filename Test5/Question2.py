# # 2. Hospital Patient Queue Management
# ### Problem Statement
# A hospital stores patient details in SQLite.
# Each patient has:
# * Patient ID
# * Name
# * Age
# * Priority Level
# ### Requirements
# 1. Fetch all patients.
# 2. Create a **Priority Queue** based on Priority Level.
# 3. Attend patients in order of priority.
# 4. After attending a patient, update the database.
# 5. Display the remaining patients.
# ### Concepts
# * SQLite
# * Priority Queue
# * UPDATE Query
# * Heap/Priority Queue
# ---




import sqlite3
import heapq


class Patient:

    def __init__(self, patient_id, name, age, priority_level):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.priority_level = priority_level


class PatientQueue:

    def __init__(self):
        self.queue = []

    def add_patient(self, patient):
        heapq.heappush(self.queue, (patient.priority_level, patient.patient_id, patient))

    def get_next_patient(self):

        if len(self.queue) == 0:
            return None

        return heapq.heappop(self.queue)[2]

    def is_empty(self):
        return len(self.queue) == 0


def create_database():

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients(
            patient_id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            priority_level INTEGER,
            attended INTEGER DEFAULT 0
        )
    """)

    cursor.execute("DELETE FROM patients")

    patients = [
        (1, "Aman", 32, 3, 0),
        (2, "Riya", 28, 1, 0),
        (3, "Karan", 45, 2, 0),
        (4, "Meera", 39, 4, 0),
        (5, "Sohan", 55, 2, 0)
    ]

    cursor.executemany(
        "INSERT INTO patients VALUES (?,?,?,?,?)",
        patients
    )

    conn.commit()
    conn.close()


def fetch_patients():

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT patient_id,name,age,priority_level
        FROM patients
        WHERE attended = 0
    """)

    rows = cursor.fetchall()

    patient_list = []

    for row in rows:
        patient = Patient(row[0], row[1], row[2], row[3])
        patient_list.append(patient)

    conn.close()

    return patient_list


def update_status(patient_id):

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE patients SET attended = 1 WHERE patient_id=?",
        (patient_id,)
    )

    conn.commit()
    conn.close()


def display_patient(patient):

    print("---------------------------")
    print("Patient ID :", patient.patient_id)
    print("Name       :", patient.name)
    print("Age        :", patient.age)
    print("Priority   :", patient.priority_level)


def main():

    create_database()

    queue = PatientQueue()

    patients = fetch_patients()

    for patient in patients:
        queue.add_patient(patient)

    print("\nPatients Attended According to Priority\n")

    while not queue.is_empty():

        patient = queue.get_next_patient()

        display_patient(patient)

        update_status(patient.patient_id)

    print("\nRemaining Patients\n")

    remaining = fetch_patients()

    if len(remaining) == 0:
        print("No patients left.")
    else:
        for patient in remaining:
            display_patient(patient)


if __name__ == "__main__":
    main()
