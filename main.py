from address import AddressBook
from contact import Contact
from validate import generate_user_data
from addressbookmain import AddressBookMain
import os
import csv
import json

CSV_DIRECTORY = "Data/csv"
JSON_DIRECTORY = "Data/json"

os.makedirs(CSV_DIRECTORY, exist_ok=True)
os.makedirs(JSON_DIRECTORY, exist_ok=True)

def main():
    """Main function for Address Book system."""
    manager = AddressBookMain()
    current_book = None

    while True:
        print("\nMain Menu:")
        print("1. Create Address Book")
        print("2. Select Address Book")
        print("3. Delete Address Book")
        print("4. Display Address Books")
        print("5. Manage Contacts")
        print("6. Search Person by City/State")
        print("7. View Person by City/State")
        print("8. Count Person by City/State")
        print("9. Exit")

        choice = input("Select an option: ")

        match choice:
            case "1":
                manager.create_address_book(input("Enter Address Book Name: "))
            case "2":
                current_book = manager.select_address_book(input("Enter Address Book Name: "))
                if current_book:
                    manage_contacts(current_book)
                else:
                    print("Address Book not found!")
            case "3":
                manager.delete_address_book(input("Enter Address Book Name: "))
            case "4":
                manager.display_address_books()
            case "5":
                if current_book:
                    manage_contacts(current_book)
                else:
                    print("No Address Book selected!")
            case "6":
                search_type = input("Search by (city/state): ").strip().lower()
                location = input(f"Enter {search_type} name: ").strip()
                manager.search_person_by_location(location, search_type)
            case "7":
                search_type = input("Search by (city/state): ").strip().lower()
                location = input("Enter the (city/state): ").strip()
                if search_type in ["city", "state"]:
                    manager.view_person_by_location(location, search_type)
                else:
                    print("Invalid option! Choose 'city' or 'state'.")
            case "8":
                search_type = input("Enter City or State: ").strip().lower()
                location = input("Count by (city/state): ").strip()
                if search_type in ["city", "state"]:
                    manager.count_person_by_location(location, search_type)
                else:
                    print("Invalid option! Choose 'city' or 'state'.")
            case "9":
                manager.save_all_books_to_csv()
                print("Address Books saved. Exiting...")
                break
            case _:
                print("Invalid choice. Try again.")

def manage_contacts(book):
    """Handles the contact use cases in the selected Address Book."""
    while True:
        print("\nContact Menu:")
        print("1. Add Contact 2. Show Contacts 3. Edit Contact 4. Delete Contact 5. Sort Contacts Alphabetically 6. Back")

        choice = input("Choose an option: ")

        match choice:
            case "1":
                book.add_contact()
            case "2":
                book.display_contacts()
            case "3":
                book.edit_contact()
            case "4":
                book.delete_contact()
            case "5":
                sort_by = input("Sort by (City/State/Zip): ").strip().lower()
                if sort_by in ["city", "state", "zip"]:
                    book.sort_contacts(sort_by)
                else:
                    print("Invalid option! Choose city, state, or zip.")        
            case "6":
                break
            case _:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
