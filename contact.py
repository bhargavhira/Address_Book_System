class Contact:
    
    def __init__(self, first_name, last_name, address, city, state, zip, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number
        self.email = email
    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.address + " " + self.zip + " " + self.phone_number + " " + self.email + "\n"
    