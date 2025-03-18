import re

def validate_data(data_dict):
    """
    Returns a dictionary with validated values or False if invalid.
    """
    validated_data = {}
    
    for key, value in data_dict.items():
        if key == "first_name" or key == "last_name":
            if re.match(r"^[A-Z][a-z]{2,}$", str(value).title()):
                validated_data[key] = value
            else:
                validated_data[key] = False
        
        elif key == "email":
            pattern = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
            if re.match(pattern, str(value)):
                validated_data[key] = value
            else:
                validated_data[key] = False

        elif key == "zip_code":
            if re.match(r"^\d{5,6}$", str(value)):  
                validated_data[key] = value
            else:
                validated_data[key] = False

        elif key == "phone":
            if re.match(r"^\d{10}$", str(value)):  
                validated_data[key] = value
            else:
                validated_data[key] = False

        else:
            validated_data[key] = value

    return validated_data

def validation_wrapper(func):
    """
    A decorator that applies data validation to a function's dictionary input.
    Supports instance methods (class functions).
    """
    def wrapper(self, data_dict):
        validated_data = validate_data(data_dict)
         
        if False in validated_data.values():
            print("\n Validation Failed! Please enter valid details.")
            return

        return func(self, validated_data)

    return wrapper
