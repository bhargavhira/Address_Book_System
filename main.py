from address import AddressBook
from contact import Contact
from validate import validation_wrapper  # Import validation wrapper

class AddressBookMain:
    def __init__(self):
        print("Welcome to Address Book Program")
        self.address_book = AddressBook()

    @validation_wrapper
    def add_contact(self, contact_data):
        """ Adds a contact after validation. """
        contact = Contact(
            contact_data["first_name"],
            contact_data["last_name"],
            contact_data["address"],
            contact_data["city"],
            contact_data["state"],
            contact_data["zip_code"],
            contact_data["phone"],
            contact_data["email"]
        )
        self.address_book.add_contact(contact)
        print("\n Contact added successfully!")

    def get_contact_input(self):
        """ Collects user input and stores it in a dictionary for validation. """
        return {
            "first_name": input("Enter First Name (Starts with a capital letter, min 3 chars): "),
            "last_name": input("Enter Last Name (Starts with a capital letter, min 3 chars): "),
            "address": input("Enter Address: "),
            "city": input("Enter City: "),
            "state": input("Enter State: "),
            "zip_code": input("Enter ZIP Code (5-6 digits): "),
            "phone": input("Enter Phone Number (10 digits): "),
            "email": input("Enter Email: ")
        }

if __name__ == "__main__":
    book = AddressBookMain()

    while True:
        contact_data = book.get_contact_input()
        book.add_contact(contact_data)
