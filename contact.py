class Contact:
    """
    Represents a contact with basic details.
    """
    def __init__(self, **kwargs):
        """
        Initializes contact attributes using keyword arguments.
        """
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        """Returns contact details as a formatted string."""
        return (f"{self.first_name} {self.last_name}, {self.address}, {self.city}, "
                f"{self.state}, {self.zip_code}, {self.phone_number}, {self.email}\n")
