import psycopg2
import csv
from psycopg2 import sql

class PhoneBook:
    def __init__(self):
        self.conn_params = {
            'host': 'localhost',
            'database': 'phonebook_db',
            'user': 'postgres',
            'password': 'yourpassword'
        }
        self.conn = None
        self.cur = None
        
    def connect(self):
        """Establish connection to PostgreSQL database"""
        try:
            self.conn = psycopg2.connect(**self.conn_params)
            self.cur = self.conn.cursor()
            print("Connected to PostgreSQL database!")
        except Exception as e:
            print(f"Error connecting to database: {e}")
    
    def disconnect(self):
        """Close database connection"""
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
    
    def create_tables(self):
        """Create the phonebook table if it doesn't exist"""
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50),
                    phone VARCHAR(20) NOT NULL UNIQUE,
                    email VARCHAR(100),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.conn.commit()
            print("Phonebook table created successfully!")
        except Exception as e:
            self.conn.rollback()
            print(f"Error creating table: {e}")
    
    def insert_from_console(self):
        """Insert data from user input via console"""
        print("\nEnter contact details:")
        first_name = input("First name: ")
        last_name = input("Last name (optional): ")
        phone = input("Phone number: ")
        email = input("Email (optional): ")
        
        try:
            self.cur.execute("""
                INSERT INTO phonebook (first_name, last_name, phone, email)
                VALUES (%s, %s, %s, %s)
            """, (first_name, last_name, phone, email))
            self.conn.commit()
            print("Contact added successfully!")
        except Exception as e:
            self.conn.rollback()
            print(f"Error adding contact: {e}")
    
    def insert_from_csv(self, filename):
        """Insert data from CSV file"""
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header if exists
                for row in reader:
                    # Assuming CSV format: first_name,last_name,phone,email
                    self.cur.execute("""
                        INSERT INTO phonebook (first_name, last_name, phone, email)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (phone) DO NOTHING
                    """, (row[0], row[1], row[2], row[3] if len(row) > 3 else None))
            self.conn.commit()
            print(f"Data from {filename} imported successfully!")
        except Exception as e:
            self.conn.rollback()
            print(f"Error importing from CSV: {e}")
    
    def update_contact(self):
        """Update contact information"""
        print("\nUpdate contact:")
        phone = input("Enter phone number of contact to update: ")
        
        # Check if contact exists
        self.cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
        contact = self.cur.fetchone()
        
        if not contact:
            print("Contact not found!")
            return
        
        print(f"\nCurrent details: {contact}")
        print("\nWhat would you like to update?")
        print("1. First name")
        print("2. Last name")
        print("3. Phone number")
        print("4. Email")
        choice = input("Enter your choice (1-4): ")
        
        field_map = {
            '1': 'first_name',
            '2': 'last_name',
            '3': 'phone',
            '4': 'email'
        }
        
        if choice in field_map:
            new_value = input(f"Enter new {field_map[choice]}: ")
            try:
                self.cur.execute(
                    sql.SQL("UPDATE phonebook SET {} = %s WHERE phone = %s").format(
                        sql.Identifier(field_map[choice])
                    ),
                    (new_value, phone)
                )
                self.conn.commit()
                print("Contact updated successfully!")
            except Exception as e:
                self.conn.rollback()
                print(f"Error updating contact: {e}")
        else:
            print("Invalid choice!")
    
    def query_contacts(self):
        """Query contacts with different filters"""
        print("\nQuery contacts:")
        print("1. Show all contacts")
        print("2. Search by first name")
        print("3. Search by last name")
        print("4. Search by phone number")
        print("5. Search by email")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            self.cur.execute("SELECT * FROM phonebook ORDER BY first_name")
        elif choice == '2':
            name = input("Enter first name to search: ")
            self.cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", (f"%{name}%",))
        elif choice == '3':
            name = input("Enter last name to search: ")
            self.cur.execute("SELECT * FROM phonebook WHERE last_name ILIKE %s", (f"%{name}%",))
        elif choice == '4':
            phone = input("Enter phone number to search: ")
            self.cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"%{phone}%",))
        elif choice == '5':
            email = input("Enter email to search: ")
            self.cur.execute("SELECT * FROM phonebook WHERE email ILIKE %s", (f"%{email}%",))
        else:
            print("Invalid choice!")
            return
        
        contacts = self.cur.fetchall()
        if not contacts:
            print("No contacts found!")
        else:
            print("\nContacts:")
            for contact in contacts:
                print(f"ID: {contact[0]}, Name: {contact[1]} {contact[2]}, Phone: {contact[3]}, Email: {contact[4]}")
    
    def delete_contact(self):
        """Delete contact by username or phone"""
        print("\nDelete contact:")
        print("1. Delete by first name")
        print("2. Delete by phone number")
        choice = input("Enter your choice (1-2): ")
        
        if choice == '1':
            name = input("Enter first name to delete: ")
            self.cur.execute("DELETE FROM phonebook WHERE first_name = %s RETURNING *", (name,))
        elif choice == '2':
            phone = input("Enter phone number to delete: ")
            self.cur.execute("DELETE FROM phonebook WHERE phone = %s RETURNING *", (phone,))
        else:
            print("Invalid choice!")
            return
        
        deleted = self.cur.fetchall()
        self.conn.commit()
        
        if not deleted:
            print("No contacts deleted!")
        else:
            print(f"Deleted {len(deleted)} contact(s):")
            for contact in deleted:
                print(f"ID: {contact[0]}, Name: {contact[1]} {contact[2]}, Phone: {contact[3]}")
    
    def menu(self):
        """Main menu for the application"""
        while True:
            print("\nPhoneBook Application")
            print("1. Add contact (console)")
            print("2. Import contacts from CSV")
            print("3. Update contact")
            print("4. Query contacts")
            print("5. Delete contact")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == '1':
                self.insert_from_console()
            elif choice == '2':
                filename = input("Enter CSV filename: ")
                self.insert_from_csv(filename)
            elif choice == '3':
                self.update_contact()
            elif choice == '4':
                self.query_contacts()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")

# Main execution
if __name__ == "__main__":
    pb = PhoneBook()
    pb.connect()
    pb.create_tables()
    pb.menu()
    pb.disconnect()