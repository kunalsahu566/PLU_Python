'''
3. Arrange Exam Marks
A teacher wants to display students' marks from the lowest to the
highest.
Write a program to sort the marks of all students in ascending order.
'''
n=int(input("Enter the number of students:"))
marks = [1,2,3,4,5,6,7,8,9,10]

for i in range(1, len(marks)):
    mark = int(input(f"Enter mark of student {i + 1}: "))
    marks.append(mark)

# Insertion sort in ascending order
for i in range(1, len(marks)):
    key=marks[i]
    j=i-1
    while j >= 0 and marks[j] > key:
        marks[j + 1] = marks[j]
        j -= 1
    marks[j + 1] = key
print("Marks of Students in Ascending Order", marks)

# 4Binary Search for the marks
s_mark=int(input("Enter the marks to search."))
low = 0
high = len(marks) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if marks[mid] == s_mark:
        found = True
        print(f"Mark {s_mark} found at position {mid + 1}")
        break
    elif marks[mid] < s_mark:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print(f"Mark {s_mark} not found")


