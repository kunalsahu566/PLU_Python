# # 3. Online Banking Transaction Analyzer
# ### Problem Statement
# A bank stores transactions in SQLite.
# Each transaction contains:
# * Transaction ID
# * Account Number
# * Amount
# * Date
# * Type (Credit/Debit)
#  Requirements
# 1. Retrieve all transactions.
# 2. Sort them by amount using **Quick Sort**.
# 3. Search transactions using Transaction ID.
# 4. Calculate total credits and debits.
# 5. Display the top 5 highest-value transactions.
#  Concepts
# * SQL
# * Quick Sort
# * Binary Search
# * Aggregation



import sqlite3


class Transaction:

    def __init__(self, transaction_id, account_number, amount, date, transaction_type):
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.amount = amount
        self.date = date
        self.transaction_type = transaction_type


def create_database():

    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            transaction_id INTEGER PRIMARY KEY,
            account_number TEXT,
            amount REAL,
            date TEXT,
            transaction_type TEXT
        )
    """)

    cursor.execute("DELETE FROM transactions")

    transactions = [
        (1, "AC1001", 5000, "2026-07-01", "Credit"),
        (2, "AC1002", 1200, "2026-07-02", "Debit"),
        (3, "AC1001", 3500, "2026-07-03", "Credit"),
        (4, "AC1003", 800, "2026-07-04", "Debit"),
        (5, "AC1002", 2200, "2026-07-05", "Credit"),
        (6, "AC1004", 1500, "2026-07-06", "Debit"),
        (7, "AC1001", 9000, "2026-07-07", "Credit"),
        (8, "AC1005", 300, "2026-07-08", "Debit")
    ]

    cursor.executemany(
        "INSERT INTO transactions VALUES (?,?,?,?,?)",
        transactions
    )

    conn.commit()
    conn.close()


def fetch_transactions():

    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")

    rows = cursor.fetchall()

    transaction_list = []

    for row in rows:
        transaction = Transaction(row[0], row[1], row[2], row[3], row[4])
        transaction_list.append(transaction)

    conn.close()

    return transaction_list


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    smaller = []
    greater = []

    for i in range(1, len(arr)):

        if arr[i].amount <= pivot.amount:
            smaller.append(arr[i])
        else:
            greater.append(arr[i])

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid].transaction_id == target:
            return arr[mid]

        elif arr[mid].transaction_id < target:
            low = mid + 1

        else:
            high = mid - 1

    return None


def calculate_totals(transactions):

    credit = 0
    debit = 0

    for transaction in transactions:

        if transaction.transaction_type == "Credit":
            credit += transaction.amount
        else:
            debit += transaction.amount

    return credit, debit


def display_transaction(transaction):

    print("-----------------------------")
    print("Transaction ID :", transaction.transaction_id)
    print("Account Number :", transaction.account_number)
    print("Amount         :", transaction.amount)
    print("Date           :", transaction.date)
    print("Type           :", transaction.transaction_type)


def display_all(transactions):

    for transaction in transactions:
        display_transaction(transaction)


def main():

    create_database()

    transactions = fetch_transactions()

    print("\nAll Transactions\n")
    display_all(transactions)

    sorted_amount = quick_sort(transactions)

    print("\nTransactions Sorted by Amount\n")
    display_all(sorted_amount)

    sorted_id = sorted(transactions, key=lambda x: x.transaction_id)

    tid = int(input("\nEnter Transaction ID to Search: "))

    result = binary_search(sorted_id, tid)

    if result:
        print("\nTransaction Found\n")
        display_transaction(result)
    else:
        print("Transaction Not Found")

    credit, debit = calculate_totals(transactions)

    print("\nTotal Credit :", credit)
    print("Total Debit  :", debit)

    print("\nTop 5 Highest Transactions\n")

    top = sorted_amount[-5:]

    for transaction in top:
        display_transaction(transaction)


if __name__ == "__main__":
    main()