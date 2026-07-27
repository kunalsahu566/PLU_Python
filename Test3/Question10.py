'''10. School Annual Report
A school has recorded the marks of 50 students.
Write a program that:
Sorts the marks in ascending order.
Accepts a mark from the user.
Checks whether that mark exists in the sorted list.
Displays the position if found; otherwise, prints "Mark Not Found.
'''


# Bubble Sort Function
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Binary Search Function
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# Input marks of 50 students
marks = []

print("Enter marks of 50 students:")
for i in range(50):
    mark = int(input(f"Student {i + 1}: "))
    marks.append(mark)

# Sort the marks
bubble_sort(marks)

print("\nMarks in Ascending Order:")
print(marks)

# Search for a mark
target = int(input("\nEnter the mark to search: "))

position = binary_search(marks, target)

if position != -1:
    print(f"Mark found at position {position + 1}.")
else:
    print("Mark Not Found.")