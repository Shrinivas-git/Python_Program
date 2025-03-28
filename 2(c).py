class NegativeNumberError(Exception):
    pass
def check_posi_num(number):
    if number < 0:
        raise NegativeNumberError("Number cannot be negative")
try:
    check_posi_num(-5)
except NegativeNumberError as e:
    print(f"error{e}")


