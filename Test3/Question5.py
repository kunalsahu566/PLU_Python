'''
5. Insert New Book by Price
A bookstore maintains a sorted list of book prices.
A new book arrives, and its price needs to be placed at the correct
position while keeping the list sorted.
Write a program to perform this task.
'''


# Binary Search 
def binary_search(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid + 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return low

# Input
n = int(input("Enter number of book prices: "))
books = []

print("Enter sorted book prices:")
for i in range(n):
    books.append(int(input()))

new_price = int(input("Enter new book price: "))

# Find position using Binary Search
pos = binary_search(books, 0, len(books) - 1, new_price)

books.append(0) 
i = len(books) - 2

while i >= pos:
    books[i + 1] = books[i]
    i -= 1

books[pos] = new_price

print("Updated sorted book prices:")
print(books)