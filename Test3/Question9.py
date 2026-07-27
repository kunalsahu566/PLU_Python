'''9. Library Book Search
A library has 10,000 books, and the Book IDs are already arranged in
ascending order.
Write a program to find a given Book ID efficiently.
Also mention which searching algorithm you used and why it is suitable.
'''

# Create a sorted list of book IDs
book_ids = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]

# Binary search algorithm

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


search_id = int(input("Enter the Book ID to search: "))
result = binary_search(book_ids, search_id)

if result != -1:
    print(f"Book ID {search_id} found at position {result + 1}")
else:
    print(f"Book ID {search_id} not found")

print("\nSearching algorithm used: Binary Search")
print("Why suitable? Because the Book IDs are already sorted, and binary search")
print("reduces the search space by half each time, making it much faster than")
print("linear search for large lists like 10,000 books.")


