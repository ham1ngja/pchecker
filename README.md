# pchecker.py

Pchecker.py is a password checker written in Python. It was created entirely for learning purposes and should not be used for real-life applications.

Below, you can view the entire source code of pchecker.py. Scroll [further down below](#code-explanation) to see the code broken down and explained in far more detail.

```python
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
```

## Code Explanation

### class Colour

```python
class Colour:
    RESET = "\033[0m"
    RED = "\033[31m"
    ORANGE = "\033[38;5;208m"
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
```

The code above declares five class variables that contain ANSI escape codes for various colours. This step is not entirely necessary; however, it is included to increase the human-readability of the output.

A different colour will be used depending on the degree of security of each aspect of the password, such as length, what characters it contains, etc.

### User Input

Using argparse, the user is allowed to type in their password directly in the terminal so that it can be checked. This is where the `password_input` function comes in.

This creates the parser:

```python
parser = argparse.ArgumentParser(description='Process a password.' )
```

This allows us to add an argument, which will be expected when the program is run:

```python
parser.add_argument('input_string', type=str, help='The password you want to input')
```

The next line of code actually parses the arguments provided:

```python
args = parser.parse_args()
```

Finally, the password typed in is placed inside the variable `password` before it is returned to the main block.

The line of code that calls this function is:

```python
password = password_input()
```

The code above calls the `password_input()` function without arguments and stores the result in `password`.

### Common Passwords

The next step is to evaluate the password's security. Before we perform any analysis, we first check it against a database of known insecure passwords.

The program uses a small list that can be found in the GitHub repository for this program, which is based on Daniel Miessler's [10-million-password-list-top-100.txt](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt).

Naturally, a much larger list can and should be utilized; however, for the purposes of this program, a small list of around 100 passwords would suffice.

In the source code, `is_password_in_file(search_string)` is what enables this functionality.

```python
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
```

Before accessing the file, `try` and `except` are used to enable error handling. If the file is not found, `except FileNotFoundError` runs, which outputs a message and then does `exit()`.

Assuming that the file is found, it is opened, and each line is compared to the password the user has typed in. If a match is found, the user is informed that their password is very insecure, and the program ends.

If the password is not found in the list, then a different message is output, and the program continues to run. This function is called by this line, in the main block:

```python
is_password_in_file(password)
```

This line calls the `is_password_in_file` function and sends it the password so that the comparison can occur.

### Check Length

If the password supplied by the user passes the list check, it will be further analysed, by first checking its length.

This is done through the following method:

```python
# Check the password length
    if len(password) < 12:

        print(f'''> [Length] {Colour.RED}[Poor]{Colour.RESET}: A password with a character length of {len(password)} is generally considered unsuitable. Please select a password that is at least 12 characters long.\n''')

    elif 12 <= len(password) <= 16:

        print(f'''> [Length] {Colour.ORANGE}[Ok]{Colour.RESET}: A password length of {len(password)} is generally considered fine for accounts that do not hold very sensitive information, such as a casual email account. If your account contains sensitive data, please consider a password length of at least 17.\n''')

    elif 17 <= len(password) <= 24:

        print(f'''> [Length] {Colour.YELLOW}[Good]{Colour.RESET}: A password length of {len(password)} is generally considered good. If your data is very sensitive, consider a password of 25 characters, or more.\n''')

    elif len(password) > 24:

        print(f'''> [Length] {Colour.GREEN}[Excellent]{Colour.RESET}: A password length of {len(password)} is generally considered excellent. Bear in mind that once you get over 32 characters, some services may not support a password of that length, and you might be required to shorten it.\n''')
```

The function utilizes four `if` statements and prints a different message based on the length of the password, instructing the user on whether their password is secure or not, depending on the context.

This function is called by `check_length(password)` in the main block.

### Check Characters

Once the length has been examined, the program looks at the contents of the password itself. This occurs in the following function:

```python
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
```

First off, using a regular expression, the program checks if the password contains lowercase letters.

```python
has_lower = bool(re.search(r'[a-z]', password))
```

The answer is stored as a boolean value, either `True` or `False`, in the `has_lower` variable.

```python
has_upper = bool(re.search(r'[A-Z]', password))
has_digit = bool(re.search(r'\d', password))
```

The following two lines check if the password contains uppercase letters and digits.

The fourth line checks if the password contains characters from a special set of symbols that are usually allowed in passwords.

```python
has_special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
```

Once the boolean values have been obtained, a series of if statements determine what is to be printed. First, the program checks if all four variables are true.

```python
if has_lower and has_upper and has_digit and has_special_char:

    print(f'''> [Mix] {Colour.GREEN}[Excellent]{Colour.RESET}: The password has a healthy mix of lowercase and uppercase letters, as well as numbers and special characters.\n''')
```

If the result is not `True`, it goes to the `elif` statement that follows, and it checks if it has everything but special characters.

```python
elif has_lower and has_upper and has_digit:

	print(f'''> [Mix] {Colour.YELLOW}[Good]{Colour.RESET}: The password has a mix of lowercase and uppercase letters, as well as numbers.\n''')
```

Finally, if this is not the case, there is an `else` statement in place to catch all other possibilities:

```python
else:

	print(f'''> [Mix] {Colour.RED}[Poor]{Colour.RESET}: Please make sure your password contains a healthy mix of letters, both lower and upper case, numbers, and symbols e.g. !@#$%^&*(),.?":{{}}|<>\n''')
```

The reason the print statement has `{{}}` instead of just `{}` is because `{}` is used to insert variable values in `print(f''''''`) statements. As a result, the brackets are used twice to escape.

