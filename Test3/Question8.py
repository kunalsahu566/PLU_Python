'''
8. Hospital Emergency Queue
A hospital has a list of patients with different priority levels.
Write a program to arrange the patients so that the patient with the
highest priority is treated first.
'''

n = int(input("Enter the number of patients: "))
patients = []

for i in range(n):
    patient = {
        "name": input(f"Enter name of patient {i + 1}: "),
        "id": int(input(f"Enter ID of patient {i + 1}: ")),
        "priority": int(input(f"Enter priority level of patient {i + 1}: "))
    }
    patients.append(patient)

# Insertion sort by priority level (highest first)
for i in range(1, len(patients)):
    key = patients[i]
    j = i - 1
    while j >= 0 and patients[j]["priority"] < key["priority"]:
        patients[j + 1] = patients[j]
        j -= 1
    patients[j + 1] = key

print("Patients arranged by priority:")
for patient in patients:
    print(patient)

# Binary search by patient ID
search_id = int(input("Enter patient ID to search: "))
low = 0
high = len(patients) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if patients[mid]["id"] == search_id:
        found = True
        print(f"Patient found: {patients[mid]}")
        break
    elif patients[mid]["id"] < search_id:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Patient not found")
