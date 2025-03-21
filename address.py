from validate import validate_data
from contact import Contact

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        
        #Duplicate check karega
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                print("Contact already exists! Duplicate entries are not allowed.")
                return
        """Handles user input and adds a contact."""
        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "address": input("Enter Address: "),
            "city": input("Enter City: "),
            "state": input("Enter State: "),
            "zip_code": input("Enter Zip Code: "),
            "phone_number": input("Enter Phone Number: "),
            "email": input("Enter Email: ")
        }

        validated_data = validate_data(user_data)
        if validated_data:
            contact = Contact(**validated_data)
            self.contacts.append(contact)
            print("Contact added successfully!")

    def display_contacts(self):
        """Displays all contacts."""
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nAddress Book Contacts:")
        for contact in self.contacts:
            print(contact)

    def edit_contact(self):
        """Edits an existing contact."""
        search_name = input("Enter first name of the contact to edit: ").strip().lower()
        for contact in self.contacts:
            if contact.first_name.lower() == search_name:
                print(f"Editing Contact: {contact}\n")
                updated_data = {
                    "address": input("Enter New Address: ") or contact.address,
                    "city": input("Enter New City: ") or contact.city,
                    "state": input("Enter New State: ") or contact.state,
                    "zip_code": input("Enter New Zip Code: ") or contact.zip_code,
                    "phone_number": input("Enter New Phone Number: ") or contact.phone_number,
                    "email": input("Enter New Email: ") or contact.email,
                }
                for key, value in updated_data.items():
                    setattr(contact, key, value)

                print("Contact updated successfully!")
                return
        print("Contact not found!")

    def delete_contact(self):
        name = input("Enter first name of the contact to delete: ").strip().lower()
        for contact in self.contacts:
         if contact.first_name.lower() == name:
            self.contacts.remove(contact)
            print(f"Contact '{contact.first_name} {contact.last_name}' deleted successfully!")
            return

         print("Contact not found!")

    def sort_contacts(self):
        self.contacts.sort(key=lambda contact: (contact.first_name.lower(), contact.last_name.lower()))
        print("Contacts Sorted Successfully !")
             