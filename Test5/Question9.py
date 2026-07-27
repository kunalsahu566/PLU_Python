# # 9. Library Book Borrowing System
# ### Problem Statement
# A library stores books and borrowing history.
# Tables:
# Books
# Members
# Borrowed Books
# ### Requirements
# 1. Display all available books.
# 2. Sort books alphabetically using **Merge Sort**.
# 3. Search books by Book ID.
# 4. Borrow a book.
# 5. Update book availability.
# 6. Display overdue books.
# ### Concepts
# * Merge Sort
# * Binary Search
# * SQLite
# * SQL UPDATE


import sqlite3
from datetime import datetime, timedelta


class Book:

    def __init__(self, book_id, title, author, available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available


def create_database():

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        book_id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        available INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS members(
        member_id INTEGER PRIMARY KEY,
        name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS borrowed_books(
        borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER,
        book_id INTEGER,
        borrow_date TEXT,
        return_date TEXT,
        status TEXT
    )
    """)

    cursor.execute("DELETE FROM books")
    cursor.execute("DELETE FROM members")
    cursor.execute("DELETE FROM borrowed_books")

    books = [
        (1, "Python Basics", "John Smith", 1),
        (2, "Data Structures", "Ada Lovelace", 1),
        (3, "Machine Learning", "Alan Turing", 0),
        (4, "Algorithms", "Kurtis Lee", 1)
    ]

    members = [
        (1, "Kunal"),
        (2, "Riya")
    ]

    borrowed = [
        (1, 3, "2026-07-01", "2026-07-15", "Borrowed")
    ]

    cursor.executemany(
        "INSERT INTO books VALUES (?,?,?,?)",
        books
    )
    cursor.executemany(
        "INSERT INTO members VALUES (?,?)",
        members
    )
    cursor.executemany(
        """INSERT INTO borrowed_books
        (member_id,book_id,borrow_date,return_date,status)
        VALUES (?,?,?,?,?)""",
        borrowed
    )

    conn.commit()
    conn.close()


def fetch_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM books WHERE available=1"
    )
    rows = cursor.fetchall()
    books = []
    for row in rows:
        books.append(Book(row[0], row[1], row[2], row[3]))
    conn.close()
    return books


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i].title.lower() < right[j].title.lower():
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


def merge_sort(books):
    if len(books) <= 1:
        return books
    mid = len(books) // 2
    left = merge_sort(books[:mid])
    right = merge_sort(books[mid:])
    return merge(left, right)


def binary_search(books, book_id):
    low = 0
    high = len(books) - 1

    while low <= high:
        mid = (low + high) // 2
        if books[mid].book_id == book_id:
            return books[mid]
        elif books[mid].book_id < book_id:
            low = mid + 1
        else:
            high = mid - 1
    return None


def borrow_book(member_id, book_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT available FROM books WHERE book_id=?",
        (book_id,)
    )
    result = cursor.fetchone()
    if result == None or result[0] == 0:
        conn.close()
        return False
    borrow_date = datetime.now().strftime("%Y-%m-%d")
    return_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
    cursor.execute(
        """INSERT INTO borrowed_books
        (member_id,book_id,borrow_date,return_date,status)
        VALUES (?,?,?,?,?)""",
        (member_id, book_id, borrow_date, return_date, "Borrowed")
    )
    cursor.execute(
        "UPDATE books SET available=0 WHERE book_id=?",
        (book_id,)
    )
    conn.commit()
    conn.close()
    return True


def overdue_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT book_id,member_id,return_date
    FROM borrowed_books
    WHERE status='Borrowed'
    """)
    rows = cursor.fetchall()
    conn.close()
    today = datetime.now().date()
    found = False
    print("\nOverdue Books\n")
    for row in rows:
        return_date = datetime.strptime(row[2], "%Y-%m-%d").date()
        if return_date < today:
            found = True

            print("Book ID :", row[0])
            print("Member ID :", row[1])
            print("Return Date :", row[2])
            print("----------------------")

    if not found:
        print("No Overdue Books")


def display_books(books):
    for book in books:

        print("-----------------------")
        print("Book ID :", book.book_id)
        print("Title :", book.title)
        print("Author :", book.author)
        print("Available :", "Yes" if book.available else "No")


def main():
    create_database()
    books = fetch_books()
    print("\nAvailable Books\n")
    display_books(books)
    sorted_books = merge_sort(books)
    print("\nBooks Sorted Alphabetically\n")
    display_books(sorted_books)
    books_by_id = sorted(books, key=lambda x: x.book_id)
    book_id = int(input("\nEnter Book ID to Search : "))
    result = binary_search(books_by_id, book_id)
    if result:
        print("\nBook Found\n")
        display_books([result])
    else:
        print("Book Not Found")
    if borrow_book(1, 2):
        print("\nBook Borrowed Successfully")
    else:
        print("\nBook Not Available")
    print("\nAvailable Books After Borrowing\n")
    display_books(fetch_books())
    overdue_books()


if __name__ == "__main__":
    main()