This function is called by `check_characters(password)` in the main block.

### Check Space

The last check performed is `check_space(password)`. As the name suggests, it checks if the password contains any space characters.

```python
def check_space(password):

    if ' ' in password:

        print(f'''> [Space] {Colour.RED}[Poor]{Colour.RESET}: Your password contains a space. Whilst this is not necessarily an issue, many services either do not accept them, or they strip them from the password. Please avoid using spaces.\n''')

    else:

        print(f'''> [Space] {Colour.GREEN}[Excellent]{Colour.RESET}: Your password does not contain a space. Whilst spaces in passwords are not necessarily an issue, many services either do not accept them, or they strip them from the password.\n''')
```

Although there is technically nothing wrong with having space characters in a password, many services do not allow it. This is due to the potential confusion that it may cause, and some may even sanitize the password by stripping the space characters out altogether.

## Quality Assurance

Let us test the code for any potential issues that might arise due to different types of input.

### Common Password

**Input**
```bash
python3 pchecker.py 'pass'
```

**Output**
```
> [List] [Poor]: The password you have entered is very common, and thus easily guessable with a dictionary attack. Please select a stronger password.
```

The program correctly identified the password as common, and terminated.

### Common Password With Special Characters

**Input**
```bash
python3 pchecker.py 'pa$$'
```

**Output**
```
> [List] [Excellent]: Your password was not found in a list of commonly used passwords.

> [Length] [Poor]: A password with a character length of 4 is generally considered unsuitable. Please select a password that is at least 12 characters long.

> [Mix] [Poor]: Please make sure your password contains a healthy mix of letters, both lower and upper case, numbers, and symbols e.g. !@#$%^&*(),.?":{}|<>

> [Space] [Excellent]: Your password does not contain a space. Whilst spaces in passwords are not necessarily an issue, many services either do not accept them, or they strip them from the password.
```

The program identified the short length of the password, and suggested a longer variant, as well as proposed that different kinds of characters should be added.

### Short Password Without Symbols

**Input**
```bash
python3 pchecker.py 'fluffymelons'
```

**Output**
```
> [List] [Excellent]: Your password was not found in a list of commonly used passwords.

> [Length] [Ok]: A password length of 12 is generally considered fine for accounts that do not hold very sensitive information, such as a casual email account. If your account contains sensitive data, please consider a password length of at least 17.

> [Mix] [Poor]: Please make sure your password contains a healthy mix of letters, both lower and upper case, numbers, and symbols e.g. !@#$%^&*(),.?":{}|<>

> [Space] [Excellent]: Your password does not contain a space. Whilst spaces in passwords are not necessarily an issue, many services either do not accept them, or they strip them from the password.
```

The program identified the length of the password as 12, which can be acceptable in situations where no sensitive data is being protected.

### Short Password With a Symbol

**Input**
```bash
python3 pchecker.py 'fluffy-melons'
```

