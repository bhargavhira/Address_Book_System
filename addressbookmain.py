from address import AddressBook

class AddressBookMain:
    def __init__(self):
        self.books = {} 

    def create_address_book(self, name):
        """Creates a new Address Book with a unique name."""
        if name in self.books:
            print(f"Address Book '{name}' already exists!")
        else:
            self.books[name] = AddressBook()
            print(f"Address Book '{name}' created successfully.")

    def select_address_book(self, name):
        """Returns the selected Address Book."""
        return self.books.get(name, None)

    def delete_address_book(self, name):
        """Deletes an Address Book."""
        if name in self.books:
            del self.books[name]
            print(f"Address Book '{name}' deleted successfully.")
        else:
            print("Address Book not found!")

    def display_address_books(self):
        """Displays all available Address Books."""
        if not self.books:
            print("No Address Books available.")
        else:
            print("\nAvailable Address Books:")
            for name in self.books:
                print(f"- {name}")
