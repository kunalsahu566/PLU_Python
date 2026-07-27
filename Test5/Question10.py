# # 10. Sales Performance Dashboard
# ### Problem Statement
# A retail company stores sales information.
# Each sale contains:
# * Salesperson ID
# * Product
# * Quantity
# * Revenue
# * Region
# ### Requirements
# 1. Retrieve all sales records.
# 2. Sort records based on revenue.
# 3. Search a salesperson using Employee ID.
# 4. Display Top 5 salespersons.
# 5. Find the highest revenue region.
# 6. Update monthly incentive status for eligible salespersons.
# ### Concepts
# * SQL GROUP BY
# * Sorting
# * Binary Search
# * Dictionaries
# * SQLite
# 


import sqlite3
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Sale:
    salesperson_id: int
    product: str
    quantity: int
    revenue: float
    region: str


def create_table_and_insert_data():
    connection = sqlite3.connect("sales.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sales (
            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
            salesperson_id INTEGER NOT NULL,
            product TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            revenue REAL NOT NULL,
            region TEXT NOT NULL,
            incentive_status TEXT NOT NULL DEFAULT 'Pending'
        )
        """
    )

    cursor.execute("DELETE FROM sales")

    demo_sales = [
        (101, "Laptop", 2, 120000.0, "North", "Pending"),
        (102, "Phone", 5, 75000.0, "South", "Pending"),
        (101, "Mouse", 10, 20000.0, "North", "Pending"),
        (103, "Monitor", 3, 90000.0, "East", "Pending"),
        (102, "Keyboard", 4, 40000.0, "South", "Pending"),
        (104, "Headset", 6, 60000.0, "West", "Pending"),
    ]

    cursor.executemany(
        """
        INSERT INTO sales (salesperson_id, product, quantity, revenue, region, incentive_status)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        demo_sales,
    )

    connection.commit()
    connection.close()


def fetch_sales() -> List[Sale]:
    connection = sqlite3.connect("sales.db")
    cursor = connection.cursor()
    cursor.execute("SELECT salesperson_id, product, quantity, revenue, region FROM sales")
    rows = cursor.fetchall()
    connection.close()

    return [Sale(salesperson_id=row[0], product=row[1], quantity=row[2], revenue=row[3], region=row[4]) for row in rows]


def sort_by_revenue(sales: List[Sale]) -> List[Sale]:
    return sorted(sales, key=lambda sale: sale.revenue, reverse=True)


def binary_search_by_id(sales: List[Sale], target_id: int) -> Optional[Sale]:
    low = 0
    high = len(sales) - 1

    while low <= high:
        mid = (low + high) // 2
        if sales[mid].salesperson_id == target_id:
            return sales[mid]
        elif sales[mid].salesperson_id < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return None


def top_5_salespersons(sales: List[Sale]) -> Dict[int, float]:
    totals: Dict[int, float] = defaultdict(float)
    for sale in sales:
        totals[sale.salesperson_id] += sale.revenue
    return dict(sorted(totals.items(), key=lambda item: item[1], reverse=True)[:5])


def highest_revenue_region(sales: List[Sale]) -> str:
    totals: Dict[str, float] = defaultdict(float)
    for sale in sales:
        totals[sale.region] += sale.revenue
    return max(totals.items(), key=lambda item: item[1])[0]


def update_incentive_status(threshold: float):
    connection = sqlite3.connect("sales.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT salesperson_id, SUM(revenue) AS total_revenue
        FROM sales
        GROUP BY salesperson_id
        HAVING SUM(revenue) >= ?
        """,
        (threshold,),
    )
    eligible = [row[0] for row in cursor.fetchall()]

    for salesperson_id in eligible:
        cursor.execute("UPDATE sales SET incentive_status = 'Eligible' WHERE salesperson_id = ?", (salesperson_id,))

    connection.commit()
    connection.close()


def display_sale(sale: Sale):
    print(f"Salesperson ID: {sale.salesperson_id}")
    print(f"Product: {sale.product}")
    print(f"Quantity: {sale.quantity}")
    print(f"Revenue: {sale.revenue}")
    print(f"Region: {sale.region}")
    print("-" * 30)


def main():
    print("Creating table and inserting demo data...\n")
    create_table_and_insert_data()

    sales = fetch_sales()
    print("All sales records:")
    for sale in sales:
        display_sale(sale)

    sorted_sales = sort_by_revenue(sales)
    print("\nSales sorted by revenue:")
    for sale in sorted_sales:
        display_sale(sale)

    search_id = int(input("\nEnter Salesperson ID to search: "))
    result = binary_search_by_id(sorted_sales, search_id)
    if result is None:
        print("Salesperson not found.")
    else:
        print("\nSalesperson found:")
        display_sale(result)

    print("\nTop 5 salespersons by total revenue:")
    for salesperson_id, total_revenue in top_5_salespersons(sales).items():
        print(f"Salesperson ID: {salesperson_id}, Total Revenue: {total_revenue}")

    print(f"\nHighest revenue region: {highest_revenue_region(sales)}")

    update_incentive_status(50000.0)
    print("\nIncentive status updated for eligible salespersons.")


if __name__ == "__main__":
    main()








