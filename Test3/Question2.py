'''
2. Product ID Search
An e-commerce website stores product IDs in ascending order.
Write a program to find whether a customer-entered product ID exists in
the inventory. If it exists, display its index; otherwise, display "Product
Not Available in the Inventory."
'''


products=[
    {"id":101, "Name":"Laptop"},
    {"id":102, "Name":"Mouse"},
    {"id":103, "Name":"Keyboard"},
    {"id":104, "Name":"Monitor"},
    {"id":105, "Name":"Printer"},
    {"id":106, "Name":"Speaker"},
    {"id":107, "Name":"Webcam"},
    {"id":108, "Name":"Headphones"},
    {"id":109, "Name":"RAM"},
    {"id":110, "Name":"Hard Disk"}
]

search_id = int(input("Enter Product ID:"))

low = 0
high = len(products) - 1

while low <= high:
    mid = (low + high) // 2

    if products[mid]["id"] == search_id:
        print("\n===== Product Found =====")
        print("Index       :", mid)
        print("Product ID  :", products[mid]["id"])
        print("Product Name:", products[mid]["Name"])
        break

    elif products[mid]["id"] < search_id:
        low = mid + 1

    else:
        high = mid - 1
else:
    print("Product Not Available in the Inventory.")