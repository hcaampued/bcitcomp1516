# hero caampued
# kam fai cheung
# jessica huang


import re


def is_valid_license_plate(plate):
    valid_license = r"^[A-Z]{3}[0-9]{3}|[0-9]{3}|[A-Z]{3}|[A-Z]{2}[0-9][ -]?|[0-9]{2}[A-Z]$"
    return bool(re.search(valid_license, plate))


def is_valid_python_variable_name(variable_name):
    valid_variable = r"^_?([a-z]_?)+$"
    return len(variable_name) <= 32 and bool(re.search(valid_variable, variable_name))


def is_valid_email_address(email):
    pass


def is_valid_human_height(height):
    pass


def main():
    # test is_valid_license_plate()
    print(is_valid_license_plate("ABC123"))
    print(is_valid_license_plate("123ABC"))
    print(is_valid_license_plate("AB1 23C"))
    print(is_valid_license_plate("AB1-23C"))

    # test valid_python_variable_name()
    print(is_valid_python_variable_name("first_name"))
    print(is_valid_python_variable_name("_x_"))
    print(is_valid_python_variable_name("a"))
    print(is_valid_python_variable_name("a_good_variable_name"))
    print(is_valid_python_variable_name("x__x"))
    print(is_valid_python_variable_name("abcdefghijklmnopqrstuvwxyzabcdefg"))  # 33 characters
    print(is_valid_python_variable_name("_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a"))  # 32 characters


if __name__ == "__main__":
    main()
