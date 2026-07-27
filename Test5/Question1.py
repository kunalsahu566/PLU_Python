import sqlite3


class Product:
    def __init__(self, product_id, product_name, category, quantity, price):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.quantity = quantity
        self.price = price


def create_database():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        category TEXT,
        quantity INTEGER,
        price REAL
    )
    """)

    cursor.execute("DELETE FROM products")

    products = [
        (1, "Laptop", "Electronics", 12, 55000),
        (2, "Mouse", "Electronics", 8, 1200),
        (3, "Keyboard", "Electronics", 15, 2500),
        (4, "Chair", "Furniture", 5, 4500),
        (5, "Desk", "Furniture", 20, 8000),
        (6, "Notebook", "Stationery", 30, 150),
        (7, "Pen", "Stationery", 7, 25),
        (8, "Monitor", "Electronics", 9, 12000)
    ]

    cursor.executemany("INSERT INTO products VALUES(?,?,?,?,?)", products)

    conn.commit()
    conn.close()


def fetch_products():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    product_list = []

    for row in rows:
        product = Product(row[0], row[1], row[2], row[3], row[4])
        product_list.append(product)

    conn.close()

    return product_list


def merge(left, right, key):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if getattr(left[i], key) <= getattr(right[j], key):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(products, key):

    if len(products) <= 1:
        return products

    mid = len(products) // 2

    left = merge_sort(products[:mid], key)
    right = merge_sort(products[mid:], key)

    return merge(left, right, key)


def binary_search(products, target):

    low = 0
    high = len(products) - 1

    while low <= high:

        mid = (low + high) // 2

        if products[mid].product_id == target:
            return products[mid]

        elif products[mid].product_id < target:
            low = mid + 1

        else:
            high = mid - 1

    return None


def display_product(product):
    print("-------------------------------")
    print("Product ID :", product.product_id)
    print("Name       :", product.product_name)
    print("Category   :", product.category)
    print("Quantity   :", product.quantity)
    print("Price      :", product.price)


def display_all(products):

    for product in products:
        display_product(product)


def low_stock(products):

    print("\nProducts having stock below 10\n")

    found = False

    for product in products:

        if product.quantity < 10:
            display_product(product)
            found = True

    if not found:
        print("No low stock products.")


def main():

    create_database()

    products = fetch_products()

    while True:

        print("\n====== SMART INVENTORY MANAGEMENT ======")
        print("1. Display All Products")
        print("2. Sort by Quantity")
        print("3. Search Product ID")
        print("4. Low Stock Products")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_all(products)
        elif choice == "2":
            sorted_products = merge_sort(products, "quantity")
            print("\nProducts Sorted by Quantity\n")
            display_all(sorted_products)

        elif choice == "3":
            sorted_products = merge_sort(products, "product_id")
            pid = int(input("Enter Product ID: "))
            result = binary_search(sorted_products, pid)

            if result is None:
                print("Product Not Found")
            else:
                print("\nProduct Found\n")
                display_product(result)
        elif choice == "4":
            low_stock(products)
        elif choice == "5":
            print("Thank You")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()