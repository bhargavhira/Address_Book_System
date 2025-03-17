from contact import Contact

class AddressBookMain:
    def __init__(self):
        print("Welcome to Address Book Program")
    
    def add_contact(self):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip_code = input("Enter ZIP Code: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
        print("\nContact Added Successfully:\n", contact)

if __name__ == "__main__":
    book = AddressBookMain()
    book.add_contact()
