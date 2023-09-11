import re

def is_valid_digits(input_string):
    pattern = r'^\d+$'
    return bool(re.match(pattern, input_string))


# Примеры использования:
print(is_valid_digits("1928346"))    # True
print(is_valid_digits("123Д02349"))  # False
print(is_valid_digits("1111111111"))
print(is_valid_digits("g452g268g62"))