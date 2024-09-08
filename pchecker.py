import argparse
import re


# Prepare colours
class Colour:
    RESET = "\033[0m"
    RED = "\033[31m"
    ORANGE = "\033[38;5;208m"
    YELLOW = "\033[33m"
    GREEN = "\033[32m"

# Have the user input a password via argparse
def password_input():
    # Create the parser
    parser = argparse.ArgumentParser(description='Process a password.' )

    # Add the argument
    parser.add_argument('input_string', type=str, help='The password you want to input')

    # Parse the arguments
    args = parser.parse_args()

    # Access the input string
    password = args.input_string

    return password

# Check list
def is_password_in_file(search_string):
    try:
        with open('list.txt', 'r') as file:
            for line in file:
                if search_string in line:
                        print(f'''> [List] {Colour.RED}[Poor]{Colour.RESET}: The password you have entered is very common, and thus easily guessable with a dictionary attack. Please select a stronger password.\n''')
                        exit()
        print(f'''> [List] {Colour.GREEN}[Excellent]{Colour.RESET}: Your password was not found in a list of commonly used passwords.\n''')

    except FileNotFoundError:
        print('The password list was not found.')
        exit()


def check_length(password):

# Check the password length
    if len(password) < 12:

        print(f'''> [Length] {Colour.RED}[Poor]{Colour.RESET}: A password with a character length of {len(password)} is generally considered unsuitable. Please select a password that is at least 12 characters long.\n''')

    elif 12 <= len(password) <= 16:

        print(f'''> [Length] {Colour.ORANGE}[Ok]{Colour.RESET}: A password length of {len(password)} is generally considered fine for accounts that do not hold very sensitive information, such as a casual email account. If your account contains sensitive data, please consider a password length of at least 17.\n''')

    elif 17 <= len(password) <= 24:

        print(f'''> [Length] {Colour.YELLOW}[Good]{Colour.RESET}: A password length of {len(password)} is generally considered good. If your data is very sensitive, consider a password of 25 characters, or more.\n''')

    elif len(password) > 24:

        print(f'''> [Length] {Colour.GREEN}[Excellent]{Colour.RESET}: A password length of {len(password)} is generally considered excellent. Bear in mind that once you get over 32 characters, some services may not support a password of that length, and you might be required to shorten it.\n''')


def check_characters(password):
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if has_lower and has_upper and has_digit and has_special_char:

        print(f'''> [Mix] {Colour.GREEN}[Excellent]{Colour.RESET}: The password has a healthy mix of lowercase and uppercase letters, as well as numbers and special characters.\n''')

    elif has_lower and has_upper and has_digit:

        print(f'''> [Mix] {Colour.YELLOW}[Good]{Colour.RESET}: The password has a mix of lowercase and uppercase letters, as well as numbers.\n''')

    else:

        print(f'''> [Mix] {Colour.RED}[Poor]{Colour.RESET}: Please make sure your password contains a healthy mix of letters, both lower and upper case, numbers, and symbols e.g. !@#$%^&*(),.?":{{}}|<>\n''')

def check_space(password):

    if ' ' in password:

        print(f'''> [Space] {Colour.RED}[Poor]{Colour.RESET}: Your password contains a space. Whilst this is not necessarily an issue, many services either do not accept them, or they strip them from the password. Please avoid using spaces.\n''')

    else:

        print(f'''> [Space] {Colour.GREEN}[Excellent]{Colour.RESET}: Your password does not contain a space. Whilst spaces in passwords are not necessarily an issue, many services either do not accept them, or they strip them from the password.\n''')


# Attribute the return value of password_input() to {password}
password = password_input()

# Check whether the password is in the commonly used password list
is_password_in_file(password)

# Check the length of the password, and issue recommendations
check_length(password)

# Check whether the password contains letters, numbers, and special characters
check_characters(password)

# Check if the password contains spaces
check_space(password)
