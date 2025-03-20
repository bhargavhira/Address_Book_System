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
                
    def search_person_by_location(self, location, search_type):
        """Search for a person in a city or state across multiple Address Books."""
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
           
