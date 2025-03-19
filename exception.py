class ContactNotFoundError(Exception):
    """ Raised when the contact to be edited is not found in the Address Book. """
    def __init__(self, name):
        super().__init__(f"Error: Contact '{name}' not found in the Address Book.")