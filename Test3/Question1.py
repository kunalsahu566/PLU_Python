'''
1. Student Roll Number Search
A teacher has stored the roll numbers of students in a list in the order
they registered. The list is not sorted.
Write a program to check whether a given roll number exists in the list.
If found, display its position; otherwise, print "Student Not Found."
'''

roll_no = [123, 222, 345, 443, 555, 678, 319]

search_roll_no = int(input("Enter Roll Number Of the required Student: "))

if search_roll_no in roll_no:
    pi = roll_no.index(search_roll_no) +1
    print(f"Roll Number {search_roll_no} Found at Position {pi}.")
else:
    print("Student Not Found in the System.")