**Output**
```
> [List] [Excellent]: Your password was not found in a list of commonly used passwords.

> [Length] [Ok]: A password length of 13 is generally considered fine for accounts that do not hold very sensitive information, such as a casual email account. If your account contains sensitive data, please consider a password length of at least 17.

> [Mix] [Poor]: Please make sure your password contains a healthy mix of letters, both lower and upper case, numbers, and symbols e.g. !@#$%^&*(),.?":{}|<>

> [Space] [Excellent]: Your password does not contain a space. Whilst spaces in passwords are not necessarily an issue, many services either do not accept them, or they strip them from the password.
```

In this instance, the user added a dash in between the two words in the password, which is an improvement; however, there are no numbers or upper case letters.

### Medium Password With Digits and Symbols

**Input**
```bash
python3 pchecker.py 'fluffy-m3lons-bunnies'
```

**Output**
```
> [List] [Excellent]: Your password was not found in a list of commonly used passwords.

> [Length] [Good]: A password length of 21 is generally considered good. If your data is very sensitive, consider a password of 25 characters, or more.

> [Mix] [Poor]: Please make sure your password contains a healthy mix of letters, both lower and upper case, numbers, and symbols e.g. !@#$%^&*(),.?":{}|<>

> [Space] [Excellent]: Your password does not contain a space. Whilst spaces in passwords are not necessarily an issue, many services either do not accept them, or they strip them from the password.
```

In this example, the user has added one more word, lengthening the password, and they have replaced a letter with a digit, thus increasing the strength of the password. However, adding symbols as well would be highly indicated.

### Medium Password With Digits, Symbols, and Upper Case Letters

**Input**
```bash
python3 pchecker.py 'fluffy-m3lons-bunniE$'
```

**Output**
```
> [List] [Excellent]: Your password was not found in a list of commonly used passwords.

> [Length] [Good]: A password length of 21 is generally considered good. If your data is very sensitive though, consider a password of 25 characters, or more.

> [Mix] [Excellent]: The password has a healthy mix of lowercase and uppercase letters, as well as numbers and special characters.

> [Space] [Excellent]: Your password does not contain a space. Whilst spaces in passwords are not necessarily an issue, many services either do not accept them, or they strip them from the password.
```

The user inputs a medium-length password, which is much more secure as it has a healthy mix of digits, symbols, and letters.

### Long Secure Password

**Input**
```bash
python3 pchecker.py 'fluffy-m3lons-bunniE$-up0n-Hallow33n'
```

**Output**
```
> [List] [Excellent]: Your password was not found in a list of commonly used passwords.

> [Length] [Excellent]: A password length of 36 is generally considered excellent. Bear in mind that once you get over 32 characters, some services may not support a password of that length, and you might be required to shorten it.

> [Mix] [Excellent]: The password has a healthy mix of lowercase and uppercase letters, as well as numbers and special characters.

> [Space] [Excellent]: Your password does not contain a space. Whilst spaces in passwords are not necessarily an issue, many services either do not accept them, or they strip them from the password.
```

In the case of a long, and more secure password, the output all came out excellent. The password is of a good length, it contains all types of symbols, and it does not contain a space.

### Long Secure Password With a Space

**Input**
```bash
python3 pchecker.py 'fluffy-m3lons-bunniE$-up0n- Hallow33n'
```

**Output**
```
> [List] [Excellent]: Your password was not found in a list of commonly used passwords.

> [Length] [Excellent]: A password length of 37 is generally considered excellent. Bear in mind that once you get over 32 characters, some services may not support a password of that length, and you might be required to shorten it.

> [Mix] [Excellent]: The password has a healthy mix of lowercase and uppercase letters, as well as numbers and special characters.

> [Space] [Poor]: Your password contains a space. Whilst this is not necessarily an issue, many services either do not accept them, or they strip them from the password. Please avoid using spaces.
```

In this instance, all the metrics were excellent, except for the space section, which was `Poor` due to the presence of a space character in the password.

### Long Secure Password Without Quotation Marks

**Input**
```bash
python3 pchecker.py fluffy-m3lons-bunniE$-up0n- Hall?w33n
```

**Output**
```
zsh: no matches found: Hall?w33n
```

In this instance, the user added a `?` to the password but forgot to add quotation marks around the argument itself, resulting in an error.
