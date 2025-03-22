import os
import csv
import json
from validate import validate_data
from contact import Contact

CSV_DIRECTORY = "Data/csv"
JSON_DIRECTORY = "Data/json"

os.makedirs(CSV_DIRECTORY, exist_ok=True)
os.makedirs(JSON_DIRECTORY, exist_ok=True)

class AddressBook:
    def __init__(self, name=""):
        self.contacts = []
        self.name = name
        if name:
            self.load_from_file()

    def add_contact(self):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")

        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                print("Contact already exists! Duplicate entries are not allowed.")
                return

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
            self.save_to_file()
            print("Contact added successfully!")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nAddress Book Contacts:")
            for contact in self.contacts:
                print(contact)

    def edit_contact(self):
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

                self.save_to_file()
                print("Contact updated successfully!")
                return
        print("Contact not found!")

    def delete_contact(self):
        name = input("Enter first name of the contact to delete: ").strip().lower()
        for contact in self.contacts:
            if contact.first_name.lower() == name:
                self.contacts.remove(contact)
                self.save_to_file()
                print(f"Contact '{contact.first_name} {contact.last_name}' deleted successfully!")
                return

        print("Contact not found!")

    def sort_contacts(self, sort_by):
        valid_keys = {"city": "city", "state": "state", "zip": "zip_code"}

        if sort_by not in valid_keys:
            print("Invalid sort option! Choose from city, state, or zip.")
            return
        
        self.contacts.sort(key=lambda contact: getattr(contact, valid_keys[sort_by]).lower())
        print(f"Contacts sorted by {sort_by}.")

    def save_to_file(self):
        if not self.name:
            print("Error: Address Book name is not set.")
            return

        csv_path = os.path.join(CSV_DIRECTORY, f"{self.name}.csv")
        json_path = os.path.join(JSON_DIRECTORY, f"{self.name}.json")

        with open(csv_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["First Name", "Last Name", "Address", "City", "State", "Zip", "Phone", "Email"])
            for contact in self.contacts:
                writer.writerow([contact.first_name, contact.last_name, contact.address,
                                 contact.city, contact.state, contact.zip_code,
                                 contact.phone_number, contact.email])

        with open(json_path, mode="w") as file:
            json.dump([contact.__dict__ for contact in self.contacts], file, indent=4)

    def load_from_file(self):
        csv_path = os.path.join(CSV_DIRECTORY, f"{self.name}.csv")

        if not os.path.exists(csv_path):
            return

        with open(csv_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contact_data = {
                    "first_name": row["First Name"],
                    "last_name": row["Last Name"],
                    "address": row["Address"],
                    "city": row["City"],
                    "state": row["State"],
                    "zip_code": row["Zip"],
                    "phone_number": row["Phone"],
                    "email": row["Email"]
                }
                self.contacts.append(Contact(**contact_data))

        print(f"Loaded {len(self.contacts)} contacts from {self.name}.csv")
 