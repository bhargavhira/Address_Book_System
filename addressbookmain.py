from address import AddressBook
import os
import csv
import json

CSV_DIRECTORY = "Data/csv"
JSON_DIRECTORY = "Data/json"

os.makedirs(CSV_DIRECTORY, exist_ok=True)
os.makedirs(JSON_DIRECTORY, exist_ok=True)

class AddressBookMain:
    def __init__(self):
        self.books = {}
        self.load_all_books()

    def create_address_book(self, name):
        if name in self.books:
            print(f"Address Book '{name}' already exists!")
        else:
            self.books[name] = AddressBook()
            self.save_address_book(name)
            print(f"Address Book '{name}' created successfully.")

    def select_address_book(self, name):
        return self.books.get(name, None)

    def delete_address_book(self, name):
        if name in self.books:
            del self.books[name]
            csv_path = os.path.join(CSV_DIRECTORY, f"{name}.csv")
            json_path = os.path.join(JSON_DIRECTORY, f"{name}.json")

            if os.path.exists(csv_path):
                os.remove(csv_path)
            if os.path.exists(json_path):
                os.remove(json_path)

            print(f"Address Book '{name}' deleted successfully.")
        else:
            print("Address Book not found!")

    def display_address_books(self):
        if not self.books:
            print("No Address Books available.")
        else:
            print("\nAvailable Address Books:")
            for name in self.books:
                print(f"- {name}")

    def save_address_book(self, name):
        if name in self.books:
            book = self.books[name]
            csv_path = os.path.join(CSV_DIRECTORY, f"{name}.csv")
            json_path = os.path.join(JSON_DIRECTORY, f"{name}.json")

            with open(csv_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["First Name", "Last Name", "Address", "City", "State", "Zip", "Phone", "Email"])
                for contact in book.contacts:
                    writer.writerow([contact.first_name, contact.last_name, contact.address,
                                     contact.city, contact.state, contact.zip_code,
                                     contact.phone_number, contact.email])

            with open(json_path, mode="w") as file:
                json.dump([contact.__dict__ for contact in book.contacts], file, indent=4)

    def save_all_books(self):
        for book_name in self.books:
            self.save_address_book(book_name)
        print("All Address Books saved successfully.")

    def load_all_books(self):
        for file_name in os.listdir(CSV_DIRECTORY):
            if file_name.endswith(".csv"):
                book_name = file_name.replace(".csv", "")
                csv_path = os.path.join(CSV_DIRECTORY, file_name)

                address_book = AddressBook()
                if os.path.exists(csv_path):
                    with open(csv_path, mode="r") as file:
                        reader = csv.reader(file)
                        next(reader, None)
                        for row in reader:
                            if len(row) == 8:
                                address_book.add_contact(*row)

                self.books[book_name] = address_book
        print("All Address Books loaded successfully.")

    def search_person_by_location(self, location, search_type):
        found = False
        for book_name, book in self.books.items():
            for contact in book.contacts:
                if (search_type == "city" and contact.city.lower() == location.lower()) or \
                   (search_type == "state" and contact.state.lower() == location.lower()):
                    print(f"Found in '{book_name}': {contact}")
                    found = True
        if not found:
            print("No contacts found in the given location.")

    def view_person_by_location(self, location, search_type):
        view_persons_by_location = {}

        for book_name, book in self.books.items():
            for contact in book.contacts:
                if (search_type == "city" and contact.city.lower() == location.lower()) or \
                   (search_type == "state" and contact.state.lower() == location.lower()):
                    view_persons_by_location.setdefault(book_name, []).append(str(contact))

        if view_persons_by_location:
            print(f"\nPersons in {search_type.title()} '{location}':")
            for book_name, contacts in view_persons_by_location.items():
                print(f"\nAddress Book: {book_name}")
                for contact in contacts:
                    print(contact)
        else:
            print(f"No persons found in {search_type.title()} '{location}'.")

    def count_person_by_location(self, location, search_type):
        count_by_location = {}

        for book_name, book in self.books.items():
            count = sum(1 for contact in book.contacts if
                        (search_type == "city" and contact.city.lower() == location.lower()) or 
                        (search_type == "state" and contact.state.lower() == location.lower()))
            if count > 0:
                count_by_location[book_name] = count

        if count_by_location:
            print(f"\nNumber of persons in {search_type.title()} '{location}':")
            for book_name, count in count_by_location.items():
                print(f"Address Book: {book_name} - {count} contact(s)")
        else:
            print(f"No persons found in {search_type.title()} '{location}'.")
