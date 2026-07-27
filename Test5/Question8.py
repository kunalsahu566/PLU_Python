import sqlite3


class RideBookingSystem:

    def __init__(self):
        self.graph = {}

    def create_database(self):
        conn = sqlite3.connect("ride_booking.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS drivers(
            driver_id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT,
            available INTEGER
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings(
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            pickup_location TEXT,
            drop_location TEXT,
            driver_id INTEGER,
            status TEXT
        )
        """)

        cursor.execute("DELETE FROM bookings")
        cursor.execute("DELETE FROM drivers")

        drivers = [
            (1, "Aman", "A", 1),
            (2, "Nina", "B", 1),
            (3, "Ravi", "C", 1),
            (4, "Sara", "D", 0)
        ]

        cursor.executemany(
            "INSERT INTO drivers VALUES (?,?,?,?)",
            drivers
        )

        conn.commit()
        conn.close()


    def create_graph(self):

        self.graph = {
            "A": ["B", "C"],
            "B": ["A", "D"],
            "C": ["A", "D"],
            "D": ["B", "C"]
        }


    def available_drivers(self):
        conn = sqlite3.connect("ride_booking.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT driver_id,name,location FROM drivers WHERE available=1"
        )
        drivers = cursor.fetchall()
        conn.close()
        return drivers

    def bfs(self, start):
        queue = []
        visited = []
        queue.append(start)
        visited.append(start)
        while len(queue) > 0:
            node = queue.pop(0)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited

    def find_driver(self, pickup):
        drivers = self.available_drivers()
        order = self.bfs(pickup)
        for location in order:
            for driver in drivers:
                if driver[2] == location:
                    return driver

        return None

    def book_ride(self, customer, pickup, drop):
        driver = self.find_driver(pickup)
        if driver == None:
            return False

        conn = sqlite3.connect("ride_booking.db")
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO bookings
        (customer_name,pickup_location,drop_location,driver_id,status)
        VALUES (?,?,?,?,?)
        """,
        (customer, pickup, drop, driver[0], "Assigned"))

        cursor.execute(
            "UPDATE drivers SET available=0 WHERE driver_id=?",
            (driver[0],)
        )

        conn.commit()
        conn.close()

        print("\nDriver Assigned :", driver[1])


    def display_bookings(self):

        conn = sqlite3.connect("ride_booking.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bookings")
        bookings = cursor.fetchall()
        conn.close()
        print("\nBooking Details\n")
        for booking in bookings:
            print("----------------------------")
            print("Booking ID :", booking[0])
            print("Customer   :", booking[1])
            print("Pickup     :", booking[2])
            print("Drop       :", booking[3])
            print("Driver ID  :", booking[4])
            print("Status     :", booking[5])


def main():

    system = RideBookingSystem()
    system.create_database()
    system.create_graph()
    print("Available Drivers\n")
    drivers = system.available_drivers()
    for driver in drivers:
        print(driver)
    customer = input("\nEnter Customer Name : ")
    pickup = input("Enter Pickup Location (A-D): ")
    drop = input("Enter Drop Location (A-D): ")
    system.book_ride(customer, pickup, drop)
    system.display_bookings()

if __name__ == "__main__":
    main()