import re

def validate_data(data):
    """Validates contact details using regex rules."""
    patterns = {
        "first_name": r"^[A-Z][a-z]{2,}$",
        "last_name": r"^[A-Z][a-z]{2,}$",
        "email": r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",
        "zip_code": r"^\d{5,6}$",
        "phone_number": r"^\d{10}$"
    }

    for key, value in data.items():
        if key in patterns and not re.match(patterns[key], value):
            print(f"Invalid {key.replace('_', ' ').title()}. Please enter a valid value.")
            return None  

    return data

def validation_wrapper(func):
    """Decorator that validates input data before passing it to a function."""
    def wrapper(*args):
        validated_args = [validate_data(arg) if isinstance(arg, dict) else arg for arg in args]
        return func(*validated_args) if all(validated_args) else None
    return wrapper

@validation_wrapper
def generate_user_data(user_data):
    return user_data
