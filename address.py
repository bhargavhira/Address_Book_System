class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\nAddress Book Contacts:")
        for contact in self.contacts:
            print(contact)

