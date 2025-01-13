import sqlite3
from tabulate import tabulate  # Optional for better display
def setup_database():
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT DEFAULT 'Open'
    )''')
    conn.commit()
    conn.close()
if __name__ == "__main__":
    setup_database()
def add_ticket():
    title = input("Enter ticket title: ")
    description = input("Enter ticket description: ")

    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tickets (title, description) VALUES (?, ?)", (title, description))
    conn.commit()
    conn.close()

    print("Ticket created successfully!")
def view_tickets():
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()
    conn.close()

    if tickets:
        print(tabulate(tickets, headers=["ID", "Title", "Description", "Status"], tablefmt="grid"))
    else:
        print("No tickets found.")
def update_ticket_status():
    ticket_id = input("Enter the ticket ID to update: ")
    new_status = input("Enter the new status (Open/Closed/In Progress): ")

    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (new_status, ticket_id))
    conn.commit()
    conn.close()

    print("Ticket updated successfully!")
def delete_ticket():
    ticket_id = input("Enter the ticket ID to delete: ")

    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
    conn.commit()
    conn.close()

    print("Ticket deleted successfully!")
def main_menu():
    while True:
        print("\nIT Ticketing System")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Update Ticket Status")
        print("4. Delete Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            update_ticket_status()
        elif choice == "4":
            delete_ticket()
        elif choice == "5":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    setup_database()
    main_menu()
try:
    # database operation
except sqlite3.Error as e:
    print(f"Database error: {e}")
def seed_data():
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO tickets (title, description) VALUES (?, ?)", [
        ("Printer not working", "The office printer is not responding."),
        ("Slow internet", "Internet speed is unusually slow in the office."),
    ])
    conn.commit()
    conn.close()
