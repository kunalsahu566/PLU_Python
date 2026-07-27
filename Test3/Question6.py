'''
6. Employee Salary Report
An HR department has employee salary records collected from two different
branches.
Write a program to combine both lists and display all salaries in
ascending order.
'''

# Input salaries for branch 1
n1 = int(input("Enter the number of employees in Branch 1: "))
branch1 = []
for i in range(n1):
    salary = float(input(f"Enter salary of employee {i + 1} in Branch 1: "))
    branch1.append(salary)

# Input salaries for branch 2
n2 = int(input("Enter the number of employees in Branch 2: "))
branch2 = []
for i in range(n2):
    salary = float(input(f"Enter salary of employee {i + 1} in Branch 2: "))
    branch2.append(salary)

print("Salaries of Branch 1:", branch1)
print("Salaries of Branch 2:", branch2)

# Combine both lists
combined = branch1 + branch2

# Sort using insertion sort
for i in range(1, len(combined)):
    key = combined[i]
    j = i - 1
    while j >= 0 and combined[j] > key:
        combined[j + 1] = combined[j]
        j -= 1
    combined[j + 1] = key

print("Combined salaries in ascending order:", combined)

