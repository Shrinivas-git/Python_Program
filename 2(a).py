class CustomTypeError(Exception):
    pass

class IndexOutOfRangeError(Exception):
    pass

def check_type(value, expected_type):
    if not isinstance(value, expected_type):
        raise CustomTypeError

def check_index(index, valid_range):
    if index < 0 or index >= valid_range:
        raise IndexOutOfRangeError

# Example usage
try:
    check_type("123", int)
except CustomTypeError:
    print("CustomTypeError: Expected type int")

try:
    check_index(5, 3)
except IndexOutOfRangeError:
    print("IndexOutOfRangeError: Index out of range")
