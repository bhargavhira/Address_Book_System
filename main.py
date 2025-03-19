from address import AddressBook
from contact import Contact
from validate import generate_user_data

def main():
    """Main function for Address Book system."""
    address_book = AddressBook()

    while True:
        print("\n Address Book Menu:")
        print("1️ Add Contact")
        print("2️ Show Contacts")
        print("3️ Edit Contact")
        print("4️ Delete Contact")
        print("5️ Exit")

        choice = input("Select an option: ")

        match choice:
            case "1":
                address_book.add_contact()
            case "2":
                address_book.display_contacts()
            case "3":
                address_book.edit_contact()
            case "4":
                address_book.delete_contact()
            case "5":
                print("Exiting Address Book. Goodbye!")
                break
            case _:
                print("Invalid option! Please select a valid choice.")

if __name__ == "__main__":
    main()
